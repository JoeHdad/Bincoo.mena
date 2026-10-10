<?php
// TEMPLATE ONLY. Do not put real keys in this file or anywhere in the repo.
// Create a copy named bincoo-config.php in the cPanel home folder (/home/bincoomena/),
// next to public_html, NOT inside it, and paste the OpenRouter key there.
return array(
    'openrouter_key' => 'PASTE-YOUR-OPENROUTER-KEY-HERE',

    // Optional: models tried in order. Default is Gemini 2.5 Flash, then a free Gemma model.
    // 'models' => array('google/gemini-2.5-flash', 'google/gemma-4-31b-it:free'),

    // Where contact requests from the chat are emailed.
    'lead_email' => 'bincoo@kuvani.com',
);
