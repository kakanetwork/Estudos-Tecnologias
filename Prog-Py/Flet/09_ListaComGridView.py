import os
import flet as ft

os.environ["FLET_WS_MAX_MESSAGES_SIZE"] = "8000000"

def main(page: ft.Page):
                                                # aqui coloco as propriedades que a linha terá
    linha = ft.Row(wrap=True,                   # para quebrar a linha
                   scroll="always",             # ativa o rolamento 
                   expand=True                  # para que o rolamento funcione em Grid/List views
                   )
    
    page.add(linha)
    for i in range(100):                        # adicionando 100 itens
        linha.controls.append( 
            ft.Container(                       # container é utilizado para decorar/estilizar algum controle
                ft.Text(f"Item {i}"),           # será o texto do item 
                width=100,                      # largura
                height=100,                     # altura
                alignment=ft.alignment.center,  # para alinhamento
                bgcolor=ft.colors.AMBER_100,    # define a cor de fundo
                border=ft.border.all(2, ft.colors.AMBER_600), # define a espessura e cor da borda
                border_radius=ft.border_radius.all(8)         # define o raio da borda (arredondamento de pontas)
            )
        )
    page.update()
ft.app(target=main)