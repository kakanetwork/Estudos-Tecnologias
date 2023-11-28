import flet as ft

def main(page: ft.Page):

    lista = ft.ListView(spacing=5,   # espaço entre cada elemento
                        expand=True) # habilita o scroll (melhor desempenho ao contrário de page.scroll)
    for i in range(100):
        lista.controls.append(ft.Text(f"Estamos na linha {i}"))
    
    # trabalhando com o ListView temos um melhor desempenho na renderização
    page.add(lista)

ft.app(target=main)