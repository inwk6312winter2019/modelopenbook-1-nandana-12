#PART - 1

import re
'''
def list_ifname_ip(fobj):
	reg_pat = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
	name_list = []
	ip_list = []
	dic = {}
	for line in fobj:
		line = line.strip()
		word = line.split()
		for i in range(len(word)-1):
			if(word[i] in 'nameif'):
				name_list.append(word[i+1])
			if(reg_pat.match(word[i])):
				ip_list.append((word[i],word[i+1]))
	#print(name_list)
	#print(ip_list)
	for i in range(len(name_list)):
		dic[name_list[i]] = ip_list[i] 
	return dic



fin = open("running-config.cfg")
d = list_ifname_ip(fin)

for i,j in d.items():
	print(i, " ",j)

# PART 2

filein = open("running-config.cfg",'r')
fileout = open("config_file",'w')
#reg = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
#ip_addr = []
for line in filein:
	#line = line.strip()
	#word = line.split()

	for i in word:
		if(reg.match(i)):
			if(('192' in i) or ('172'in i)
				ip_addr.append(i)
	line = line.replace('192','10')
	line = line.replace('172','10')
	line = line.replace('255.255.0.0','255.0.0.0')
	line = line.replace('255.255.255.0','255.0.0.0')
	fileout.write(line)

final_file = open("config_file",'r')
for l in final_file:
	print(l)
#print(ip_addr)

'''

# TASK 3

file_in = open("running-config.cfg")
transit_list = []
fw_list = []
global_list = []
for my_line in file_in:
	my_line = my_line.strip()
	if("transit_access_in" in my_line):
		transit_list.append(my_line)
	elif("global_access" in my_line):
		global_list.append(my_line)
	elif("fw-management_access_in" in my_line):
		fw_list.append(my_line)

print(transit_list,end = "\n")
print(fw_list,end = "\n")
print(global_list,end = "\n")






