# 🌤️ Clima API com Cache (FastAPI + OpenWeatherMap)

Este é um mini projeto em Python que expõe uma API para consultar a temperatura de cidades, utilizando **cache com TTL (Time-To-Live)** para melhorar a performance e reduzir chamadas desnecessárias à API externa.

---

## 🚀 Tecnologias

* [FastAPI](https://fastapi.tiangolo.com/)
* [Uvicorn](https://www.uvicorn.org/)
* [HTTPX](https://www.python-httpx.org/)
* [Cachetools](https://cachetools.readthedocs.io/en/stable/)
* [OpenWeatherMap API](https://openweathermap.org/api)

---

## ⚙️ Instalação

```bash
git clone https://github.com/Fsp30/Chache_basic_with_FastApi.git
cd clima-api-cache

python -m venv venv
venv\Scripts\activate     

pip install -r requirements.txt
```

---

## 🔐 Configuração

Crie um arquivo `.env` na raiz do projeto com a sua chave da API do OpenWeatherMap:

```
OPENWEATHER_API_KEY=sua_chave_aqui
```

---

## ▶️ Como rodar

```bash
uvicorn main:app --reload
```

Acesse a documentação automática em:

```
http://localhost:8000/docs
```

---

## 📡 Exemplos de uso

* Buscar o clima de uma cidade (usando cache):

  ```
  GET /climate/São Paulo
  ```

* Forçar atualização ignorando o cache:

  ```
  GET /climate/São Paulo?force=true
  ```

---

## 🧠 O que o cache faz?

* Armazena os dados por 10 minutos (TTL = 600 segundos).
* Evita chamadas repetidas para a mesma cidade.
* Usa `cachetools.TTLCache` em memória.

---

## 📂 Estrutura do Projeto

```
.
├── main.py
├── weather_service.py
├── .env
├── requirements.txt
└── venv/ (não versionado)
```

---

## ✅ Melhorias Futuras (opcional)

* Endpoint para listar cidades em cache.
* Rota para limpar o cache manualmente.
* Persistência do cache em disco.

---

## 📜 Licença

Este projeto é livre para uso educacional ou pessoal.
