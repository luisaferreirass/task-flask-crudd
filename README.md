**# 📋 Task Flask CRUD

## 📝 Sobre o projeto

API REST de gerenciamento de tarefas (To-Do List) desenvolvida com **Flask**. O projeto implementa as operações CRUD (Create, Read, Update, Delete) completas para gerenciar tarefas de forma eficiente através de endpoints REST, utilizando armazenamento em memória.

Ideal para aprendizado de desenvolvimento web com Python, demonstrando conceitos de:
- Framework Flask
- APIs RESTful
- Operações CRUD
- Manipulação de dados JSON
- Rotas e métodos HTTP
- Testes automatizados com Pytest

## 🚀 Tecnologias utilizadas

- **Python 3.x**
- **Flask 2.3.0** - Framework web
- **Werkzeug 2.3.0** - WSGI toolkit
- **Requests 2.31.0** - HTTP library
- **Pytest 7.4.3** - Framework de testes

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

### Executando os testes
```bash
pytest
```

ou para ver mais detalhes:
```bash
pytest -v
```

## 🎯 Funcionalidades

- ✅ **Criar** novas tarefas
- 📖 **Visualizar** lista de tarefas
- 🔍 **Buscar** tarefa específica por ID
- ✏️ **Editar** tarefas existentes
- 🗑️ **Excluir** tarefas
- 🧪 Testes automatizados

## 🛠️ Modelo de dados

### Task (Tarefa)

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | Integer | Identificador único (auto-incremento) |
| title | String | Título da tarefa |
| description | String | Descrição detalhada |
| completed | Boolean | Status de conclusão (padrão: False) |

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
  "description": "Aprender sobre APIs REST com Flask"
}
```

**Resposta:**
```json
{
  "message": "Nova tarefa criada com sucesso",
  "id": 1
}
```

### Listar todas as tarefas
```bash
GET /tasks
```

**Resposta:**
```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Estudar Flask",
      "description": "Aprender sobre APIs REST com Flask",
      "completed": false
    }
  ],
  "total_tasks": 1
}
```

### Buscar tarefa por ID
```bash
GET /tasks/1
```

### Atualizar uma tarefa
```bash
PUT /tasks/1
Content-Type: application/json

{
  "title": "Estudar Flask - Concluído",
  "description": "Aprender sobre APIs REST com Flask",
  "completed": true
}
```

**Resposta:**
```json
{
  "message": "Tarefa atualizada com sucesso"
}
```

### Deletar uma tarefa
```bash
DELETE /tasks/1
```

**Resposta:**
```json
{
  "message": "Tarefa deletada com sucesso"
}
```

## ⚠️ Observações

- Os dados são armazenados em memória, portanto serão perdidos ao reiniciar a aplicação
- Para persistência de dados, considere implementar um banco de dados (SQLite, PostgreSQL, etc.)

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📄 Licença

Este projeto está sob a licença MIT.

## 👩‍💻 Autora

Desenvolvido por [Luisa Ferreira](https://github.com/luisaferreirass)
```
