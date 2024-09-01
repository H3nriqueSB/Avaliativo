import customtkinter as ctk
from PIL import Image

# Inicializando a janela principal
app = ctk.CTk()
app.geometry("300x200")
app.title("Contador de Cliques com Imagens")

# Lista para armazenar as imagens e contadores
lista = []
contador_1 = 0
contador_2 = 0

# Carregando as imagens
imagem1 = ctk.CTkImage(Image.open("alchool.png"), size=(50, 50))
imagem2 = ctk.CTkImage(Image.open("alchool.png"), size=(50, 50))

# Função para adicionar imagem à lista e atualizar o contador
def adicionar_imagem(imagem, contador, label):
    lista.append(imagem)
    contador[0] += 1
    label.configure(text=f"Imagem {imagem}: {contador[0]} cliques")

# Criando os contadores como listas para serem mutáveis dentro da função
contador_1_ref = [0]
contador_2_ref = [0]

# Criando os botões e os labels
botao_1 = ctk.CTkButton(app, image=imagem1, text="", command=lambda: adicionar_imagem("image1", contador_1_ref, label_1))
botao_1.pack(pady=10)

botao_2 = ctk.CTkButton(app, image=imagem2, text="", command=lambda: adicionar_imagem("image2", contador_2_ref, label_2))
botao_2.pack(pady=10)

label_1 = ctk.CTkLabel(app, text="Imagem 1: 0 cliques")
label_1.pack()

label_2 = ctk.CTkLabel(app, text="Imagem 2: 0 cliques")
label_2.pack()

# Iniciando o loop da aplicação
app.mainloop()
