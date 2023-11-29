import flet as ft

def main(page: ft.Page):

    # o autofocus inicia o app com ele já "clicado"/aberto
    nome = ft.TextField(label="nome", autofocus=True) 
    sobrenome = ft.TextField(label="sobrenome")
    coluna = ft.Column()

    def btn_click(e):
        coluna.controls.append(ft.Text(f"Bem vindo, {nome.value} {sobrenome.value}!"))
        nome.value = ""
        sobrenome.value = ""
        page.update()
        nome.focus()

    page.scroll = 'adaptive' #  a rolagem está habilitada e a barra de rolagem é sempre mostrada ao executar o aplicativo como web ou desktop. igual ao always 
    
    page.add(
        nome,
        sobrenome,
        ft.ElevatedButton("Diga Bem Vindo!", on_click=btn_click),
        coluna,
    )

ft.app(target=main)