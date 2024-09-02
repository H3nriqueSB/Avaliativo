import customtkinter as ctk
from PIL import Image, ImageTk

carrinholista = {}

imagenlista = {
    "imagem1": ctk.CTkImage(Image.open("entrada/amarelo.png"), size=(100, 100)),
    "imagem2": ctk.CTkImage(Image.open("entrada/azul.png"), size=(100, 100)),
    "imagem3": ctk.CTkImage(Image.open("entrada/branco.png"), size=(100, 100)),
    "imagem4": ctk.CTkImage(Image.open("entrada/rosa.png"), size=(100, 100)),
    "imagem5": ctk.CTkImage(Image.open("entrada/roxo.png"), size=(100, 100)),
    "imagem6": ctk.CTkImage(Image.open("entrada/verde.png"), size=(100, 100))
}

valorlista = {
    'amarelo': 25.00,
    'azul': 15.00,
    'branco': 50.00,
    'rosa': 10.00,
    'roxo': 50.00,
    'verde':25.00
}

def adicionar_imagem_ao_dicionario(chave):
    carrinholista[chave] = imagenlista[chave]
    print(f"Imagem '{chave}' adicionada ao dicionário:", carrinholista)

def visualizar2():
    if senha2.cget("show") == "*":
        senha2.configure(show="")
        button3.configure(text="Ocultar")
    else:
        senha2.configure(show="*")
        button3.configure(text="Mostrar")

def visualizar3():
    if senha1.cget("show") == "*":
        senha1.configure(show="")
        button2.configure(text="Ocultar")
    else:
        senha1.configure(show="*")
        button2.configure(text="Mostrar")

def mudar_imagem_fundo(nova_imagem):
    img = Image.open(nova_imagem) 
    img_tk = ImageTk.PhotoImage(img)
    label_img.configure(image=img_tk)
    label_img.image = img_tk  

def menu_carrinho():
    menucadastro.place_forget() 

    menucarrinho = ctk.CTkFrame(app, width=1000, height=700, corner_radius=10, fg_color='gray')
    menucarrinho.place(x=10, y=50)    

    label_menucarrinho = ctk.CTkLabel(menucarrinho, text='LISTA DE PEDIDOS', width=200, font=("Arial", 20))
    label_menucarrinho.place(x=400, y=20)

    frame_lista_imagens = ctk.CTkFrame(menucarrinho, width=900, height=600, fg_color='gray')
    frame_lista_imagens.place(x=50, y=80)

    def mostrar_imagens():
        limite_colunas = 7  
        for idx, (chave, imagem) in enumerate(carrinholista.items()):
            imagem_label = ctk.CTkLabel(frame_lista_imagens, image=imagem, text='')
            
            row = idx // limite_colunas
            column = idx % limite_colunas
            
            imagem_label.grid(row=row, column=column, padx=10, pady=5)

    mostrar_imagens()

    voltar = ctk.CTkButton(menucarrinho, text='Voltar', width=200, command=lambda: menucarrinho.place_forget())
    voltar.place(x=400, y=650)

def abrir_novo_menu():
    menucadastro.place_forget()

    menucardapio = ctk.CTkFrame(app, width=1000, height=700, corner_radius=10, fg_color='gray')
    menucardapio.place(x=460, y=150)

    label_menucardapio = ctk.CTkLabel(menucardapio, text='OPÇÕES DE CARDAPIO', width=200)
    label_menucardapio.place(x=400, y=20)

    imagem_entrada = Image.open('entrada.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    imagem_dochef = Image.open('chef.png')
    imagem_dochef = imagem_dochef.resize((200, 200))
    imagem_tk2 = ImageTk.PhotoImage(imagem_dochef)

    imagem_sobremesa = Image.open('sobremesa.png')
    imagem_sobremesa = imagem_sobremesa.resize((200, 200))
    imagem_tk3 = ImageTk.PhotoImage(imagem_sobremesa)

    imagem_alchool = Image.open('alchool.png')
    imagem_alchool = imagem_alchool.resize((200, 200))
    imagem_tk4 = ImageTk.PhotoImage(imagem_alchool)

    imagem_bebida = Image.open('bebida.png')
    imagem_bebida = imagem_bebida.resize((200, 200))
    imagem_tk5 = ImageTk.PhotoImage(imagem_bebida)

    imagem_principal = Image.open('principal.png')
    imagem_principal = imagem_principal.resize((200, 200))
    imagem_tk6 = ImageTk.PhotoImage(imagem_principal)

    imagem_carrinho = Image.open('carrin.png')
    imagem_carrinho = imagem_carrinho.resize((50, 50))
    carrinho_tk = ImageTk.PhotoImage(imagem_carrinho)

    carrinho = ctk.CTkButton(menucardapio, image=carrinho_tk, text='', width=50, height=50, command=menu_carrinho)
    carrinho.place(x=20, y=20)
    carrinho.image = carrinho_tk

    entrada = ctk.CTkButton(menucardapio, image=imagem_tk, text='', width=200, height=200, command=abrir_novo_menu2)
    entrada.place(x=100, y=100)
    entrada.image = imagem_tk

    menudochef = ctk.CTkButton(menucardapio, image=imagem_tk2, text='', width=200, height=200, command=abrir_novo_menu3)
    menudochef.place(x=400, y=100)
    menudochef.image = imagem_tk2

    menusobremesa = ctk.CTkButton(menucardapio, image=imagem_tk3, text='', width=200, height=200, command=abrir_novo_menu4)
    menusobremesa.place(x=700, y=100)
    menusobremesa.image = imagem_tk3

    menualchool = ctk.CTkButton(menucardapio, image=imagem_tk4, text='', width=200, height=200, command=abrir_novo_menu5)
    menualchool.place(x=400, y=380)
    menualchool.image = imagem_tk4

    menubebida = ctk.CTkButton(menucardapio, image=imagem_tk5, text='', width=200, height=200, command=abrir_novo_menu6)
    menubebida.place(x=100, y=380)
    menubebida.image = imagem_tk5

    menuprincipal = ctk.CTkButton(menucardapio, image=imagem_tk6, text='', width=200, height=200, command=abrir_novo_menu7)
    menuprincipal.place(x=700, y=380)
    menuprincipal.image = imagem_tk6

    voltar = ctk.CTkButton(menucardapio, text='Voltar', width=200, command=lambda: [menucardapio.place_forget(), restaurar_menu_cadastro()])
    voltar.place(x=400, y=650)
    mudar_imagem_fundo('food1.jpg')

def restaurar_menu_cadastro():
    menucadastro.place(x=75, y=200)
    mudar_imagem_fundo('restau.png')

#Rosquinhas
def abrir_novo_menu2():
    menucadastro.place_forget()

    menuentrada = ctk.CTkFrame(app, width=1000, height=700, corner_radius=10, fg_color='gray')
    menuentrada.place(x=460, y=150)

    label_menuentrada = ctk.CTkLabel(menuentrada, text='OPÇÕES DE ENTRADA', width=200)
    label_menuentrada.place(x=400, y=20)

    imagem_entrada = Image.open('entrada/rosa.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menuentrada, image=imagem_tk, text='', width=200, height=200, command=lambda: adicionar_imagem_ao_dicionario("imagem4"))
    entrada.place(x=400, y=100)
    entrada.image = imagem_tk

    imagem_entrada = Image.open('entrada/azul.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menuentrada, image=imagem_tk, text='', width=200, height=200, command=lambda: adicionar_imagem_ao_dicionario("imagem2"))
    entrada.place(x=100, y=100)
    entrada.image = imagem_tk

    imagem_entrada = Image.open('entrada/verde.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menuentrada, image=imagem_tk, text='', width=200, height=200, command=lambda: adicionar_imagem_ao_dicionario("imagem6"))
    entrada.place(x=700, y=100)
    entrada.image = imagem_tk

    imagem_entrada = Image.open('entrada/branco.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menuentrada, image=imagem_tk, text='', width=200, height=200, command=lambda: adicionar_imagem_ao_dicionario("imagem3"))
    entrada.place(x=100, y=380)
    entrada.image = imagem_tk

    imagem_entrada = Image.open('entrada/amarelo.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menuentrada, image=imagem_tk, text='', width=200, height=200, command=lambda: adicionar_imagem_ao_dicionario("imagem1"))
    entrada.place(x=400, y=380)
    entrada.image = imagem_tk

    imagem_entrada = Image.open('entrada/roxo.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menuentrada, image=imagem_tk, text='', width=200, height=200, command=lambda: adicionar_imagem_ao_dicionario("imagem5"))
    entrada.place(x=700, y=380)
    entrada.image = imagem_tk

    voltar = ctk.CTkButton(menuentrada, text='Voltar', width=200, command=lambda: [menuentrada.place_forget()])
    voltar.place(x=400, y=650)

def abrir_novo_menu3():
    menucadastro.place_forget()

    menudochef = ctk.CTkFrame(app, width=1000, height=700, corner_radius=10, fg_color='gray')
    menudochef.place(x=460, y=150)

    label_menucardapio = ctk.CTkLabel(menudochef, text='OPÇÕES DO CHEF', width=200)
    label_menucardapio.place(x=400, y=20)

    imagem_entrada = Image.open('menudochef/bolo.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menudochef, image=imagem_tk, text='', width=200, height=200)
    entrada.place(x=100, y=100)
    entrada.image = imagem_tk

    imagem_entrada = Image.open('menudochef/chocolate.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menudochef, image=imagem_tk, text='', width=200, height=200)
    entrada.place(x=700, y=100)
    entrada.image = imagem_tk

    imagem_entrada = Image.open('menudochef/fruta.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menudochef, image=imagem_tk, text='', width=200, height=200)
    entrada.place(x=400, y=100)
    entrada.image = imagem_tk

    imagem_entrada = Image.open('menudochef/lazanha.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menudochef, image=imagem_tk, text='', width=200, height=200)
    entrada.place(x=400, y=380)
    entrada.image = imagem_tk

    imagem_entrada = Image.open('menudochef/sorvete.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menudochef, image=imagem_tk, text='', width=200, height=200)
    entrada.place(x=100, y=380)
    entrada.image = imagem_tk

    imagem_entrada = Image.open('menudochef/torta.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menudochef, image=imagem_tk, text='', width=200, height=200)
    entrada.place(x=700, y=380)
    entrada.image = imagem_tk

    voltar = ctk.CTkButton(menudochef, text='Voltar', width=200, command=lambda: [menudochef.place_forget()])
    voltar.place(x=400, y=650)

def abrir_novo_menu4():
    menucadastro.place_forget()

    menudochef = ctk.CTkFrame(app, width=1000, height=700, corner_radius=10, fg_color='gray')
    menudochef.place(x=460, y=150)

    label_menucardapio = ctk.CTkLabel(menudochef, text='OPÇÕES DE SOBREMESA', width=200)
    label_menucardapio.place(x=400, y=20)

    imagem_entrada = Image.open('sobremesa/balinha.jfif')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menudochef, image=imagem_tk, text='', width=200, height=200)
    entrada.place(x=100, y=100)
    entrada.image = imagem_tk

    imagem_entrada = Image.open('sobremesa/chocolate.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menudochef, image=imagem_tk, text='', width=200, height=200)
    entrada.place(x=400, y=100)
    entrada.image = imagem_tk

    imagem_entrada = Image.open('sobremesa/cupcacke.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menudochef, image=imagem_tk, text='', width=200, height=200)
    entrada.place(x=700, y=100)
    entrada.image = imagem_tk

    imagem_entrada = Image.open('sobremesa/gelatina.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menudochef, image=imagem_tk, text='', width=200, height=200)
    entrada.place(x=700, y=380)
    entrada.image = imagem_tk

    imagem_entrada = Image.open('sobremesa/pudimsonic.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menudochef, image=imagem_tk, text='', width=200, height=200)
    entrada.place(x=400, y=380)
    entrada.image = imagem_tk

    imagem_entrada = Image.open('sobremesa/sorvete2.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menudochef, image=imagem_tk, text='', width=200, height=200)
    entrada.place(x=100, y=380)
    entrada.image = imagem_tk

    voltar = ctk.CTkButton(menudochef, text='Voltar', width=200, command=lambda: [menudochef.place_forget()])
    voltar.place(x=400, y=650)

def abrir_novo_menu5():
    menucadastro.place_forget()

    menualchool = ctk.CTkFrame(app, width=1000, height=700, corner_radius=10, fg_color='gray')
    menualchool.place(x=460, y=150)

    label_menucardapio = ctk.CTkLabel(menualchool, text='OPÇÕES DE CERVEJA', width=200)
    label_menucardapio.place(x=400, y=20)

    imagem_entrada = Image.open('Cachaça/cerv1.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menualchool, image=imagem_tk, text='', width=200, height=200)
    entrada.place(x=100, y=100)
    entrada.image = imagem_tk

    imagem_entrada = Image.open('Cachaça\cerv2.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menualchool, image=imagem_tk, text='', width=200, height=200)
    entrada.place(x=400, y=100)
    entrada.image = imagem_tk

    imagem_entrada = Image.open('Cachaça\cerv3.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menualchool, image=imagem_tk, text='', width=200, height=200)
    entrada.place(x=700, y=100)
    entrada.image = imagem_tk

    imagem_entrada = Image.open('Cachaça\cerv6.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menualchool, image=imagem_tk, text='', width=200, height=200)
    entrada.place(x=700, y=380)
    entrada.image = imagem_tk

    imagem_entrada = Image.open('Cachaça\cerv5.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menualchool, image=imagem_tk, text='', width=200, height=200)
    entrada.place(x=400, y=380)
    entrada.image = imagem_tk

    imagem_entrada = Image.open('Cachaça\cerv4.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menualchool, image=imagem_tk, text='', width=200, height=200)
    entrada.place(x=100, y=380)
    entrada.image = imagem_tk

    voltar = ctk.CTkButton(menualchool, text='Voltar', width=200, command=lambda: [menualchool.place_forget()])
    voltar.place(x=400, y=650)

def abrir_novo_menu6():
    menucadastro.place_forget()

    menubebida = ctk.CTkFrame(app, width=1000, height=700, corner_radius=10, fg_color='gray')
    menubebida.place(x=460, y=150)

    label_menucardapio = ctk.CTkLabel(menubebida, text='OPÇÕES DE BEBIDAS', width=200)
    label_menucardapio.place(x=400, y=20)

    imagem_entrada = Image.open('bebidas/bebida1.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menubebida, image=imagem_tk, text='', width=200, height=200)
    entrada.place(x=100, y=100)
    entrada.image = imagem_tk

    imagem_entrada = Image.open('bebidas/bebida2.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menubebida, image=imagem_tk, text='', width=200, height=200)
    entrada.place(x=400, y=100)
    entrada.image = imagem_tk

    imagem_entrada = Image.open('bebidas/bebida3.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menubebida, image=imagem_tk, text='', width=200, height=200)
    entrada.place(x=700, y=100)
    entrada.image = imagem_tk

    imagem_entrada = Image.open('bebidas/bebida4.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menubebida, image=imagem_tk, text='', width=200, height=200)
    entrada.place(x=100, y=380)
    entrada.image = imagem_tk

    imagem_entrada = Image.open('bebidas/bebida5.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menubebida, image=imagem_tk, text='', width=200, height=200)
    entrada.place(x=400, y=380)
    entrada.image = imagem_tk

    imagem_entrada = Image.open('bebidas/bebida6.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menubebida, image=imagem_tk, text='', width=200, height=200)
    entrada.place(x=700, y=380)
    entrada.image = imagem_tk

    voltar = ctk.CTkButton(menubebida, text='Voltar', width=200, command=lambda: [menubebida.place_forget()])
    voltar.place(x=400, y=650)

def abrir_novo_menu7():
    menucadastro.place_forget()

    menuprincipal = ctk.CTkFrame(app, width=1000, height=700, corner_radius=10, fg_color='gray')
    menuprincipal.place(x=460, y=150)

    label_menucardapio = ctk.CTkLabel(menuprincipal, text='OPÇÕES DE LANCHES', width=200)
    label_menucardapio.place(x=400, y=20)

    imagem_entrada = Image.open('principal/comid.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menuprincipal, image=imagem_tk, text='', width=200, height=200)
    entrada.place(x=100, y=100)
    entrada.image = imagem_tk

    imagem_entrada = Image.open('principal/comid1.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menuprincipal, image=imagem_tk, text='', width=200, height=200)
    entrada.place(x=400, y=100)
    entrada.image = imagem_tk

    imagem_entrada = Image.open('principal/comid3.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menuprincipal, image=imagem_tk, text='', width=200, height=200)
    entrada.place(x=700, y=100)
    entrada.image = imagem_tk

    imagem_entrada = Image.open('principal/comid6.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menuprincipal, image=imagem_tk, text='', width=200, height=200)
    entrada.place(x=700, y=380)
    entrada.image = imagem_tk

    imagem_entrada = Image.open('principal/comid5.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menuprincipal, image=imagem_tk, text='', width=200, height=200)
    entrada.place(x=400, y=380)
    entrada.image = imagem_tk

    imagem_entrada = Image.open('principal/comid4.png')
    imagem_entrada = imagem_entrada.resize((200, 200))
    imagem_tk = ImageTk.PhotoImage(imagem_entrada)

    entrada = ctk.CTkButton(menuprincipal, image=imagem_tk, text='', width=200, height=200)
    entrada.place(x=100, y=380)
    entrada.image = imagem_tk

    voltar = ctk.CTkButton(menuprincipal, text='Voltar', width=200, command=lambda: [menuprincipal.place_forget()])
    voltar.place(x=400, y=650)

app = ctk.CTk()
app.geometry('1920x1080')
app.configure(fg_color='black')

img_path = 'restau.png'
img = Image.open(img_path) 
img_tk = ImageTk.PhotoImage(img)

label_img = ctk.CTkLabel(app, image=img_tk, text='')
label_img.place(x=0, y=40)

menucadastro = ctk.CTkFrame(app, width=400, height=300, corner_radius=10, fg_color='gray')
menucadastro.place(x=75, y=200)

frametexto = ctk.CTkLabel(menucadastro, text='Usuario', width=200)
frametexto.place(x=100, y=20)

user1 = ctk.CTkEntry(menucadastro, width=250)
user1.place(x=75, y=50)

frametexto2 = ctk.CTkLabel(menucadastro, text='Senha', width=200)
frametexto2.place(x=100, y=95)

senha1 = ctk.CTkEntry(menucadastro, width=250, show='*')
senha1.place(x=75, y=125)

frametexto3 = ctk.CTkLabel(menucadastro, text='Confirme a Senha', width=200)
frametexto3.place(x=100, y=170)

senha2 = ctk.CTkEntry(menucadastro, width=250, show='*')
senha2.place(x=75, y=200)

button3 = ctk.CTkButton(menucadastro, text='Mostrar', width=20, command=visualizar2)
button3.place(x=330, y=200)

button2 = ctk.CTkButton(menucadastro, text='Mostrar', width=20, command=visualizar3)
button2.place(x=330, y=125)

button1 = ctk.CTkButton(menucadastro, text='CADASTRO', width=200, command=abrir_novo_menu)
button1.place(x=100, y=245)

app.mainloop()
