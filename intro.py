def sumList(numberList):

  sum = 0

  for item in numberList:
    sum += item
  
  #ritorno la somma 
  return sum

print ("Somma {}" . format(sumList([10,20,30,40])))