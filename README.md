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

Daí então podemos começar a instalar as dependências!

```
$ sudo apt install pip
```

Pip é o instalador de pacotes do python, necessário para instalação das dependências da aplicação

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

Ative este ambiente virtual, assim poderás instalar todas as dependências sem afetar a máquina local

```
$ . venv/bin/activte
```

## Construído com

* [Flask](http://www.http://flask.pocoo.org/) -Framework utilizado
