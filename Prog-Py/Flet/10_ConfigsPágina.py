import flet as ft 

def main(page: ft.Page):
    page.title = "Configurações da Página" # para o titulo da página
    page.theme_mode = ft.ThemeMode.DARK    # para alterar o tema padrão da página
    page.update()
    pass

ft.app(target=main)