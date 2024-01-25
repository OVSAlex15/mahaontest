maximum8 = 0
name8 = str
maximum9 = 0
name9 = str
maximum10 = 0
name10 = str
maximum11 = 0
name11 = str

l =[]

file = open('mat_dv.txt','r')
for i in file:
    s = str(i)
    parts = s.split(' ')
    if parts[2] == '8' and int(parts[3])+int(parts[4]) >= maximum8:
        maximum8 = int(parts[3])+int(parts[4])
        name8 = str(parts[0] +' '+ parts[1]+ ' ')
    elif parts[2] == '9' and int(parts[3])+int(parts[4]) >= maximum9:
        maximum9 = int(parts[3])+int(parts[4])
        name9 = str(parts[0] +' '+ parts[1]+ ' ')
    elif parts[2] == '10' and int(parts[3])+int(parts[4]) >= maximum10:
        maximum10 = int(parts[3])+int(parts[4])
        name10 = str(parts[0] +' '+ parts[1]+ ' ')
    elif parts[2] == '11' and int(parts[3])+int(parts[4]) >= maximum11:
        maximum11 = int(parts[3])+int(parts[4])
        name11 = str(parts[0] +' '+ parts[1]+ ' ')
        
print(maximum8,name8)
print(maximum9,name9)
print(maximum10,name10)
print(maximum11,name11)


        