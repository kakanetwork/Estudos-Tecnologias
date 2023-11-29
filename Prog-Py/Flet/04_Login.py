import flet as ft

def main(page: ft.Page):

    titulo = ft.Text(value="Formulário de Cadastro", size=20, weight="bold", text_align="center")
    nome = ft.TextField(label="Digite o seu Nome", 
                        autofocus=True)             # autofocus, ele inicia a página com foco naquela entrada
                        
    senha = ft.TextField(label="Digite sua senha", 
                         password=True,             # transforma o campo em oculto (para senhas)
                         can_reveal_password=True)  # can_reveal é  para revelar a senha (ocultar/desocultar)

    descritivo = ft.TextField(label="Faça uma breve descrição do problema (Opcional)", 
                              autofocus=True, 
                              multiline=True,       # multiline permite várias linhas na caixa
                              max_length=100,       # limita o máximo de caracteres a ser escrito
                              max_lines=10)         # limita o máximo de linhas a ser mostrada (pode se ter mais linhas como carácter)
    
    site = ft.TextField(label="Digite a URL do site em questão", 
                        prefix_text="https://")     # o prefix adiciona o texto antes do que foi digitado como um prefixo 


    def login(e):

        # verifica se os campos são vazios, e se sim informa que é obrigatório (gera um erro)
        if not nome.value:
            nome.error_text = "Este campo é obrigatório"
            page.update()
        if not senha.value:
            senha.error_text = "Este campo é obrigatório" 
            page.update()
        else:
            print(nome.value, senha.value)

            # serve para limpar os campos (nesse caso não é necessário, só em múltiplas tentativas de login)
            # nome.value = "" 
            # senha.value = ""
            # descritivo.value = ""
            
            # limpa a página (semelhante a criar outra página na mesma)
            page.clean()

            # informa o nome da pessoa que logou em uma nova página após o clean
            page.add(ft.Text(f"Olá, {nome.value}\nSeja Bem Vindo a página!"))
    
    # onclick = leva para a função login()
    btn = ft.FilledButton(text="Clique aqui!", on_click=login)
    page.theme_mode = ft.ThemeMode.DARK # altera o modo do tema para a´dark

    # adiciona e da update nos elementos
    page.add(
        titulo,
        nome,
        senha,
        descritivo,
        btn
    )

ft.app(target=main)