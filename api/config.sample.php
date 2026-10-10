<?php
// TEMPLATE ONLY. Do not put real keys in this file or anywhere in the repo.
// Create a copy named bincoo-config.php in the cPanel home folder (/home/bincoomena/),
// next to public_html, NOT inside it, and paste the OpenRouter key there.
return array(
    'openrouter_key' => 'PASTE-YOUR-OPENROUTER-KEY-HERE',

    // Free models, tried in order. To upgrade later, e.g. 'anthropic/claude-haiku-5.5'.
    'models' => array(
        'google/gemma-4-31b-it:free',
        'nvidia/nemotron-3-super-120b-a12b:free',
        'openrouter/free',
    ),

    // Where contact requests from the chat are emailed.
    'lead_email' => 'bincoo@kuvani.com',
);
