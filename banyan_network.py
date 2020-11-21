import random


#### Function determining path from Switch Stage A to Switch Stage B ####
def switchAtoB (input, dest):
    if input == 'A1':
        if dest[0] == '0':
            path2 = 'B1'
        else:
            path2 = 'B3'
    if input == 'A2':
        if dest[0] == '0':
            path2 = 'B2'
        else:
            path2 = 'B4'
    if input == 'A3':
        if dest[0] == '0':
            path2 = 'B1'
        else:
            path2 = 'B3'
    if input == 'A4':
        if dest[0] == '0':
            path2 = 'B2'
        else:
            path2 = 'B4'  

    return path2  


#### Function determining path from Switch Stage B to Switch Stage C ####
def switchBtoC (input, dest):
    if input == 'B1':
        if dest[1] == '0':
            path3 = 'C1'
        else:
            path3 = 'C2'
    if input == 'B2':
        if dest[1] == '0':
            path3 = 'C1'
        else:
            path3 = 'C2'
    if input == 'B3':
        if dest[1] == '0':
            path3 = 'C3'
        else:
            path3 = 'C4'
    if input == 'B4':
        if dest[1] == '0':
            path3 = 'C3'
        else:
            path3 = 'C4'  
            
    return path3   

#### Function determining path from Switch Stage C to Output ####
def switchCtoOutput (input, dest):
    if input == 'C1':
        if dest[2] == '0':
            path4 = '0'
        else:
            path4 = '1'
    if input == 'C2':
        if dest[2] == '0':
            path4 = '2'
        else:
            path4 = '3'
    if input == 'C3':
        if dest[2] == '0':
            path4 = '4'
        else:
            path4 = '5'
    if input == 'C4':
        if dest[2] == '0':
            path4 = '6'
        else:
            path4 = '7'  
            
    return path4   

def main():

    #### Taking number of inputs from User ####
    inputs = []
    n = int(input("Enter the number of inputs\n"))

    #### Generating random numbers from 0-7 ####
    for i in range(n):
        randNum = random.randint(0, 7)
        while randNum in inputs:
            randNum = random.randint(0, 7)
        inputs.append(randNum)
    print(inputs)

    #### Batcher -Sorting the inputs in ascending order ####
    inputs.sort()
    input_dict = {}
    for i in range(n):
        input_dict[i] = inputs[i]
    print("Randomly generated numbers for each input port are \n", input_dict) 
    
    #### Defining the starting points for each input port ####
    starting_points = { '0': 'A1', '1': 'A2', '2': 'A3', '3': 'A4', '4': 'A1', '5': 'A2', '6': 'A3', '7': 'A4'}           


    #### Driver code to generate paths from all inputs to all destinations ####
    for i in range(n):
        x = bin(input_dict[i])[2:].zfill(3)
        path1 = starting_points[str(i)]
        path2 = switchAtoB(path1, x)
        path3 = switchBtoC(path2, x)
        path4 = switchCtoOutput(path3, x)
        print("Path from input port"+str(i)+" to output port"+str(input_dict[i])+" is"+ " "+ path1+"-->"+path2+"-->"+path3+"-->"+path4)


#### Calling the main function ####
if __name__ == '__main__':
    # switchAtoB(input, dest)
    # switchBtoC(input, dest)
    # switchCtoOutput(input, dest)   
    main()       