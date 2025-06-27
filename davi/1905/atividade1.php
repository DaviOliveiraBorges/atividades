<html>
    <head>

    </head>
    <body>
        <?php

        $n1 = $_POST['n1'];
        $n2 = $_POST['n2'];
        $calc = $_POST['calcular'];
        switch($calc){
            case 'soma':
                echo $n1 + $n2;
                break;
            case 'subtracao':
                echo $n1 - $n2;
                break;
            case 'multiplicacao':
                echo $n1 * $n2;
                break;
            case 'divisao':
                echo $n1 / $n2;
                break;
            default:
                echo 'preencha o formulario novamente';
                break;
        }
        ?>
    </body>
</html> 