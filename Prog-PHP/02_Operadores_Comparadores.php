<?php
// Operadores Matemáticos

/*
+      Adição              $a + $b       Soma dos valores $a e $b
-      Subtração           $a - $b       Diferença entre $a e $b
*      Multiplicação       $a * $b       Produto dos valores $a e $b
/      Divisão             $a / $b       Quociente da divisão entre $a e $b
%      Módulo              $a % $b       Resto da divisão entre $a e $b
**     Exponenciação       $a ** $b      $a elevado à potência $b
*/
    
$valor1 = 100;
$valor2 = 50;

echo $valor1 - $valor2, " ", $valor1 + $valor2, "\n";
echo $valor1 * $valor2, " ", $valor1 / $valor2, "\n";
echo $valor1 % $valor2, "\n";

// Operadores lógicos

/*
==     Igual                    $a == $b      Verdadeiro se $a for igual a $b
!=     Diferente                $a != $b      Verdadeiro se $a não for igual a $b
===    Estritamente Igual       $a === $b     Verdadeiro se $a for igual a $b e do mesmo tipo
!==    Estritamente Diferente   $a !== $b     Verdadeiro se $a não for igual a $b e/ou não for do mesmo tipo
>      Maior que                $a > $b       Verdadeiro se   $a for maior que $b
<      Menor que                $a < $b       Verdadeiro se $a for menor que $b
>=     Maior ou Igual a         $a >= $b      Verdadeiro se $a for maior ou igual a $b
<=     Menor ou Igual a         $a <= $b      Verdadeiro se $a for menor ou igual a $b
&&     E lógico                 $a && $b      Verdadeiro se tanto $a quanto $b forem verdadeiros
||     Ou lógico                $a || $b      Verdadeiro se pelo menos um dos valores ($a ou $b) for verdadeiro
!      Negação                  !$a           Verdadeiro se $a for falso, e vice-versa
*/

$a = 10;
$b = "10";
$c = true;
echo $a == $b, "\n"; // True
echo $a != $b, "\n"; // false
echo $a === $b, "\n"; // false -> ele considera o tipo (number/string)
echo $a >= $b, "\n"; // True -> pois é igual
echo ($a == $b) && ($a >= $b), "\n"; // True 
echo ($a == $b) || ($a != $b), "\n"; // True -> apenas uma das comparações tem que ser Verdadeira
echo !$c, "\n"; // False -> pois $c é True (se $c for false, ele retorna True)

?>
