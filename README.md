# Mergers

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
virtualenvwrapper
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

É necessário possui mysql-client e mysql-server para usar o banco de dados da aplicação, portanto, instale se for necessário com:

```
$ sudo apt install mysql-client mysql-server -y
```

Daí então podemos começar a instalar as dependências para rodar a aplicação:

```
$ sudo apt install pip
```

pip é o instalador de pacotes do python, necessário para instalação das dependências da aplicação

```
$ sudo apt install virtualenvwrapper
```

Responsável por isolar nossa aplicação da máquina "hospedeira", garantido um controle maior sobre as dependências da aplicação

```
$ git clone https://github.com/wadsongarbes/mergers
```

Por fim, baixa a aplicação e a armazena no repositório de mesmo nome (mergers)


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

## Chega!

No shell onde o servidor está rodando, tecle `ctrl + c` e desative o ambiente virtual com `(venv) $ deactivate`

## Construído com

* [Flask](http://www.http://flask.pocoo.org/) - Framework utilizado
