"""
The main program should use functions from music_reports and display modules
"""
import file_handling
import music_reports
import curses


def scroll_list(stdscr, lists):
    pass
#


def menu(stdscr, albums):
    stdscr = curses.initscr()

    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)


    run = True
    cmd = 0

    stdscr.addstr(0, 4, "Music library.")
    options = ["Get albums by genre",
				"Get longest album",
				"Get total albums length",
				"Get genre stats",
				"Get last oldest",
				"Get last oldest of genre"]


    while run:
        i = 0
        while i < len(options): # print all questions in the same way;
            stdscr.addstr(i + 2, 0, "{}) {}".format(i+1, options[i]) )
            i += 1
        stdscr.addstr(i + 2, 0, " Exit")

        if cmd == len(options):
            stdscr.addstr(len(options) + 2, 0, " Exit", curses.A_BOLD)
        else:
            stdscr.addstr(cmd + 2, 0, "{}) {}".format(cmd + 1, options[cmd]), curses.A_BOLD)


        c=stdscr.getch()

        if c==curses.KEY_UP and cmd > 0:
            cmd -= 1
        elif c==curses.KEY_DOWN and cmd < len(options):
            cmd += 1
        elif (c==curses.KEY_ENTER or c==10) and cmd == 0:

        elif (c==curses.KEY_ENTER or c==10) and cmd == len(options):
            run = False

    #

    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()

    curses.endwin()
#

def main():
    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should repeat displaying menu and asking for
    input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """
    albums = file_handling.import_data()

    curses.wrapper(menu, albums)


#

if __name__ == '__main__':
    main()

