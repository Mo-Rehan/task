# 2. Parse below output to form dictionary where output should be like {key: []}
#     ex:     input:       in string
# 	            device1   vlan1
# 				device2   vlan2
# 				device3   vlan1
# 				device2   vlan3
# 				device1   vlan4
# 				device2   vlan1
# 				device3   vlan6
			
# 			output: 
# 			    {"device1": ["vlan1", "vlan4"], "device2": ["vlan2", "vlan1", "vlan3"], "device3": ["vlan1", "vlan6"]}



str ="""device1   vlan1
		device2   vlan2
		device3   vlan1
		device2   vlan3
		device1   vlan4
		device2   vlan1
		device3   vlan6 """
dictonary={}
for subString in str.split("\n\t\t"):
    
    l = list(subString.split("   "))
    if l[0] in dictonary:
        dictonary[l[0]].append(l[1])
    else:
        dictonary[l[0]] = list(l[1].split(" "))

print(dictonary)

