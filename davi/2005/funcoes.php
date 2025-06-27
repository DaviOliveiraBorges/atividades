<html>
    <head>

    </head>
    <body>
        <?php
        $x = "sistemaacademico";
        echo strlen($x);
        echo "<br>";
        echo ucfirst($x);
        echo "<br>";
        $texto = "sistema academico: divulgação de nota de alunos";
        echo str_replace("nota", "media", $texto);
        echo "<br>";
        echo strtoupper($texto);
        echo "<br>";
        echo strtolower($texto);
        echo "<br>";
        echo date($texto);
        echo "<br>";
        echo gettype($texto);
        echo "<br>";
        echo "SETTYPE";
        echo "<br>";    
        $num = 45;        
        settype($num, "string");
        echo gettype($num); 
        echo "<br>";
        echo $num;  
        ?>
    </body>
</html>
