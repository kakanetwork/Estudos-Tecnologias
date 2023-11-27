import flet as ft

def main(page):
    def adiciona_tarefa(e):
        # adiciona uma checkbox com o valor informado na caixa
        page.add(ft.Checkbox(label=tarefa.value)) 

        # zera a caixa após adicionar task
        tarefa.value = "" 

        # o focus, ele deixa o cursor clicado na caixa de texto mesmo após o clique no botão (permitindo escrever novamente sem clicar na caixa)
        tarefa.focus() 

        tarefa.update() 

    # caixa de texto input
    tarefa = ft.TextField(hint_text="O que deve ser feito?", width=300) 
    page.add(ft.Row([tarefa, ft.ElevatedButton("Adicionar", on_click=adiciona_tarefa)])) 
ft.app(target=main)