class loguin:
    def __init__(self):
        self.registro = {}
        self.cadastrar
        #self.base_dados
        self.logar
        self.status = False
        if self.status == False:
            self.apresentacao()
        else:
            print('logado no sistema')
      #  print(self.registro)
                 
    def cadastrar(self):
        usuario = input('Entre com o novo login: \n')
        
        while usuario =='':
            print('não do usuario não pode ser vazio'.title())
            usuario = input('Entre com o novo login: \n')
            
        senha = input('Entre com a senha: \n')
        self.usuario = usuario
        
        self.senha = senha
        
        while len(senha)<=5:
            print('senha deve ser maior que 5 caracteres')
            senha = input('Entre com a senha:\n')
        print('cadastrato com sucesso\n')
        
        self.registro[usuario]=senha
        
        self.logar()
              
    def logar(self):
            
        usuario = input('Entre com o login: ')
        
        while usuario =='':
            usuario = input('Entre com um login valido: ')
        
        senha = input('entre com a senha\n')
       
        while senha == '' or len(senha)<=5:
            senha = input('entre com uma senha validaa a cima de 5 caracteres\n')
        
        if self.registro.get(usuario):
            if self.registro[usuario]==senha:
                print('logado')
                self.status = True
            else:
                print('Senha errada\n')
                self.apresentacao()
        else:
            print('usuário não existe\n')
            self.apresentacao()
    
    def apresentacao(self):
        escolha = input('escolha 1 para logar, 2 para cadastrar')
        while escolha != '1' and escolha != '2':
            escolha = input('escolha 1 para logar, 2 para cadastrar')
        if escolha == '1':
            self.logar()
        elif escolha =='2':
            self.cadastrar()
            
a=loguin()
a
