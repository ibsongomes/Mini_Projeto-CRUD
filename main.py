import tkinter as tk
from tkinter import ttk, messagebox
from db import criar_funcionario, listar_funcionarios, buscar_por_id, atualizar_funcionario, deletar_funcionario

root = tk.Tk()
root.title("CRUD Funcionários - Tkinter + MySQL")
root.geometry("1000x600")

frame_form = tk.Frame(root)
frame_form.pack(pady=10)

labels = ["Nome", "Cargo", "Salário", "Setor", "Telefone", "Email", "Data Admissão (YYYY-MM-DD)", "ID (para buscar/editar)"]
entries = {}

for i, label in enumerate(labels):
    tk.Label(frame_form, text=label).grid(row=i, column=0, sticky="w", padx=5)
    entry = tk.Entry(frame_form, width=40)
    entry.grid(row=i, column=1, padx=5, pady=4)
    entries[label] = entry

def get_form_data():
    return {
        "nome": entries["Nome"].get(),
        "cargo": entries["Cargo"].get(),
        "salario": entries["Salário"].get(),
        "setor": entries["Setor"].get(),
        "telefone": entries["Telefone"].get(),
        "email": entries["Email"].get(),
        "data_admissao": entries["Data Admissão (YYYY-MM-DD)"].get()
    }

def clear_form():
    for e in entries.values():
        e.delete(0, tk.END)

frame_table = tk.Frame(root)
frame_table.pack(pady=10)

cols = ("id", "nome", "cargo", "salario", "setor", "telefone", "email", "data_admissao")
tree = ttk.Treeview(frame_table, columns=cols, show="headings", height=12)

for col in cols:
    tree.heading(col, text=col.upper())
    tree.column(col, width=120)

tree.pack()

def atualizar_tabela():
    for item in tree.get_children():
        tree.delete(item)
    for func in listar_funcionarios():
        tree.insert("", tk.END, values=(
            func["id"],
            func["nome"],
            func["cargo"],
            func["salario"],
            func["setor"],
            func["telefone"],
            func["email"],
            func["data_admissao"]
        ))

def cadastrar():
    dados = get_form_data()

    if not dados["nome"]:
        messagebox.showerror("Erro", "O nome é obrigatório.")
        return

    salario = dados["salario"]
    if salario:
        try:
            dados["salario"] = float(salario)
        except:
            messagebox.showerror("Erro", "Salário inválido.")
            return

    novo_id = criar_funcionario(
        dados["nome"], dados["cargo"], dados["salario"], dados["setor"],
        dados["telefone"], dados["email"], dados["data_admissao"]
    )

    messagebox.showinfo("Sucesso", f"Funcionário cadastrado com ID {novo_id}")
    clear_form()
    atualizar_tabela()

def buscar():
    try:
        func_id = int(entries["ID (para buscar/editar)"].get())
    except:
        messagebox.showerror("Erro", "Digite um ID válido.")
        return

    func = buscar_por_id(func_id)

    if not func:
        messagebox.showinfo("Info", "Funcionário não encontrado.")
        return


    entries["Nome"].insert(0, func["nome"])
    entries["Cargo"].insert(0, func["cargo"])
    entries["Salário"].insert(0, func["salario"])
    entries["Setor"].insert(0, func["setor"])
    entries["Telefone"].insert(0, func["telefone"])
    entries["Email"].insert(0, func["email"])
    entries["Data Admissão (YYYY-MM-DD)"].insert(0, func["data_admissao"])

def atualizar():
    try:
        func_id = int(entries["ID (para buscar/editar)"].get())
    except:
        messagebox.showerror("Erro", "ID inválido.")
        return

    dados = get_form_data()
    dados_limpos = {}

    for chave, valor in dados.items():
        if valor.strip():
            if chave == "salario":
                valor = float(valor)
            dados_limpos[chave] = valor

    if not dados_limpos:
        messagebox.showinfo("Info", "Nenhum campo para atualizar.")
        return

    ok = atualizar_funcionario(func_id, dados_limpos)

    if ok:
        messagebox.showinfo("Sucesso", "Funcionário atualizado.")
        clear_form()
        atualizar_tabela()
    else:
        messagebox.showerror("Erro", "ID não encontrado.")

def deletar():
    try:
        func_id = int(entries["ID (para buscar/editar)"].get())
    except:
        messagebox.showerror("Erro", "ID inválido.")
        return

    confirm = messagebox.askyesno("Confirmar", "Deseja realmente deletar?")
    if not confirm:
        return

    ok = deletar_funcionario(func_id)
    if ok:
        messagebox.showinfo("Sucesso", "Funcionário deletado.")
        clear_form()
        atualizar_tabela()
    else:
        messagebox.showerror("Erro", "ID não encontrado.")

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn1 = tk.Button(frame_buttons, text="Cadastrar", width=15, command=cadastrar)
btn2 = tk.Button(frame_buttons, text="Buscar por ID", width=15, command=buscar)
btn3 = tk.Button(frame_buttons, text="Atualizar", width=15, command=atualizar)
btn4 = tk.Button(frame_buttons, text="Deletar", width=15, command=deletar)
btn5 = tk.Button(frame_buttons, text="Listar Todos", width=15, command=atualizar_tabela)

btn1.grid(row=0, column=0, padx=5)
btn2.grid(row=0, column=1, padx=5)
btn3.grid(row=0, column=2, padx=5)
btn4.grid(row=0, column=3, padx=5)
btn5.grid(row=0, column=4, padx=5)

atualizar_tabela()

root.mainloop()
