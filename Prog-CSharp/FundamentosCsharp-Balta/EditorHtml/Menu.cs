
using System.Drawing;

namespace EditorHtml
{
    public static class Menu
    {

        public static void Mostrar()
        {
            Console.Clear();
            Console.BackgroundColor = ConsoleColor.Blue;
            Console.ForegroundColor = ConsoleColor.Black;

            Tela();
            EscreverOpcoes();

            var opcao = short.Parse(Console.ReadLine() ?? "0");

            ManipularOpcoesMenu(opcao);

        }

        public static void Tela()
        {

            string linha1 = "+" + new string('-', 30) + "+" + "\n";
            string colunas = "|" + new string(' ', 30) + "|" + "\n";

            Console.Write(linha1);
            for (int linhas = 0; linhas <= 10; linhas++)
            {
                Console.Write(colunas);
            }
            Console.Write(linha1);


        }

        public static void EscreverOpcoes()
        {
            Console.SetCursorPosition(3, 2);
            Console.WriteLine("Editor HTML");
            Console.SetCursorPosition(3, 3);
            Console.WriteLine("=====================");
            Console.SetCursorPosition(3, 4);
            Console.WriteLine("Selecione uma opção abaixo: ");
            Console.SetCursorPosition(3, 6);
            Console.WriteLine("1 - Novo Arquivo");
            Console.SetCursorPosition(3, 7);
            Console.WriteLine("2 - Abrir");
            Console.SetCursorPosition(3, 9);
            Console.WriteLine("0 - Sair");
            Console.SetCursorPosition(3, 10);
            Console.Write("Opção: ");

        }

        public static void ManipularOpcoesMenu(short opcao)
        {
            switch (opcao)
            {
                case 1: Editor.Mostrar(); break;
                case 2: break;
                case 0:
                    {
                        Console.Clear();
                        Environment.Exit(0);
                        break;
                    }
                default: Console.WriteLine("Opção Inválida!"); break;
            }
        }
        
        
    }
}