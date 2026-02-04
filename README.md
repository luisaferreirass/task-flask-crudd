# 📋 Task Flask CRUD

## 📝 Sobre o projeto

API REST de gerenciamento de tarefas (To-Do List) desenvolvida com **Flask** e **SQLAlchemy**. O projeto implementa as operações CRUD (Create, Read, Update, Delete) completas para gerenciar tarefas de forma eficiente através de endpoints REST.

Ideal para aprendizado de desenvolvimento web com Python, demonstrando conceitos de:
- Framework Flask
- ORM com SQLAlchemy
- Banco de dados SQLite
- APIs RESTful
- Operações CRUD

## 🚀 Tecnologias utilizadas

- **Python 3.x**
- **Flask** - Framework web
- **Flask-SQLAlchemy** - ORM para banco de dados
- **SQLite** - Banco de dados

## ⚙️ Como executar

### Pré-requisitos

- Python 3.x instalado
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/luisaferreirass/task-flask-crudd.git
cd task-flask-crudd
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Executando a aplicação
```bash
python app.py
```

A API estará disponível em: `http://localhost:5000`

## 🎯 Funcionalidades

- ✅ **Criar** novas tarefas
- 📖 **Visualizar** lista de tarefas
- ✏️ **Editar** tarefas existentes
- 🗑️ **Excluir** tarefas
- 💾 Persistência de dados com SQLite

## 🛠️ Modelo de dados

### Task (Tarefa)

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | Integer | Chave primária (auto-incremento) |
| title | String(100) | Título da tarefa |
| description | Text | Descrição detalhada |
| done | Boolean | Status de conclusão (padrão: False) |

## 📸 Endpoints da API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/tasks` | Lista todas as tarefas |
| GET | `/tasks/<id>` | Visualiza uma tarefa específica |
| POST | `/tasks` | Cria uma nova tarefa |
| PUT | `/tasks/<id>` | Atualiza uma tarefa existente |
| DELETE | `/tasks/<id>` | Exclui uma tarefa |

## 💡 Exemplos de uso

### Criar uma tarefa
```bash
POST /tasks
Content-Type: application/json

{
  "title": "Estudar Flask",
  "description": "Aprender sobre APIs REST com Flask",
  "done": false
}
```

### Listar todas as tarefas
```bash
GET /tasks
```

### Atualizar uma tarefa
```bash
PUT /tasks/1
Content-Type: application/json

{
  "title": "Estudar Flask - Concluído",
  "done": true
}
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📄 Licença

Este projeto está sob a licença MIT.

## 👩‍💻 Autora

Desenvolvido por [Luisa Ferreira](https://github.com/luisaferreirass)
```
