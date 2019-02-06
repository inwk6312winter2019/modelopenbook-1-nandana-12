import re

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




