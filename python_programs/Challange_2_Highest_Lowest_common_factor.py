__author__ = 'virendrapatel'

x = int(input("Please input number 1 to calculate HCF and LCF:\n"))
y = int(input("Please input number 2 to calculate HCF and LCF:\n"))

# print (x+" : "+y)

div1=[]
div2=[]

for i in range(1, x+1):
    if x%i == 0:
        div1.append(i)

for t in range(1, y+1):
    if y%t == 0:
        div2.append(t)

# print(div1)
# print(div2)

new_list = set(div1).intersection(div2)

# print(new_list)

print("Highest common factor for {0} and {1} is :-> {2}".format(x,y,max(new_list)))

print("Lowest common factor for {0} and {1} is :-> {2}".format(x,y,min(new_list)))

