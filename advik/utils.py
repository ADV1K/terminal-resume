try:
    import msvcrt
except ImportError:
    msvcrt = None
    import sys, tty, termios


def getch() -> str:
    """Gets a single character from standard input. Does not echo to the screen."""
    if msvcrt:
        return msvcrt.getch().decode("utf-8")

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def clear():
    """Clears the screen using the ANSI escape code for clearing the terminal."""
    print("\033c", end="")
