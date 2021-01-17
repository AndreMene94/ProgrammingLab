a = 'ciao'

try:
  float(a)
except Exception as e:
  print("Non riesco a convertire la stringa in numero: {}".format(e))
  a=0