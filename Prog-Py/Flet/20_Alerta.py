import flet as ft

def main(page: ft.Page):
    def atualizar(e):
        page.banner.open = False
        page.clean()
        page.add(
            ft.Text("Corpo da página atualizada"),
        )

    def mais_tarde(e):
        page.banner.open = False
        page.add(
            ft.Text("Corpo da página será atualizado mais tarde"),
        )

    def cancelar(e):
        page.banner.open = False
        page.update()

    page.banner = ft.Banner(
            bgcolor = ft.colors.AMBER_900,
            leading=ft.Icon(ft.icons.WARNING_AMBER_SHARP),
            content=ft.Text("Olá, já temos uma nova atualização disponível para você!"),
            actions=[
                    ft.TextButton("Atualizar Agora", on_click=atualizar),
                    ft.TextButton("Atualizar Mais Tarde", on_click=mais_tarde),
                    ft.TextButton("Cancelar", on_click=cancelar),                        
            ],
    )

    def abrir_alerta(e):
        page.banner.open = True
        page.update()

    page.add(
        ft.ElevatedButton("Aviso!", on_click=abrir_alerta),
        ft.Text("Corpo da página"),
    )

ft.app(target=main)