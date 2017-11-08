file=open("unique_ip.txt","r")
count_lines=0
for line in file:
	count_lines+=1
	print(line)
print("Total line=",count_lines)
#print(f.readlines())

