import ui, os
from datetime import datetime

chkin = False

master_today = datetime.today()
master_str_today = f'{master_today:%Y-%m-%d}'
master_now = datetime.now()
master_str_now = f'{master_now:%Y-%m-%d %H:%M:%S}'
master_path = 'log/' + master_str_today + '.csv'

if os.path.exists(master_path):
	with open(master_path, encoding='utf-8') as f:
		for row in f:
			lastRow = row.rstrip()
		columns = lastRow.split(',')
		lastTime = columns[0]
		status = columns[1]
	
	label = sender.superview['label1']
	text = 'last status\n' + status + 'at ' + lastTime
	label.text = text

	if status == 'check_in':
		chkin = False
	elif status == 'check_out':
		chkin = True
				

def checkin(sender):
	global chkin
	if chkin == False:
		chkin = True
		
		today = datetime.today()
		str_today = f'{today:%Y-%m-%d}'
		now = datetime.now()
		str_now = f'{now:%Y-%m-%d %H:%M:%S}'
		
		path = 'log/' + str_today + '.csv'
		
		with open(path, mode='a', encoding='utf-8') as f:
			f.write(str_now + ',check_in\n')
		
		label = sender.superview['label1']
		text = 'last status\n' + 'cecked in\n' + 'at ' + str_now
		label.text = text
		
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
		
		path = 'log/' + str_today + '.csv'
		
		with open(path, mode='a', encoding='utf-8') as f:
			f.write(str_now + ',check_out\n')
		
		label = sender.superview['label1']
		text = 'last status\n' + 'cecked out\n' + 'at ' + str_now
		label.text = text
		
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
