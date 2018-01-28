import json

# Read input file line by line
# if variable, look for parameters
# use both variable and parameters to build dictionary
#	in the same format as our json template
# convert dictionary to json format and write to file

f = open('input_Kr.txt', 'r')
lines = list(f)

all_vars = []

i = 0
while i < len(lines):
	if "$" in lines[i]: #variable begins
		var_name = lines[i].strip(" $").rstrip("\n")
		params = []

		while lines[i].strip(" $") != "end\n":
			if "=" in lines[i]:
				param = {}
				param_valdesc = lines[i].split("=")
				val_desc = param_valdesc[1].split(",")
				param["name"] = param_valdesc[0].strip()
				param["value"] = val_desc[0].strip()

				if param["name"][0] == "!": # commented out variable
					param["name"] = param["name"][1:].lstrip()
					param["isValid"] = "false"
				else:
					param["isValid"] = "true"

				if len(val_desc) > 1:
					param["description"] = val_desc[1].strip(" !").rstrip("\n")
				else:
					param["description"] = ""
				params.append(param)

			i += 1

		variable = {"type": "var", "description": ""}
		variable["name"] = var_name
		variable["data"] = {"parameters": params}

		all_vars.append(variable)

	i+=1

json_shell = {}
json_shell["variables"] = all_vars

new_f = open('input_Kr.json', 'w+')

new_f.write(json.dumps(json_shell))

new_f.close()
f.close()	
