import random
import curses
def main (stdscr):
    # creat window for 
    curses.curs_set(0)
    scner_height , scner_width = stdscr.getmaxyx()
    window = curses.newwin(scner_height,scner_width,0,0)
    window.keypad(True)
    window.timeout(125)
     # frist position of snake in in interface window 
    x_snke = scner_height//4
    y_snke = scner_width//2
    #creat snake 
    snake = [
        (x_snke,y_snke),# head of snake 
        (x_snke,y_snke-1),#body of snake 
        (x_snke,y_snke*2)# footer of snake
    ]
    # creat food of snake and the position in intreface 
    food = [scner_height//2,scner_width//2]
    window.addch(food[0],food[1],curses.ACS_DIAMOND)# added and desplay food in inteface 
    # added key  for direction of snake 
    key = curses.KEY_LEFT()
    while True : 
        next_key = window.getch()
        key=key if next_key == -1 else next_key

        head_y,head_x=snake[0]
        if head_y in [scner_height-1,0]or head_x in [0,scner_width] or snake[0]in snake[1:] :
            curses.endwin()
            break
        
    new_head= [head_y,head_x]
    if key == curses.KEY_DOWN:
        head_y +=1
    elif key == curses.KEY_UP:
        head_y -=1
    elif key == curses.KEY_LEFT:
        head_x -=1
    elif key == curses.KEY_RIGHT:
        head_x +=1
        





