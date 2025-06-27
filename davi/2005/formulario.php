<html>
    <head>

    </head>
    <body>
        <?php

        $n1 = $_POST['n1'];
        $n2 = $_POST['n2'];
        $faltas = $_POST['faltas'];

        function calcularMedia($n1, $n2){
        return ($n1 + $n2)/2;
        }

        $resultado = calcularMedia($n1, $n2);

        if($resultado >= 6 && $resultado <=  10 && $faltas < 32){
            echo "aluno aprovado com nota ". $resultado;
        }
        elseif ($resultado < 6 && $resultado >= 4 && $faltas < 32) {
            echo "aluno em recuperação com nota " . $resultado;
        }
        elseif($resultado < 4 || $faltas > 32){
            echo "aluno reprovado";
        }
        else{
            echo "preencha novamente o formulario";
        }
        ?>
    </body>
</html> 