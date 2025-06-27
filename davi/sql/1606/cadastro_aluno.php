<?php
require("../mysql.php");

if (!$conn) {
    die("Falha na conexão: " . mysqli_connect_error());
}

$nome = $_POST['aluno'] ?? '';
$cpf = $_POST['cpf'] ?? '';
$complemento = $_POST['complemento'] ?? '';
$cep = $_POST['cep'] ?? '';
$bairro = $_POST['bairro'] ?? '';
$cidade = $_POST['cidade'] ?? '';
$estado = $_POST['estado'] ?? '';
$telefone = $_POST['telefone'] ?? '';

if ($nome && $cpf && $bairro && $cidade && $estado) {  

    $stmt = mysqli_prepare($conn, "INSERT INTO aluno (nome, cpf, complemento, cep, bairro, cidade, estado, telefone) VALUES (?, ?, ?, ?, ?, ?, ?, ?)");
    mysqli_stmt_bind_param($stmt, "ssssssss", $nome, $cpf, $complemento, $cep, $bairro, $cidade, $estado, $telefone);

}

    if (mysqli_stmt_execute($stmt)) {
        echo "Aluno cadastrado com sucesso!";
    } else {
        echo "Erro ao cadastrar aluno: " . mysqli_error($conn);
    }

    mysqli_stmt_close($stmt);
    mysqli_close($conn);
?>
