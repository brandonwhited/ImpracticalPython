def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    while wall_on_right():
        move()
    if is_facing_north() and right_is_clear():
        turn_right()
        move()
        turn_right()
        move()
        
def descend():
    while front_is_clear() and wall_on_right():
        move()
 
while not at_goal():
    if wall_in_front():
       jump()
    if wall_on_right() and front_is_clear():
       descend()
    if wall_in_front() and wall_on_right():
        turn_left()
    if at_goal():
        done()       
    if wall_on_right() and front_is_clear():
        move()
        

 
    
