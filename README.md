# Weather Data Pipeline

Pipeline ETL desenvolvido em Python para extração, transformação
e armazenamento de dados meteorológicos provenientes de uma API REST.

## Tecnologias

- Python 3.13
- Pandas
- Requests
- SQLite
- SQL
- Pytest
- Git

## Objetivo

Demonstrar conceitos fundamentais de Engenharia de Dados,
incluindo integração com APIs, processamento de dados,
armazenamento relacional e testes automatizados.

## Arquitetura

```text
Open-Meteo API
      |
      v
Extract (Python + Requests)
      |
      v
Transform (Pandas)
      |
      v
Load (SQLite)
      |
      v
SQL Analytics
```

## Funcionalidades

- Extração de dados meteorológicos via API REST.
- Processamento de temperatura, umidade e precipitação.
- Tratamento de registros duplicados e valores ausentes.
- Conversão e ordenação de datas.
- Armazenamento em banco SQLite.
- Atualização de registros existentes por chave primária.
- Consultas SQL para indicadores meteorológicos.
- Testes automatizados com Pytest.

## Estrutura do projeto

```text
weather-data-pipeline/
├── src/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── tests/
│   └── test_pipeline.py
├── data/
├── main.py
├── queries.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/weather-data-pipeline.git
cd weather-data-pipeline
```

Substitua `SEU-USUARIO` pelo usuário do GitHub.

### 2. Criar ambiente virtual

```bash
python -m venv .venv
```

No Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar dependências

```bash
python -m pip install -r requirements.txt
```

### 4. Executar o pipeline

```bash
python main.py
```

### 5. Executar consultas SQL

```bash
python queries.py
```

### 6. Executar testes

```bash
python -m pytest -v
```

## Resultados de uma execução

O pipeline processou 72 registros meteorológicos,
correspondentes a três dias de previsão horária.

Exemplos de indicadores obtidos:

| Indicador | Resultado |
|---|---|
| Registros processados | 72 |
| Temperatura média | 21,35 °C |
| Temperatura máxima | 27,7 °C |
| Precipitação total prevista | 27,4 mm |
| Testes automatizados | 4 aprovados |

Os resultados são referentes à consulta realizada
em 21/10/2026 e podem variar em novas execuções.

## Consultas SQL

O projeto utiliza operações como:

- SELECT
- COUNT
- AVG
- MAX
- MIN
- SUM
- GROUP BY
- ORDER BY

## Qualidade dos dados

A transformação remove registros duplicados por horário
e descarta linhas com valores ausentes.

O carregamento utiliza uma chave primária e UPSERT,
evitando a duplicação de horários já armazenados.

## Melhorias futuras

- Suporte a múltiplas cidades.
- Orquestração com Apache Airflow.
- Integração com PostgreSQL.
- Armazenamento em nuvem.
- Monitoramento e logs estruturados.

## Fonte dos dados

Open-Meteo Weather Forecast API.

## Autor

Projeto desenvolvido para estudo e aplicação prática
de conceitos de Engenharia de Dados.