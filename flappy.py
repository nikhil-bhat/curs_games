#imports
import curses
import random
#endimports
#globals
birdx=30
birdy=10
pipex=[40,45,50,55,60]
pipey=[20,25,10,30,12]
score=0
#endglobal
def draw_border(stdscr,score):
    y,x=stdscr.getmaxyx()
    stdscr.addstr(5,5,"X"*(x-5))
    stdscr.addstr(y-5,5,"X"*(x-5))
    stdscr.refresh()
    pass
def draw_bird(stdscr):
    stdscr.addstr(birdy,birdx,"b")
    stdscr.refresh()
    pass
def draw_pipes(stdscr):
    global pipex
    global pipey
    for index,xcord in enumerate(pipex):
        if xcord<=5:
            del pipex[index]
            del pipey[index]
            xtoadd=55
            y,x=stdscr.getmaxyx()
            ytoadd=random.randint(5,y-15)
            pipex.append(xtoadd)
            pipey.append(ytoadd)
            pass
        else:
            for i in range(0,5):
                stdscr.addstr(pipey[index]+i,pipex[index],"|")
                pass
            for i in range(8,13):
                stdscr.addstr(pipey[index]+i,pipex[index],"|")
            pipex[index]-=1
            pass
        pass
    stdscr.refresh()
    pass
def game_start(stdscr):
    """ Houses the game-loop.
    draws sleeps , calls collide to check
    """
    global birdy
    curses.flash()#flash the screen
    curses.curs_set(0)#set the cursor invisible
    stdscr.nodelay(1)
    while True:
        stdscr.erase()
        draw_border(stdscr,score)
        draw_bird(stdscr)
        draw_pipes(stdscr)
        #if collide()==True:
        #    game_over(stdscr,score)
        #    pass
        up=stdscr.getch()
        if up==ord(' '):
            if birdy<=10:
                birdy=10
                pass
            else:
                birdy-=1
                pass
            pass
        else:
            y,x=stdscr.getmaxyx()
            if birdy>=y-10:
                birdy=y-10
                pass
            else:
                birdy+=1
                pass
        curses.flushinp()
        curses.napms(20)
def game_over(stdscr):
    """Flashes the screen.
    gives a choice between playing and quitting
    """
    pass
def collide():
    """The advanced collison detector.
    """
    global score
    for index,xcords in enumerate(pipex):
        if xcords==birdx:
            if birdy in range(pipey[i],pipey[i]+6) or birdy in range(pipey[i]+8,pipey[i]+13):
                return True
            pass
        pass
    return False
if __name__=='__main__':
    curses.wrapper(game_start)
#changelog
#This is the second version of the orginal code that was hastenly put down together
#Features to be added
#score serialization
#endlog
