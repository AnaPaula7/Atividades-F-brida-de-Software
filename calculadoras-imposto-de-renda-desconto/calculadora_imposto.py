import tkinter as tk
from tkinter import messagebox

def calcular_imposto():
    try:
        salario = float(entry_salario.get())
        if salario <= 2000:
            imposto = 0
        elif salario <= 5000:
            imposto = salario * 0.10
        else:
            imposto = salario * 0.20

        messagebox.showinfo("Resultado", f"Salário: R$ {salario:.2f}\nImposto a pagar: R$ {imposto:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor válido para o salário.")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora de Imposto de Renda")

# Texto e entrada para o salário
label_salario = tk.Label(janela, text="Informe o valor do seu salário:")
label_salario.pack()

entry_salario = tk.Entry(janela)
entry_salario.pack()

# Botão para calcular o imposto
btn_calcular = tk.Button(janela, text="Clique aqui para Calcular o Imposto de Renda", command=calcular_imposto)
btn_calcular.pack()

# Iniciar a interface gráfica
janela.mainloop()
