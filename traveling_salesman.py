



class State:
	def __init__(self):
		self.position = 0
		self.ordered_visited = []
		self.visited = [] #sorted by node order, not visit order
		self.distance = 0
	
	def clone(self):
		new_state = State()
		new_state.position = self.position
		new_state.ordered_visited = list(self.ordered_visited) #clone
		new_state.visited = list(self.visited) #clone
		new_state.distance = self.distance

		return new_state

	def step_forward(self, next_position):
		curr_position = self.position
		new_state = self.clone()

		new_state.ordered_visited.append(curr_position)
		new_state.visited = sorted(new_state.ordered_visited)

		new_state.position = next_position
		new_state.distance += matrix[curr_position][next_position]

		return new_state


def breadth_first_search(curr_list):
	next_list = []

	same_visits_dict = {}

	for state in curr_list:
		#determina possiveis proximos estados:
		visited_and_position = state.visited + [state.position]

		possible_next_nodes = []
		for x in range(1, node_count):
			if not x in visited_and_position:
				possible_next_nodes.append(x)

		if possible_next_nodes == [] and state.position != 0: #SE nao tem para onde ir, pode ir pro 0, a menos que jan esteja lah
			possible_next_nodes = [0]
		

		#cria proximos possiveis:
		for next_position in possible_next_nodes:
			next_state = state.step_forward(next_position)

			# print(next_state.visited, next_position)

			#ver se jah nao existe na next_list algum caminho menor ateh position passando pelos mesmos visited em outra ordem:
			key = tuple(next_state.visited + [next_state.position])

			if key in same_visits_dict:
				if next_state.distance < same_visits_dict[key].distance:
					same_visits_dict[key] = next_state
			else:
				same_visits_dict[key] = next_state
			
		next_list = list(same_visits_dict.values())

	return next_list



# matrix = [
# 	[0, 2, 3, 4],
# 	[2, 0, 6, 7],
# 	[3, 6, 0, 9],
# 	[4, 7, 9, 0],
# ]

# matrix = [
# 	[0, 42, 93, 77, 44, 26, 56, 80, 59, 3],
# 	[4, 0, 85, 67, 97, 14, 56, 4, 41, 97],
# 	[71, 27, 0, 38, 70, 47, 89, 13, 50, 19],
# 	[75, 74, 22, 0, 77, 29, 74, 26, 14, 36],
# 	[94, 77, 52, 74, 0, 4, 90, 91, 27, 86],
# 	[17, 11, 44, 93, 43, 0, 69, 6, 76, 68],
# 	[55, 93, 87, 13, 48, 89, 0, 37, 27, 34],
# 	[60, 23, 11, 2, 69, 65, 87, 0, 99, 49],
# 	[90, 29, 49, 71, 25, 66, 44, 27, 0, 51],
# 	[29, 98, 85, 94, 3, 63, 46, 25, 20, 0],
# ]

matrix = [
	[0, 78, 28, 41, 48, 40, 40, 75, 91, 40, 9, 39, 90, 77, 100],
	[79, 0, 35, 53, 16, 99, 32, 89, 73, 39, 64, 52, 61, 60, 60],
	[96, 40, 0, 73, 75, 95, 91, 4, 53, 61, 1, 44, 34, 38, 29],
	[28, 59, 40, 0, 47, 17, 35, 52, 87, 58, 11, 39, 24, 41, 83],
	[49, 75, 71, 62, 0, 92, 98, 49, 72, 21, 45, 99, 45, 10, 91],
	[22, 49, 7, 72, 11, 0, 97, 92, 37, 68, 9, 61, 96, 38, 64],
	[97, 10, 54, 5, 63, 80, 0, 80, 63, 25, 28, 46, 6, 11, 36],
	[81, 9, 88, 87, 43, 26, 35, 0, 56, 34, 42, 97, 7, 53, 85],
	[45, 68, 76, 72, 21, 75, 29, 20, 0, 36, 22, 76, 27, 70, 8],
	[54, 49, 97, 73, 11, 9, 44, 75, 82, 0, 54, 23, 1, 58, 4],
	[10, 49, 40, 33, 29, 4, 66, 30, 96, 96, 0, 60, 28, 63, 98],
	[20, 67, 38, 12, 36, 88, 5, 45, 74, 54, 2, 0, 79, 60, 53],
	[1, 41, 22, 21, 38, 16, 65, 53, 95, 49, 69, 45, 0, 95, 94],
	[5, 82, 88, 20, 61, 57, 43, 56, 73, 44, 43, 94, 8, 0, 40],
	[97, 82, 19, 74, 63, 85, 8, 37, 20, 99, 70, 48, 13, 41, 0],
]

node_count = len(matrix)

first_state = State()

curr_list = [first_state]
next_list = []

while True:
	next_list = breadth_first_search(curr_list)

	if len(next_list) == 0:
		break

	for next_state in next_list:
		print(next_state.distance, next_state.ordered_visited, next_state.position)

	curr_list = next_list



print("distances:")
for state in curr_list:
	print(state.distance)


#se der certo, sobra apenas um estado com a distancia minima




#testes antes de implementar coisas:
def pre_tests():
	print("=" * 20)
	my_dict = {}
	my_dict[(1, 2)] = 3
	print(my_dict[(1, 2)])

	print(tuple([1, 2]))




import random

def generate_matrix(n):
	matrix = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]

	for i in range(n):
		matrix[i][i] = 0
		print(matrix[i], ",")


# generate_matrix(15)