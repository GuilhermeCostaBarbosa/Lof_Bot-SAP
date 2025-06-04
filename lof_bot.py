import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import pyautogui
import time



# Função para abrir o arquivo e armazená-lo na variável
def carregar_planilha():
    # Abre a caixa de diálogo para escolher um arquivo Excel
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos Excel", ".xlsx;.xls")])

    if arquivo:
        # Lê a planilha com o pandas e armazena em uma variável chamada 'tabela'
        global tabela  # Variável global para armazenar os dados
        tabela = pd.read_excel(arquivo)

        # Exibe uma mensagem para confirmar que a planilha foi carregada
        label_resultado.config(text=f"Planilha carregada com sucesso! ({arquivo})")

        print(tabela)

        time.sleep(3)
        pyautogui.PAUSE = 1

        # clicar na transação
        pyautogui.click(x=126, y=306)
        pyautogui.press('enter')

        # Informar centro hospitalar
        pyautogui.click(x=131, y=230)
        pyautogui.write('2701')
        pyautogui.click(x=132, y=203)
        pyautogui.hotkey('Ctrl', 'a')

        pyautogui.PAUSE = 0.3

        for linha in tabela.index:
            # digitar material
            material = str(tabela.loc[linha, 'material'])
            pyautogui.write(material)
            pyautogui.press('enter')

            # digitar quando começa
            valido_de = str(tabela.loc[linha, 'valido_de'])
            pyautogui.write(valido_de)
            pyautogui.press('tab')

            # digitar quando termina
            valido_ate = str(tabela.loc[linha, 'valido_ate'])
            pyautogui.write(valido_ate)
            pyautogui.press('tab')

            # digitar fornecedor
            fornecedor = str(tabela.loc[linha, 'fornecedor'])
            pyautogui.write(fornecedor)
            pyautogui.press('tab')

            # digitar organização de compras
            orgc = str(tabela.loc[linha, 'orgc'])
            pyautogui.write(orgc)
            pyautogui.click(x=375, y=271)

            # digitar contrato
            contrato = str(tabela.loc[linha, 'contrato'])
            pyautogui.write(contrato)
            pyautogui.press('tab')

            # digitar linha
            item = str(tabela.loc[linha, 'item'])
            pyautogui.write(item)
            pyautogui.press('tab')

            # clicar fx
            pyautogui.click(x=500, y=270)

            # salvar
            pyautogui.click(x=230, y=49)
            pyautogui.click(x=231, y=204)
            pyautogui.hotkey('Ctrl', 'a')

        # Automatizar pedido
        pyautogui.click(x=265, y=48)
        pyautogui.PAUSE = 1

        # acessar transação MM02
        pyautogui.click(x=124, y=53)
        pyautogui.write('MM02')
        pyautogui.press('enter')

        # Ler planilha XSLX

        pyautogui.PAUSE = 0.5

        # Entrar no cadastro do item
        for linha in tabela.index:
            material = str(tabela.loc[linha, 'material'])
            pyautogui.click(x=139, y=182)
            pyautogui.hotkey('Ctrl', 'a')

            pyautogui.write(material)
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.press('enter')

            pyautogui.click(x=456, y=403)
            pyautogui.click(x=177, y=775)
            pyautogui.click(x=233, y=53)
            time.sleep(5)


# Criando a janela principal
root = tk.Tk()
root.title("Carregar Planilha")

# Definindo a variável global para armazenar a planilha
tabela = None

# Adicionando um botão para carregar a planilha
btn_carregar = tk.Button(root, text="Carregar Planilha", command=carregar_planilha)
btn_carregar.pack(pady=10)

# Label para exibir o status da operação
label_resultado = tk.Label(root, text="Nenhuma planilha carregada ainda.")
label_resultado.pack(pady=10)

# Exibindo a janela
root.mainloop()