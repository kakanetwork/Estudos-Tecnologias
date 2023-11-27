import tkinter as tk


def abrir_janela():
    # abre uma nova janela acima da janela atual 
    janela2 = tk.Toplevel() 
    janela2.title("Janela Número 2")

    # destroy = fecha a janela aberta
    botao_fechar = tk.Button(janela2, text="Fechar a janela", command= janela2.destroy)
    botao_fechar.grid(column=0, row=0)


janela = tk.Tk()
janela.title("Janela Número 1")

botao = tk.Button(janela, text="Clique aqui", command=abrir_janela)
botao.grid(column=0, row=0, padx=10, pady=10)

janela.mainloop()