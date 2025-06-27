<html>
    <head>

    </head>
    <body>
        <?php
        $grupo = array("vaz", "luciano", "vitor", "sofia", "david");
        $i = 0;
        do{
            $aluno = $grupo[1];
            echo $aluno[$i];
            echo $aluno . "<br>";
            $i++;
        }while($i<count($grupo));



        for ($i = 0; $i < count($grupo); $i++)
        {
            $aluno = $grupo[1];
            echo $aluno . "<br>";
        }

        $disciplinas = array("educaçao sexual", "computaria", "anatomia pratica", "duelo de espadas");
        foreach($disciplinas as $value){
            echo $value  ."<br>";
        }
        ?>
    </body>
</html>