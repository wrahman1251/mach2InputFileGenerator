import json



with open('input_Kr.json', 'r') as f:
	json_mach2 = json.load(f)

new_file = open('new_mach2_input.txt', 'w+')

for variable in json_mach2['variables']:
	new_file.write('$'+variable['name']+'\n')
	for parameter in variable['data']['parameters']:
		if parameter['isValid'] == "true":
			new_line = '\t' + parameter['name'] + ' = ' + parameter['value']

			if parameter['description'] != "":
				new_line += ' ! ' + parameter['description'] + '\n'
			else:
				new_line += '\n'

			new_file.write(new_line)

	new_file.write('$end\n')


new_file.close()

