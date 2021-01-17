# Creare oggetto CSVFile
# init(filename)
# name
# getData()
# return dati

#definisco classe CSVFile
class CSVFile:

  #definisco costruttore con nome del file per inizializzare l'oggetto
  def __init__(self,name):
    self.name = name

  #definisco il metodo getData per estrarre i dati numerici dal file in una lista
  def getData(self):
    csvValues = []
    csvFile = open(self.name, "r")

    for line in csvFile:
      elements = line.split(',')
      if elements[0] != 'Date':
        value = elements[1]
        csvValues.append(float(value))
    csvFile.close()
    return csvValues




#inizializzo l'oggetto CSVFile
myFile = CSVFile(name='shampoo_sales.csv')

myFile2 = CSVFile(name='shampoo_salesss.csv')


#stampo la lista creata dal metodo getData()
print(myFile.getData())

print(myFile2.getData())