<?php

require_once('snapchat.php')

// Log in:
$snapchat = new Snapchat('username', 'password');

$friends = $snapchat->getFriends();

echo "$friends"
?>