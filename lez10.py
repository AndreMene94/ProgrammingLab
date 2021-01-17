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

  def predict(self, predict_set):
    utilities = Utilities()
    increment_average = utilities.computeAvgIncrement(predict_set)
    predicted_increment = (self.global_increment_average+ increment_average)/2

    predicted_value = predict_set[-1] + predicted_increment

    return predicted_value





#sales_value = [8,19,31,41,50,52,60]



#test = [1,2,3,4,5,6,7,8,9,10]
#print (test[1:5])
csvFile = CSVFile('shampoo_sales.csv')
sales_value = csvFile.getData()
errors = []

# Setto il punto di divisione tra i dati di training e test set
train_test_cutoff = 24

# Ricavo la lunghezza del test set che mi sevrira' dopo
test_set_len = len(sales_value)-train_test_cutoff

# Imposto la finestra usata per il predict (quanti prev_months)
window = 3

test_set_len = len(sales_value)-train_test_cutoff


model = IncrementModel()
predictions = []

training_set = sales_value[0:train_test_cutoff]

print ('Training Set: {}'.format(training_set))

model.fit(training_set)

error_sum = 0

for i in range (test_set_len):
  print ('Indice: {}'.format(int(i)))
  window_start =  train_test_cutoff+i-window-1
  window_end = train_test_cutoff+i-1 

  predict_set = sales_value[window_start:window_end]
  
  print('Predict set: {}'.format(predict_set))

  prediction = model.predict(predict_set)
  predictions.append(int(prediction))

  error_sum += abs(prediction - sales_value[train_test_cutoff+i])

error_average = error_sum/test_set_len
print('Errore: {}'.format(error_average))
print(predictions)



'''
prev_months= sales_value[4:7]
model = IncrementModel()
model.fit(sales_value[0:4])
prediction = model.predict(prev_months)
print (prediction)
'''
#pyplot.plot(sales_value[0:23] + [prediction], color='tab:red')
#pyplot.plot(sales_value, color='tab:blue')
#pyplot.show()


#csvFile = CSVFile('shampoo_sales_err.csv')

#sales_value = csvFile.getData()
#prev_months = sales_value[24:36]
#prediction = model.predict(prev_months)
#print(prediction)
