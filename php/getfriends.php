<?php

require_once('src/snapchat.php');

// Log in:
$snapchat = new Snapchat('snapmecatz', 'fuckyoni');

$friends = $snapchat->getFriends();

foreach ($friends as $a) {
    // Note that there is no $b here.
    $output=print_r("$a->name,", true);
    file_put_contents('friends.txt', $output, FILE_APPEND);
  }
?>