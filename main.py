return_to_start()

# Sunflower global
sunflower_values = []
for flower in range(get_world_size()):
	sunflower_values.insert(flower, None)

while True:
	
	plant_order = [
		"tree",
		"carrot", 
		"tree",
		"pumpkin",
		"pumpkin",
		"pumpkin",
		"sunflower",
		"grass"
	]
	
	drone_col = get_pos_x()
		
	if num_items(Items.Fertilizer) < get_world_size():
		trade(Items.Fertilizer, get_world_size())
	
	harvest_column(plant_order[drone_col])
	
	move(East)
