<!DOCTYPE html>
<html>
<head>
    
</head>
<body>
    <?php
    // Declarando as varáveis
    $a = 10;
    $b = 20;
    $soma = $a + $b; // variável com a soma
    
    if ($soma == 30){ // a condição deve está dentro de parênteses e a abertura feita com chaves
        echo "A soma é igual a 30"; // lembrar do ponto e vírgula ao final
    }
    elseif ($soma == 50){ // elseif mesmo resultado de elif(em python)
        echo "A soma é igual a 50";
    }
    else{ 
        echo "A soma é diferente de  30";
    }


    // Fazendo um login com IF/ELSE básico
    $user = "root"; 
    $password = "root"; 
    if($user == "root" && $password == "root"){ // onde user e password devem ser ambos igual a "root"
        echo "<h1>Bem vindo ao servidor $user!</h1>"; // echo com HTML organizado, e chamando o nome do user para apresentação
    }
    else{
        echo "<h1>Usuário ou senha incorreto!</h1>";
    }
    ?>

</body>
</html>