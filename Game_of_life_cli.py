##ASSEMENT GAME OF LIFE BY pavanthatipamula6@gmail.com

import sys
from os import system, name


class present_grid:
    def __init__(self,pre_grid):
        self.pre_grid=pre_grid
class future_grid:
    def __init__(self,fut_grid):
        self.fut_grid=fut_grid

pret_grid=[]
futt_grid=[]

global M,N

list=[]
list.append(present_grid(pret_grid))
list.append(future_grid(futt_grid))

##generation count
count=0

##to clear screen
def clear():
	## for windows
	if name == 'nt':
		_ = system('cls')
	## for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')

##menu for cli
def menu():
    clear()
    print("\t Generation count \t ",count)
    print("\t 1 \t Record present gen")
    print("\t 2 \t Print present gen")
    print("\t 3 \t Print Next gen")
    print("\t 4 \t Search a cell (using row,column no) ")
    print("\t h \t help")
    print("\t q \t quit")


##initializing zero grid for next generation

def initialising_zero_grid(M,N):
    futt_grid=[]
    for i in range(M):
            futt_grid.insert(i+1,[])
            for j in range (N):
                   futt_grid[i].append(0)
    list[1].fut_grid=futt_grid
    return futt_grid
        


## Function to print next generation
def nextGeneration(present_grid,future_grid,M,N):
        for l in range(M):
            for m in range(N):
                        ## finding no Of Neighbours
                        ## that are alive subtract 1
                        aliveNeighbours = 0
                        for i in range (-1,2):
                                for j in range(-1,2):

                                        if(l + i<0 or m + j<0 or  l + i>M-1 or m + j>N-1):
                                                pass
                                        else:
                                                aliveNeighbours +=int(present_grid[l + i][m + j])

                                        
                        ## The cell needs to be subtracted
                        ## from its neighbours as it was
                        ## counted before
                        
                                                
                        aliveNeighbours -= int(present_grid[l][m])
                        

                        ## Implementing the Rules of Life

                        ## alone cell dies
                        if ((present_grid[l][m] == 1) and(aliveNeighbours < 2)):
                                future_grid[l][m]=(0)

                        ## dies due to over population
                        elif ((present_grid[l][m] == 1) and(aliveNeighbours > 3)):
                                future_grid[l][m]=(0)

                        ## new cell is born
                        elif ((present_grid[l][m] == 0) and(aliveNeighbours == 3)):
                                future_grid[l][m]=(1)

                        ## Remains the same
                        else:
                                future_grid[l][m]=(present_grid[l][m])
        return future_grid
        

##nextGeneration(list[0].pre_grid,list[1].fut_grid,M,N)
def record_pret_gen(M,N,b_list):
    global count
    count=1
    print("recorded Generation")
    pret_grid=[]
    list[0].pre_grid=pret_grid
    k=0
    for i in range(M):
            pret_grid.insert(i+1,[])
            for j in range (N):
                   pret_grid[i].append(int(b_list[k]))
                   k+=1
    list[0].pre_grid=pret_grid

    
##for generation and printing next generation
def print_next_gen(M,N):
    global count
    print("Next Generation");
    initialising_zero_grid(M,N)

    list[1].fut_grid=nextGeneration(list[0].pre_grid,list[1].fut_grid,M,N)

    for i in range (M):

            for j in range (N):
            
                    if (list[1].fut_grid[i][j] == 0):
                            print(".",end='')
                    else:
                            print("*",end='')
            
            print();
    count+=1
    list[0].pre_grid=list[1].fut_grid


##to print present generation    
def print_present_gen(M,N):
    print("Present Generation");
    for i in range (M):
        for j in range (N):
            if (list[0].pre_grid[i][j] == 0):
                print(".",end='')
            else:
                print("*",end='')

        print();


####searches present state of cell
def search(location):
    m=int(location[0])
    n=int(location[1])
    if (list[0].pre_grid[m][n] == 0):
        print(".",end='')
    else:
        print("*",end='')




def input_data():
    b=input()
    b_list=b.replace(' ',',')
    b_list=b_list.split(',')
    return b_list

def help():
    print("______________------______________")
    print(" \".\" represents dead cells")
    print(" \"*\" represents dead cells")
    print("add grid rows no. and columns no. \n  while initialising program")
    print("In search add co-ordinates as row,column")
    print("next generation simulates the next generation and shows result")
    print("______________------______________")
    print("made by nobody_0417 aka pavanthatipamula")




def main():
    script = sys.argv[0]
    M = int(sys.argv[1])
    N = int(sys.argv[2])
    initialising_zero_grid(M,N)
    list.append(future_grid(futt_grid))

    action=input('\nSelect Option :')
    
    if action == '1':
        menu()
        print("\nEnter the Cell data : ")
        b_list=input_data()
        if len(b_list)== (M*N) :
            record_pret_gen(M,N,b_list)
            print('Cells Recorded')
        else:
            print("Please enter the cells again")
    elif action == '2':
        menu()
        print_present_gen(M,N)
    elif action == '3':
        menu()
        print_next_gen(M,N)
    elif action == '4':
        menu()
        print("\nEnter the co-ordinates of cell : ")
        b_list=input_data()
        search(b_list)
    elif action == 'h':
        help()
    elif action == 'q':
        exit()
    else:
        print("please enter a valid input")
    
    main()


menu()
if __name__ == '__main__':
   main()
