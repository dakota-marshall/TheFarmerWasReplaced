def return_to_start():
	while get_pos_x() != 0:
		move(East)
	while get_pos_y() != 0:
		move(South)

def is_even_y_position():
	return get_pos_y() % 2 == 0

def buy_seeds(seed):
	world_size = get_world_size()
	if num_items(seed) < world_size:
		trade(seed, world_size)

def check_soil():
	if get_ground_type() != Grounds.Soil:
		till()
		return True
	else:
		return False

def fertilize():
	while not can_harvest():
		if num_items(Items.Fertilizer) < get_world_size():
			trade(Items.Fertilizer, get_world_size())
		use_item(Items.Fertilizer)

def water_tile():
	water_level = get_water()
	if get_ground_type() != Grounds.Soil:
		return
	
	# Get water tank if need be
	if num_items(Items.Water_Tank) < 1:
		trade(Items.Empty_Tank, 10)
	
	# Water if low
	if water_level < 0.75:
		use_item(Items.Water_Tank)
		
def harvest_column(item):
	
	for tile in range(get_world_size()):
		
		# Water
		water_tile()
		
		if item == "carrot":
			buy_seeds(Items.Carrot_Seed) 
			# Move on if we cant harvest carrot
			if get_entity_type() == Entities.Carrots and not can_harvest():
				move(North)
				continue
			if check_soil():
				plant(Entities.Carrots)
				move(North)
				continue
			if get_ground_type() == Grounds.Soil and get_entity_type() == None:
				plant(Entities.Carrots)
				move(North)
				continue
			if can_harvest():
				harvest()
				plant(Entities.Carrots)
			else: 
				fertilize()
				harvest()
				plant(Entities.Carrots)
				
		if item == "tree":
			if (get_entity_type() == Entities.Bush or get_entity_type() == Entities.Tree) and not can_harvest():
				move(North)
				continue
			else:
				if is_even_y_position():
					plant(Entities.Tree)
				else:
					plant(Entities.Bush)

			if can_harvest() and get_entity_type() == Entities.Bush:
				use_item(Items.Fertilizer)
				# Start Maze function if it occurs
				if get_entity_type() == Entities.Hedge:
					solve_maze()
					return_to_start()
					break		
					
			if can_harvest():
				harvest()
				if is_even_y_position():
					plant(Entities.Tree)
				else:
					plant(Entities.Bush)
			else:
				harvest()
				if is_even_y_position():
					plant(Entities.Tree)
				else:
					plant(Entities.Bush)

		if item == "pumpkin":
			buy_seeds(Items.Pumpkin_Seed)
			# Move on if we cant harvest pumpkin
			if get_entity_type() == Entities.Pumpkin and not can_harvest():
				move(North)
				continue
			if check_soil():
				plant(Entities.Pumpkin)
				move(North)
				continue
			if get_ground_type() == Grounds.Soil and get_entity_type() == None:
				plant(Entities.Pumpkin)
				move(North)
				continue
			if can_harvest():
				harvest()
				plant(Entities.Pumpkin)
			else: 
				fertilize()
				harvest()
				plant(Entities.Pumpkin)
				
		if item == "sunflower":
			buy_seeds(Items.Sunflower_Seed) 
			if get_entity_type() == Entities.Sunflower and not can_harvest():
				move(North)
				continue
			if check_soil():
				plant(Entities.Sunflower)
				sunflower_values[tile] = None
				move(North)
				continue
				
			if get_entity_type() != Entities.Sunflower:
				plant(Entities.Sunflower)
				move(North)
				sunflower_values[tile] = None
				continue

			petal_count = measure()
			sunflower_values[tile] = petal_count
			
			# We dont have all sunflowers ready yet, skip
			if None in sunflower_values:
				move(North)
				continue
				
			if max(sunflower_values) == petal_count and can_harvest():
				harvest()
				plant(Entities.Sunflower)
				
				

		if item == "grass":
			if can_harvest():
				harvest()
		
		move(North)
