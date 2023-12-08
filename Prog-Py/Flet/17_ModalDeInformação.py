import flet as ft

import time
tempo_atual = time.localtime()
data = time.strftime("%d/%m/%Y", tempo_atual) 
hora = time.strftime("%H:%M", tempo_atual)


def main(page: ft.Page):
    alerta = ft.AlertDialog(        # criar um alerta (não possui modal, logo ele pode ser fechado, sem a necessidade de alguma confirmação/ação, apenas um clique fora)
        title=ft.Text("Aviso!"),    # titulo do alerta
        # content é o corpo do alerta, aqui eu introduzi a biblioteca Time para informar a data da manutenção que é a data/hora atual
        content=ft.Text(f"Olá Usuário, teremos uma manutenção programada para a data {data} às {hora}"),
        on_dismiss=lambda e: print("Alerta fechado"), # aqui informa quando o alerta for fechado (caso seja necessário fazer algo no fechamento dele)
    )

    # precisamos criar uma função que gera ou abre o alerta, ao clicar em um botão
    def abrir_alerta(e):
        page.dialog = alerta # aqui atribuímos nosso widget de alerta criado, as configurações de dialog da página
        alerta.open = True   # nesse momento, a abertura do alerta é realizado
        page.update()        # e a página é atualizada

    page.add(
        ft.Text("Olá Mundo!"),
        ft.ElevatedButton("Informação", on_click=abrir_alerta) # botão que gera o alerta
    )

ft.app(target=main)