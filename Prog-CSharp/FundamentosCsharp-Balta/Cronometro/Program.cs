namespace Cronometro
{
    class Program
    {
        static void Main(string[] args)
        {
            Menu();
        }

        static void Menu()
        {
            Console.Clear();
            Console.WriteLine("S = Segundo");
            Console.WriteLine("M = Minuto");
            Console.WriteLine("0 = Sair");
            Console.WriteLine("Quanto tempo deseja contar?");

            string entrada = Console.ReadLine() ?? "";
            entrada = entrada.ToLower();

            char tipo = entrada[^1];
            int tempo = int.Parse(entrada[..^1]);
            int multiplicador = 1;


            if (tipo == 'm') multiplicador = 60; // Lembrar que CHAR é aspas simples
            if (tempo == 0) System.Environment.Exit(0);

            Iniciar(tempo * multiplicador);
        
        }

        static void Iniciar(int tempo)
        {
            int tempoatual = 0;

            while (tempoatual != tempo)
            {
                Console.Clear();
                tempoatual++;
                Console.WriteLine(tempoatual);
                Thread.Sleep(1000);
            }

            Console.Clear();
            Console.WriteLine("Cronometro Finalizado!");
            Thread.Sleep(3000);
            Menu();

        }
    }
}
