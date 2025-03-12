# importando o módulo
# import datetime  # importa todas as funções do módulo
from datetime import date, datetime, time

# Passando uma data específica
data = date(2025, 3, 12) # ano, mês, dia.
print(data)
print(date.today()) # Pega a data local atual

data_hora = datetime(2025, 3, 12, 7, 13, 35) # ano, mês, dia, hora, minutos, segundos
print(data_hora)
print(datetime.today()) # data e hora local atual

hora = time(10, 20, 0) # hora, minutos, segundos
print(hora)