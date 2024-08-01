import os
import PyPDF2
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import re

def extrair_paginas(input_path, output_path, paginas):
    with open(input_path, 'rb') as arquivo_pdf_original:
        leitor_pdf = PyPDF2.PdfReader(arquivo_pdf_original)
        
        escritor_pdf = PyPDF2.PdfWriter()

        # Verificar se as páginas solicitadas estão dentro dos limites válidos
        total_paginas = len(leitor_pdf.pages)
        paginas_a_extrair = [pagina_num for pagina_num in paginas if 1 <= pagina_num <= total_paginas]

        for pagina_num in paginas_a_extrair:
            escritor_pdf.add_page(leitor_pdf.pages[pagina_num - 1])

        with open(output_path, 'wb') as arquivo_pdf_novo:
            escritor_pdf.write(arquivo_pdf_novo)


def encontrar_parcela(texto_boleto, parcela_a_extrair):
    padrao = r"RECBTO\. PAR.*?(\d+)/(\d+)"
    resultado = re.search(padrao, texto_boleto)
    if resultado:
        parcela_encontrada = int(resultado.group(1))
        return parcela_encontrada == parcela_a_extrair
    else:
        return False

def selecionar_pasta():
    pasta_selecionada = filedialog.askdirectory()
    entry_pasta.delete(0, tk.END)
    entry_pasta.insert(0, pasta_selecionada)

def selecionar_destino():
    destino_selecionado = filedialog.askdirectory()
    entry_destino.delete(0, tk.END)
    entry_destino.insert(0, destino_selecionado)

def extrair_paginas_pdf():
    pasta_input = entry_pasta.get()
    parcela_a_extrair = int(entry_parcela.get())
    destino = entry_destino.get()

    if not os.path.exists(destino):
        os.makedirs(destino)

    status_var.set("Extraindo pagina...")

    for nome_arquivo in os.listdir(pasta_input):
        if nome_arquivo.endswith('.pdf'):
            input_path = os.path.join(pasta_input, nome_arquivo)
            output_path = os.path.join(destino, f'parcela_{parcela_a_extrair}_{nome_arquivo}')

            with open(input_path, 'rb') as arquivo_pdf:
                leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)
                
                for pagina_num in range(len(leitor_pdf.pages)):
                    texto_pagina = leitor_pdf.pages[pagina_num].extract_text()

                    if encontrar_parcela(texto_pagina, parcela_a_extrair):
                        extrair_paginas(input_path, output_path, [pagina_num + 1])
                        break
                        
    status_var.set("Extração concluída!")

# Criar a janela principal
janela = tk.Tk()
janela.title("Extrair parcelas de carnê PDF")
janela.configure(bg="#f0f0f0")

# Estilos
style = ttk.Style()
style.theme_use('alt') # Usar tema clam
style.configure("TButton", background="#4CAF50", foreground="white", font=("Arial", 10, "bold"))
style.configure("TEntry", font=("Arial", 10), padding=5)
style.configure("TLabel", font=("Arial", 10), padding=5)

# Widgets
label_pasta = tk.Label(janela, text="Pasta:")
entry_pasta = tk.Entry(janela, width=40)
button_selecionar_pasta = tk.Button(janela, text="Selecionar Pasta", command=selecionar_pasta)

label_parcela = tk.Label(janela, text="Número da Parcela:")
entry_parcela = tk.Entry(janela, width=10)

label_destino = tk.Label(janela, text="Destino:")
entry_destino = tk.Entry(janela, width=40)
button_selecionar_destino = tk.Button(janela, text="Selecionar Destino", command=selecionar_destino)

button_extrair = tk.Button(janela, text="Extrair parcela", command=extrair_paginas_pdf, state=tk.DISABLED)
label_status = tk.Label(janela, text="")

status_var = tk.StringVar()
label_status_real = tk.Label(janela, textvariable=status_var, fg="green")

def verificar_campos():
    pasta_input = entry_pasta.get()
    parcela_a_extrair = entry_parcela.get()
    destino = entry_destino.get()

    if pasta_input and parcela_a_extrair and destino:
        button_extrair.config(state=tk.NORMAL)
        status_var.set("Pronto para extrair!")
    else:
        button_extrair.config(state=tk.DISABLED)
        status_var.set("Selecione todas as opções.")

# Chamar a função verificar_campos sempre que os campos forem modificados
entry_pasta.bind("<KeyRelease>", lambda event: verificar_campos())
entry_parcela.bind("<KeyRelease>", lambda event: verificar_campos())
entry_destino.bind("<KeyRelease>", lambda event: verificar_campos())

# Layout
label_pasta.grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_pasta.grid(row=0, column=1, padx=10, pady=10)
button_selecionar_pasta.grid(row=0, column=2, padx=10, pady=10)

label_parcela.grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_parcela.grid(row=1, column=1, padx=10, pady=10)

label_destino.grid(row=2, column=0, padx=10, pady=10, sticky="e")
entry_destino.grid(row=2, column=1, padx=10, pady=10)
button_selecionar_destino.grid(row=2, column=2, padx=10, pady=10)

button_extrair.grid(row=3, column=0, columnspan=3, pady=10)
label_status.grid(row=4, column=0, columnspan=3, pady=10)
label_status_real.grid(row=5, column=0, columnspan=3, pady=10)

# Iniciar a janela
janela.mainloop()