"""
The main program should use functions from music_reports and display modules
"""
import file_handling
import music_reports
import curses

class Options:
	def __init__(self):
		self.options = ["Exit"]
		self.indexes = [0]
		self.states = [None]
		self.current = 0

	def add(self, option, elements, index=0):
		i = len(self.options) - 1

		self.options[i] = option
		if type(elements) == list and len(elements) > 0:
			self.states[i] = elements
			index2 = index if index < len(elements) else 0
			self.indexes[i] = index2

		self.options.append("Exit")
		self.indexes.append(0)
		self.states.append(None)
	#
	def is_bold(self, whch):
		return True if whch == self.current else False
	#
	def scr_print(self, stdscr, first_line=2):
		i = 0
		line_no = first_line
		while i < len(self.options):
			if type(self.states[i]) == list:
				opts = self.states[i]
				index = self.indexes[i]
				stdscr.addstr(line_no, 0, "- {}: {}".format(self.options[i], opts[index]) )
			else:
				stdscr.addstr(line_no, 0, "- {}".format(self.options[i]) )
			i += 1
			line_no += 1
		#

		# bold the whch's option;
		line_no = first_line + self.current
		if type(self.states[self.current]) == list:
			opts = self.states[self.current]
			index = self.indexes[self.current]
			stdscr.addstr(line_no, 0, "- {}: {}".format(self.options[self.current], opts[index]), curses.A_BOLD)
		else:
			stdscr.addstr(line_no, 0, "- {}".format(self.options[self.current]), curses.A_BOLD)
	#
	def move_up(self):
		if self.current > 0:
			self.current -= 1
	#
	def move_down(self):
		if self.current < len(self.options) - 1:
			self.current += 1
	#
	def print_next_element(self, stdscr, first_line=2):
		if type(self.states[self.current]) != list:
			return

		opts = self.states[self.current]
		index = self.indexes[self.current]
		if index == len(opts) - 1:
			return

		self.indexes[self.current] += 1
		line_no = first_line + self.current
		stdscr.addstr(line_no, 0, "- {}: {}".format(self.options[self.current], opts[index+1]), curses.A_BOLD)
	#
	def print_prev_element(self, stdscr, first_line=2):
		if type(self.states[self.current]) != list:
			return

		opts = self.states[self.current]
		index = self.indexes[self.current]
		if index == 0:
			return

		self.indexes[self.current] -= 1
		line_no = first_line + self.current
		stdscr.addstr(line_no, 0, "- {}: {}".format(self.options[self.current], opts[index-1]), curses.A_BOLD)
	#
	def is_exit(self):
		return False if self.current < len(self.options) - 1 else True
	#
#

def scroll_list(stdscr, lists):
	pass
#


def menu(stdscr, albums):
	stdscr = curses.initscr()

	curses.noecho()
	curses.cbreak()
	stdscr.keypad(True)


	run = True if len(albums) > 0 else False
	cmd = 0

	stdscr.addstr(0, 4, "Music library.")
	options = Options()
	options.add("Get longest album", None)
	options.add("Get total albums length", None)
	options.add("Get genre stats", None)
	options.add("Get last oldest", None)
	options.add("Get last oldest of genre", None)
	options.add("Get last oldest of genre", None)

	genres = music_reports.get_genres(albums)
	if len(genres) > 0:
		options.add("Get albums by genre", genres)

	while run:
		options.scr_print(stdscr)

		c=stdscr.getch()

		if c==curses.KEY_UP:
			options.move_up()
		elif c==curses.KEY_DOWN:
			options.move_down()
		elif c==curses.KEY_RIGHT:
			options.print_next_element(stdscr, 2)
		elif c==curses.KEY_LEFT:
			options.print_prev_element(stdscr, 2)
		#elif (c==curses.KEY_ENTER or c==10) and cmd == 0:
		#	pass
		elif (c==curses.KEY_ENTER or c==10) and options.is_exit():
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

