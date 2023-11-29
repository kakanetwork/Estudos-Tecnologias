import flet as ft

def main(page: ft.Page):
    lv = ft.ListView(spacing=10, 
                     expand=1, 
                     item_extent=50 # Uma altura ou largura fixa (para ListView horizontal) de um item para otimizar a renderização.
                     )
    page.add(lv)


    # com esse código, os itens são carregados por lotes e não completos (o carregamento vai acontecendo de acordo com o tempo que você fica na página)
    for i in range(5000):
        lv.controls.append(
            ft.Text(f"Linha {i}")
        )
        if i % 100 == 0:
            page.update()
    page.update()

ft.app(target=main)