from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'título': 'Percy Jackson - O Ladrão de Raios',
        'autor': 'Rick Riordan',
    },
    {
        'id': 3,
        'título': 'Harry Potter e o Cálice de Fogo',
        'autor': 'J.K Rowlling',
    },
]

# Consultar todos os livros

@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar por (id)

@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
       if livro.get('id') == id:
           return jsonify(livro)

# Editar um livro

@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
        
# Criar um livro

@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

# Excluir um livro

@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            
    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)