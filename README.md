# 📋 Task Flask CRUD

## 📝 Sobre o projeto

Aplicação web simples de gerenciamento de tarefas (To-Do List) desenvolvida com **Flask** e **SQLAlchemy**. O projeto implementa as operações CRUD (Create, Read, Update, Delete) completas para gerenciar tarefas de forma eficiente através de uma interface web intuitiva.

Ideal para aprendizado de desenvolvimento web com Python, demonstrando conceitos de:
- Framework Flask
- ORM com SQLAlchemy
- Banco de dados SQLite
- Templates HTML com Jinja2
- Roteamento e métodos HTTP

## 🚀 Tecnologias utilizadas

- **Python 3.x**
- **Flask** - Framework web
- **Flask-SQLAlchemy** - ORM para banco de dados
- **SQLite** - Banco de dados
- **HTML/CSS** - Interface do usuário
- **Jinja2** - Template engine

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
pip install flask flask-sqlalchemy
```

### Executando a aplicação
```bash
python app.py
```

A aplicação estará disponível em: `http://localhost:5000`

## 📁 Estrutura do projeto
```
task-flask-crudd/
├── app.py                 # Aplicação principal Flask
├── instance/
│   └── tasks.db          # Banco de dados SQLite (gerado automaticamente)
├── templates/
│   ├── base.html         # Template base
│   ├── index.html        # Página principal (lista de tarefas)
│   ├── create.html       # Formulário de criação
│   └── update.html       # Formulário de atualização
├── static/
│   └── css/
│       └── style.css     # Estilos CSS
└── README.md
```

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

## 📸 Rotas da aplicação

| Rota | Método | Descrição |
|------|--------|-----------|
| `/` | GET | Lista todas as tarefas |
| `/create` | GET, POST | Cria uma nova tarefa |
| `/update/<id>` | GET, POST | Atualiza uma tarefa existente |
| `/delete/<id>` | POST | Exclui uma tarefa |

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📄 Licença

Este projeto está sob a licença MIT.

## 👩‍💻 Autora

Desenvolvido por [Luisa Ferreira](https://github.com/luisaferreirass)
