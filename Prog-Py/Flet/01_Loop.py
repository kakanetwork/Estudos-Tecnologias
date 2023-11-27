import flet as ft
import time

def main(page: ft.Page):
    t = ft.Text() # caixa para adicionar textos
    page.add(t) # realiza o update da página junto a adição do texto

    # vai atribuindo +1 para o texto e atualizando a página em seguida
    i = 0 
    while True:
        t.value = f"Step {i}"
        i += 1
        page.update()
        time.sleep(0.2)
        
ft.app(target=main)