# 📦 Pipeline de Dados: SQL Server → Python → MinIO (Landing Zone)

## 📌 Visão geral
Este projeto implementa um pipeline simples de engenharia de dados que extrai informações de um banco SQL Server, converte os dados em arquivos CSV e os envia para um bucket no MinIO chamado `landing-zone`.

---

## 🧱 Arquitetura do fluxo

```
SQL Server (NetflixDB)
        ↓
Python (pyodbc + pandas)
        ↓
CSV (temporário em C:/temp)
        ↓
MinIO (bucket: landing-zone)
```

---

## ⚙️ Tecnologias utilizadas

- Python 3.x
- pandas
- pyodbc
- MinIO Python SDK
- SQL Server Express
- MinIO Server

---

## 📂 Estrutura do projeto

```
C:/temp/
 ├── exportar_minio.py
 ├── C:/temp (arquivos CSV temporários)

MinIO:
 ├── bucket: landing-zone
```

---

## 🚀 Pré-requisitos

### 1. SQL Server
- Instalação do SQL Server Express
- Banco de dados criado (ex: NetflixDB)
- Instância ativa: `.\SQLEXPRESS`

### 2. MinIO Server
- Download do `minio.exe`
- Execução manual:

```bash
C:\minio\minio.exe server C:\minio-data --console-address ":9001"
```

- Acesso:
  - API: http://localhost:9000
  - Console: http://localhost:9001

- Credenciais padrão:
  - user: minioadmin
  - password: minioadmin

### 3. Python dependências

```bash
pip install pandas pyodbc minio
```

---

## 🧾 Script principal

O script realiza:

1. Conexão com SQL Server
2. Leitura de tabelas definidas
3. Exportação para CSV
4. Upload dos arquivos para MinIO

---

## 📌 Exemplo de configuração SQL Server

```python
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=.\\SQLEXPRESS;"
    "DATABASE=NetflixDB;"
    "Trusted_Connection=yes;"
)
```

---

## 📌 Configuração MinIO

```python
client = Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)
```

---

## 📊 Fluxo de execução

### 1. Iniciar MinIO (OBRIGATÓRIO)

```bash
C:\minio\minio.exe server C:\minio-data --console-address ":9001"
```

---

### 2. Executar script Python

```bash
python exportar_minio.py
```

---

## 📁 Organização dos dados no MinIO

Os dados são armazenados no bucket `landing-zone` como arquivos CSV:

```
landing-zone/
 ├── Conteudo.csv
 ├── Ator.csv
 ├── Diretor.csv
 ├── Pais.csv
 ├── Genero.csv
```

---

## ⚠️ Problemas comuns

### ❌ MinIO não conecta
Erro: Connection refused :9000

✔ Solução: verificar se o MinIO está rodando

---

### ❌ SQL Server não conecta
Erro: instance not found

✔ Solução: verificar `.\\SQLEXPRESS` ativo

---

### ❌ erro SSL no SQL Server
✔ Solução:
- usar `ODBC Driver 17`
- evitar `Encrypt=Yes`

---

## 💡 Melhorias futuras

- Exportação incremental
- Upload direto em memória (sem CSV local)
- Agendamento automático (Task Scheduler)
- Organização tipo Data Lake:

```
landing-zone/tabela/ano/mes/dia/
```

- Leitura dinâmica de tabelas (sem lista fixa)

---

## 🧠 Resumo

Este projeto demonstra um pipeline básico de engenharia de dados local:

✔ Extract (SQL Server)
✔ Transform (pandas)
✔ Load (MinIO - Data Lake simples)

---

## 📌 Autor
Projeto de estudo em Engenharia de Dados com foco em pipelines locais e conceitos de Data Lake.

