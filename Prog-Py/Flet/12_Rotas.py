import flet as ft

def main(page: ft.Page):
    page.title = "Inicio" 
    page.add(ft.Text(f"Rota inicial {page.route}")) # com page.route informa a rota atual 

    # essa função serve para informar se o usuario tentou uma nova rota dinamicamente
    def exibir_rota(route):
        page.add(ft.Text(f"Nova Rota {route}"))
    
    page.on_route_change = exibir_rota # o on_route_change captura mudanças de rotas dinâmicas


    def nova_rota(e):
        page.route = "/compras" # informamos qual a rota que ele deve seguir
        page.clean()            # limpas a página
        page.title = "Compras"  # definimos novo titulo para a página
        page.update()
    
    page.add(ft.FilledButton("Ir para compras", on_click=nova_rota)) # ao clicar no botão, ativa a mudança de rota estática

    page.update()

ft.app(target=main)