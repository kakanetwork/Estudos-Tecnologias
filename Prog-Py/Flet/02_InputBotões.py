import flet as ft

def main(page: ft.Page):
    # adiciona em uma coluna os textos (controles)
    page.add(
        ft.Column(controls=[
            ft.Text("A"),
            ft.Text("B"),
            ft.Text("C")
        ])
    )

    # adiciona em uma linha os textos (controles)
    page.add(
    ft.Row(controls=[
        ft.Text("A"),
        ft.Text("B"),
        ft.Text("C")
    ])
    )

    def botao_clicado(e):
        page.add(ft.Text(nome.value)) # utilizando a variável com o ".value" ele me retornara o valor atribuído a ela

    # adiciona a caixa de pergunta(input) e o botão com uma função ao ser clicado (informa o texto "clicado")
    nome = ft.TextField(label="Digite seu nome", width=300) # dessa forma posso mandar apenas a variável para a linha
    page.scroll = 'always' #  a rolagem está habilitada e a barra de rolagem é sempre mostrada.

    page.add(
        ft.Row(controls=[
            nome,
            ft.ElevatedButton(text="Clique aqui!", on_click=botao_clicado)
        ])
    )

ft.app(target=main)