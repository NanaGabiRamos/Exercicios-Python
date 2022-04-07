from MeioDeTransporte import MeioDeTransporte

class Aquatico(MeioDeTransporte):
   def __init__(self, numVelas, tamCasco):
      super()
      self.__numVelas = numVelas
      self.__tamCasco = tamCasco

   #Geters e Seters
   #**************************#
   def get_numVelas(self):
      return self.__numVelas

   def set_numVelas(self, num:int):
      self.__numVelas = num

   def get_tamCasco(self):
      return self.__tamCasco

   def set_tamCasco(self, tam:int):
      self.__tamCasco = tam

   def informacoes(self):
      print(f'Número de Velas: {self.__numVelas}')
      print(f'Tamanho do Casco: {self.__tamCasco} m')