return_to_start()

# Sunflower global
sunflower_values = []
sunflower_count = { "value": 0 }
for flower in range(get_world_size()):
	sunflower_values.append(None)
	sunflower_values.append(None)

while True:
	
	plant_order = [
		"tree",
		"carrot", 
		"sunflower",
		"sunflower",
		"pumpkin",
		"pumpkin",
		"pumpkin",
		"grass",
		"carrot"
	]
	
	drone_col = get_pos_x()
		
	if num_items(Items.Fertilizer) < get_world_size():
		trade(Items.Fertilizer, get_world_size())
	
	harvest_column(plant_order[drone_col])
	
	move(East)
	
	if get_pos_x() == 0:
		sunflower_count["value"] = 0
