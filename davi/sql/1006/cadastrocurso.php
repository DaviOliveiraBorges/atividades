<?php
// sql.php
$host = "localhost";
$user = "root";
$pass = ""; // senha padrão do XAMPP é vazia
$db = "sis_academico";

$conn = mysqli_connect($host, $user, $pass, $db);

if (!$conn) {
    die("Falha na conexão: " . mysqli_connect_error());
}
?>


<?php
$nome = $_POST['aluno'] ?? null;
$curso = $_POST['curso'] ?? null;

if ($nome && $curso) {
    require("mysql.php"); 

    $stmt = mysqli_prepare($conn, "INSERT INTO matricula (nome, curso) VALUES (?, ?)");
    mysqli_stmt_bind_param($stmt, "ss", $nome, $curso);

    if (mysqli_stmt_execute($stmt)) {
        echo "Aluno cadastrado com sucesso!";
    } else {
        echo "Erro ao cadastrar aluno: " . mysqli_error($conn);
    }

    mysqli_stmt_close($stmt);
    mysqli_close($conn);
} else {
    echo "Por favor, preencha todos os campos.";
}
?>