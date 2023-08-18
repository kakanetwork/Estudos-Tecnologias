
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

// ==============================================================================================================

// Tipos de dados

const string = "Texto" // tipo string
const number = 10 // tipo numero (pode ser float)
const boolean = true // tipo bool
const object = {nome: "Meu_nome", sobrenome: "Meu_sobrenome"} // object formado por chave:valor (semelhante a dict em python)
const array = [{fruta: "banana"}, {fruta: "maçã"}] // array guarda vários objects, semelhante a lista de dict's em python

// typeof para verificar o tipo da variável
console.log(typeof number, typeof string, typeof boolean, typeof object, typeof array)

console.log(string, number, boolean)
console.log(object, object.nome, object.sobrenome) // pode se chamar todos os itens, ou apenas os especificados após "."

// no array pode se chamar todos os objects (1° caso)
// chamar apenas o objeto especificado pela sua posição (2° caso)
// chamar apenas o item dentro do objeto (3° caso)
console.log(array, array[0], array[1].fruta) 


// ==============================================================================================================
