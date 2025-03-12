# Formatação de datas e horas
from datetime import datetime

data_hora_atual = datetime.now()
data_mascara_ptbr = "%d/%m/%Y %H:%M"

print(data_hora_atual)
print(data_hora_atual.strftime(data_mascara_ptbr))

data_hora_str   = "2025-03-12 13:32"
data_mascara_en = "%Y-%m-%d %H:%M"

print(datetime.strptime(data_hora_str, data_mascara_en))