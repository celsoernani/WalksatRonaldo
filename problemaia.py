class Margem:
		def __init__(self,mission,barco,canibais, margem1, margem1):
		self.mission = mission
		self.barco = barco
		self.canibais = canibais
		self.margem1 = margem1
		self.margem2 = margem2

		def conferindo(margem1, margem2):z
		if self.margem1[0].len >= 0 and self.missionaryRight >= 0 \
                   and self.cannibalLeft >= 0 and self.cannibalRight >= 0 \
                   and (self.missionaryLeft == 0 or self.missionaryLeft >= self.cannibalLeft) \
                   and (self.missionaryRight == 0 or self.missionaryRight >= self.cannibalRight):
			return True
		else:
			return False

mission = [1,1,1]
canibais = [2,2,2]
barco = []
margem1 = [mission, canibais]
margem2 = []

print("Atualmente a margem1 contem: " , margem1)

barco = [mission[0], canibais[0]]
margem1[0].remove(1)
margem1[1].remove(2)


print("Atualmente a margem1 contem: " , margem1)
margem2.append(barco[1])

print("Barco em caminho com" , barco)
barco.remove(2)

print("Barco deixou um Canibal")

print("Atualmente a margem1 contem: " , margem1)
print("Atualmente a margem2 contem: " , margem2)
print("Atualmente o barco contem: " , barco)


margem1[0].append(barco[0])
barco.remove(1)
print("Atualmente a margem1 contem: " , margem1)
print("Atualmente a margem2 contem: " , margem2)
print("Atualmente o barco contem: " , barco)

barco.append(margem1[1][0])
barco.append(margem1[1][0])

margem1[1].remove(2)
margem1[1].remove(2)

print("Atualmente a margem1 contem: " , margem1)
print("Atualmente a margem2 contem: " , margem2)
print("Atualmente o barco contem: " , barco)

margem2.append(barco[0])
barco.remove(2)
print("Barco deixou um Canibal")
print("Atualmente a margem1 contem: " , margem1)
print("Atualmente a margem2 contem: " , margem2)
print("Atualmente o barco contem: " , barco)

margem1[1].append(barco[0])
barco.remove(2)
print("Atualmente a margem1 contem: " , margem1)
print("Atualmente a margem2 contem: " , margem2)
print("Atualmente o barco contem: " , barco)




barco.append(margem1[0][0])
barco.append(margem1[0][1])
margem1[0].remove(1)
margem1[0].remove(1)

print("Barco deixou um Mission e pegou um Canibal")
print("Atualmente a margem1 contem: " , margem1)
print("Atualmente a margem2 contem: " , margem2)
print("Atualmente o barco contem: " , barco)


margem2.append(barco[0])
margem2.remove(2)
barco.remove(1)
barco.append(margem2[0])

print("Atualmente a margem1 contem: " , margem1)
print("Atualmente a margem2 contem: " , margem2)
print("Atualmente o barco contem: " , barco)

margem1[1].append(barco[1])
barco.remove(2)
barco.append(margem1[0][0])
margem1[0].remove(1)

print("Atualmente a margem1 contem: " , margem1)
print("Atualmente a margem2 contem: " , margem2)
print("Atualmente o barco contem: " , barco)

margem2.append(barco[0])
margem2.append(barco[1])
barco.remove(1)
barco.remove(1)
barco.append(margem2[0])
margem2.remove(2)

print("Atualmente a margem1 contem: " , margem1)
print("Atualmente a margem2 contem: " , margem2)
print("Atualmente o barco contem: " , barco)

barco.append(margem1[1][0])
margem1[1].remove(2)
margem2.append(barco[0])
barco.remove(2)
print("Atualmente a margem1 contem: " , margem1)
print("Atualmente a margem2 contem: " , margem2)
print("Atualmente o barco contem: " , barco)

barco.append(margem1[1][0])
margem1[1].remove(2)
margem2.append(barco[0])
margem2.append(barco[1])
barco.remove(2)
barco.remove(2)


print("Atualmente a margem1 contem: " , margem1)
print("Atualmente a margem2 contem: " , margem2)
print("Atualmente o barco contem: " , barco)














