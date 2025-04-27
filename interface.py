import tkinter as tk
from tkinter import filedialog
import subprocess

def escolher_imagem():
    caminho = filedialog.askopenfilename(
        title="Escolha uma imagem",
        filetypes=[("Imagens", "*.jpg *.jpeg *.png")]
    )
    if caminho:
        subprocess.run(["python3", "main.py", caminho])

def iniciar_interface():
    root = tk.Tk()
    root.title("Imagem para Música 🎼")
    
    # Definindo o tamanho da janela
    largura_janela = 300
    altura_janela = 150

    # Pegando o tamanho da tela
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    # Calculando as coordenadas para centralizar
    pos_x = (largura_tela // 2) - (largura_janela // 2)
    pos_y = (altura_tela // 2) - (altura_janela // 2)

    # Aplicando o tamanho e posição
    root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

    label = tk.Label(root, text="Escolha uma imagem para gerar música 🎵", wraplength=250)
    label.pack(pady=20)

    botao = tk.Button(root, text="Selecionar Imagem", command=escolher_imagem)
    botao.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    iniciar_interface()
