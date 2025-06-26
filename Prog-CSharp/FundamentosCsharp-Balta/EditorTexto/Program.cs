namespace EditorTexto;

class Program
{
    static void Main(string[] args)
    {
        Menu();
    }

    static void Menu()
    {
        Console.Clear();
        Console.WriteLine("O que deseja fazer?");
        Console.WriteLine("1 - Abrir Arquivo");
        Console.WriteLine("2 - Criar Novo Arquivo");
        Console.WriteLine("0 - Sair");
        Console.WriteLine("");
        short opcao = short.Parse(Console.ReadLine() ?? "");

        switch (opcao)
        {
            case 1: AbrirArquivo(); break;
            case 2: CriarArquivo(); break;
        }
    }
    static void AbrirArquivo()
    {
        Console.Clear();
        Console.WriteLine("Qual o caminho do arquivo? (Digite ./{nome_arquivo.txt} para procurar na pasta atual)");

        string caminho = Console.ReadLine() ?? "";

        if (caminho[..2] == "./") caminho = Path.Combine(Directory.GetCurrentDirectory(), caminho[2..]);

        using (var arquivo = new StreamReader(caminho))
        {
            string texto = arquivo.ReadToEnd();
            Console.WriteLine("");
            Console.WriteLine($"Conteúdo do Arquivo {caminho}:");
            Console.WriteLine($"{texto}");
        }

        Console.WriteLine("");
        Console.WriteLine("Voltando pro menu...");
        Thread.Sleep(5000);
        Menu();

    }

    static void CriarArquivo()
    {
        Console.Clear();
        Console.WriteLine("Digite seu texto abaixo (ESC para salvar)");
        Console.WriteLine("-----------------------");
        string texto = "";

        do
        {
            texto += Console.ReadLine();
            texto += Environment.NewLine;
        }
        while (Console.ReadKey().Key != ConsoleKey.Escape);
        {
            Console.Write(texto);
        }

        SalvarArquivo(texto);

    }

    static void SalvarArquivo(string texto)
    {
 
        string nomeArquivo = Console.ReadLine() ?? "novo_arquivo";

        string caminho = Path.Combine(Directory.GetCurrentDirectory(), nomeArquivo); // formando o caminho do arquivo (atual de execução)

        using (var arquivo = new StreamWriter(caminho))
        {
            arquivo.Write(texto);
        }   



    }
}
