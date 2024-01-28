import tkinter as tk
from tkinter import PhotoImage

#informações do cliente
deposito=0
saldo_c1= 1500
saque1=0

def menu():
    global saldo_c1
    def destruir_menu():
        print("destruiu")
        lb_deposito.destroy()
        lb_saque.destroy()
        lb_saldo.destroy()
        lb_fim.destroy()  
    
    def depositar():
        global et_dep, saldo_c1
        print("Deposito")
        destruir_menu()
            
        def dep():
            global saldo_c1
            print("depositou")
            deposito = int(et_dep.get())
            print("novo saldo", saldo_c1 + deposito)
            saldo_c1= saldo_c1+deposito            
            destruir_menu()
            et_dep.destroy()
            lb_msaldo.destroy()
            bt_depo.destroy()
            menu()
            
        et_dep= tk.Entry(janela)
        et_dep.place(x= 250 , y=260)
        
        lb_msaldo= tk.Label(janela, text=f"💰 R$ {saldo_c1}" , bg= "grey")
        lb_msaldo.place(x=180, y=260)

        bt_depo=tk.Button(janela, text="DEPOSITAR", bg= "green", command=dep)
        bt_depo.place(x=245,y=350) 

    def sacar():
        global et_saque, saldo_c1
        destruir_menu()
        def saq():
            global et_saque, saldo_c1
            print("Sacou")
            saque = int(et_saque.get())
            print("novo saldo", saldo_c1-saque)
            saldo_c1= saldo_c1-saque
            destruir_menu()
            et_saque.destroy()
            lb_msaldo.destroy()
            bt_saque.destroy()
            menu()


        et_saque= tk.Entry(janela)
        et_saque.place(x= 250 , y=260)
            
        lb_msaldo= tk.Label(janela, text=f"💰 R$ {saldo_c1}" , bg= "grey")
        lb_msaldo.place(x=180, y=260)

        bt_saque=tk.Button(janela, text="SACAR", bg= "green", command=saq)
        bt_saque.place(x=245,y=350)

    def saldo():
        print("verificando saldo")
        def voltar():
            print("voltando")
            lb_saldo2.destroy()
            bt_voltar.destroy()
            menu()
        destruir_menu()
        lb_saldo2 = tk.Label(janela, text = f"R$ {saldo_c1}", bg = "red")
        lb_saldo2.place(x= 180, y= 250)
        bt_voltar = tk.Button(janela, text = "VOLTAR", bg = "#01DF01", command = voltar)
        bt_voltar.place(x= 240, y= 350)
        
    def encerrar():
        def sair():
            lb_encerrar.destroy()
            bt_sair.destroy()
            acesso()
        destruir_menu()
        lb_encerrar = tk.Label(janela, text = "VOLTE SEMPRE!", bg = "red")
        lb_encerrar.place(x= 230, y= 250)
        bt_sair = tk.Button(janela, text = "SAIR", bg = "#01DF01", command = sair)
        bt_sair.place(x= 255, y= 330)
        
    def acesso():
        print("Acessando")
#        destruir_menu()      
        def entrar():
            print("Entrou")
            menu()
            lb_acesso.destroy()
            bt_entrar.destroy()
            lb_acesso2.destroy()
            lb_acesso3.destroy()

        lb_acesso = tk.Label(janela, text = "BEM-VINDO!", bg = "grey")
        lb_acesso.place(x= 240, y= 250)
        
        lb_acesso2 = tk.Label(janela, text = "DESEJA ACESSAR O", bg = "white")
        lb_acesso2.place(x= 220, y= 290)

        lb_acesso3 = tk.Label(janela, text = "CAIXA ELETRÔNICO?", bg = "white")
        lb_acesso3.place(x= 215, y= 315)

        
        bt_entrar = tk.Button(janela, text = "ENTRAR", bg = "#01DF01", command = entrar)
        bt_entrar.place(x= 250, y= 350)

        
        

    #botoes
    #bt1 deposito
    lb_deposito= tk.Label(janela, text= "DEPOSITO", fg= "black" , bg= "white")
    lb_deposito.place(x=170 , y=300)
    bt_deposito= tk.Button(janela, text="     ", command=depositar)
    bt_deposito.place(x=140 , y=300 )

    #bt2 saque
    lb_saque= tk.Label(janela, text= "SAQUE", fg= "black" , bg= "white")
    lb_saque.place(x=170 , y=348)
    bt_saque=tk.Button(janela, text="     ", command=sacar)
    bt_saque.place(x=140 , y=348 )

    #bt3 saldo
    lb_saldo= tk.Label(janela, text= "SALDO", fg= "black" , bg= "white")
    lb_saldo.place(x=340 , y=300)
    bt_saldo=tk.Button(janela, text="      ", command=saldo)
    bt_saldo.place(x=390 , y=300 )

    #bt4 sair
    lb_fim= tk.Label(janela, text= "SAIR", fg= "black" , bg= "white")
    lb_fim.place(x=350 , y=348)
    bt_fim=tk.Button(janela, text="      ", command=encerrar)
    bt_fim.place(x=390 , y=348 )

#config da janela
janela= tk.Tk()
janela.title("Caixa Eletronico")
janela.geometry("557x626")

#carregar a imagem de fundo da janela
image_fundo= PhotoImage(file=r"C:\Users\danie\OneDrive\Documentos\Gaab\python\caixa\interface.png")

#criar label que carregue imagem de fundo
label_fundo= tk.Label(janela, image=image_fundo)
label_fundo.place(x= 0, y=0, relwidth=1, relheight=1)
menu()



janela.mainloop()