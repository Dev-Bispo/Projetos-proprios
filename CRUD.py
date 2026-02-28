from conexao import Usuario, Jogos, Historico, Endereco, _Session
from flask import flash


class Operacaoes:

    def add_usuario(nome,username,genero,data_nascimento,senha,nivel):

        with _Session()  as session:
            usuario = Usuario(nome,username,genero,data_nascimento,senha,nivel) 
            session.add(usuario)
            session.commit()

    def del_usuario(nome):

        with _Session() as session:
            usuario_del = session.query(Usuario).filter(Usuario.nome == nome).first()
            if usuario_del:
                session.delete(usuario_del)
                session.commit() 
            else:
                return flash("usuario nao encontrado", "error")   

    def atualizar_usuario(nome,novo,coluna):

        with _Session() as session:
            usuario_novo = session.query(Usuario).filter(Usuario.nome == nome).first()
            if usuario_novo:
                setattr(usuario_novo,coluna,novo)
                session.commit()
            else:
                return flash("usuario nao foi encontrado", 'error')   
    def visualiza_usuario(email,senha):
        with _Session() as session:
            usuario = session.query(Usuario).filter(Usuario.)
    # ========== FUNÇÕES PARA JOGOS ==========

    def add_jogo(nome, tipo):
        with _Session() as session:
            jogo = Jogos(nome=nome, tipo=tipo)
            session.add(jogo)
            session.commit()

    def del_jogo(nome):
        with _Session() as session:
            jogo_del = session.query(Jogos).filter(Jogos.nome == nome).first()
            if jogo_del:
                session.delete(jogo_del)
                session.commit()
            else:
                return flash("jogo nao encontrado", "error")

    def atualizar_jogo(nome, novo, coluna):
        with _Session() as session:
            jogo_novo = session.query(Jogos).filter(Jogos.nome == nome).first()
            if jogo_novo:
                setattr(jogo_novo, coluna, novo)
                session.commit()
            else:
                return flash("jogo nao foi encontrado", 'error')

    # ========== FUNÇÕES PARA ENDEREÇO ==========

    def add_endereco(logradouro, bairro, cidade, estado, numero):
        with _Session() as session:
            endereco = Endereco(
                logradouro=logradouro,
                bairro=bairro,
                cidade=cidade,
                estado=estado,
                numero=numero
            )
            session.add(endereco)
            session.commit()

    def del_endereco(id_endereco):
        with _Session() as session:            
            endereco_del = session.query(Endereco).filter(Endereco.id_endereco == id_endereco).first()
            if endereco_del:
                session.delete(endereco_del)
                session.commit()
            else:
                return flash("endereco nao encontrado", "error")

    def atualizar_endereco(id_endereco, novo, coluna):
        with _Session() as session:
            endereco_novo = session.query(Endereco).filter(Endereco.id_endereco == id_endereco).first()
            if endereco_novo:
                setattr(endereco_novo, coluna, novo)
                session.commit()
            else:
                return flash("endereco nao foi encontrado", 'error')
             
      









        