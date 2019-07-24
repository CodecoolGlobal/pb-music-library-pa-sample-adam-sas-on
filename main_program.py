"""
The main program should use functions from music_reports and display modules
"""
import file_handling
import music_reports
import curses


def scroll_list(stdscr, lists):
	pass
#


def print_options(stdscr, options, whch, first_line=2):
	i = first_line
	bold_line = -1
	bold_element = None

	for option,elements in options.items():
		if elements[0] == False:
			continue
		opts = elements[2]
		index = elements[1]

		if i == whch + first_line:
			bold_element = option
			bold_line = i

		if index < len(opts):
			stdscr.addstr(i, 0, "- {}: {}".format(option, opts[index]) )
		else:
			stdscr.addstr(i, 0, "- {}".format(option) )
		i += 1

	if bold_line >= first_line:
		elements = options[bold_element]
		opts = elements[2]
		index = elements[1]

		if index < len(opts):
			stdscr.addstr(bold_line, 0, "- {}: {}".format(bold_element, opts[index]), curses.A_BOLD)
		else:
			stdscr.addstr(bold_line, 0, "- {}".format(bold_element), curses.A_BOLD)
#

def switch_element_option(options, whch, increment):
	i = 0
	element = None
	for option,elements in options.items():
		if elements[0] == False:
			continue

		
		i += 1

#

def menu(stdscr, albums):
	stdscr = curses.initscr()

	curses.noecho()
	curses.cbreak()
	stdscr.keypad(True)


	run = True if len(albums) > 0 else False
	cmd = 0

	stdscr.addstr(0, 4, "Music library.")
	options = {"Get longest album": [True, 0, []],
				"Get total albums length": [True, 0, []],
				"Get genre stats": [True, 0, []],
				"Get last oldest": [True, 0, []],
				"Get last oldest of genre": [True, 0, []],
				"Get albums by genre":[True, 0, []],
				"Exit":[True, 0, []]}
# TEST_QUESTIONS = 5

	genres = music_reports.get_genres(albums)
	if len(genres) > 0:
		options["Get albums by genre"] = [True, 0, genres]
	else:
		options["Get albums by genre"] = [False, 0, []]

	while run:
		print_options(stdscr, options, cmd)


		c=stdscr.getch()

		if c==curses.KEY_UP and cmd > 0:
			cmd -= 1
		elif c==curses.KEY_DOWN and cmd < len(options):
			cmd += 1
		elif c==curses.KEY_RIGHT and i4genres < len(genres)-1 and cmd == TEST_QUESTIONS:
			i4genres += 1
		elif c==curses.KEY_LEFT and i4genres > 0 and cmd == TEST_QUESTIONS:
			i4genres -= 1
		elif (c==curses.KEY_ENTER or c==10) and cmd == 0:
			pass
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

