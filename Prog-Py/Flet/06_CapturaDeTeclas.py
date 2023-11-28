import flet as ft

def main(page: ft.Page):

    def teclas(e: ft.KeyboardEvent):
        page.add(ft.Text(f"Tecla pressionada {e.key}, shift: {e.shift}, alt: {e.alt}"))

    page.on_keyboard_event = teclas
    page.scroll = 'hidden' #  a rolagem está habilitada, mas a barra de rolagem está sempre oculta.
    page.add(ft.Text("Pressione qualquer tecla ou uma combinação de teclas (CTRL, ALT, SHIFT, META) para ver o resultado"))
    

ft.app(target=main)