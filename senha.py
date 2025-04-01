import random

confirmacao = input("Deseja uma senha aleatoria?")
if confirmacao == "S":     
    def Senha():
        n1 = []
        n2 = [] 
        n3 = []
        al = " A B C D E F G H I J K L M N O P Q R S T U V W X Y Z "   
        ca = "! @ # $ % ^ & * ? ~"
        nu = "1 2 3 4 5 6 7 8 9 0 "
        n1 = al.split() 
        n2 = ca.split()
        n3 = nu.split()
        senha = []   
        for i in range(10):      
            senha.append(random.choice(n1)) 
            senha.append(random.choice(n2))
            senha.append(random.choice(n3))
            senha1 = " ".join(senha)
            senha2 = senha1.replace(" ","")
            
            
        print(senha2)   
      
vai = Senha()
    