# Use a imagem oficial do Python como base
FROM python:3.8-slim-buster

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie os arquivos do projeto para o contêiner
COPY . /app

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Use a imagem do MySQL 5.7
FROM mysql:5.7

# Defina a senha do root do MySQL
ENV MYSQL_ROOT_PASSWORD 27184199

# Exponha a porta 3306 para o MySQL
EXPOSE 3306

# Comando para executar o script da API Python quando o contêiner é iniciado
CMD ["python", "./main.py"]


