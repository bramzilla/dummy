import msvcrt

print("This is a little dummy test. Press x to close.")

while True:
    if msvcrt.kbhit() and msvcrt.getch() == b'x':
        break