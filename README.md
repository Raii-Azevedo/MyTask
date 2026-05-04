# TaskHub - Kanban com Subtarefas e Catalogo de Documentos

Aplicacao web feita com Django para organizar tarefas em formato Kanban, com checklist de subtarefas, deadline e prioridade, alem de uma pagina para catalogar links de documentos por cliente.

## Funcionalidades

- Kanban com colunas: To Do, Doing, Done
- Criacao e edicao de tarefas
- Prioridade por tarefa: Alta, Media, Baixa
- Deadline por tarefa
- Checklist de subtarefas (checkbox) dentro da tarefa-pai
- Pagina de catalogo de documentos com:
  - Titulo
  - Link
  - Cliente
  - Data de criacao/modificacao (data de referencia)
- Busca de documentos por titulo, cliente ou URL
- Tema dark

## Stack

- Python 3.12
- Django 6
- PostgreSQL
- psycopg (driver PostgreSQL)

## Estrutura principal

- `config/`: configuracoes do projeto Django
- `board/`: app principal (kanban + documentos)
- `manage.py`: comandos Django

## Requisitos

- Python instalado
- PostgreSQL instalado e em execucao

## Instalacao

1. Criar e ativar ambiente virtual (Windows PowerShell):

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

2. Instalar dependencias:

```powershell
pip install django psycopg[binary]
```

## Configuracao do banco (PostgreSQL)

Defina as variaveis de ambiente antes de rodar migracoes e servidor.

PowerShell:

```powershell
$env:POSTGRES_DB="mytask_db"
$env:POSTGRES_USER="mytask_user"
$env:POSTGRES_PASSWORD="sua_senha_forte"
$env:POSTGRES_HOST="localhost"
$env:POSTGRES_PORT="5432"
```

A aplicacao ja esta configurada para ler essas variaveis em `config/settings.py`.

## Rodando o projeto

1. Aplicar migracoes:

```powershell
python manage.py migrate
```

2. Subir servidor de desenvolvimento:

```powershell
python manage.py runserver
```

3. Acessar no navegador:

- Kanban: `http://127.0.0.1:8000/`
- Documentos: `http://127.0.0.1:8000/documents/`
- Admin: `http://127.0.0.1:8000/admin/`

## Comandos uteis

Criar superusuario:

```powershell
python manage.py createsuperuser
```

Verificar integridade do projeto:

```powershell
python manage.py check
```

Gerar novas migracoes apos alteracoes de modelo:

```powershell
python manage.py makemigrations
python manage.py migrate
```

## Observacoes

- O projeto foi alterado para usar PostgreSQL no lugar de SQLite.
- Se existir `db.sqlite3` na raiz, ele nao e mais utilizado com a configuracao atual.
