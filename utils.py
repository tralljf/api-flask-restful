from models import Pessoas, Usuarios

def iserir_usuario():
    usuario = Usuarios(login='thiago', password=1234)
    usuario.save()

if __name__ == "__main__":
    iserir_usuario()