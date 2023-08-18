<?php
class Pessoa {
    private $nome;
    private $idade;
    
    public function __construct($nome, $idade) {
        $this->nome = $nome;
        $this->idade = $idade;
    }
    
    public function apresentar() {
        echo "Olá, eu sou {$this->nome} e tenho {$this->idade} anos.";
    }
}

$pessoas = [
    new Pessoa("Alice", 25),
    new Pessoa("Bob", 30),
    new Pessoa("Carol", 28)
];

foreach ($pessoas as $pessoa) {
    $pessoa->apresentar();
    echo "<br>";
}

$idadeMedia = array_reduce($pessoas, function($acumulador, $pessoa) {
    return $acumulador + $pessoa->idade;
}, 0) / count($pessoas);

echo "A idade média das pessoas é: " . $idadeMedia . " anos.";
?>
