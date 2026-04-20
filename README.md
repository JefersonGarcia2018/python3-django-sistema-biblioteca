# Sistema de Biblioteca 📚

Um sistema web completo, responsivo e seguro focado no gerenciamento ágil de seu acervo literário. Desenvolvido em **Python e Django**, este projeto permite organizar, catalogar e acompanhar os seus livros e autores preferidos.

## 🚀 Tecnologias e Ferramentas

O projeto utiliza um stack sólido, nativo e leve, visando alta manutenibilidade e performance:

*   **Backend:** Python 3 + Django
*   **Database:** SQLite 3 nativo (ideal para bibliotecas de escopo pessoal a médio porte)
*   **Frontend (Interface):** TailwindCSS integrado via CDN
*   **Comportamento Dinâmico:** Vanilla JavaScript (ES6+) e chamadas nativas de Fetch API para o carregamento sem interrupções.
*   **Ambiente de Desenvolvimento:** Linux/Ubuntu

## 🏗️ Arquitetura

O sistema emprega a arquitetura **MVT** (Model, View, Template) tradicional do ecossistema Django de forte coesão, particionado em dois aplicativos altamente independentes (*apps*):

1.  **`usuarios`**: App responsável pela gestão estrutural de segurança, cadastros e login, expandindo o `AbstractUser` e integrando rotas customizadas de validação de sessões baseadas em E-mail como credencial principal.
2.  **`livros`**: O core de negócios e principal interface de dados, possuindo relacionamentos base unindo *Autores* aos *Livros*. Engloba os modelos, os formulários com verificações integradas, e a lógica das transações C.R.U.D.

-----
### Vídeo demonstração - Sistema de Biblioteca
[![Assista ao vídeo de exemplo](https://img.youtube.com/vi/9V3cCOrKcMs/maxresdefault.jpg)](https://youtu.be/9V3cCOrKcMs)
-----

## 💻 Como Rodar o Projeto

Caso faça um fork ou baixe, você pode rodar esse repositório em desenvolvimento em sua própria base:

**1. Clone o repositório e inicie um ambiente virtual (venv):**
```bash
git clone https://github.com/JefersonGarcia2018/python3-django-sistema-biblioteca.git
cd python3-django-sistema-biblioteca
python3 -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
```

**2. Instale o Django:**
*(Verifique a versão no arquivo local, recomendado usar o Django LTS recente).*
```bash
pip install django
```

**3. Execute as Migrations para construir seu Banco na máquina local:**
```bash
python manage.py makemigrations
python manage.py migrate
```

**4. Inicialize a biblioteca:**
```bash
python manage.py runserver
```

Acesse em `http://127.0.0.1:8000/` localmente e navegue pelo projeto!
