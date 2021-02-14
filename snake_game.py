import random
import curses

x = curses.initscr()                                        #to initialise the screen
curses.curs_set(0)                                          # set to 0 so that it doesnt show on the screen
height, width = x.getmaxyx()                                # get the width and height of the window
window = curses.newwin(height, width, 0, 0)                 # create a new window using the height and width and starting it at the top left
window.keypad(1)                                            #accepts keypad input
window.timeout(100)                                         #refresh the screen every 100ms

#create the snakes initial start position
snake_x = width/4
snake_y = height/2
snake_body = [
    [snake_y, snake_x],
    [snake_y, snake_x-1],
    [snake_y, snake_x-2]
]

#create the food (make it center of the screen)
food = [height/2, width/2]
window.addch(int(food[0]), int(food[1]), curses.ACS_DIAMOND)       #add the food to the window

key = curses.KEY_RIGHT  #need to tell the snake where to go initially

#for every movement of the snake
while True:
    next_key = window.getch()                                # have to know what the next key is
    key = key if next_key == -1 else next_key

    if snake_body[0][0] in [0, height] or snake_body[0][1]  in [0, width] or snake_body[0] in snake_body[1:]:
        curses.endwin()
        quit()

    new_head = [snake_body[0][0], snake_body[0][1]]       # determine the location of the new snake head

    if key == curses.KEY_DOWN:                            # if snake goes up
        new_head[0] += 1                                  # minus 1 on y axis
    if key == curses.KEY_UP:                              # if snake goes down
        new_head[0] -= 1                                  # add 1 on y axis
    if key == curses.KEY_LEFT:                            # if snake goes left
        new_head[1] -= 1                                  # minus 1 on x axis
    if key == curses.KEY_RIGHT:                           # if snake goes right
        new_head[1] += 1                                  # add 1 on x axis

    snake_body.insert(0, new_head)                        #insert the new snake head

    if snake_body[0] == food:                             # determine if the snake has gotten the food
        food = None                                       # in case it got the food, must select new food --> set the food to None
        while food is None:
            new_food = [
                random.randint(1, height-1),
                random.randint(1, width-1)
            ]
            food = new_food if new_food not in snake_body else None
        window.addch(food[0], food[1], curses.ACS_DIAMOND)    #add the new position of the food
    else:
        tail = snake_body.pop()
        window.addch(int(tail[0]), int(tail[1]), ' ')    #add a space to the tail of the snake

    window.addch(int(snake_body[0][0]), int(snake_body[0][1]), curses.ACS_CKBOARD) #adding the snake head to the screen
