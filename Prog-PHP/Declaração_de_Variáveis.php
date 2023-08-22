<!DOCTYPE html>
<html>

<head>
    <title>Servidor</title>
</head>

<body>
    <!--  Abrindo tag PHP dentro do HTML  -->
    <?php

    // ECHO E DECLARAÇÃO DE VARIÁVEL

    echo "Olá mundo"; // print comum (pode ser utilizado aspas simples e/ou duplas)
    $nome = "Nome"; // declarando variável 
    $idade = 20; // declarando variável inteira
    echo "$nome $idade"; // duas formas de printar as variáveis
    echo $nome.$idade; // ponto e virgula é obrigatório ao final de cada linha em PHP


    // OPERADORES MATEMÁTICOS

    $a = 10; // declarando variável inteira
    $b = 20; // declarando variável inteira
    $c = $a + $b; // atribuindo valor a variável
    echo $c; // imprimindo variável inteira
    echo "$a + $b"; // realizando a conta diretamente no echo
    
    // HTML + PHP
    echo "<center>"; // utilizando para centralizar
    echo "<b>$nome</b><br>"; // deixando em negrito e dando espaçamento
    echo "<b>$a</b><br>"; // pode-se trabalhar de qualquer forma mesclando ambos 
    

    ?>
</body>
</html>