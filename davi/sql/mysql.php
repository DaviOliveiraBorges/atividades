<?php
$host = "localhost";
$user = "root";
$pass = ""; 
$db = "sis_academico";

$conn = mysqli_connect($host, $user, $pass, $db);

if (!$conn) {
    die("Falha na conexão: " . mysqli_connect_error());
}
?>
