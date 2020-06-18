from cs50 import get_int

#Define main so we can call on a function the we define after it's implemented
def main():
    #Request how tall the user want's the parymid and run parymid function
    height = get_int("How tall do you want your parymid? ")
    parymid(height)

def parymid(height):
    #Recursively print the parymid and escape when height is 0
    if height == 0:
        return
    else:
        parymid(height-1)

    #Print the inital row for the parymid recursion
    for i in range(height):
        print("#", end="")
        i = i + 1
    print("\n")

main()
