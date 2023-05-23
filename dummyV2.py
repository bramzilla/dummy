import msvcrt

print("This is a little dummy test. Press x to close.")

while True:
    if msvcrt.kbhit() and msvcrt.getch() == b'x':
        break

# old hash 26d3d596858181254802694a11df4521ed456f4ab528b7c3efa897fc1d2d190b
# new hash da84a42a07086e7beb2215539c03b3914e78c01d061f1e86474662a791ba36e7