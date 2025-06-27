<?php
$conexao = mysqli_connect("localhost", "root", "", "sis_academico");

if (!$conexao) {
    die("Não foi possível conectar ao banco de dados, erro detectado: " . mysqli_connect_error());
}

mysqli_set_charset($conexao, 'utf8');

echo 'Conexão bem sucedida<br>';

$novocurso = 'Programação Web';
$atualizar = "UPDATE matricula SET curso= '$novocurso' WHERE curso= 'Desenvolvimento Web'";

$apagar = "DELETE from matricula WHERE nome= 'Deyse Pereira'";

if (mysqli_query($conexao, $atualizar)) {
    echo "Dados atualizados com sucesso!";
} else {
    echo "Erro ao atualizar dados: " . mysqli_error($conexao);
}



mysqli_close($conexao);
?>
