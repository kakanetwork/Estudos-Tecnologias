
/* 
FOR -> 
i = 0; é onde se inicia a contagem
i <= 10; É a condição/até onde vai
i++; soma +1 ao i a cada loop
*/
for(i = 0; i <= 10; i++){
    console.log(i)
}

// Utilizando FOR para percorrer itens dentro de objeto (semelhante ao for in lista no python)
// lembrar de declarar x como let ou var
let object = {casa: "verde", portao: "azul", parede: "branca"}
for(let x in object){ // Utiliza-se o "in" para percorrer itens
    console.log(x) // dessa forma apenas as chaves serão percorridas
    console.log(object[x]) // dessa forma apenas os Valores
    console.log('Obj: ' + x + '| cor: ' + object[x]) // dessa forma ambos respectivamente nas suas posições
}

// Utilizando FOR para percorrer objetos dentro de arrays 
let array = [{casa: "verde", portao: "azul", parede: "branca"},
             {casa: "vermelho", portao: "cinza", parede: "verde"},
             {casa: "roxo", portao: "preto", parede: "rosa"}]

for (let x of array){ // utiliza-se o "of" para percorrer arrays
    console.log(x) // dessa forma ira mostrar os objetos do array por completo
    console.log(x.casa) // dessa forma ira pegar apenas o valor de cada chave dentro de cada objeto
    console.log('Cada: ' + x.casa + ' | Portão: ' + x.portao + ' | Parede: ' + x.parede) // dessa forma ira mostrar cada objeto separadamente organizado
}