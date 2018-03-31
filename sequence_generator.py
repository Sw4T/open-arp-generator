import random


def matrix_random_walk(matrix, length_sequence, init_x, init_y):

	position_x = init_x
	position_y = init_y
	cur_symbol = matrix[position_y][position_x]

	list_symbol = [cur_symbol]

	for i in range(length_sequence):
		x_or_y = bool(random.getrandbits(1))  # True mean x, False mean y
		right_or_left = bool(random.getrandbits(1))  # True mean Right(Down), False mean Left(Up)

		if x_or_y:  # On bouge sur l'axe des x
			if right_or_left:  # On bouge vers la droite
				# position_x = (position_x + cur_symbol+1) % 7
				position_x = (position_x + 3) % 7
				cur_symbol = matrix[position_y][position_x]
			else: # On bouge vers la gauche
				# position_x = (position_x - cur_symbol+1) % 7
				position_x = (position_x + 6) % 7
				cur_symbol = matrix[position_y][position_x]
		else:  # On bouge sur l'axe des y
			if right_or_left:  # On bouge vers le bas
				# position_y = (position_y + cur_symbol+1) % 7
				position_y = (position_y + 9) % 7
				cur_symbol = matrix[position_y][position_x]
			else:  # On bouge vers le haut
				# position_y = (position_y - cur_symbol+1) % 7
				position_y = (position_y + 12) % 7
				cur_symbol = matrix[position_y][position_x]
		list_symbol.append(cur_symbol)
	return list_symbol

