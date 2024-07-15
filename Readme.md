# 🍉 Nutriwise 
O NutriWise foi criado na disciplina de GAC-116 Programação WEB. A ideia do sistema é funcionar como um intermediador do nutricionista e o cliente, em que o profissional adiciona a tabela nutricional e o cliente pode acessar. 

## 👨‍💻 Tecnologias Utilizadas
- 🟧 HTML
- 🟦 CSS
- 🟨 JavaScript
- 🐍 Python
- 🤠 Django

## 🎲 Modelagem de dados

![Diagrama UML](/docs/NutriWise-Diagram.png)

## ✅ Como Executar o Projeto (Ambiente Linux)

1. Instale o python na máquina:

       sudo apt install python3-pip


2. Clone este repositório em sua máquina local:

       git clone https://github.com/ootaviofonseca/NutriWise.git


3. Instale a virtualenv:

       pip install virtualenv


4. Crie o ambiente virtual (venv) para isolar as instalações/dependências do Python:

       python3 -m venv venv


5. Ative o ambiente virtual (venv) no seu computador utilizando o comando abaixo:

       source venv/bin/activate (Linux)
       venv\Scripts\Activate (Windows)

6. Instale as dependências:

       pip install -r requirements.txt

7. Execute os seguintes comandos:
       
       python manage.py makemigrations
       python manage.py migrate

8. Inicie a execução do projeto django utilizando o comando abaixo:

       python manage.py runserver

9. Para acessar o Django Admin:

       1. coloque o seguinte comando no terminal:
              python manage.py createsuperuser (você prenche seus dados para criar um super usuário)
       
       2. Coloque um "/admin" na frente do endereço da página

       3. Coloque seu login e senha criado anteriormente


 
## 🤝 Desenvolvedores

Este projeto foi desenvolvido por:

- [Guilherme Grego Santos](https://github.com/GregoSX)
- [Otavio Augusto Trindade Fonseca](https://github.com/ootaviofonseca)
- [Thiago Odilon de Almeida](https://github.com/teagoodilon)

## 📚 Referências

- [Django - Documentação](https://docs.djangoproject.com/en/5.0/)