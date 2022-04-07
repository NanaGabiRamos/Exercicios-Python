from Aereo import Aereo
from Aquatico import Aquatico
from Terrestre import Terrestre

#Instância dos objetos
#**************************************************#
carro = Terrestre(4,4,'HGT-SUL','Vermelho')
moto = Terrestre(4,0,'LFG-CLT','Preta')

navio = Aquatico(0,25)
caravela = Aquatico(3,15)

balao = Aereo(0)
aviao = Aereo(2)
#*************************************************#
# Carro #*****************************************#
print('-----Carro-----')
carro.ligar()
carro.andar()
carro.freiar()
carro.desligar()
print('---Informações do veiculo---')
carro.informacoes()
#Testando geters e seters#***********************#
carro.set_cor('Azul')
carro.set_numeroDePortas(2)
carro.set_numeroDeRodas(5)
carro.set_placa('GSF-POR')
print('---Informações do veiculo atualizadas---')
print(f'Número de Rodas: {carro.get_numeroDeRodas()}')
print(f'Número de Portas: {carro.get_numeroDePortas()}')
print(f'Placa: {carro.get_placa()}')
print(f'Carro: {carro.get_cor()}')
print('\n')

# Caravela #**************************************#
print('-----Caravela-----')
caravela.ligar()
caravela.andar()
caravela.freiar()
caravela.desligar()
print('---Informações do veiculo---')
caravela.informacoes()
#Testando geters e seters#***********************#
caravela.set_numVelas(5)
caravela.set_tamCasco(45)
print('---Informações do veiculo atualizadas---')
print(f'Número de velas: {caravela.get_numVelas()}')
print(f'Tamanho do Casco: {caravela.get_tamCasco()} m')
print('\n')

# Avião #*****************************************#
print('-----Avião-----')
aviao.ligar()
aviao.andar()
aviao.freiar()
aviao.desligar()
print('---Informações do veiculo---')
aviao.informacoes()
#Testando geters e seters#***********************#
aviao.set_numAsas(5)
print('---Informações do veiculo atualizadas---')
print(f'Número de Asas: {aviao.get_numAsas()}')
print('\n')