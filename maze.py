def solve_maze():
	directions = [North, East, South, West]
	current_direction_index = 0
	
	while get_entity_type() != Entities.Treasure:
		
		# Move in direction
		#move_result = move(directions[current_direction_index])
	
	
		# Move right if we can
		current_direction_index = (current_direction_index + 1) % 4
		move_result = move(directions[current_direction_index])
		
		# If we cant, try forward again
		if not move_result:
			current_direction_index = (current_direction_index - 1) % 4
			move_result = move(directions[current_direction_index])
		else:
			continue
		
		# If that fails, try left
		if not move_result:
			current_direction_index = (current_direction_index - 1) % 4
			move_result = move(directions[current_direction_index])
		else: 
			continue
		
		# If that fails, turn around
		if not move_result:
			current_direction_index = (current_direction_index - 1) % 4
		else:
			continue
		
	
	harvest()
	
		
