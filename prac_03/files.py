#-------STEP [1]---------
name = input("Please enter your name\n>")
with open("names.txt" , 'w') as file:
    file.write(name+"\n")

#-------STEP [2]---------
with open("names.txt" , 'r') as file:
    lines = file.readline()
    print("Your name is %s"%name)

with open("numbers.txt" , "w") as file:
    file.write("17\n")
    file.write("42\n")
    file.write("400\n")

#-------STEP [3]---------
with open("numbers.txt",'r' ) as file:
    nums = []
    for line in file.readlines():
        nums.append(  int(line.strip('\n') ))
    print(" sum : %d"%( nums[0] + nums[1]  ))

#-------STEP [4]---------
with open("numbers.txt",'r' ) as file:
    nums = []
    for line in file.readlines():
        nums.append(  int(line.strip('\n') ))
    print(" sum : %d"%(sum(nums) ))

