import os

# Caminho da pasta onde estão as imagens
pasta = "TAROT"

# Extensões permitidas (neste caso, imagens no formato .webp)
extensoes_permitidas = [".webp"]

# Função para listar os arquivos na pasta
def listar_imagens(pasta):
    try:
        # Obtém a lista de arquivos na pasta
        arquivos = os.listdir(pasta)
        # Filtra os arquivos pelas extensões permitidas
        imagens = [arquivo for arquivo in arquivos if os.path.splitext(arquivo)[1].lower() in extensoes_permitidas]
        return imagens
    except FileNotFoundError:
        return f"A pasta '{pasta}' não foi encontrada."
    except Exception as e:
        return f"Ocorreu um erro: {e}"

# Chama a função e exibe as imagens
imagens = listar_imagens(pasta)
print("Imagens encontradas na pasta:")
print(imagens)
