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
  def getData(self, start=None, end=None):

    if(isinstance(self.name, str)==False):
      raise Exception("Il valore {} non è una stinga".format(self.name))
      return None
    

    csvValues = []

    try:
      csvFile = open(self.name, "r")
    except Exception as e:
      print('Il file "{}" non esiste: \n"{}"'.format(self.name, e))
      #ritorno null dalla funzione
      return None
    

    for line in csvFile:
      elements = line.split(',')
      if elements[0] != 'Date':
        dateVal = elements[0]
        value = elements[1]
        try:
          value=float(value)
        except Exception as e:
          print('Il carattere è di tipo stringa: \n{}\n'.format(e))
          value=0
          #salto al prossimo giro del ciclo
          continue
        csvValues.append((value))
    csvFile.close()
    return csvValues[start:end]






#inizializzo l'oggetto CSVFile
myFile = CSVFile(name='shampoo_sales.csv')

#myFile = CSVFile(name=2)

#inizializzo l'oggetto CSVFile
#myFile2 = CSVFile(name='shampoo_salessss.csv')


#stampo la lista creata dal metodo getData()
print(myFile.getData(5,10))

#print(myFile2.getData())