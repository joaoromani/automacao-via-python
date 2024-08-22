# from tkinter import Tk
#
# janela = Tk()
# janela.mainloop()


# import random
# nomes = ["João", "Carlos", "Erik"]
# sorteado = random.choice(nomes)
# print(f"O sorteado foi: {sorteado}")

import time
import pyautogui
import pyperclip

# Abrindo navegador
pyautogui.press('win')
time.sleep(1)
pyautogui.write('chrome')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)


# Acessar pagina dos Dados
link_dados = "https://docs.google.com/spreadsheets/d/1FyHcbNuuK3izKfoEbu9_x1x04SUw2TITHSZv36pYC-U/edit?resourcekey=&gid=1736113315#gid=1736113315"
pyperclip.copy(link_dados)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)

# Estamos na planilha
# Copiar emails
pyautogui.click(x=367, y=350)
time.sleep(1)
pyautogui.hotkey('ctrl', 'c')
emails_str = pyperclip.paste().strip().replace('\r', '')
emails = emails_str.split('\n')[1:]

# Copiar numeros favoritos
pyautogui.click(x=576, y=340)
time.sleep(1)
pyautogui.hotkey('ctrl', 'c')
numeros_str = pyperclip.paste().strip().replace('\r', '')
numeros = numeros_str.split('\n')[1:]

# Copiar nomes
pyautogui.click(x=740, y=340)
time.sleep(1)
pyautogui.hotkey('ctrl', 'c')
nomes_str = pyperclip.paste().strip().replace('\r', '')
nomes = nomes_str.split('\n')[1:]


# Abrir nova guia + gmail
pyautogui.hotkey('ctrl', 't')
time.sleep(1)
abrir_gmail = "https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?compose=new"
pyperclip.copy(abrir_gmail)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(3)
pyautogui.click(x=1270, y=469)

# Enviando os emails
pyperclip.copy(', '.join(emails) )
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)
pyautogui.press('tab')
time.sleep(1)
pyautogui.write('Relatorio Automacao')
pyautogui.press('tab')
time.sleep(1)
mensagem = "Fala galera! Testando o código aqui :)"
pyperclip.copy(mensagem)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')
pyautogui.press('enter')


