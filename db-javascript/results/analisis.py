import pandas as pd

# Carga los resultados del CSV
results = pd.read_csv('C:\upv\juice-shop\frontend\db-javascript\results.csv')

# Muestra las primeras filas para tener una idea de los datos
print(results.head())

# Podrías también filtrar por ejemplo solo los resultados de alta severidad
# high_severity = results[results['severity'] == 'high']
# print(high_severity)