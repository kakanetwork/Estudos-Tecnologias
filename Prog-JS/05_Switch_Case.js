
const variavel = "var"

// Switch indicado para evitar o uso de IF's
switch (variavel){ 
    case "aula":
        console.log("A variável é aula")
        break // cada case deve possuir um break, se não o código roda todas opções
    case "video":
        console.log("A variável é video")
        break
    case "var":
        console.log("A variável é Var")
        break
    default: // default seria equivalente a um Else
        console.log("A variável não é nenhum dos valores acima")
        break
}