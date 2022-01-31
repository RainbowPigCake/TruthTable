class Input:
	values = []
	name = ""
	def __init__(self,name, temp = []): 
		# constructor
		# name stores the boolean expression
		# temp is an optional parameter for the inputs it may already have 
		self.name = name # store name
		self.values = temp.copy() # copy so that reference is not made

	def _not(self): # not function
		temp = []
		for i in self.values:
			temp.append(i)
		for i in range(len(temp)):
			temp[i] = int(not(temp[i]))
		return Input("Function", temp)

	def _or(self, other):
		temp = []
		for i in range(len(self.values)):
			temp.append(self.values[i] or other.values[i])
		return Input("Function", temp)

	def _and(self, other):
		temp = []
		for i in range(len(self.values)):
			temp.append(self.values[i] and other.values[i])
		return Input("Function", temp)

	def _xor(self, other):
		temp = []
		for i in range(len(self.values)):
			temp.append(int(self.values[i] != other.values[i]))
		return Input("Function", temp)
	
	def __repr__(self):
		# table of the outputs
		return str(self.values)

	def __mul__(self,other):
		# and
		if other == -1:
			return self._not()
		return self._and(other)

	def __add__(self,other):
		# or
		return self._or(other)

	def __neg__(self):
		# negation / not
		return self._not()

	def __truediv__(self, other):
		# xor
		return self._xor(other)

class Table:
	# a table will have inputs
	inputs = []
	def __init__(self, inputs):
		# fill in the initial inputs
		bit = 0
		counter = 0
		for i in range(len(inputs)): # loops through each variable
			for j in range(2**len(inputs)): # loop through each row
				inputs[i].values.append(bit) # store a 1 or 0 
				counter += 1
				if counter >= 2**(len(inputs)-i)//2: # invert the bit to store
					bit = int(not(bit))
					counter = 0
		self.inputs = inputs

	def __repr__(self):
		# display
		to = ""
		for i in self.inputs:
			to += i.name + ": " + str(i.values) + "\n"
		return to

	def add_input(self, variable):
		self.inputs.append(variable)

	def display_as_cols(self):
		# string representation
		s = ""
		for i in range(len(self.inputs)):
			s += " " * (len(inputs[i].name)) + self.inputs[i].name + " " * (len(inputs[i].name ))

		s += "\n"

		for i in range(len(self.inputs[0].values)):
			for j in range(len(self.inputs)):
				s += " " * (len(inputs[j].name) * 2 - 1) + str(inputs[j].values[i]) + " " * (len(inputs[j].name))
			s += "\n"
		print (s)

	def display_as_matrix(self):
		# display all of the expressions as arrays
		temp = []
		for i in self.inputs:
			temp.append(i.name)
		temp = tuple(temp)
		copy = []
		for i in self.inputs:
			copy.append(i.values.copy())
		print([temp] + list(zip(*copy)))

	def export(self):
		# export to csv for copy paste
		s = ""
		for i in range(len(self.inputs)):
			s += self.inputs[i].name + ","

		s += "\n"

		for i in range(len(self.inputs[0].values)):
			for j in range(len(self.inputs)):
				s += str(inputs[j].values[i]) + ","
			s += "\n"
		print (s)

	def get_names(self):
		# returns array of all of the names of the expressions
		names = []
		for i in range(len(self.inputs)):
			names.append(self.inputs[i].name)
		return names
	def inside_table(self, name):
		for i in inputs:
			if i.name == name:
				return True
		return False

def clean_bedmas(s):
	# adds * symbols for the and operation EX: AB -> A*B and removes ALL spaces
	indices = []
	s = s.replace(' ','')
	for i in range(len(s)-1):
		if s[i] != '(' and s[i] in alphaset and s[i+1] in alphaset:
			indices.append(str(s[i]) + str(s[i+1]))
		elif s[i] == ')' and s[i+1] in alphaset:
			indices.append(str(s[i]) + str(s[i+1]))
	for i in indices:
		s = s.replace(i, i[0] + "*" + i[1])
	return s

def clean_nums(s):
	# rows turn into expressions
	temp = []
	for i in range(len(s)):
		if s[i].isdigit():
			# store the number and the name of the expression that should be there
			temp.append([s[i], t.inputs[int(s[i])-1].name])
	for a,b in temp:
		s = s.replace(a, "("+b+")")
	return s

def remove_spaces(s):
	# remove all spaces
	t = ""
	for i in range(len(s)):
		if s[i] != " ":
			t += s[i]
	return t

def print_kmap(num):
	refer = []
	two = [
		[0,1],
		[2,3]
	]

	three = [
		[0,1,3,2],
		[4,5,7,6]
	]
	
	four = [
		[0,1,3,2],
		[4,5,7,6],
		[12,13,15,14],
		[8,9,11,10]
	]
	
	if num == 2:
		refer = two
	elif num == 3:
		refer = three
	elif num == 4:
		refer = four



	kmap = []
	
	vals = []
	for i in range(len(t.inputs[-1].values)):
		if t.inputs[-1].values[i] == 1:
			vals.append(i)

	for i in range(len(refer)):
		row = []
		for j in range(len(refer[0])):
			if refer[i][j] in vals:
				row.append(1)
			else:
				row.append(0)
		kmap.append(row)
		row = []
	
	print(initial, 'variable k-map of:', t.inputs[-1].name)
	print()

	names = ""
	for i in range(initial):
		names += t.inputs[i].name
	print(names[:len(names)//2] + '\\' + names[len(names)//2:])
	for i in range(len(kmap)):
		print(*kmap[i])

def str_is_binary(s):
	for i in s:
		if i != "0" and i != "1":
			return False
	return True

# alphabet set and array

alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

alphaset = {'A','B','C','D','E','F','G','H','I','J','K','L','M' ,  'N',	'O'    ,'P','Q','R','S'  , 'T'    ,'U','V','W','X','Y','Z', '('}
# letters N, O, T are missing because of special stuff ----- FIXED
# premade finite input variables	
A=Input('A')
B=Input('B')
C=Input('C')
D=Input('D')
E=Input('E')
F=Input('F')
G=Input('G')
H=Input('H')
I=Input('I')
J=Input('J')
K=Input('K')
L=Input('L')
M=Input('M')
N=Input('N')
O=Input('O')
P=Input('P')
Q=Input('Q')
R=Input('R')
S=Input('S')
T=Input('T')
U=Input('U')
V=Input('V')
W=Input('W')
X=Input('X')
Y=Input('Y')
Z=Input('Z')

# inputs will store the initial inputs
inputs = []
initial = "hi"

# flag for whether inputs have been successfully gotten 
flag = False
while not flag:
	initial = input("Inputs? (# or letters): ")
	# numeric initialization
	if initial.isnumeric():
		initial = int(initial)
		if 0 < initial <= 26:
			for i in range(initial):
				inputs.append(eval(alpha[i]))
			flag = True
	# alpha initialization
	else:
		# remove spaces then add all of the inputs
		initial = initial.replace(" ", "").split(",")
		for i in initial:
			if len(i) == 1:
				inputs.append(eval(i.upper()))
			else:
				flag = True
		if flag:
			# if not successful then restart 
			flag = False
			inputs.clear()
		else:
			initial = len(inputs)
			flag = True

# create table with the initial inputs
t = Table(inputs)

print(t)

while True:
	valid = True
	num_eq = 1
	try:
		# format command
		s = remove_spaces(input("Enter an equation: ").upper().strip())
		s = s.split(',')
		for i in s:
			if i == "D":
				t.display_as_cols()
			elif i == "F":
				t.display_as_matrix()
			elif i == "E":
				t.export()
			elif i == "R":
				t.inputs = t.inputs[:initial]
				t.display_as_matrix()
			elif i == "Z":
				if len(t.inputs) > initial:
					t.inputs.pop()
			elif i == "PRODUCT":
				print("Product of Maxterms of: " + t.inputs[-1].name + "\n" )
				out = "π"
				vals = []
				for i in range(len(t.inputs[-1].values)):
					if t.inputs[-1].values[i] == 0:
						vals.append(i)
				vals = str(vals)
				vals = vals.replace("[","(")
				vals = vals.replace("]",")")
				vals = vals.replace(" ", "")
				print(out + vals + "\n")

			elif i == "SUM":
				print("Sum of Minterms of: " + t.inputs[-1].name + "\n" )
				out = "Σ"
				vals = []
				for i in range(len(t.inputs[-1].values)):
					if t.inputs[-1].values[i] == 1:
						vals.append(i)
				vals = str(vals)
				vals = vals.replace("[","(")
				vals = vals.replace("]",")")
				vals = vals.replace(" ", "")
				print(out + vals + "\n")

			elif i == "CNF":
				# prints the product of maxterms
				cnf = "CNF of: " + t.inputs[-1].name + "\n\n"
				for i in range(len(t.inputs[-1].values)):
					if t.inputs[-1].values[i] == 0:
						cnf += "("
						for j in range(initial):
							if t.inputs[j].values[i] == 0:
								cnf += t.inputs[j].name + "+"
							else:
								cnf += t.inputs[j].name + "'+"
						cnf = cnf[:-1]
						cnf += ")"
				print(cnf + "\n")

			elif i == "DNF":
				# prints the sum of minterms
				dnf = "DNF of: " + t.inputs[-1].name + "\n\n"
				for i in range(len(t.inputs[-1].values)):
					if t.inputs[-1].values[i] == 1:
						dnf += "("
						for j in range(initial):
							if t.inputs[j].values[i] == 0:
								dnf += t.inputs[j].name + "'"
							else:
								dnf += t.inputs[j].name 
						dnf += ")+"
				print(dnf[:-1] + "\n")
			elif i == "K":
				print_kmap(initial)
			elif i == "I":
				inp = input("Enter a boolean output ex. '00110001': ").strip()
				print(inp)
				if len(inp) == 2 ** initial and str_is_binary(inp):
					name = f"EQ{num_eq}"
					num_eq += 1
					inp = list(inp)  
					t.add_input(Input(name, list(map(int, inp))))
				t.display_as_matrix()

			elif i == "HELP" or i == "H":
				print("d       -> display table")
				print("f       -> display as rows")
				print("e       -> display as csv")
				print("r       -> reset table")
				print("z       -> undo most recent operation")
				print("dnf     -> get the sum of minterms")
				print("cnf     -> get the product of maxterms")
				print("sum     -> get the sigma thing")
				print("product -> get the pi thing")
				print("k       -> display a k map for the most recent equation (max 4 var)")
				print("i       -> insert a boolean output")
			# elif i == "I":
			# 	print("Enter one-by-one, the truth table values\n")
			# 	vals = []
			# 	while len(vals) < 2 ** initial:
			# 		vals.append(int(input()))
			# 	temp = Input("I",vals)
			# 	print(temp)
			# 	dnf = ""
			# 	for i in range(len(vals)):
			# 		if vals[i] == 1:
			# 			dnf += "("
			# 			for j in range(initial):
			# 				if vals[j] == 0:
			# 					dnf += t.inputs[j].name + "'"
			# 				else:
			# 					dnf += t.inputs[j].name 
			# 			dnf += ")+"
			# 	print(dnf, "dnf here")
			# 	temp.name = (dnf[:-1] + "\n")
			# 	t.add_input(temp)
			else:
				cleans = i
				cleans = clean_nums(i)
				name = cleans
				for i in range(len(cleans)):
					if cleans[i].isalpha():
						if cleans[i] not in t.get_names():
							valid = False
							break
				cleans = cleans.replace("\'","._not()")
				cleans = cleans.replace("’","._not()")
				cleans = cleans.replace("(+)", "/")
				cleans = clean_bedmas(cleans)
				name = name.replace("/", "⊕")
				cleans = cleans.replace("⊕","/")
				
				if valid and not t.inside_table(name):
					t.add_input(Input(name,eval(cleans).values))
					cleans = cleans.replace("._not()","'")
					print(cleans)
					print(t)
					print()
	except Exception as e:
		print("hi")
		print(e)