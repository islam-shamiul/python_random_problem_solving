import sys,random,copy,time
width = 60
height = 20
next_cells = []

for i in range(width):
    colum = []
    for j in range(height):
        if random.randint(0, 1) == 0:
            colum.append("#")
        else:
            colum.append(" ")

    next_cells.append(colum)


while True:
    print("\n\n\n\n\n\n")

    current_cell = copy.deepcopy(next_cells)

    for y in range(height):
        for x in range(width):
            print(current_cell[x][y],end="")
        print()

    for x in range (width):
        for y in range (height):
            left = (x-1)%width
            right = (x+1)%width
            upper = (y-1)%height
            lower = (y+1)%height
            living_cell = 0
            if current_cell[left][upper] == "#":
                living_cell +=1

            if current_cell[x][upper] == "#":
                living_cell +=1

            if current_cell[right][upper] == "#":
                living_cell +=1

            if current_cell[left][y] == "#":
                living_cell +=1

            if current_cell[right][y] == "#":
                living_cell +=1

            if current_cell[left][lower] == "#":
                living_cell +=1

            if current_cell[x][lower] == "#":
                living_cell +=1

            if current_cell[right][lower] == "#":
                living_cell +=1    

            if current_cell[x][y] == "#" and (living_cell == 2 or living_cell == 3):
                next_cells[x][y] = "#"

            elif current_cell[x][y] == " " and living_cell == 3:
                next_cells[x][y] = "#"

            else: 
                next_cells[x][y] = " "
    time.sleep(1)
