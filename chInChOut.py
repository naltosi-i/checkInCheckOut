import ui

chkin = False

def checkin():
	if chkin == False:
		chkin = True
		
	else:
		return 


def checkout():
	if chkin == True:
		chkin = False
		
	else:
		return 

v = ui.load_view()
v.present('sheet')
