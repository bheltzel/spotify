<?php

require_once(__DIR__ . '/db/db.php');

$db = New db;
$sql = "select rank + 1 as song_rank, song, artist from chart where chart_type = 'medium_term'";
$r = $db -> select($sql);

echo(json_encode($r));

