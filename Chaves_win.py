from tkinter import *
from tkinter import ttk
import random
import pygame
import os

# Iniciar o mixer para tocar som
pygame.mixer.init()

# Lista de músicas de fundo (mp3)
music_files = [
    "/mnt/data/lullaby.mp3"  # Você pode substituir pelo caminho de outras músicas
]

# Lista de chaves (exemplos fictícios para fins lúdicos e educativos)
windows_keys = [
    "VK7JG-NPHTM-C97JM-9MPGT-3V66T",
    "W269N-WFGWX-YVC9B-4J6C9-T83GX",
    "MH37W-N47XK-V7XM9-C7227-GCQG9",
    "XGVPP-NMH47-7TTHJ-W3FW7-8HV2C"
]

# Frases fixas que formam a canção
lullaby_phrases = [
    "Nana neném, que o céu vai brilhar,",
    "O Windows vai ativar sem precisar chorar.",
    "Com amor no coração e a luz da manhã,",
    "A *** te dá a chave: {key}, manhã.",
    "Fecha os olhos devagar, respira bem baixinho,",
    "A Microsoft cuidando dos seus sonhinhos..."
]

# Função para gerar a canção
def generate_lullaby():
    selected_key = random.choice(windows_keys)
    text_output = ""
    for phrase in lullaby_phrases:
        if "{key}" in phrase:
            phrase = phrase.format(key=selected_key)
        text_output += phrase + "\n"
    text_box.config(state=NORMAL)
    text_box.delete(1.0, END)
    text_box.insert(END, text_output)
    text_box.tag_remove("key", "1.0", END)
    text_box.tag_config("key", foreground="blue", font=("Segoe UI", 12, "bold"))

    # Enfatizar chave
    key_index = text_output.find(selected_key)
    if key_index != -1:
        start = f"1.0+{key_index}c"
        end = f"1.0+{key_index+len(selected_key)}c"
        text_box.tag_add("key", start, end)

    text_box.config(state=DISABLED)

# Função para tocar música
def play_music():
    pygame.mixer.music.stop()
    music_file = random.choice(music_files)
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)  # -1 = repetir indefinidamente

# Criar interface principal
root = Tk()
root.title("Canção de Ninar das Chaves 💙")
root.geometry("600x400")
root.configure(bg="#001f3f")

style = ttk.Style()
style.theme_use('clam')
style.configure("TButton", foreground="black", background="#7FDBFF", font=("Segoe UI", 10, "bold"))

# Título
title_label = Label(root, text="✨ Canção de Ninar com Chave do Windows ✨", font=("Segoe UI", 14, "bold"),
                    bg="#001f3f", fg="white")
title_label.pack(pady=10)

# Caixa de texto
text_box = Text(root, width=70, height=10, wrap=WORD, font=("Segoe UI", 11), bg="white", fg="black")
text_box.pack(padx=10, pady=10)
text_box.config(state=DISABLED)

# Botões
button_frame = Frame(root, bg="#001f3f")
button_frame.pack(pady=10)

generate_btn = ttk.Button(button_frame, text="🎵 Nova Canção", command=generate_lullaby)
generate_btn.grid(row=0, column=0, padx=5)

music_btn = ttk.Button(button_frame, text="🎧 Tocar Música", command=play_music)
music_btn.grid(row=0, column=1, padx=5)

# Inicializar com uma canção
generate_lullaby()

root.mainloop()
