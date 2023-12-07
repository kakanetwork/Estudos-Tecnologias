import flet as ft
import time

def main(page: ft.Page):
    tempo_atual = time.localtime()
    data = time.strftime("%d/%m/%Y", tempo_atual) 
    hora = time.strftime("%H:%M", tempo_atual)

    alerta = ft.AlertDialog(
        title=ft.Text("Aviso!"),
        content=ft.Text(f"Olá Usuário, teremos uma manutenção programada para a data {data} às {hora}"),
        on_dismiss=lambda e: print("Alerta fechado")
    )

    def abrir_alerta(e):
        page.dialog = alerta
        alerta.open = True
        page.update()

    def verificar_hora():
        # Verificar se a hora é 17:54
        if hora == "18:12" and not alerta.open:
            abrir_alerta(None)  # Se a hora for 17:54 e o alerta não estiver aberto, abrir o alerta

    # Iniciar a verificação da hora
    verificar_hora()

    page.add(
        ft.Text("Olá Mundo!")
    )

ft.app(target=main)
