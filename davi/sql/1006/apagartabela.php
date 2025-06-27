<?php
$conexao = mysqli_connect("localhost", "root", "", "");

if (!$conexao) {
    die("Não foi possível conectar ao banco de dados, erro detectado: " . mysqli_connect_error());
}

mysqli_set_charset($conexao, 'utf8');

echo 'Conexão bem sucedida<br>';

$apagar = "DROP DATABASE teste";

if (mysqli_query($conexao, $apagar)) {
    echo 'O banco de dados foi apagado.<br>';
} else {
    echo 'Deu erro na remoção do banco: ' . mysqli_error($conexao) . '<br>';
}

mysqli_close($conexao);
?>
