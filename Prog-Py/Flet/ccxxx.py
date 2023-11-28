import flet as ft

def main(page: ft.Page):
    valores = {
        'contratante': '',
        'medida': '',
        'partes': '',
        'prolabore': '',
        'exito': '',
        'foro': '',
        'data': '',
    }
    
    def btn_click(e):
        valores['contratante'] = contratante.value
        valores['medida'] = medida.value
        valores['partes'] = partes.value
        valores['prolabore'] = prolabore.value
        valores['exito'] = exito.value
        valores['foro'] = foro.value
        valores['data'] = data.value

        print(valores)
    
    titulo = ft.Text(value='Contrato de Prestação de Serviços Advocatícios', size=20, weight='bold')

    contratante  = ft.TextField(label='Nome do Contratante', width=300, autofocus=True)
    medida       = ft.TextField(label='Medida', width=300)
    partes       = ft.TextField(label='Partes', width=300)
    prolabore    = ft.TextField(label='Prolabore', width=300, prefix_text='R$') 
    exito        = ft.TextField(label='Exito', width=300, suffix_text='%')
    foro         = ft.TextField(label='Foro', width=300)
    data         = ft.TextField(label='Data', width=300)

    btn_gerar = ft.FilledButton(text='Gerar Contrato', on_click=btn_click)

    page.add(
        ft.Column(
            controls = [
                titulo,
                contratante,
                medida,
                partes,
                prolabore,
                exito,
                foro,
                data,
                btn_gerar
            ]
        )

    )

ft.app(target=main)

print('teste')