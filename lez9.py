#from matplotlib import pyplot


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
    return csvValues


class Utilities():

  def computeAvgIncrement(self, data):
    data_length = len(data)
    increments_sum = 0
    for i, val in enumerate(data):
      if (i>0):
        increment = val - data[i-1]
        increments_sum += increment
    
    increment_average = increments_sum/(data_length-1)
    return increment_average

class Model(object):

  def fit(self, data):
    pass

  def predict(self):
    pass


class IncrementModel(Model):

  def fit(self, data):
    utilities = Utilities()
    self.global_increment_average = utilities.computeAvgIncrement(data)
    #print(self.global_increment_average)
    #return increment_average

  def predict(self, prev_months):
    utilities = Utilities()
    increment_average = utilities.computeAvgIncrement(prev_months)
    predicted_increment = (self.global_increment_average+ increment_average)/2

    predicted_value = prev_months[-1] + predicted_increment

    return predicted_value





#sales_value = [8,19,31,41,50,52,60]


csvFile = CSVFile('shampoo_sales_err.csv')
sales_value = csvFile.getData()
training_set = sales_value[0:20]
model = IncrementModel()
model.fit(sales_value[20:23])
prediction = model.predict(training_set)
print(prediction)

'''
prev_months= sales_value[4:7]
model = IncrementModel()
model.fit(sales_value[0:4])
prediction = model.predict(prev_months)
print (prediction)

pyplot.plot(sales_value + [prediction], color='tab:red')
pyplot.plot(sales_value, color='tab:blue')
pyplot.show()
'''

#csvFile = CSVFile('shampoo_sales_err.csv')

#sales_value = csvFile.getData()
#prev_months = sales_value[24:36]
#prediction = model.predict(prev_months)
#print(prediction)
