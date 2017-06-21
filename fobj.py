class Ship:
	anphib=False
	warship = True
	
	
	def __init__(self,unitdesig,initlat,initlong):
		self.unit_desig = unitdesig
		self.grid_loc_lat = initlat
		self.grid_loc_long = initlong
		
	def say_location():
		print(grid_loc_lat,grid_loc_long)
		
s1 = Ship('Celestia',5.0,7.0)

s1.say_location


