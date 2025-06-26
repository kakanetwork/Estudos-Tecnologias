using System.Text;

namespace EditorHtml
{
    public static class Editor
    {

        public static void Mostrar()
        {

            Console.Clear();
            Console.BackgroundColor = ConsoleColor.White;
            Console.ForegroundColor = ConsoleColor.Black;
            Console.Clear();
            Console.WriteLine("Modo Editor");
            Console.WriteLine("---------------------");

            Iniciar();

        }

        public static void Iniciar()
        {

            var texto = new StringBuilder();

            do
            {
                texto.AppendLine(Console.ReadLine());
            }
            while (Console.ReadKey().Key != ConsoleKey.Escape);

            Console.WriteLine("---------------------");
            Console.WriteLine("Deseja Salvar o arquivo?");
            Console.WriteLine("1 - Salvar");
            Console.WriteLine("0 - Sair");
            short opcaoSalvar = short.Parse(Console.ReadLine() ?? "0");

            if (opcaoSalvar == 1) SalvarArquivo(texto);
            else if (opcaoSalvar == 0) Environment.Exit(0);
            else Console.WriteLine("Opção Inválida!"); Environment.Exit(0);

        }

        public static void SalvarArquivo(StringBuilder texto)
        {

            Console.Clear();
            Console.WriteLine("Escolha o nome do arquivo (Insira a extensão): ");
            string nomeArquivo = Console.ReadLine() ?? "novo_arquivo";
            nomeArquivo = nomeArquivo.Trim(); // Remove espaços no início e fim
            nomeArquivo = nomeArquivo.Replace(" ", "_"); // Substitui espaços por _
            string caminho = Path.Combine(Directory.GetCurrentDirectory(), nomeArquivo); // formando o caminho do arquivo (atual de execução)

            using (var arquivo = new StreamWriter(caminho))
            {
                arquivo.Write(texto);
            }

        }

    }
}