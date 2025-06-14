These things I want to fix / improve in my Pomodoro timer program:

- [ ] Fix the geometry error that appears when I run the program. For some reason, the geometry error was not loggeg in log files but it was printed to the console. Maybe also logging should be improved. Below is the error message and it was printed when I was resizing the window:
"
QWindowsWindow::setGeometry: Unable to set geometry 201x200+1299+145 (frame: 201x200+1299+145) on QWidgetWindow/"PomodoroTimerClassWindow" on "\\.\DISPLAY1". Resulting geometry: 201x240+1299+145 (frame: 201x240+1299+145) margins: 0, 0, 0, 0 minimum size: 200x200 MINMAXINFO(maxSize=POINT(x=0, y=0), maxpos=POINT(x=0, y=0), maxtrack=POINT(x=0, y=0), mintrack=POINT(x=200, y=200)))"

- [] I dont want to get this pygame 2.6.1 message every time I run the program.
"pygame 2.6.1 (SDL 2.28.4, Python 3.12.6)
Hello from the pygame community. https://www.pygame.org/contribute.html"

- [ ] Add simple CLI to start program from command line. I want to be able to first of all install the program using pip and then run it from command line just by typing in pomodoro. This shall launch the program. I also want to be able to run it with some arguments like --help or --version. The help message should show the description of the program and how to use it. I want to also include focus time and break time as arguments so that i can have custom setup easily available. These shall be optional arguments and if they are not provided, the program should use values from the config file. 