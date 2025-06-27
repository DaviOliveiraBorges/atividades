<html>
    <head>

    </head>
    <body>
        <?php
        $n1 = $_POST['n1'];
        $n2 = $_POST['n2'];

        function imprimirNumerosEntre($n1, $n2) {
            $inicio = min($n1, $n2);
            $fim = max($n2, $n2);
        
            echo "os numeros entre " . $n1 . " e " . $n2 . " são ";
            for ($i = $inicio; $i <= $fim; $i++) {
                echo $i . " ";
            }
        }

        echo imprimirNumerosEntre($n1, $n2);
        echo "<br>";
        echo "o maior numero " . max($n1, $n2);
        ?>

    </body>
</html> 