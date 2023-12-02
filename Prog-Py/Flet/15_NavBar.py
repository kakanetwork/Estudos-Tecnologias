import flet as ft

"""
Navbar é uma barra de navegação que fica na parte inferior da página
"""

def main(page: ft.Page):
    page.title = "Navbar"

    page.navigation_bar = ft.NavigationBar(                   # inicia uma navbar
        destinations=[                                        # define os destinos da navbar
            ft.NavigationDestination(icon=ft.icons.HOME, label="Home"), # destinos/itens que terão na navbar, junto a seu icon e nome (pode deixar sem se quiser)
            ft.NavigationDestination(icon=ft.icons.PEOPLE, label="People"),
            ft.NavigationDestination(icon=ft.icons.SETTINGS, label="Settings"),
        ]
    )
    pass

    page.add(ft.Text("Corpo da aplicação"))
ft.app(target=main)