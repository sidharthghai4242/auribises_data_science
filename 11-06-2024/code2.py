"""
    Another brick in the wall
    Mr. john:- client 
    requirement:- make a wall with 13 bricks
    jack-> 1 brick (+1 so 1,2,3,4,5)
    joe-> 2 brick (jack*2 so 2,4,6,8)
    so :-
    
    jack:-1             1
    joe:-2              3

    jack:-2             5
    joe:-4              9

    jack:-3             12
    joe:-6              13
"""
number_of_bricks=int(input("Please enter the number of bricks:- "))
jack_placed_bricks=0
total_bricks_placed=0
while(total_bricks_placed<=number_of_bricks):
    jack_placed_bricks+=1
    if(total_bricks_placed+jack_placed_bricks>=number_of_bricks):
        print("last brick to be placed by jack")   
        break
    total_bricks_placed+=jack_placed_bricks
    joe_place_bricks=jack_placed_bricks*2
    if(total_bricks_placed+joe_place_bricks>=number_of_bricks):
        print("last brick to be placed by joe")   
        break
    total_bricks_placed+=joe_place_bricks