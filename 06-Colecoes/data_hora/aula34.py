# Trabalhando com timedelta
from datetime import  timedelta, datetime

#### Simulando o tempo de lavagem de um carro
tipo_carro = "M" # P, M, G
tempo_carro_pequeno = 30 # minutos
tempo_carro_medio   = 45 # minutos
tempo_carro_grande  = 60 # minutos
data_atual = datetime.now()
tempo_estimado = 0

if tipo_carro == 'P':
    tempo_estimado = data_atual + timedelta(minutes=tempo_carro_pequeno)
    print(f'O carro chegou as {data_atual} e ficará pronto {tempo_estimado}')
elif tipo_carro == 'M':
    tempo_estimado = data_atual + timedelta(minutes=tempo_carro_medio)
    print(f'O carro chegou as {data_atual} e ficará pronto {tempo_estimado}')
else:
    tempo_estimado = data_atual + timedelta(minutes=tempo_carro_grande)
    print(f'O carro chegou as {data_atual} e ficará pronto {tempo_estimado}')