import pandas as pd

# === 1) Carregar base ===
df = pd.read_csv('https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv', sep=';', encoding='latin1')

#print (df.head(6))
#print (df.descibre())
#print (df.tail(6))

df_roubo_celular_dp = df.groupby('cisp')['roubo_celular'].sum().reset_index()
df_roubo_celular_dp =  df_roubo_celular_dp.sort_values(by='roubo_celular', ascending = False)
print(df_roubo_celular_dp)

