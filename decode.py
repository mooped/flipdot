import base64
import sys

#print(base64.b64encode(''.join(map(chr, range(84))).encode()))

def output(buffer):
    image = base64.b64decode(buffer)
    image = list(map(lambda x: [c for c in "{0:8b}".format(x)], image))
    image = zip(*image)

    print("+- FLIPDOT SIMULATOR ----------------------------------------------------------------+")

    for row in image:
        buffer = ["+"]
        buffer.extend(''.join(row).replace('0', ' ').replace('1', '#'))
        buffer.append("+")
        print(''.join(buffer))

    print("+------------------------------------------------------------------------ MOOP 2026 -+")

if __name__ == "__main__":
    output(sys.argv[1])

