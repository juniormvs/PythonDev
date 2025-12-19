import pandas as pd
import numpy as np


dados_aba1 ={
    "ID": [1,2,3,4,5],
    "Nome":["Ana", "Carlos", "Beatriz", "Marcelo","Marcela"],
    "Idade":[25,35,40,23,38],
    "Cidade":["São Paulo","Presidente Venceslau","Pirapozinho", "Maceió", "Cuiabá"]
}

dados_aba2 ={
    "ID": [1,2,3,4,5],
    "Nome":["Ana", "Carlos", "Beatriz", "Marcelo","Marcela"],
    "Idade":[25,35,40,23,38],
    "Cidade":["São Paulo","Presidente Venceslau","Pirapozinho", "Maceió", "Cuiabá"]
}

dados_aba3 ={
    "ID": [1,2,3,4,5],
    "Nome":["Ana", "Carlos", "Beatriz", "Marcelo","Marcela"],
    "Idade":[25,35,40,23,38],
    "Cidade":["São Paulo","Presidente Venceslau","Pirapozinho", "Maceió", "Cuiabá"]
}

dados_aba4 ={
    "ID": [1,2,3,4,5],
    "Nome":["Ana", "Carlos", "Beatriz", "Marcelo","Marcela"],
    "Idade":[25,35,40,23,38],
    "Cidade":["São Paulo","Presidente Venceslau","Pirapozinho", "Maceió", "Cuiabá"]
}

df_aba1 = pd.DataFrame(dados_aba1)
df_aba2 = pd.DataFrame(dados_aba2)
df_aba3 = pd.DataFrame(dados_aba3)
df_aba4 = pd.DataFrame(dados_aba4)

caminho_arquivo = "dados/clientes.xlsx"

with pd.ExcelWriter(caminho_arquivo, engine="openpyxl") as writer:
    df_aba1.to_excel(writer, sheet_name="Aba_1",index=False)
    df_aba2.to_excel(writer, sheet_name="Aba_2", index=False)
    df_aba3.to_excel(writer, sheet_name="Aba_3", index=False)
    df_aba4.to_excel(writer,sheet_name="Aba_4", index=False)
