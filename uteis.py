from datetime import datetime

def definirSaudacao():
    hora = int((datetime.now()).strftime("%H"))

    if hora < 12:
        saud = "Bom Dia!"
    elif 12 <= hora < 18:
        saud = "Boa Tarde!"
    else:
        saud = "Boa Noite!"

    return formataTitulo(saud)


def formataTitulo(texto):
    tamanho = 38
    titulo = ""

    titulo += "." * tamanho
    titulo += "\n"
    titulo += texto.center(tamanho, " ")
    titulo += "\n"
    titulo += "." * tamanho

    print(titulo)
    