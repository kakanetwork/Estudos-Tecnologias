namespace AppArrays
{
    class Program
    {
        static void Main(string[] args)
        {

            // Tratamento de Exceções

            var arr = new int[3];
            string? valor = "";

            try // -> Tentativa
            {
                for (var indice = 0; indice < 3; indice++)
                {
                    Console.WriteLine(arr[indice]);
                }

                if (string.IsNullOrEmpty(valor))
                    // podemos disparar exceções manualmente também
                    throw new ArgumentNullException("O valor não pode ser nulo ou vazio.");

            }
            catch (IndexOutOfRangeException ex) // -> Capturo especificamente só os erros de "IndexOutOfRangeException"
            {
                Console.WriteLine(ex.Message);
                Console.WriteLine("Não encontrei o item na array");

            }
            catch (Exception ex) // -> Captura Genérica
            {
                Console.WriteLine("Ops, deu errado!");
                Console.WriteLine("==========================================");
                Console.WriteLine($"{ex}"); // -> Erro Completo
                Console.WriteLine("==========================================");
                Console.WriteLine($"{ex.StackTrace}"); // -> Caminho do Erro
                Console.WriteLine("==========================================");
            }
            finally // Sempre vai passar no Finally, se deu erro ou não
            {
                Console.WriteLine("Chegou o fim!");
            }


        }

        static void ArraysEstudando()
        {
            Console.Clear();

            // Informar tipagem dos Arrays dessa forma
            var arrayInt = new int[5]; // -> iniciando na posição 0.
            var arrayStr = new string[5];
            var arrayBool = new bool[5];

            // Apenas mostrar o objeto, vai retornar o nome do objeto.
            Console.WriteLine(arrayInt); // -> System.Int32[].
            Console.WriteLine(arrayStr); // -> System.String[].
            Console.WriteLine(arrayBool); // -> System.Boolean[].

            // Para guardar dados
            arrayInt[0] = 12; // -> na posição 0, adicionei o item 12.
            arrayStr[3] = "teste"; // -> na posição 3, adicionado "teste".
            arrayBool[2] = true; // -> na posição 2, adicionado True.

            // Para mostrar os dados guardados
            Console.WriteLine(arrayInt[0]); // -> 12.
            Console.WriteLine(arrayStr[3]); // -> teste.
            Console.WriteLine(arrayBool[2]); // -> True.

            // arrayInt[12] = 1; // -> Gera erro, pois eu inicei o Array apenas com 5 posições e não 12

            // Para guardar os dados já na declaração
            var meuArray = new int[5] { 12, 23, 45, 21, 92 }; // -> Deve ser exatamente igual a quantidade de posições
            Console.WriteLine(string.Join(", ", meuArray)); // -> 12, 23, 45, 21, 92
            Console.WriteLine(meuArray[2]); // -> 45

            // Lembrando que arrays são RT (Reference Type), ou seja:
            // meuArray = arrayInt;
            Console.WriteLine(meuArray[0]); // -> 12
            arrayInt[0] = 329;
            Console.WriteLine(meuArray[0]); // -> 329, ou seja mesmo alterando só o arrayInt, ele altera o meuArray por ser RT

            // Para copiar e não se tornar um RT e sim uma Cópia de Valor, usa o CopyTo ou Array.Copy.

            meuArray.CopyTo(arrayInt, 0); // Índice 0 indica que será copiado os valores de arrayInt a partir do índice 0.
            Array.Copy(arrayInt, 2, meuArray, 0, 2); // Array Origem, Ponto Inicial de Cópia, Array Destino, Ponto Inicial de Cola, Quantidade de Itens a ser Colados.

            // Percorrer o Array

            for (var indice = 0; indice < meuArray.Length; indice++)
            {
                Console.WriteLine(meuArray[indice]);
            }

            // Percorrer o Array com FOREACH (Ideal)

            foreach (var item in meuArray)
            {
                Console.WriteLine(item);
            }
        }

    }
}