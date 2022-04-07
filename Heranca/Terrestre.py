import string
from MeioDeTransporte import MeioDeTransporte

class Terrestre(MeioDeTransporte):
   def __init__(self,numeroDeRodas, numeroDePortas, placa, cor):
      super()
      self.__numeroDeRodas = numeroDeRodas
      self.__numeroDePortas = numeroDePortas
      self.__placa = placa
      self.__cor = cor


   #Geters e Seters
   #**********************************#
   def get_numeroDeRodas(self):
      return self.__numeroDeRodas

   def set_numeroDeRodas(self, num:int):
      self.__numeroDeRodas = num

   def get_numeroDePortas(self):
      return self.__numeroDePortas

   def set_numeroDePortas(self, numPortas:int):
      self.__numeroDePortas = numPortas

   def get_placa(self):
      return self.__placa

   def set_placa(self, placa:str):
      self.__placa = placa

   def get_cor(self):
      return self.__cor
   
   def set_cor(self, cor:str):
      self.__cor = cor

   def informacoes(self):
      print(f'Número de Rodas: {self.__numeroDeRodas}')
      print(f'Número de Portas: {self.__numeroDePortas}')
      print(f'Placa: {self.__placa}')
      print(f'Cor: {self.__cor}')