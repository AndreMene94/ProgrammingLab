
import statistics as stat

class ExamException(Exception):
    pass



class MovingAverage():

  # Costruttore MovingAverage
  # param window -> lunghezza della finestra
  def __init__(self,window):

    # Verifico che la finestra sia di tipo intero
    if not isinstance(window, int):
      raise ExamException('Invalid type for window, only int supported. Got "{}"'.format(type(window)))

    # Verifico che la finestra non sia minore di 1
    if (window<1):
      raise ExamException('The window is minor than 1. It\'s impossible to calculate the Moving Average.')

    self.window = window

  # Metodo computed
  # param list -> lista da elaborare
  # ritorna la lista elaborata dopo il calcolo della media mobile
  def compute(self,numberList):

    # Verifico che la lista di numeri sia di tipo lista
    if not (isinstance(numberList,list)): 
      raise ExamException('Invalid type for data. Only list supported. Got "{}"'.format(type(list)))

    movingAverage = []
    numberListLen = len(numberList)

    # Verifico che la finestra sia <= della lunghezza della lista
    if (numberListLen < self.window):
      raise ExamException("Warning! The window value is higher than the list of numbers. Expected a value less or equal to {}".format(numberListLen))

    # Verifico che nella lista siano presenti solo int o float
    for item in numberList:
       if not (isinstance(item, int) or  isinstance(item,float)):
        raise ExamException("Warning! There's a not valid data type in the list. Got {}".format(type(item)))
    


    for i,item in enumerate(numberList):
      rangeEnd = i + (self.window)
      if (rangeEnd<=numberListLen):
        print(i, rangeEnd, numberList[i:rangeEnd])
        movingAverage.append(stat.mean(numberList[i:rangeEnd]))

    return movingAverage 



  


