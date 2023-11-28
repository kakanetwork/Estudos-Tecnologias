import flet as ft
import time

def main(page: ft.Page):
    for i in range(100):
        page.controls.append(ft.Text(f"Estamos na linha {i}"))
        time.sleep(0.5) 
        page.scroll = "always"
        page.update()
        
ft.app(main)