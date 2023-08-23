

<?php
$numero = $_POST['numero']; // pegando as variáveis do FORM HTML pelo método POST
$inicia = $_POST['inicia'];
$termina = $_POST['termina'];

if($inicia > $termina){ // no caso do user digitar um número maior no "inicia" do que no "termina"
    echo "<script>alert('O número que inicia tem que ser menor ou igual ao que termina');</script>"; // alert para criar aviso na tela
    echo "<script>window.location.href = 'index.html';</script>"; // utilizando do <script> -> Javascript e location.href para redirecionamento após aviso
}

echo "<h1><b>Tabuada do $numero</b></h1>"; 
echo "<h2>Iniciando em: $inicia<br>Terminando em: $termina</h2>";
for($inicia; $inicia<=$termina; $inicia++){ // utilizando loop FOR para realizar a tabuada
    $resultado = $numero * $inicia; // realizando a multiplicação
    echo "<h3>$numero x $inicia = $resultado</h3>"; 
}

?>