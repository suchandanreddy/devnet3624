from flask import Flask
from netmiko import ConnectHandler
from time import sleep
from plotly.offline import plot
from plotly.graph_objs import Scatter

app = Flask(__name__)

@app.route('/memory/')
def index():
	
	device = {
    	        'device_type': 'cisco_ios',
    		'ip':   '172.16.31.1',
    		'username': 'cisco',
    		'password': 'cisco',
		}
	
		
	flag = 1
	iter_out = ''

	used_mem_list = []
	time_list = []

	while 1:

		net_connect = ConnectHandler(**device)
		mem_out = net_connect.send_command('show process memory sorted')
		net_connect.disconnect()
		line_count = 0

		iter_out += '<br/>' + '<font face="verdana" color="green" size="4"><html><body><h1>' + 'Memory output iteration ' + str(flag) + '</h1></body></html></font>' + '<br/>'

		for line in mem_out.splitlines():
			iter_out += '<font face="Courier" size="2"><html><body><h1>' + line + '<br/>' + '</h1></body></html></font>'
			if line_count == 0:
				temp = line.split()
				used_mem_list.append(temp[5])
			line_count += 1
			if line_count == 10:
				break

		time_list.append(flag)
		if flag == 5:
			break
		sleep(1)
		flag = flag + 1

	my_plot_div = plot([Scatter(x=time_list, y=used_mem_list)], output_type='div')
	plot_out = '<body>' + my_plot_div + '</body>' 

	Output = plot_out + iter_out

	return Output


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
