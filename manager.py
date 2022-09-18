import os
import sys
from dotenv import load_dotenv
from src.database.initialize import Initialize


def create():
    _, message = Initialize.create_database()
    print(message)


def delete():
    _, message = Initialize.drop_database()
    print(message)


def seed(base_path: str):
    _, message = Initialize.salary_data(base_path)
    print(message)


if __name__ == "__main__":
    # Define path do projeto e carrega variáveis de ambiente
    functions = ["delete", "create", "seed"]
    base_path = os.path.dirname(os.path.abspath(__file__))
    load_dotenv(f"{base_path}/config/.env")

    # Faz a chamada da função passada como parâmetro
    args = sys.argv
    if len(args) != 2:
        raise Exception("Comando inválido, utilize sempre python manager.py <nome_da_funcao>.")

    if args[1] not in functions:
        raise Exception(f"Função não encontrada. Estão disponíveis: {', '.join(functions)}")

    if args[1] in ["delete", "create"]:
        globals()[args[1]]()
    else:
        globals()[args[1]](base_path)
