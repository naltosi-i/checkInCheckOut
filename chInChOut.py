import ui
from datetime import datetime

chkin = False


def checkin(sender):
	global chkin
	if chkin == False:
		chkin = True
		
		today = datetime.today()
		str_today = f'{today:%Y-%m-%d}'
		now = datetime.now()
		str_now = f'{now:%Y-%m-%d %H:%M:%S}'
		
		path = 'log/' + str_today + '.log'
		
		with open(path, mode='a', encoding='utf-8') as f:
			f.write(str_now + ' - check_in\n')
		
		return 
		
	else:
		return

def checkout(sender):
	global chkin
	
	if chkin == True:
		chkin = False
		
		today = datetime.today()
		str_today = f'{today:%Y-%m-%d}'
		now = datetime.now()
		str_now = f'{now:%Y-%m-%d %H:%M:%S}'
		
		path = 'log/' + str_today + '.log'
		
		with open(path, mode='a', encoding='utf-8') as f:
			f.write(str_now + ' - check_out\n')
		
		return 
		
	else:
		return

#def main():
#	checkin()
#	checkout()
	
	
#if __name__ == '__main__':
#	main()
	
v = ui.load_view()
v.present('sheet')
