# README padrão para meus projetos

[English](https://github.com/Tche-Marco/opencv/blob/master/readme-en.md)

<h1>Nome do projeto</h1>

> Status: Em desenvolvimento

### Esse projeto é uma aplicação WEB criada com o intuito de...

## Modelos de classe do projeto:

- User (classe para representar um usuário)
- Nome da classe (classe para representar um objeto)

### Principais atributos:

- User: name (primeiro nome do usuário)
- User: mail (e-mail do usuário)
- User: birth (data de nascimento do usuário)
- User: active (usuário está ativo?)
- Nome da classe: campo (descrição do campo)

### Métodos para implementação de alguns recursos, como:

- Mensagem de sucesso ao criar um usuário.
- Funções para gerenciar o perfil do usuário.
- Função para obter idade a partir da data de aniversário.

## Recursos em desenvolvimento:

- Verificação de conta e alteração de senha por e-mail.

## Tecnologias usadas:

<table>
  <tr>
    <td>Python</td>
    <td>Django</td>
    <td>PostgreSQL</td>
  </tr>
  <tr>
    <td>3.10</td>
    <td>3.2</td>
    <td>12</td>
  </tr>
</table>

## Como rodar a aplicação:

Crie e habilite um ambiente virtual

```console
  python -m venv venv
```

```console
  venv\Scripts\activate | windows
  .venv/bin/activate | linux e macOs
```

Instale as dependências do projeto

```console
  pip install -r requirements.txt
```

Definindo os valores padrões para as variáveis de ambiente (.env)

```
  Copie o arquivo .env.example e renomeie-o para .env
```

Configurando o banco de dados local

```
  O banco de dados está sendo hospedado localmente, para configurar os acessos, use o arquivo .env e insira as
  informações de acesso do seu banco local.
```

Exemplo de Configuração

```
  SECRET_KEY=Sua chave do Django
  DEBUG=True
  DB_ENGINE=django.db.backends.postgresql
  DB_NAME=Nome do banco de dados
  DB_USER=Usuário do banco de ados
  DB_PASSWORD=Senha do banco de dados
  DB_HOST=Hospedagem do Banco (padrão='localhost')
  DB_PORT=Porta de acesso do Banco de dados (padrão=5432)
```

## Uso

Passe os modelos para o banco de dados:

```console
python manage.py makemigrations
```

```console
python manage.py migrate
```

Rode o servidor:

```console
python manage.py runserver 8000
```

O servidor estará disponível em:

```console
http://127.0.0.1:8000/
```
