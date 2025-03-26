namespace AppMaui
{
    public partial class MainPage : ContentPage
    {

        public MainPage()
        {
            InitializeComponent();
        }

        private void Button_Clicked(object sender, EventArgs e)
        {
            try
                {
                    double etanol = Convert.ToDouble(txt_etanol.Text); // Convertendo o valor do etanol para double
                    double gasolina = Convert.ToDouble(txt_gasolina.Text); // Convertendo o valor da gasolina para double

                    string msg_aviso = "";

                    if (etanol <= (gasolina * 0.7)) // Se o valor do etanol for menor ou igual a 70% do valor da gasolina
                        {
                            msg_aviso = "Abasteça com Etanol!";
                        }
                    else
                        {
                            msg_aviso = "Abasteça com Gasolina!";
                        }

                    DisplayAlert("Calculado", msg_aviso, "OK");
                }

            catch(Exception ex)
                {
                    DisplayAlert("Erro", ex.Message, "OK");
                }

        } // Fecha Método
    } // Fecha Classe
} // Fecha Namespace
