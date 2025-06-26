
namespace PrimeiroApp
{
    class Program

    {
        static void Main(string[] args)
        {
            string texto = "Este texto é um teste";

            var resu = texto.Split(" ");

            Product mouse = new(1, "Mouse", 100, EProductType.Service);


            mouse.Id = 100;

            Console.WriteLine(mouse.Id);
            Console.WriteLine(mouse.Name);
            Console.WriteLine(mouse.Price);
            Console.WriteLine(mouse.Type);
            Console.WriteLine((int)mouse.Type);

            decimal preco = 149.99m;
            Console.WriteLine($"O preço do produto é: {preco:C}");

        }

    }

    struct Product
    {

        public Product(int id, string name, double price, EProductType type)
        {
            Id = id;
            Name = name;
            Price = price;
            Type = type;
        }

        public int Id;
        public string Name;
        public double Price;
        public EProductType Type;


        public double PriceInDolar(double dolar)
        {
            return Price * dolar;
        }

    }

    enum EProductType
    {
        Product = 1,
        Service = 2,
    }
    
    

}