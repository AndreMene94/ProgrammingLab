# Inizializzo una lista vuota per salvare i valori
total_values = []
# Apro e leggo il file, linea per linea
my_file = open("shampoo_sales.csv", "r")
salesSum = 0
for line in my_file:
 # Faccio lo split di ogni riga sulla virgola
  elements = line.split(',')
 # Se NON sto processando l’intestazione...
  if elements[0] != 'Date':
 # Setto la data e il valore
    date = elements[0]
    value = elements[1]
    salesSum +=float(value)
 # Aggiungo alla lista dei valori questo valore
    total_values.append(float(value))

print(total_values)
print(salesSum)