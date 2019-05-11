import ui
from datetime import datetime

chkin = False



def checkin():
	if chkin == False:
		chkin = True
		
		today = datetime.today()
		str_today = f'{today:%Y-%m-%d}'
		now = datetime.now()
		str_now = f'{now:%Y-%m-%d %H:%M:%S}'
		
		path = '/log/' + str_today + '.log'
		
		with open(path, mode='a', encoding='utf-8') as f:
			f.write(str_now + ' - 出勤\n')
		
	else:
		return


def checkout():
	if chkin == True:
		chkin = False
		
	else:
		return

#v = ui.load_view()
#v.present('sheet')
