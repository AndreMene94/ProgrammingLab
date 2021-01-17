class Pagina:

  def __init__(self, numero, capitolo, testo):
    self.numero = numero
    self.capitolo = capitolo
    self.testo = testo

pagina1 = Pagina(numero=1, capitolo="Ciccio", testo="Ciccio Bello")

print(pagina1.capitolo)



libro = []

class PaginaVuota(Pagina):
  #pass = codice "vuoto"
  pass

class PaginaDestra(Pagina):
  def posizione_numero(self):
    return 'destra'

class PaginaSinista(Pagina):
  def posizione_numero(self):
    return 'sinistra'

paginaDestra = PaginaDestra(numero=1, capitolo="Ciccio", testo="Ciccio Bello")

print(paginaDestra.posizione_numero())

libro.append(paginaDestra)

print(isinstance(paginaDestra,Pagina))

print(libro)