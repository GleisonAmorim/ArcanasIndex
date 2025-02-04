import os

def listar_arquivos_formatados(diretorio, prefixo):
    arquivos = os.listdir(diretorio)  # Lista todos os arquivos na pasta
    arquivos = [f for f in arquivos if os.path.isfile(os.path.join(diretorio, f))]  # Filtra apenas arquivos

    # Formatar os arquivos no padrão desejado
    arquivos_formatados = [f"'{prefixo}/{arquivo}'" for arquivo in arquivos]

    # Gerar saída formatada em blocos de até 4 por linha
    resultado = ",\n    ".join(arquivos_formatados)

    with open("lista_formatada.txt", "w", encoding="utf-8") as f:
        f.write(resultado)

    print("Lista de arquivos formatada com sucesso no arquivo 'lista_formatada.txt'.")

# Informe o caminho da pasta e o prefixo desejado
pasta = input("Digite o caminho da pasta: ")
prefixo = input("Digite o prefixo (ex: HOGWARTS): ")

listar_arquivos_formatados(pasta, prefixo)
