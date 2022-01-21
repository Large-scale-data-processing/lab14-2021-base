# Sample GraphQL python + react full stack app

## Commands used to create the repo

```bash
poetry new 
npx create-react-app
```

## Install

Install [NVM](https://github.com/nvm-sh/nvm)

```bash
poetry install
nvm install 17.4.0
nvm use 17.4.0
cd frontend
npm install
npm run build
cd ..
```

## Server

```bash
poetry shell
python lab14_2021_base/main.py
```

## In browser

Playground:
http://localhost:5000/graphql
```graphql
query{
  hello
}
```

App:
http://localhost:5000/


## Dev

Backend:
```bash
poetry shell
python lab14_2021_base/main.py
```

Frontend:
```bash
cd frontend
npm run start
#http://localhost:3000
```
