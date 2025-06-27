<html>
    <head>

    </head>
    <body>
        <?php

        $f1 = $_POST['f1'];
        $f2 = $_POST['f2'];

        function calcularMedia($f1, $f2){
        return ($f1 + $f2)/2;
        }

        $resultado = calcularMedia($f1, $f2);
        $passou = FALSE;

        if($resultado >= 6){
            $passou = TRUE;
        }
        else{
            $passou = FALSE;
        }
        var_dump($passou); 
        ?>
    </body>
</html> 