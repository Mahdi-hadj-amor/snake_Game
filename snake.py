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
    


