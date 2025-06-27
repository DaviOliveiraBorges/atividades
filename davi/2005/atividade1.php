<html>
    <head>

    </head>
    <body>
        <?php

        $n1 = $_POST['n1'];
        $n2 = $_POST['n2'];
        $n3 = $_POST['n3'];

        function numeroMaior($n1, $n2, $n3){
        return (max($n1, $n2, $n3));
        }
        echo numeroMaior($n1, $n2, $n3);
        ?>
    </body>
</html> 