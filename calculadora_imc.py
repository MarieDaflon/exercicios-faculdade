import tkinter as tk
from tkinter import messagebox


def calculo_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        resultado = peso / (altura ** 2)
        if resultado <= 18.5:
            messagebox.showinfo("Resultado", f"Seu IMC é {resultado:.2f} - Você esta abaixo do peso.")
        elif resultado <= 24.9:
            messagebox.showinfo("Resultado", f"Seu IMC é {resultado:.2f} - Seu peso esta normal")
        elif resultado <= 29.9:
            messagebox.showinfo("Resultado", f"Seu IMC é {resultado:.2f} - Você esta sobrepeso.")
        elif resultado <= 34.9:
            messagebox.showinfo("Resultado", f"Seu IMC é {resultado:.2f} - Obesidade grau 1")
        elif resultado <= 39.9:
            messagebox.showinfo("Resultado", f"Seu IMC é {resultado:.2f} - Obesidade grau 2 (severa)")
        else:
            messagebox.showinfo("Resultado", f"Seu IMC é {resultado:.2f} - Obesidade grau 3 (mórbida)")
    except ValueError:
        messagebox.showerror("Resultado", "Digite um número válido!")



# Criando a janela
janela = tk.Tk()
janela.title("Calculando IMC")

# Criando os widgets
label_peso = tk.Label(janela, text="Peso:")
label_peso.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_peso = tk.Entry(janela)
entry_peso.grid(row=0, column=1, padx=10, pady=5)

label_altura = tk.Label(janela, text="Altura:")
label_altura.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_altura = tk.Entry(janela)
entry_altura.grid(row=1, column=1, padx=10, pady=5)

botao_comp = tk.Button(janela, text="Calcular", command=calculo_imc)
botao_comp.grid(row=2, columnspan=2, padx=10, pady=5)

# Rodando o loop principal
janela.mainloop()
