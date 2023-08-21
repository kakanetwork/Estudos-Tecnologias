
// Funções 

// pode utilizar a função com o console.log e sem nenhum parâmetro
function funcao1(){
    console.log('Função ativada')
}   
funcao1()

// da mesma forma que a função pode ter os parâmetros
function funcao2(valor1, valor2) {
    console.log(valor1 + valor2)
}
funcao2(10, 20)

// outra forma de utilizar as funções com o Return 
function funcao3(valor1, valor2, valor3) {
    return valor1 + valor2 + valor3
}

// e a saída podem ser de várias formas, desde a função direta no console
// ou sendo atribuída a uma variável
let retorno = funcao3(10, 20, 30)
console.log(retorno)
console.log(funcao3(10, 20, 30))