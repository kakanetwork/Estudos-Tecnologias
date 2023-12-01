import flet as ft

def main(page: ft.Page):
    page.title = "Routes Example"

    def muda_rota(route):
        page.views.clear()                                          # limpa as views (páginas/telas) do app (usado apenas nas páginas home)
        page.views.append(
            ft.View(                                                # cria uma view (página/tela) com as propriedades/widgets abaixo
                "/",                                                # vinculada a url/rota "/"
                [
                    ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.colors.SURFACE_VARIANT),     # cor da barra (variação de cor de fundo)
                    ft.ElevatedButton("Visite nossa loja", on_click=lambda _: page.go("/loja")), # redireciona ao clicar no botão para a página "/loja"                                 
                ],
            )
        )


        if page.route == "/loja":                            # se a rota for "/loja" (se a página atual for a loja) carregara as informações abaixo
            page.views.append(              
                ft.View(
                    "/loja",
                    [
                        ft.AppBar(title=ft.Text("loja"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Volte para o inicio", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()


    def view_pop(view):
        page.views.pop()            # Remove a última visualização da lista, simula o ato de "voltar"
        top_view = page.views[-1]   # Obtém a visualização mais recente após a remoção da última visualização
        page.go(top_view.route)     # Redireciona para a rota da visualização mais recente, efetivamente "voltando" para a página anterior



    page.on_route_change = muda_rota 
    page.on_view_pop = view_pop # on_view_pop monitora toda vez que o usuario clicar no botão back(voltar) da view
    page.go(page.route)
    
ft.app(target=main)