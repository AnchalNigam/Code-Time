# def largestNumber(array): 
	
# 	# extval is a empty list for extended 
# 	# values and ans for calculating answer 
# 	extval, ans = [], "" 
	
# 	# calculating the length of largest number 
# 	# from given and add 1 for further operation 
# 	l = len(str(max(array))) + 1
# 	# print(l)
# 	# iterate given values and 
# 	# calculating extended values 
# 	for i in array: 
# 		temp = str(i) * l 
# 		print(temp, i, (temp[:l:], i))
# 		# make tuple of extended value and 
# 		# equivalant original value then 
# 		# append to list 
# 		extval.append((temp[:l:], i)) 
        
	
# 	# sort extval in descending order 
# 	extval.sort(reverse = True) 
	
# 	# iterate extended values 
# 	for i in extval: 
		
# 		# concatinate original value equivalant 
# 		# to extended value into ans variable 
# 		ans += str(i[1]) 

# 	if int(ans)==0: 
# 		return "0"
# 	return ans 

# # Driver code 
# a = [ 472, 663, 964, 722, 485, 852, 635, 368, 676, 319, 412 ]


# print(largestNumber(a)) 



# other way - not got success
# a = [ 472, 663, 964, 722, 485, 852, 4, 635, 368, 676, 319, 412 ]
# a = [ 980, 674, 250, 359, 98, 969, 143, 379, 363, 106, 838, 923, 969, 880, 997, 664, 152, 329, 975, 377, 995, 943, 369, 515, 722, 302, 496, 124, 692, 993, 341, 785, 400, 113, 302, 563, 121, 230, 358, 911, 437, 438, 494, 599, 168, 866, 689, 444, 684, 365, 470, 176, 910, 204, 324, 657, 161, 884, 623, 814, 231, 694, 399, 126, 426 ]
a = [3, 30, 34, 5, 9]
maxElem = max(a)
maxElemLen = len(str(maxElem))
divider = int('1' + ''.join(['0']*(maxElemLen-1)))
resArr = []
for i in a:
	if len(str(i)) != maxElem:
		newDigit = int(str(i) + ''.join(['0']*(maxElemLen-len(str(i)))))
		resArr.append((newDigit//divider, maxElemLen-len(str(i)), newDigit%divider,i))
	else:
		resArr.append((i//divider, maxElemLen-len(str(i)), i%divider, i))
print(resArr)
resArr.sort(reverse=True)
print(resArr)
digit = ""
for value in resArr:
	digit += str(value[3])
# if int(digit) == 0:
# 	return "0"      98997995993980975969969943923911910884880866838814785722694692689684674664657623599563515496494470444438437426400399379377369365363359358341329324302302250231230204176168161152143126124121113106           
print(digit, digit == "99799599398980975969969943923911910884880866838814785722694692689684674664657623599563515496494470444438437426400399379377369365363359358341329324302302250231230204176168161152143126124121113106", "23" == "23")
