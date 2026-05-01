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

## O CHAT È BURRO LEIA O QUE O EU ESCREVI ENQUANTO AINDA TINHA FÉ NA HUMANIDADE


aproveitando que ainda sei o que eu fiz, voce deverá, baixar o sql server express no site da microsoft, depois baixar o SSMS, depois de ter instalado os dois (Nessa ordem) voce deve entrar no SSMS e criar o banco de dados com as tabelas, no caso voce ira usar o arquivo .BAK pra restaurar o banco igual eu deixei, descubra como fazer isso, depois de ter o banco com as tabelas criadas, voce deve baixar o arquivo .exe do MINIO (https://chatgpt.com/c/69f3e748-1048-832f-ab8e-bc983a48a1e6  , cole isso na url), apos baixar voce ja tem os 2 servidores, agora voce precisa fazer os 2 funcionarem, pra isso, no terminal CMD, Cole: sqlcmd -S .\SQLEXPRESS -E -C , depois que aparecer o >1 , cole: SELECT @@VERSION; depois GO.

NOTA: O cmd que voce colocou os prompt pra ativar o SQL, apos fazer o que falei, pode fechar ele sem problemas, porem o do minio deve ficar aberto, para rodar o minio.

com isso o sql esta 100 por cento, agora falta o Minio, com o mino baixado, cole isso no CMD: C:\minio\minio.exe server C:\minio-data --console-address ":9001", se der tudo certo, entre nessa url: http://localhost:9000, caso nao de troque o ultimo 0 por 1, dentro do navegador do MINIO, crie o Bucket "landing-zone", aqui voce ja fez tudo com o minio, agora saia do navegador sem fechar ele, e crie OUTRO terminal CMD, deixe o cmd do minio aberto.

Apos criar outro CMD garanta que voce tem uma pasta chamada "temp" no disco C, com o arquivo "exportar_minio.py", se ja tem isso, digite no CMD: cd C:\temp , e por ultimo: python exportar_minio.py

apos isso a landing zone vai ser preenchida com o CSV das tabelas, agora esta em suas mões continuar o que eu fiquei 17:30 ate as 23:10.
