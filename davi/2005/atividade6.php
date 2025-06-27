<html>
    <head>

    </head>
    <body>
        <?php

    $numeros = [5, 5, 3, 7, 7, 7]; 
    $iguais = 0;

    for ($i = 1; $i < count($numeros); $i++) {

        if ($numeros[$i] == $numeros[$i - 1]) {
            echo "O número " . $numeros . " é igual ao anterior   ";
            $iguais++;
        }
    }

    echo "Total de números iguais ao anterior" . $iguais;
    ?>

    </body>
</html> 