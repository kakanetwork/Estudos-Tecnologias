import flet as ft
import time

def main(page: ft.Page):
    page.title = "Configurações da Página" # para o titulo da página
    page.theme_mode = ft.ThemeMode.DARK   # para alterar o tema padrão da página
    page.update()

    t = ft.Text() # caixa para adicionar textos
    page.add(t) # realiza o update da página junto a adição do texto

    # vai atribuindo +1 para o texto e atualizando a página em seguida
    i = 0 
    while True:
        t.value = f"Step {i}"
        i += 1
        page.update()

ft.app(target=main)