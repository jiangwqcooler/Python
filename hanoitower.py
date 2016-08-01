def move_disk(disk_quantity, tower_A, tower_B, tower_C):
	if disk_quantity == 1:
		print "Move the disk %s to %s." % (tower_A, tower_C)
	else:
		move_disk(disk_quantity-1, tower_A, tower_C, tower_B)
		#move_disk(disk_quantity, tower_A, tower_B, tower_C)
		print "Move the disk %s to %s." % (tower_A, tower_C)
		move_disk(disk_quantity-1, tower_B, tower_A, tower_C)
		
disk_quantity = raw_input("Please input disk quantity:")
disk_quantity = int(disk_quantity)
move_disk(disk_quantity, 'A', 'B', 'C')