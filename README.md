# cached-flask-api

## Requisitos

Apenas o docker é necessário para executar esse projeto. Mas é necessário copiar o arquivo `.env-example` para um arquivo `.env` e preencher a variável de ambiente `API_PORT`.

```sh
cp .env-example .env # após isso preencha a variável de ambiente no arquivo .env

docker compose up --build # executa o projeto
```

## Arquitetura

Nossa arquitetura é composta por quatro elementos, sendo eles:

- API Flask com uma rota simples que calcula o hash de uma string passada.

```sh
curl http://localhost:<API_PORT>/hash/<string> # <string> é a string passada como query param
```

- Dois servidores NGINX de cache que compartilham o mesmo volume.

- HAProxy utilizando o algoritmo Round-Robin como balanceador de carga entre dos dois servidores de cache.
