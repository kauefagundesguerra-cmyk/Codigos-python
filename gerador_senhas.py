import string
from random import choice,choices,shuffle
def gerador_senha(tamanho_senha):
    """
    Gera uma senha aleatória com o tamanho informado.
    -------------------------------------------------
    Args:
        tamanho_senha (int): Tamanho da senha.
    ------------------------------------------------
    Returns:
        str: Senha gerada
    """
    senha_min =list(choice(string.ascii_letters)+
    choice(string.punctuation)+choice(string.digits))
    caracteres =list(string.ascii_letters + string.punctuation + string.digits)
    shuffle(caracteres)
    if tamanho_senha < 4:
        print("Tamanho da senha insufuciente, tente novamente")
        raise ValueError("tamanho da senha insuficiente")
    senha =choices(caracteres,k=tamanho_senha - len(senha_min))
    senha.extend(senha_min)
    return "".join(senha)
print(gerador_senha())


