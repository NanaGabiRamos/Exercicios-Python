from MeioDeTransporte import MeioDeTransporte

class Aereo(MeioDeTransporte):
   def __init__(self, numAsa):
      super()
      self.__numAsa = numAsa

   #Geters e Seters
   #*******************************#
   def get_numAsas(self):
      return self.__numAsa

   def set_numAsas(self, num:int):
      self.__numAsa = num

   def informacoes(self):
      print(f'Número de Asas: {self.__numAsa}')