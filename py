import tkinter as tk
from PIL import Image, ImageTk
import requests
import io

# Função para buscar uma imagem de cachorro aleatória da API Dog.ceo
def buscar_imagem_cachorro():
    url = "https://dog.ceo/api/breeds/image/random"
    resposta = requests.get(url)
    dados = resposta.json()
    imagem_url = dados["message"]

    # Carregando a imagem da URL
    resposta_imagem = requests.get(imagem_url)
    imagem_bytes = io.BytesIO(resposta_imagem.content)
    imagem_pillow = Image.open(imagem_bytes)
    imagem_pillow.thumbnail((400, 400))  # Redimensionar a imagem

    imagem_tk = ImageTk.PhotoImage(imagem_pillow)
    imagem_label.config(image=imagem_tk)
    imagem_label.image = imagem_tk

# Configuração da janela principal
janela = tk.Tk()
janela.title("Imagens de Cachorros Aleatórias")

# Criação de elementos da interface
botao_buscar = tk.Button(janela, text="Buscar Imagem de Cachorro", command=buscar_imagem_cachorro)
imagem_label = tk.Label(janela)

# Layout dos elementos
botao_buscar.pack()
imagem_label.pack()

# Inicialização da janela
janela.mainloop()
