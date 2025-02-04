import os

# Caminho para a pasta que você deseja ler
caminho_da_pasta = r'C:\Users\Gleison\Desktop\RoletaArcana\hogwarts'  # Usando r para string bruta

# Lista para armazenar os nomes e extensões dos arquivos
arquivos = []

# Percorrendo todos os arquivos na pasta
for nome_arquivo in os.listdir(caminho_da_pasta):
    # Verificando se é um arquivo (não uma pasta)
    if os.path.isfile(os.path.join(caminho_da_pasta, nome_arquivo)):
        # Separando nome do arquivo e extensão
        nome, extensao = os.path.splitext(nome_arquivo)
        arquivos.append((nome, extensao))

# Exibindo os resultados
for nome, extensao in arquivos:
    print(f' {nome}{extensao}')
