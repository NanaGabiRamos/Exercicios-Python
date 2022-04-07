from MeioDeTransporte import MeioDeTransporte

class Aquatico(MeioDeTransporte):
   def __init__(self, numVelas, tamanhoCasco):
      super()
      self.__numVelas = numVelas
      self.__tamanhoCasco = tamanhoCasco

   #Geters e Seters
   #**************************#
   def get_numVelas(self):
      return self.__numVelas

   def set_numVelas(self, num:int):
      self.__numVelas = num

   def get_tamCasco(self):
      return self.__tamanhoCasco

   def set_tamCasco(self, tam:int):
      self.__tamanhoCasco = tam

   def informacoes(self):
      print(f'Número de Velas: {self.__numVelas}')
      print(f'Tamanho do Casco: {self.__tamanhoCasco} m')