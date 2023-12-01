import os
import flet as ft

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"

# o gridview é a melhor forma de renderizar alta quantidade de itens pela sua performance e controle 

def main(page: ft.Page):
    gv = ft.GridView(
        expand=True,
        max_extent=140,         # A largura e altura do item     
    )

    page.theme_mode = ft.ThemeMode.DARK
    
    page.add(gv)

    for i in range(5000):
        gv.controls.append(
            ft.Container(
                ft.Text(f"Item {i}", size=20, color="#001199"), # color pode ser definido em hexa ou usar as cores pré-programadas
                alignment=ft.alignment.center,                  # alinha todos os itens ao centro
                bgcolor=ft.colors.AMBER_100,                    # cor do fundo 
                border=ft.border.all(2, ft.colors.AMBER_600),   # cor e espessura da borda
                border_radius=ft.border_radius.all(8)           # arredondamento das pontas
            )
        )

    page.update()
ft.app(target=main)