
const a = 10
const b = 20

// toda estrutura condicional se abre com {}
// a condição deve está entre ()

if (a > b){ 
    console.log('A é maior que B')
}

// else if tem a mesma simbologia do elif em python
else if(a < b){
    console.log('A é menor que B')
}

// else no caso das outras condições não serem atendidas
else {  
    console.log('A é igual a B')
}

// if ternário -> simplifica a utilização do IF para pequenas condições /  limite de 2 resultados apenas 
let resultado = a == b ? "Verdadeiro" : "Falso";
console.log(resultado)

let resultado2 = a == b || a < b ? "Verdadeiro" : "Falso";
console.log(resultado2)