
// ==============================================================================================================

// Declaração de variáveis  

// Usando o CONST, ela possui propriedades de Imutabilidade 
const nome1 = "Teste const"

// Usando o LET, ela possui propriedades de Mutabilidade mais simples e escopo em bloco, segue exemplo:
let nome2 = "Teste let" 
nome2 = "let" // dessa forma não estou redeclarando e sim alterando o valor

// Usando o VAR, ele possui propriedades de Mutabilidade mais elevadas e possui escopo global, segue exemplo:
var nome3 = "Teste var" 
var nome3 = "Teste" // dessa forma não estou alterando valor e sim redeclarando
nome3 = "var"

console.log(nome1, nome2, nome3)

// Nomes que não podem ser variáveis pois possuem outros usos no JS
/* 
abstract arguments boolean break byte case catch char class* const
continue debugger default delete do double else enum* eval export* 
extends* false final finally float for function goto if implements
import* in instanceof in interface let long native new null package 
private protected public return short static super* switch synchronized 
this throw throws transient true try typeof var void volatile while with
*/

