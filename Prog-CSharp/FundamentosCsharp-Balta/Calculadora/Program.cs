// See https://aka.ms/new-console-template for more information

namespace Calculadora
{
    class Program
    {
        static void Main(string[] args)
        {
            Menu();
        }

        static void Menu()
        {
            while (true)
            {

                // Console.Clear();
                Console.WriteLine("Calculadora");

                Console.WriteLine("=== MENU ===");
                Console.WriteLine("Escolha a Operação que deseja utilizar: ");

                Console.WriteLine("1 - Somar");
                Console.WriteLine("2 - Subtrair");
                Console.WriteLine("3 - Multiplicar");
                Console.WriteLine("4 - Dividir");
                Console.WriteLine("0 - Sair");
                Console.Write("Escolha uma operação: ");
                string? escolha = Console.ReadLine();

                if (escolha == "0") break;

                Console.Write("Digite o primeiro número: ");
                string? entrada1 = Console.ReadLine();

                Console.Write("Digite o segundo número: ");
                string? entrada2 = Console.ReadLine();

                if (!string.IsNullOrWhiteSpace(entrada1) && !string.IsNullOrWhiteSpace(entrada2))
                {
                    float num1 = float.Parse(entrada1);
                    float num2 = float.Parse(entrada2);

                    switch (escolha)
                    {
                        case "1": Soma(num1, num2); break;
                        case "2": Subtracao(num1, num2); break;
                        case "3": Multiplicacao(num1, num2); break;
                        case "4": Divisao(num1, num2); break;
                        default: Console.WriteLine("Opção Inválida!"); break;
                    }

                }
                else
                {
                    Console.WriteLine("Um dos valores informados é inválido!");
                }

                Console.WriteLine("Pressione qualquer tecla para continuar...");
                Console.ReadKey();
            }
            
        }

        static void Soma(float num1, float num2)
        {
            Console.WriteLine($"Resultado: {num1 + num2}");
        }

        static void Subtracao(float num1, float num2)
        {
            Console.WriteLine($"Resultado: {num1 - num2}");
        }

        static void Divisao(float num1, float num2)
        {
            if (num2 == 0) Console.WriteLine("Não é possível dividir por zero!");
            else Console.WriteLine($"Resultado: {num1 / num2}");
        }
        
        static void Multiplicacao(float num1, float num2)
        {
            Console.WriteLine($"Resultado: {num1 * num2}");
        }

    }

}
