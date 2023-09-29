import psycopg2
import matplotlib.pyplot as plt
import os
from pathlib import Path


class AnaliseDados:

    def __init__(self):
        self.conn = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="mysecret",
            host="localhost",
            port="15432"
        )
        self.cursor = self.conn.cursor()

    def fazer_grafico_pizza(self, setores, tamanhos, nome_arquivo):
        fig, ax = plt.subplots()
        ax.pie(tamanhos, labels=setores, autopct='%1.1f%%')
        local_salvar = os.path.join(Path(__file__).parent, f"images_dos_graficos/{nome_arquivo}.png")
        plt.savefig(local_salvar)

    def quantidade_carro_marca(self, marca: str):
        query = "SELECT * FROM carros WHERE marca = %s"
        value = (marca.capitalize(),)
        self.cursor.execute(query, value)
        carros = self.cursor.fetchall()
        print(f"O total de carros da marca {marca} é: {len(carros)}")

    def quantidade_carro_ano(self, ano):
        try:
            ano = int(ano)
        except Exception:
            print(("Ano inválido, tente novamente!"))
            return
        query = "SELECT * FROM carros WHERE ano = %s"
        value = (ano,)
        self.cursor.execute(query, value)
        carros = self.cursor.fetchall()
        print(f"O total de carros do ano {ano} é: {len(carros)}")

    def carros_disponiveis(self):
        query = "SELECT * FROM carros WHERE disponivel = %s"
        value = (True,)
        self.cursor.execute(query, value)
        carros = self.cursor.fetchall()
        print(f"Os carros disponíveis são: ")
        for carro in carros:
            print(carro)

    def total_por_marca(self):
        query = "SELECT marca, COUNT(*) AS total FROM carros GROUP BY marca ORDER BY total DESC"
        self.cursor.execute(query)
        carros = self.cursor.fetchall()
        setores = [carro[0] for carro in carros]
        tamanhos = [carro[1] for carro in carros]
        self.fazer_grafico_pizza(setores, tamanhos, nome_arquivo="total_por_marca")

