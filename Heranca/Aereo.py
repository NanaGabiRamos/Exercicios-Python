from MeioDeTransporte import MeioDeTransporte

class Aereo(MeioDeTransporte):
   def __init__(self, numAsas):
      super()
      self.__numAsas = numAsas

   #Geters e Seters
   #*******************************#
   def get_numAsas(self):
      return self.__numAsas

   def set_numAsas(self, num:int):
      self.__numAsas = num

   def informacoes(self):
      print(f'Número de Asas: {self.__numAsas}')