# Estudo da remuneração de profissionais de dados
*O principal objetivo deste repositório é entender as principais influências da remuneração dos profissionais de dados, bem como avaliar a distribuição destes profissionais, como senioridade e principais funções.*


# Dados
Os dados utilizados foram obtidos pelo kaggle ([link](https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries)) e um script foi responsável por ler o arquivo .csv e carregar em um banco de dados MySQL local.

# Ferramentas
Este projeto foi desenvolvido em um sistema operacional Ubuntu 22.04 utilizando Python 3.10.4 em um ambiente virtual. Todas as dependências estão no arquivo requirements.txt e podem ser instaladas pelo "pip install -r requirements.txt". As principais bibliotecas utilizadas foram:

- MySQL
- Python
- SQLAlchemy
- Flask
- Pytest

# Manager
A gestão do banco de dados é feita por meio do script manager.py, que implementa funções de criação, remoção e seed de dados. Para interagir com este script em terminal, basta utilizar o comando "python manager.py <nome_data_funcao>". Os seguintes argumentos estão disponíveis:

- `python manager.py create` : faz a criação das tabelas no banco de dados.
- `python manager.py delete` : remove as tabelas com todo o conteúdo do banco de dados.
- `python manager.py seed` : carrega os dados de vinhos do arquivo csv.

## Importante
Todas as funcionalidades do manager.py e do notebook necessitam da correta configuração do arquivo de variáveis de ambiente (.env) dentro do diretório "config". Por boas práticas, este arquivo foi omitido no repositório público, porém um arquivo de exemplo foi disponibilizado. Configure um arquivo .env com as suas credenciais para que todo o sistema funcione corretamente.

# Webapp
Como forma de disponibilizar o modelo preditivo foi desenvolvida uma API capaz de receber os inputs do modelo e devolver o resultado da previsão. Seguindo as práticas de TDD, a codificação se deu por meio de testes que garantem a qualidade do sistema. Para executar todos os testes e verificar a integridade do sistema deste repositório, basta executar "pytest" no terminal.

O arquivo de inicialização do webapp é o `wsgi.py`, executando uma aplicação flask na versão desenvolvimento. Para deploy, o repositório conta com o gunicorn, configurado para o heroku.