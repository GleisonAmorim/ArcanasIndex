import os
import shutil
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

def select_folder(prompt):
    messagebox.showinfo("Selecionar Pasta", prompt)
    folder_selected = filedialog.askdirectory()
    return folder_selected

def rename_and_move_files():
    source_folder = select_folder("Selecione a pasta com as imagens:")
    if not source_folder:
        messagebox.showwarning("Aviso", "Nenhuma pasta selecionada!")
        return
    
    destination_folder = select_folder("Selecione a pasta onde os arquivos serão salvos:")
    if not destination_folder:
        messagebox.showwarning("Aviso", "Nenhuma pasta selecionada!")
        return
    
    files = sorted(os.listdir(source_folder))  # Ordena os arquivos
    
    for index, file in enumerate(files):
        old_path = os.path.join(source_folder, file)
        
        if os.path.isfile(old_path):  # Garante que é um arquivo
            extension = os.path.splitext(file)[1]  # Obtém a extensão do arquivo
            new_filename = f"{index}{extension}"  # Novo nome
            new_path = os.path.join(destination_folder, new_filename)
            
            shutil.move(old_path, new_path)  # Move e renomeia o arquivo
            print(f"{file} -> {new_filename}")
    
    messagebox.showinfo("Sucesso", "Arquivos renomeados e movidos com sucesso!")

# Criando interface gráfica
root = tk.Tk()
root.withdraw()  # Esconde a janela principal
rename_and_move_files()
