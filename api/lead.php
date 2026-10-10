<?php
// Lead endpoint: emails a contact request from the chat widget to the Bincoo MENA team.
define('BINCOO_API', true);
require __DIR__ . '/_lib.php';

$body = bm_guard_request();
$config = bm_config();

// Honeypot: real visitors never fill this hidden field.
if (bm_clean(isset($body['website']) ? $body['website'] : '', 200) !== '') {
    bm_json(200, array('ok' => true));
}
bm_rate_limit('lead', 5);

$name     = bm_clean(isset($body['name']) ? $body['name'] : '', 120);
$company  = bm_clean(isset($body['company']) ? $body['company'] : '', 160);
$country  = bm_clean(isset($body['country']) ? $body['country'] : '', 80);
$phone    = bm_clean(isset($body['phone']) ? $body['phone'] : '', 40);
$email    = bm_clean(isset($body['email']) ? $body['email'] : '', 160);
$interest = bm_clean(isset($body['interest']) ? $body['interest'] : '', 80);
$message  = bm_clean(isset($body['message']) ? $body['message'] : '', 1500);

$emailValid = $email !== '' && filter_var($email, FILTER_VALIDATE_EMAIL);
if ($name === '' || $country === '' || ($phone === '' && !$emailValid)) {
    bm_json(422, array('error' => 'missing_fields'));
}

// Last few chat turns, so the team sees what was already discussed.
$transcript = '';
if (isset($body['transcript']) && is_array($body['transcript'])) {
    foreach (array_slice($body['transcript'], -10) as $m) {
        if (!is_array($m) || !isset($m['role'], $m['content'])) {
            continue;
        }
        $who = $m['role'] === 'user' ? 'Visitor' : 'Assistant';
        $transcript .= $who . ': ' . bm_clean($m['content'], 800) . "\n\n";
    }
}

$lines = array(
    'New contact request from the Bincoo MENA website chat',
    '',
    'Name: ' . $name,
    'Company: ' . ($company !== '' ? $company : '-'),
    'Country: ' . $country,
    'Phone / WhatsApp: ' . ($phone !== '' ? $phone : '-'),
    'Email: ' . ($emailValid ? $email : '-'),
    'Interested in: ' . ($interest !== '' ? $interest : '-'),
    '',
    'Message:',
    $message !== '' ? $message : '-',
);
if ($transcript !== '') {
    $lines[] = '';
    $lines[] = '--- Chat transcript ---';
    $lines[] = trim($transcript);
}
$text = implode("\n", $lines) . "\n";

$subjectText = 'New website lead: ' . ($company !== '' ? $company : $name) . ' (' . $country . ')';
$subject = '=?UTF-8?B?' . base64_encode($subjectText) . '?=';
$headers = array(
    'From: Bincoo MENA Website <' . $config['from_email'] . '>',
    'MIME-Version: 1.0',
    'Content-Type: text/plain; charset=UTF-8',
    'Content-Transfer-Encoding: 8bit',
);
if ($emailValid) {
    $headers[] = 'Reply-To: ' . $email;
}

$sent = @mail($config['lead_email'], $subject, $text, implode("\r\n", $headers), '-f' . $config['from_email']);
if (!$sent) {
    error_log('bincoo lead: mail() failed');
    bm_json(502, array('error' => 'mail_failed'));
}
bm_json(200, array('ok' => true));
