# CNAB-parser-matheusprado1

## Descrição:

Interface web que aceita upload do arquivo CNAB, normaliza os dados e armazena em um banco de dados relacional(postgres) e exibe essas informações em tela.

## Começando:

## 1- Rodando localmente

Clone o projeto

```bash
 git clone https://github.com/matheusprado1/cnab-parser-matheusprado1.git
```

Entre no diretório do projeto

```bash
  cd cnab-parser-matheusprado1
```

Crie o ambiente virtual (venv):

```bash
  python -m venv venv
```

Entre no ambiente virtual:

```bash
  source venv/bin/activate
```
Crie um arquivo .env de acordo com o .env.example e suas credenciais


Crie a imagem docker:

```bash
  docker-compose up --build
```
Com o docker rodando entre no bash da imagem docker:

```bash
  docker exec -it cnab-parser-matheusprado1_web_1 bash
```

Rode as migrations:

```bash
  python manage.py migrate
```
Reinicie o servidor:

```bash
  docker-compose up
```
Para executar os testes basta digitar:

```
  python manage.py test
```


## 2- Como utilizar a aplicação:

1. No navegador digite a seguinte url: http://0.0.0.0:8000/api/operations/
2. De um nome para o seu arquivo
3. Clique em Escolher arquivo
4. Selecione o arquivo CNAB
5. Clique em Save File
6. No navegador digite a url com o nome da loja Ex: ``http://0.0.0.0:8000/api/operations/MERCEARIA 3 IRMÃOS``
7. Confira se digitou o nome exatamente como está no arquivo
8. Aproveite!

