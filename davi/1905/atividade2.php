<html>
    <head>

    </head>
    <body>
        <?php

        $altura = $_POST['altura'];
        $peso = $_POST['peso'];
        $resultado = $peso/($altura**2);

            if($resultado < 17){
                echo 'muito abaixo do peso';
            }
            if ($resultado > 17 & $resultado < 18.49){
                echo 'abaixo do peso';}
            if ($resultado > 18.50 & $resultado < 24.99){
                echo "peso normal";}
            if( $resultado > 25 & $resultado < 29.99){
                echo "acima do peso";}
            if ($resultado > 30 & $resultado < 39.99){
                echo "obesidade";}
        ?>
    </body>
</html> 