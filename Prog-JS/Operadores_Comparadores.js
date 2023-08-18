
// Operadores Matemáticos

/*
+      Adição              a + b       Soma dos valores a e b
-      Subtração           a - b       Diferença entre a e b
*      Multiplicação       a * b       Produto dos valores a e b
/      Divisão             a / b       Quociente da divisão entre a e b
%      Módulo              a % b       Resto da divisão entre a e b
**     Exponenciação       a ** b      a elevado à potência b
*/

const valor1 = 100
const valor2 = 50

console.log(valor1 - valor2, valor1 + valor2)
console.log(valor1 * valor2, valor1 / valor2)
console.log(valor1 % valor2 ) // % -> resto da divisão

// Operadores lógicos

/*
==     Igual                    a == b      Verdadeiro se A for igual a b
!=     Diferente                a != b      Verdadeiro se A não for igual a b
===    Estritamente Igual       a === b     Verdadeiro se A for igual a b e do mesmo tipo
!==    Estritamente Diferente   a !== b     Verdadeiro se A não for igual a b e/ou não for do mesmo tipo
>      Maior que                a > b       Verdadeiro se   a for maior que b
<      Menor que                a < b       Verdadeiro se a for menor que b
>=     Maior ou Igual a         a >= b      Verdadeiro se a for maior ou igual a b
<=     Menor ou Igual a         a <= b      Verdadeiro se a for menor ou igual a b
&&     E lógico                 a && b      Verdadeiro se tanto a quanto b forem verdadeiros
||     Ou lógico                a || b      Verdadeiro se pelo menos um dos valores (a ou b) for verdadeiro
!      Negação                  !a          Verdadeiro se a for falso, e vice-versa
*/

const a = 10
const b = "10"
const c = true
console.log(a==b) // True
console.log(a!=b) // false
console.log(a===b) // false -> ele considera o tipo (number/string)
console.log(a>=b) // True -> pois é igual
console.log(a==b && a>=b) // True 
console.log(a==b || a!=b) // True -> apenas uma das comparações tem que ser Verdadeira
console.log(!c) // False -> pois c é True (se c for false, ele retorna True)