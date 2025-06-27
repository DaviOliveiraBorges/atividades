<html>
    <head>

    </head>
    <body>
        <?php
        function valorDivisivel($n1, $n2){
            if($n1 % $n2 == 0){
                echo "os valores sao divisiveis";
            }   
            else{
                echo "os valores naos ao dividiveis";
            }
        }

        echo valorDivisivel(8, 4)
        ?>
    </body>
</html> 