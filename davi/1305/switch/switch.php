<html>
    <head>

    </head>
    <body>
        <?php
        $mod = $_POST['curso'];
        switch($mod){
            case 'm':
                echo 'manutenção de computadores: de manha e de  noite';
                break;
            case 'r':
                echo 'rede de computadores: tarde';
                break;
            case 'p':
                echo 'programação de computadpres: tarde e noite';
                break;
            case 'w':
                echo 'programação web: manhã e tarde';
                break;
            default:
                echo 'preencha o formulario novamente';
                break;
        }
        ?>
    </body>
</html>