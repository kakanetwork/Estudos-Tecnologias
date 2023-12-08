import flet as ft

def main(page: ft.Page):

    # ao ser clicado no botão confirmar ou cancelar, irá abrir a função que fecha o modal/alerta e atualiza a página
    def confirmar(e):
        alerta_dialogo.open=False
        page.update()
        
    def cancelar(e):
        alerta_dialogo.open=False
        page.update()

   
    #
    alerta_dialogo = ft.AlertDialog(                            # criar um alerta (modal)
        modal=True,                                             # Modal True, significa que o alerta só será fechado com alguma confirmação(ação)
        title=ft.Text("Confirme a ação"),                       # titulo do alerta
        content=ft.Text("Deseja realmente excluir o arquivo?"), # corpo do alerta
        actions=[                                               # aqui podemos colocar as ações/botões que permitem fechar o modal
            ft.TextButton("Apagar", on_click=confirmar),
            ft.TextButton("Cancelar", on_click=cancelar)
        ],
        actions_alignment=ft.MainAxisAlignment.END,             # define o alinhamento das ações para a direita
        on_dismiss=lambda e: print("Alerta fechado")            # informa quando for fechado
    )

    # ao ser clicado no botão "abrir alerta" será aberto o modal/alerta e atualizado a página
    def abrir_modal(e):
        page.dialog = alerta_dialogo
        alerta_dialogo.open=True
        page.update()

    
    page.add(
        ft.Text("Corpo da aplicação"),
        ft.ElevatedButton("Abrir alerta", icon=ft.icons.DELETE , icon_color="red", on_click=abrir_modal)
    )
ft.app(target=main)