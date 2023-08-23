<?php

// Cookies são armazenados no lado cliente
// em sites HTTP os cookies podem ser capturados, podendo vazar informações sensíveis
$cookie_name = "user_cookie"; 
$cookie_value = "valor_cookie";
setcookie($cookie_name, $cookie_value); // no PHP assim criamos um cookie, com nome e valor (pode ter + parâmetros)
echo $_COOKIE['user_cookie'];

// Sessões são armazenados no lado servidor (o ID da sessão é enviado via cookie para o seu navegador)
// cada usuário no site vai possuir uma hash/id de sessão único
session_start(); // assim iniciamos uma nova sessão
$email = "test@example.com"; // definindo email como autenticador
$_SESSION['email'] = $email; // criando sessão
echo $_SESSION['email']; 

?>