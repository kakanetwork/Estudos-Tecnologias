import flet as ft

""" 
NavRail é tipo o NavBar, mas é utilizado na lateral da aplicação (esquerda ou direita)
"""

def main(page: ft.Page):
    page.title = "NavRail"

    rail = ft.NavigationRail(
        selected_index=0,                           # Define o índice inicial da destinação selecionada. (tipo o autofocus)
        label_type=ft.NavigationRailLabelType.ALL,  
        #extended=True,
        min_width=100,                              # Define a largura mínima da barra de navegação.
        min_extended_width=400,                     # Define a largura mínima quando a barra de navegação está estendida.
        leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),  # Adiciona um botão flutuante no início 
        group_alignment=-0.9,                       # Define a distância do botão flutuante para os itens de destino da barra (valores = -1.0 até 1.0)
        
        destinations=[                              # Define os itens/destinos que terá na NavRail
            
            ft.NavigationRailDestination(icon=ft.icons.FAVORITE_BORDER, 
                                         selected_icon=ft.icons.FAVORITE, 
                                         label="Favoritar"),
            # a diferença de Icon_content para Icon, é que Icon_content permite transformar o icon em um controle e ter mais estilização do mesmo.
            ft.NavigationRailDestination(icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER), 
                                         selected_icon_content=ft.Icon(ft.icons.BOOKMARK), 
                                         label="Salvos"),
        ],
        
        on_change=lambda e: print("Selected destination:", # quando tiver clique, ele informara para qual destino foi (baseado em index, de 0 em diante)
                                 e.control.selected_index),# o "e.control.selected_index" que informa o index selecionado
    )


    # Adiciona uma estrutura de layout à página.
    page.add(  
        ft.Row(
            [
                rail,                            # adiciona a NavRail na linha
                ft.VerticalDivider(width=1),     # adiciona uma divisão vertical (para a NavRail)
                ft.Column([ ft.Text("Body!")], 
                          # https://flet.dev/docs/controls/row/#alignment <- link para saber mais do alinhamento
                          alignment=ft.MainAxisAlignment.START, # O MainAxisAlignment.Start alinha os filhos no início do eixo principal (á esquerda) 
                          expand=True),
            ],
            expand=True,
        )
    )


ft.app(target=main)