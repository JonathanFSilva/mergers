#  https://wadsongarbes.github.io/mergers/ - Mergers

Aplicativo de estrutura societária desenvolvido para a disciplina IHC - Interface Humano-Computador - Fatec SP

## Por onde começar ?

Estas instruções darão à você uma cópia do projeto rodando em sua máquina local para testes e feedback. Todas as instruções para baixar e rodar a aplicação se encontram abaixo!
### Pré-requisitos

```
Shell Linux 
```
```
Python2.7
```
```
mysql
```
```
pip
```
```
virtualenv
```
```
Este repositório
```

### Instalando

Por padrão, toda distribuição Linux acompanha Python2.7 e Python3.x. É possível verificar isto abrindo um shell em seu ambiente Linux e digitando:

```
$ python --version
```

A resposta deve ser:

```
Python 2.7.x
```

Instale o MySQL e suas dependências para desenvolvimento:

```
$ sudo apt install mysql-client mysql-server libmysqlclient-dev -y
```

Daí então podemos começar a instalar as dependências para rodar a aplicação:

```
$ sudo apt install pip
```

pip é o instalador de pacotes do python, necessário para instalação das dependências da aplicação

```
$ sudo apt install virtualenv
```

Responsável por isolar nossa aplicação da máquina "hospedeira", garantido um controle maior sobre as dependências da aplicação

```
$ git clone https://github.com/wadsongarbes/mergers
```

baixe a aplicação e a armazene-a no repositório de mesmo nome (mergers)

```
$ virtualenv venv && . venv/bin/activate
```
cria e ativa um ambiente virtual

```
$ pip install -r requirements.txt
```
baixa as dependências do projeto

### Criando o banco de dados

É necessário criar um banco de dados para a aplicação. Usando o shell do mysql, digite os seguintes comandos:

```
$ mysql -u root
```

caso seu banco de dados possua senha, tente:

```
$ mysql -u root -p
```

Isso garante acesso ao shell do mysql. Após tal, crie o banco de dados:

```
mysql> CREATE USER 'mer_admin'@'localhost' IDENTIFIED BY 'mer2017';
Query OK, 0 rows affected (0.00 sec)
```
```
mysql> CREATE DATABASE mergers_db;
Query OK, 1 row affected (0.00 sec)
```
```
mysql> GRANT ALL PRIVILEGES ON mergers_db . * TO 'mer_admin'@'localhost';
Query OK, 0 rows affected (0.00 sec)
```

Pronto! Agora é só cruzar os dedos e rodar!

## Criando o usuário administrador

É necessário criar um usuário administrador para fazer as participações na aplicação. para isso, digite os seguintes comandos:

```
$ flask shell
```
```
>>> from app.models import Empresa
```
```
>>> from app import db
```
```
>>> admin = Empresa(email="admin@admin.com",username="Admin",password="admin",is_admin=True)
```
```
>>> db.session.add(admin)
```
```
>>> db.session.commit()
```
## Rodando a aplicação

Entre na pasta recém clonada e crie um ambiente virtual (virtualenv)

```
$ cd mergers && virtualenv venv
```

Ative este ambiente virtual, assim será posível instalar todas as dependências do projeto sem afetar a máquina local

```
$ . venv/bin/activte
```

Instale as dependências do projeto no ambiente virtual

```
(venv) $ pip install -r requirements.txt
```

Exporte as duas variáveis necessárias para o flask

```
(venv) $ export FLASK_APP=run.py && export FLASK_CONFIG=development
```

Crie o banco de dados (é necessário exportar as variáveis primeiro!)

```
(venv) $ flask db init
```


```
(venv) $ flask db migrate
```


```
(venv) $ flask db upgrade
```

Rode o servidor

```
(venv) $ flask run
```

Acesse o link disponibilizado pelo servidor (http://127.0.0.1:5000) em seu navegador de preferência

Caso o comando acima não funcione, tente, no diretório mergers:

```
(venv) $ python run.py
```

## Cansei!

No shell onde o servidor está rodando, tecle `ctrl + c` e desative o ambiente virtual com

`(venv) $ deactivate`

## Construído com

* [Flask](http://www.http://flask.pocoo.org/) - Framework utilizado

## Dúvidas ?

Pergunte qualquer coisa na seção "Issue". Em caso de erros, poste o motivo e o log para uma melhor resposta!

* [Dúvidas](https://github.com/WadsonGarbes/mergers/issues)
