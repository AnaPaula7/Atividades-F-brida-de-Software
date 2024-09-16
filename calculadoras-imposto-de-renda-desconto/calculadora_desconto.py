import tkinter as tk
from tkinter import messagebox

def calcular_total_compra(produtos):
    total = 0.0
    for valor in produtos:
        try:
            valor_float = float(valor)
            if valor_float < 0:
                messagebox.showwarning("Aviso", "O valor do produto não pode ser negativo.")
                return None
            total += valor_float
        except ValueError:
            messagebox.showerror("Erro", "Entrada inválida. Por favor, insira números válidos.")
            return None
    return total

def aplicar_desconto(total):
    if total > 100:
        desconto = total * 0.10
    elif 50 <= total <= 100:
        desconto = total * 0.05
    else:
        desconto = 0
    valor_final = total - desconto
    return valor_final, desconto

def calcular():
    try:
        produtos = entry_produtos.get().split(',')
        total = calcular_total_compra(produtos)
        if total is not None:
            valor_final, desconto = aplicar_desconto(total)
            result_text.set(f"Valor total da compra: R$ {total:.2f}\nDesconto aplicado: R$ {desconto:.2f}\nValor final após desconto: R$ {valor_final:.2f}")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

# Configuração da interface gráfica
root = tk.Tk()
root.title("Calculadora de Compra")

tk.Label(root, text="Digite os valores dos produtos separados por vírgula (ex: 10,20,30):").pack(padx=10, pady=10)
entry_produtos = tk.Entry(root, width=50)
entry_produtos.pack(padx=10, pady=10)

tk.Button(root, text="Calcular", command=calcular).pack(padx=10, pady=10)

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text).pack(padx=10, pady=10)

root.mainloop()
