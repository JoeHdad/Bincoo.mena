<?php
// Shared helpers for the chatbot endpoints. Written for PHP 7.0+ (no newer syntax).

if (!defined('BINCOO_API')) {
    http_response_code(404);
    exit;
}

/**
 * Secrets and settings live outside public_html, in /home/<account>/bincoo-config.php,
 * so they are never served by the web server or committed to the public repo.
 */
function bm_config()
{
    static $config = null;
    if ($config !== null) {
        return $config;
    }
    $defaults = array(
        'openrouter_key' => '',
        // Gemini 2.5 Flash (low cost, needs OpenRouter credits), then a free model if it fails.
        // Avoid 'openrouter/free': it can route to classifier or reasoning-dump models.
        'models'         => array('google/gemini-2.5-flash', 'google/gemma-4-31b-it:free'),
        'lead_email'     => 'bincoo@kuvani.com',
        'from_email'     => 'noreply@bincoo-mena.com',
        'allowed_hosts'  => array('bincoo-mena.com', 'www.bincoo-mena.com'),
        'max_per_hour'   => 30,
    );
    $file = dirname(rtrim($_SERVER['DOCUMENT_ROOT'], '/')) . '/bincoo-config.php';
    $loaded = is_readable($file) ? include $file : array();
    $config = array_merge($defaults, is_array($loaded) ? $loaded : array());
    return $config;
}

function bm_json($status, $data)
{
    http_response_code($status);
    header('Content-Type: application/json; charset=utf-8');
    header('Cache-Control: no-store');
    echo json_encode($data, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
    exit;
}

/** Only accept JSON POSTs coming from the site's own pages. */
function bm_guard_request()
{
    if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
        bm_json(405, array('error' => 'method_not_allowed'));
    }
    $origin = isset($_SERVER['HTTP_ORIGIN']) ? $_SERVER['HTTP_ORIGIN'] : (isset($_SERVER['HTTP_REFERER']) ? $_SERVER['HTTP_REFERER'] : '');
    $host = strtolower((string) parse_url($origin, PHP_URL_HOST));
    if (!in_array($host, bm_config()['allowed_hosts'], true)) {
        bm_json(403, array('error' => 'forbidden'));
    }
    $raw = file_get_contents('php://input', false, null, 0, 65536);
    $body = json_decode($raw, true);
    if (!is_array($body)) {
        bm_json(400, array('error' => 'bad_request'));
    }
    return $body;
}

/** Simple per-IP sliding-window limit stored in files outside public_html. */
function bm_rate_limit($bucket, $limit)
{
    $dir = dirname(rtrim($_SERVER['DOCUMENT_ROOT'], '/')) . '/bincoo-data/ratelimit';
    if (!is_dir($dir) && !@mkdir($dir, 0700, true)) {
        $dir = sys_get_temp_dir() . '/bincoo-ratelimit';
        @mkdir($dir, 0700, true);
    }
    $ip = isset($_SERVER['REMOTE_ADDR']) ? $_SERVER['REMOTE_ADDR'] : 'unknown';
    $file = $dir . '/' . $bucket . '-' . hash('sha256', $ip) . '.json';
    $now = time();
    $hits = array();
    if (is_readable($file)) {
        $hits = json_decode((string) file_get_contents($file), true);
        $hits = is_array($hits) ? $hits : array();
    }
    $recent = array();
    foreach ($hits as $t) {
        if ($t > $now - 3600) {
            $recent[] = $t;
        }
    }
    if (count($recent) >= $limit) {
        bm_json(429, array('error' => 'rate_limited'));
    }
    $recent[] = $now;
    @file_put_contents($file, json_encode($recent), LOCK_EX);
}

/** Trim, strip control characters and cap the length of user-provided text. */
function bm_clean($value, $max)
{
    $value = is_string($value) ? $value : '';
    $value = preg_replace('/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/u', '', $value);
    $value = trim((string) $value);
    if (function_exists('mb_substr')) {
        return mb_substr($value, 0, $max, 'UTF-8');
    }
    return substr($value, 0, $max);
}
