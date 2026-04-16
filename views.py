import json
import os
from flask import Blueprint, render_template, request, redirect, url_for



main_bp = Blueprint('main', __name__)

arquivo_produtos = 'produtos.txt'

def ler_produtos():
    if not os.exists(arquivo_produtos):
        return[]
    with open('arquivo_produtos', 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except:
            return[]
        
@main_bp.route("/salvar_produto", methods=['POST'])
def salvar_produtos():
    nome = request.form.get("nome")
    quant = int(request.form.get("quantidade"))
    preco = float(request.form.get("preco"))

    novo_produto = {
        'nome': nome,
        'quantidade': quant,
        'preco': preco,
        'preco_total': preco * quant
    }

    lista_atual = ler_produtos()
    lista_atual.append(novo_produto)

    with open(arquivo_produtos, 'w', encoding='utf-8') as f:
        json.dump(lista_atual, f, indent=4)
    return redirect(url_for('main.estoque'))

@main_bp.route("/")

def index():
    return render_template("Index.html")

@main_bp.route("/estoque")

def estoque():

    produtos = [
        {
            'nome': "CLOREXIDINA, DIGLUCONATO A 0,2%" ,
            'codigo':"158648795",
            'embalagem': "Unitário",
            'quantidade': 10,
            'preco_un': 80.00,
            'preco_total': 800.00,
        },
         {
            'nome': "PARACETAMOL" ,
            'codigo':"15864856",
            'embalagem': "Unitário",
            'quantidade': 20,
            'preco_un': 90.00,
            'preco_total': 1800.00,
        }
    ]

    total_quantidade = sum(p['quantidade'] for p in produtos)

    total_reais = sum(p['preco_total'] for p in produtos)

    return render_template("Estoque.html", produtos = produtos, total_quant = total_quantidade, total_real = total_reais)



@main_bp.route("/cadastro")

def cadastro():
    return render_template("Cadastro.html")
