from flask import Flask

# Flask é um framework (conjunto de ferramentas já prontas) para facilitar o desenvolvimento web

# __name__ = "__main__" (Quando executar de forma manual)
app = Flask(__name__) # Criando uma instância da classe Flask

# Uma rota é como conseguimos comunicar com outros clientes (usuários), receber e devolver informações 

# Crairemos uma rota "Hello world!" que vai retornar uma string no formato html para quem acessar ela

@app.route("/") # Rota padrão/inicial
# Oque vai ser executado quando entrarmos nessa rota
def hello_world():
    return "Hello world!"

@app.route("/about")
def about():
    return "Página sobre"

if __name__ == "__main__": # Garantir isso quando executarmos o servidor de forma apenas manual para o desenvolvimento local
    app.run(debug=True) #Coletar informações