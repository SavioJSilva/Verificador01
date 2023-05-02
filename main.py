import pandas as pd
from twilio.rest import Client
# passo a passo de solução
# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
# Para cada arquivo:
# Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000
# Caso não seja maior do que 55.000 não quero fazer nada
# Se for maior do que 55.000: Envia um SMS com o nome, o mês e as vendas do vendedor
# Your Account SID from twilio.com/console
account_sid = "AC137b9beb2bd1041af5aaf003fd487bd0"
# Your Auth Token from twilio.com/console
auth_token  = "82fbb3b22b603399d430772b23a31964"
client = Client(account_sid, auth_token)
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mes de {mes} o vendedor {vendedor} vendeu: {vendas}')
        message = client.messages.create(
            to="+5519981515996",
            from_="+15077095991",
            body=f'No mes de {mes} o vendedor {vendedor} vendeu: {vendas}')
        print(message.sid)













