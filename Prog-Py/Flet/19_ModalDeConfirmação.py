import flet as ft

def main(page: ft.Page):

    def confirmar(e):
        alerta_dialogo.open=False
        page.update()
        
    def cancelar(e):
        alerta_dialogo.open=False
        page.update()

   

    alerta_dialogo = ft.AlertDialog(
        modal=True,
        title=ft.Text("Confirme a ação"),
        content=ft.Text("Deseja realmente excluir o arquivo?"),
        actions=[
            ft.TextButton("Apagar", on_click=confirmar),
            ft.TextButton("Cancelar", on_click=cancelar)
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Alerta fechado")
    )

    def abrir_modal(e):
        page.dialog = alerta_dialogo
        alerta_dialogo.open=True
        page.update()
        pass

    page.add(
        ft.Text("Corpo da aplicação"),
        ft.ElevatedButton("Abrir alerta", icon=ft.icons.DELETE , icon_color="red", on_click=abrir_modal)
    )
ft.app(target=main)