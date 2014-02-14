import json
from lib import switches

data = json.load(open('app/models/data.json', 'r+'))

def changeStateSwitch(id,newStatus):

	nos = len(data['data']) # Number of devices
	info = data['data']

	for i in range(0, nos):
		if info[i]['name'] == id:
			state = info[i]['status']
			if state == newStatus:
				print('already the status')
			else:
				dataType = info[i]['type']
				dataSwitch = info[i]['name'][1]
				dataStatus = ( "1" if (newStatus == "on") else "0" )
				switches.sendSignalSwitch(dataType, dataSwitch, dataStatus)
				info[i]['status'] = newStatus
				print('status changed')
		json.dump(data, open('app/models/data.json', 'w'))

	return 1