import os
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

def select_folder(prompt):
    messagebox.showinfo("Selecionar Pasta", prompt)
    folder_selected = filedialog.askdirectory()
    return folder_selected

def generate_filename_pattern():
    source_folder = select_folder("Selecione a pasta com os arquivos:")
    if not source_folder:
        messagebox.showwarning("Aviso", "Nenhuma pasta selecionada!")
        return
    
    files = sorted(os.listdir(source_folder))  # Ordena os arquivos
    total_files = len(files)
    
    if total_files == 0:
        messagebox.showwarning("Aviso", "Nenhum arquivo encontrado na pasta selecionada!")
        return
    
    example_pattern = simpledialog.askstring("Padrão de Nome", "Digite um exemplo do padrão desejado (use {num} para o número):")
    
    if not example_pattern or "{num}" not in example_pattern:
        messagebox.showwarning("Erro", "O padrão deve conter '{num}' para substituir pelo número!")
        return
    
    output = []
    for index, file in enumerate(files):
        new_filename = example_pattern.replace("{num}", str(index))
        output.append(f"{new_filename}")
    
    output_text = "\n".join(output)
    print("\nSaída gerada:\n", output_text)
    messagebox.showinfo("Sucesso", "Padrão de nomes gerado! Confira a saída no console.")

# Criando interface gráfica
root = tk.Tk()
root.withdraw()  # Esconde a janela principal
generate_filename_pattern()
