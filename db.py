# db.py
import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG
from typing import Optional, List, Dict
import datetime

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

# CREATE
def criar_funcionario(nome: str, cargo: Optional[str], salario: Optional[float],
                      setor: Optional[str], telefone: Optional[str],
                      email: Optional[str], data_admissao: Optional[str]) -> int:
    """
    data_admissao: 'YYYY-MM-DD' ou None
    retorna id criado
    """
    query = """
    INSERT INTO funcionarios (nome, cargo, salario, setor, telefone, email, data_admissao)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    da = None
    if data_admissao:
        # tenta converter para date
        da = datetime.datetime.strptime(data_admissao, "%Y-%m-%d").date()
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(query, (nome, cargo, salario, setor, telefone, email, da))
        conn.commit()
        new_id = cursor.lastrowid
        cursor.close()
        return new_id
    except Error as e:
        print("Erro ao criar funcionário:", e)
        raise
    finally:
        if conn and conn.is_connected():
            conn.close()

# READ (todos)
def listar_funcionarios() -> List[Dict]:
    query = "SELECT id, nome, cargo, salario, setor, telefone, email, data_admissao FROM funcionarios"
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        return rows
    finally:
        conn.close()

# READ (por id)
def buscar_por_id(func_id: int) -> Optional[Dict]:
    query = "SELECT id, nome, cargo, salario, setor, telefone, email, data_admissao FROM funcionarios WHERE id = %s"
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (func_id,))
        row = cursor.fetchone()
        cursor.close()
        return row
    finally:
        conn.close()

# UPDATE
def atualizar_funcionario(func_id: int, dados: Dict) -> bool:
    """
    dados: dicionário com chaves permitidas: nome,cargo,salario,setor,telefone,email,data_admissao
    Retorna True se alterou >0 linhas
    """
    campos = []
    valores = []
    for chave in ("nome","cargo","salario","setor","telefone","email","data_admissao"):
        if chave in dados:
            if chave == "data_admissao" and dados[chave]:
                # parse
                valores.append(datetime.datetime.strptime(dados[chave], "%Y-%m-%d").date())
            else:
                valores.append(dados[chave])
            campos.append(f"{chave} = %s")
    if not campos:
        return False
    valores.append(func_id)
    query = f"UPDATE funcionarios SET {', '.join(campos)} WHERE id = %s"
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query, tuple(valores))
        conn.commit()
        affected = cursor.rowcount
        cursor.close()
        return affected > 0
    finally:
        conn.close()

# DELETE
def deletar_funcionario(func_id: int) -> bool:
    query = "DELETE FROM funcionarios WHERE id = %s"
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query, (func_id,))
        conn.commit()
        affected = cursor.rowcount
        cursor.close()
        return affected > 0
    finally:
        conn.close()
