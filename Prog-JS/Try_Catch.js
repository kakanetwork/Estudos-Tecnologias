
// Try e Catch (semelhante a Try Except no python)

try{ // iniciamos com o Try e dentro colocaremos o bloco/código a ser tratado
    const a = 10
    if(a == b){ // inserindo erro proposital (b não declarado)
        console.log('A é igual a B')
    }
}
catch(e){ // catch (semelhante ao except python) com uso do (e) para capturar erro
    console.log('Um erro ocorreu...' + e) // mostrando erro capturado, o código continua 
}

console.log('Continuação') // sem o Try/Catch esse trecho não seria executado 