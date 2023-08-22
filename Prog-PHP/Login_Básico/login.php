<?php
$user = $_POST['user']; // Guardando o user/senha de acordo com o noma definido no formulário HTML
$pass = $_POST['pass']; // utilizamos o $_POST pois foi o método no formulário, se usar o get, utiliza o $_GET

if($user == 'root' && $pass == 'root'){ // verificando se foi digitado o equivalente a root para user e senha
    echo "Login Realizado com Sucesso"; // se sim o login é realizado com sucesso
}
else{
    echo "Login Inválido";
}
?>