import flet as ft

def main(page: ft.Page):
    page.title = "AppBar"
    page.theme_mode = ft.ThemeMode.DARK

    page.appbar = ft.AppBar(                # feito para criar um appbar 
        leading=ft.Icon(ft.icons.CODE),     # adiciona um icon na appbar (consultar icons em: https://gallery.flet.dev/icons-browser/)
        bgcolor="#003377",                  # cor do fundo da appbar
        title=ft.Text("Aluguel Carros"),    # titulo da appbar  
        center_title=True,                  # centralização do titulo
        actions=[                           # actions são botões/icons com interação que podemos adicionar a appbar
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED,   # o botão de icon, adiciona um icon (nesse caso é um sol)
                          on_click=lambda e: print("Clicou no sol")), # ao clicar no sol, ele da print na mensagem
            ft.PopupMenuButton(             # cria um botão (Conhecido como: 3 pontos) que abre um menu de opções
                items=[                     # esse menu aberto de opções, pode ser definida em itens com PopupMenuItem 
                    ft.PopupMenuItem(text="logar", on_click=lambda e: print("Clicou em logar") ) # texto que aparece no item do menu, e a seguir podemos atribuir uma função ao ser realizado o click
                ]
            )
        ]
    )

    page.update()
    
ft.app(target=main)