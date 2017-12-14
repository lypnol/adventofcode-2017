from runners.python import Submission

class ChloeSubmission(Submission):

	def run(self, s):
		count = 0
		for row in range(0, 128):
			input = s + "-" + str(row)
			hash = self.knot_hash_conversion(input)
			binaire = self.bin_hex_conversion(hash)
			count += binaire.count('1')
		return count



	def knot_hash_conversion(self, input):
		liste = [item for item in range(0, 256)]
		pointeur = 0
		skip_size = 0
		n = len(liste)
		ascii_code = [ord(c) for c in input] + [17, 31, 73, 47, 23]
		for j in range(0, 64):
			for lenght in ascii_code:
				subliste = [element for element in liste[pointeur:min(n, lenght + pointeur)] + liste[min(pointeur + lenght - n, 0):(pointeur + lenght) % n]]
				subliste.reverse()
				i = pointeur
				for element in subliste:
					liste[i % n] = element
					i += 1
				pointeur = (pointeur + lenght + skip_size) % n
				skip_size += 1
		sparse_hash = liste
		dense_hash = [self.xor_function(sparse_hash, indices, 16) for indices in range(0, 256, 16)]
		hexa = [self.hexa_conversion(element) for element in dense_hash]
		result = "".join(hexa)
		return result


	def xor_function(self, liste, indice_depart, bloc_lenght):
		value = liste[indice_depart]
		for j in range(indice_depart + 1, indice_depart + bloc_lenght):
			value ^= liste[j]
		return value

	def hexa_conversion(self, value):
		result = hex(value)[2:]
		if len(result) == 1:
			result = '0' + result
		return result


	def bin_hex_conversion(self, value):
		result =''
		for digit in value:
			convert = bin(int(digit, base=16))[2:]
			while len(convert)<4:
				convert = '0' + convert
			result += convert
		return result