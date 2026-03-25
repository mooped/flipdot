
class GFXGlyph:
  def __init__(self, _bitmapOffset, _width, _height, _xAdvance, _xOffset, _yOffset):
    self.bitmapOffset = _bitmapOffset
    self.width = _width
    self.height = _height
    self.xAdvance = _xAdvance
    self.xOffset = _xOffset
    self.yOffset = _yOffset

class GFXFont:
  def __init__(self, _bitmap, _glyph, _first, _last, _yAdvance):
    self.bitmap = _bitmap
    self.glyph = _glyph
    self.first = _first
    self.last = _last
    self.yAdvance = _yAdvance

font5x7FixedBitmaps = [
  0xFA, 0xB4, 0x52, 0xBE, 0xAF, 0xA9, 0x40, 0x23, 0xE8, 0xE2, 0xF8, 0x80,
  0xC6, 0x44, 0x44, 0x4C, 0x60, 0x64, 0xA8, 0x8A, 0xC9, 0xA0, 0xD8, 0x00,
  0x6A, 0xA4, 0x00, 0x95, 0x58, 0x00, 0x25, 0x5D, 0xF7, 0x54, 0x80, 0x21,
  0x3E, 0x42, 0x00, 0xD0, 0xF8, 0x00, 0xF0, 0x08, 0x88, 0x88, 0x00, 0x74,
  0x67, 0x5C, 0xC5, 0xC0, 0x59, 0x24, 0xB8, 0x00, 0x74, 0x42, 0x22, 0x23,
  0xE0, 0xF8, 0x88, 0x20, 0xC5, 0xC0, 0x11, 0x95, 0x2F, 0x88, 0x40, 0xFC,
  0x21, 0xE0, 0xC5, 0xC0, 0x32, 0x21, 0xE8, 0xC5, 0xC0, 0xF8, 0x44, 0x44,
  0x21, 0x00, 0x74, 0x62, 0xE8, 0xC5, 0xC0, 0x74, 0x62, 0xF0, 0x89, 0x80,
  0xF3, 0xC0, 0xF3, 0x60, 0x12, 0x48, 0x42, 0x10, 0xF8, 0x3E, 0x00, 0x84,
  0x21, 0x24, 0x80, 0x74, 0x42, 0x22, 0x00, 0x80, 0x74, 0x6B, 0x7B, 0xC1,
  0xC0, 0x22, 0xA3, 0xF8, 0xC6, 0x20, 0xF4, 0x63, 0xE8, 0xC7, 0xC0, 0x74,
  0x61, 0x08, 0x45, 0xC0, 0xE4, 0xA3, 0x18, 0xCB, 0x80, 0xFC, 0x21, 0xE8,
  0x43, 0xE0, 0xFC, 0x21, 0xE8, 0x42, 0x00, 0x74, 0x61, 0x38, 0xC5, 0xC0,
  0x8C, 0x63, 0xF8, 0xC6, 0x20, 0xE9, 0x24, 0xB8, 0x00, 0x38, 0x84, 0x21,
  0x49, 0x80, 0x8C, 0xA9, 0x8A, 0x4A, 0x20, 0x84, 0x21, 0x08, 0x43, 0xE0,
  0x8E, 0xEB, 0x18, 0xC6, 0x20, 0x8C, 0x73, 0x59, 0xC6, 0x20, 0x74, 0x63,
  0x18, 0xC5, 0xC0, 0xF4, 0x63, 0xE8, 0x42, 0x00, 0x74, 0x63, 0x1A, 0xC9,
  0xA0, 0xF4, 0x63, 0xEA, 0x4A, 0x20, 0x7C, 0x20, 0xE0, 0x87, 0xC0, 0xF9,
  0x08, 0x42, 0x10, 0x80, 0x8C, 0x63, 0x18, 0xC5, 0xC0, 0x8C, 0x63, 0x18,
  0xA8, 0x80, 0x8C, 0x63, 0x1A, 0xEE, 0x20, 0x8C, 0x54, 0x45, 0x46, 0x20,
  0x8C, 0x54, 0x42, 0x10, 0x80, 0xF8, 0x44, 0x44, 0x43, 0xE0, 0xF2, 0x49,
  0x38, 0x00, 0x82, 0x08, 0x20, 0x80, 0xE4, 0x92, 0x78, 0x00, 0x22, 0xA2,
  0x00, 0xF8, 0x88, 0x80, 0x61, 0x79, 0x70, 0x88, 0xE9, 0x99, 0xE0, 0x78,
  0x88, 0x70, 0x11, 0x79, 0x99, 0x70, 0x69, 0xF8, 0x70, 0x25, 0x4E, 0x44,
  0x40, 0x79, 0x71, 0xE0, 0x88, 0xE9, 0x99, 0x90, 0xBE, 0x10, 0x11, 0x19,
  0x60, 0x88, 0x9A, 0xCA, 0x90, 0xFE, 0x00, 0xDD, 0x6B, 0x18, 0x80, 0xE9,
  0x99, 0x90, 0x69, 0x99, 0x60, 0xE9, 0xE8, 0x80, 0x79, 0x71, 0x10, 0xE9,
  0x88, 0x80, 0x78, 0x61, 0xE0, 0x44, 0xE4, 0x45, 0x20, 0x99, 0x99, 0x60,
  0x8C, 0x62, 0xA2, 0x00, 0x8C, 0x6B, 0x55, 0x00, 0x8A, 0x88, 0xA8, 0x80,
  0x99, 0x71, 0xE0, 0xF2, 0x48, 0xF0, 0x29, 0x44, 0x88, 0x00, 0xFE, 0x00,
  0x89, 0x14, 0xA0, 0x00, 0x00, 0x0D, 0xB0, 0x00
  ]

font5x7FixedGlyphs = [
  GFXGlyph(     0,   0,   1,   3,    0,    0 ),   # ' '
  GFXGlyph(     0,   1,   7,   3,    1,   -7 ),   # '!'
  GFXGlyph(     1,   3,   2,   4,    0,   -7 ),   # '"'
  GFXGlyph(     2,   5,   7,   6,    0,   -7 ),   # '#'
  GFXGlyph(     7,   5,   7,   6,    0,   -7 ),   # '$'
  GFXGlyph(    12,   5,   7,   6,    0,   -7 ),   # '%'
  GFXGlyph(    17,   5,   7,   6,    0,   -7 ),   # '&'
  GFXGlyph(    22,   2,   3,   3,    0,   -7 ),   # '''
  GFXGlyph(    24,   2,   7,   3,    0,   -7 ),   # '('
  GFXGlyph(    27,   2,   7,   3,    0,   -7 ),   # ')'
  GFXGlyph(    30,   5,   7,   6,    0,   -7 ),   # '*'
  GFXGlyph(    35,   5,   5,   6,    0,   -6 ),   # '+'
  GFXGlyph(    39,   2,   2,   3,    0,   -2 ),   # ','
  GFXGlyph(    40,   5,   1,   6,    0,   -4 ),   # '-'
  GFXGlyph(    42,   2,   2,   3,    0,   -2 ),   # '.'
  GFXGlyph(    43,   5,   5,   6,    0,   -6 ),   # '/'
  GFXGlyph(    47,   5,   7,   6,    0,   -7 ),   # '0'
  GFXGlyph(    52,   3,   7,   4,    0,   -7 ),   # '1'
  GFXGlyph(    56,   5,   7,   6,    0,   -7 ),   # '2'
  GFXGlyph(    61,   5,   7,   6,    0,   -7 ),   # '3'
  GFXGlyph(    66,   5,   7,   6,    0,   -7 ),   # '4'
  GFXGlyph(    71,   5,   7,   6,    0,   -7 ),   # '5'
  GFXGlyph(    76,   5,   7,   6,    0,   -7 ),   # '6'
  GFXGlyph(    81,   5,   7,   6,    0,   -7 ),   # '7'
  GFXGlyph(    86,   5,   7,   6,    0,   -7 ),   # '8'
  GFXGlyph(    91,   5,   7,   6,    0,   -7 ),   # '9'
  GFXGlyph(    96,   2,   5,   3,    0,   -6 ),   # ':'
  GFXGlyph(    98,   2,   6,   3,    0,   -6 ),   # ';'
  GFXGlyph(   100,   4,   7,   5,    0,   -7 ),   # '<'
  GFXGlyph(   104,   5,   3,   6,    0,   -5 ),   # '='
  GFXGlyph(   107,   4,   7,   5,    0,   -7 ),   # '>'
  GFXGlyph(   111,   5,   7,   6,    0,   -7 ),   # '?'
  GFXGlyph(   116,   5,   7,   6,    0,   -7 ),   # '@'
  GFXGlyph(   121,   5,   7,   6,    0,   -7 ),   # 'A'
  GFXGlyph(   126,   5,   7,   6,    0,   -7 ),   # 'B'
  GFXGlyph(   131,   5,   7,   6,    0,   -7 ),   # 'C'
  GFXGlyph(   136,   5,   7,   6,    0,   -7 ),   # 'D'
  GFXGlyph(   141,   5,   7,   6,    0,   -7 ),   # 'E'
  GFXGlyph(   146,   5,   7,   6,    0,   -7 ),   # 'F'
  GFXGlyph(   151,   5,   7,   6,    0,   -7 ),   # 'G'
  GFXGlyph(   156,   5,   7,   6,    0,   -7 ),   # 'H'
  GFXGlyph(   161,   3,   7,   6,    1,   -7 ),   # 'I'
  GFXGlyph(   165,   5,   7,   6,    0,   -7 ),   # 'J'
  GFXGlyph(   170,   5,   7,   6,    0,   -7 ),   # 'K'
  GFXGlyph(   175,   5,   7,   6,    0,   -7 ),   # 'L'
  GFXGlyph(   180,   5,   7,   6,    0,   -7 ),   # 'M'
  GFXGlyph(   185,   5,   7,   6,    0,   -7 ),   # 'N'
  GFXGlyph(   190,   5,   7,   6,    0,   -7 ),   # 'O'
  GFXGlyph(   195,   5,   7,   6,    0,   -7 ),   # 'P'
  GFXGlyph(   200,   5,   7,   6,    0,   -7 ),   # 'Q'
  GFXGlyph(   205,   5,   7,   6,    0,   -7 ),   # 'R'
  GFXGlyph(   210,   5,   7,   6,    0,   -7 ),   # 'S'
  GFXGlyph(   215,   5,   7,   6,    0,   -7 ),   # 'T'
  GFXGlyph(   220,   5,   7,   6,    0,   -7 ),   # 'U'
  GFXGlyph(   225,   5,   7,   6,    0,   -7 ),   # 'V'
  GFXGlyph(   230,   5,   7,   6,    0,   -7 ),   # 'W'
  GFXGlyph(   235,   5,   7,   6,    0,   -7 ),   # 'X'
  GFXGlyph(   240,   5,   7,   6,    0,   -7 ),   # 'Y'
  GFXGlyph(   245,   5,   7,   6,    0,   -7 ),   # 'Z'
  GFXGlyph(   250,   3,   7,   4,    0,   -7 ),   # '['
  GFXGlyph(   254,   5,   5,   6,    0,   -6 ),   # '\'
  GFXGlyph(   258,   3,   7,   4,    0,   -7 ),   # ']'
  GFXGlyph(   262,   5,   3,   6,    0,   -7 ),   # '^'
  GFXGlyph(   265,   5,   1,   6,    0,   -1 ),   # '_'
  GFXGlyph(   266,   3,   3,   4,    0,   -7 ),   # '`'
  GFXGlyph(   268,   4,   5,   5,    0,   -5 ),   # 'a'
  GFXGlyph(   271,   4,   7,   5,    0,   -7 ),   # 'b'
  GFXGlyph(   275,   4,   5,   5,    0,   -5 ),   # 'c'
  GFXGlyph(   278,   4,   7,   5,    0,   -7 ),   # 'd'
  GFXGlyph(   282,   4,   5,   5,    0,   -5 ),   # 'e'
  GFXGlyph(   285,   4,   7,   5,    0,   -7 ),   # 'f'
  GFXGlyph(   289,   4,   5,   5,    0,   -5 ),   # 'g'
  GFXGlyph(   292,   4,   7,   5,    0,   -7 ),   # 'h'
  GFXGlyph(   296,   1,   7,   2,    0,   -7 ),   # 'i'
  GFXGlyph(   297,   4,   7,   5,    0,   -7 ),   # 'j'
  GFXGlyph(   301,   4,   7,   5,    0,   -7 ),   # 'k'
  GFXGlyph(   305,   1,   7,   2,    0,   -7 ),   # 'l'
  GFXGlyph(   307,   5,   5,   6,    0,   -5 ),   # 'm'
  GFXGlyph(   311,   4,   5,   5,    0,   -5 ),   # 'n'
  GFXGlyph(   314,   4,   5,   5,    0,   -5 ),   # 'o'
  GFXGlyph(   317,   4,   5,   5,    0,   -5 ),   # 'p'
  GFXGlyph(   320,   4,   5,   5,    0,   -5 ),   # 'q'
  GFXGlyph(   323,   4,   5,   5,    0,   -5 ),   # 'r'
  GFXGlyph(   326,   4,   5,   5,    0,   -5 ),   # 's'
  GFXGlyph(   329,   4,   7,   5,    0,   -7 ),   # 't'
  GFXGlyph(   333,   4,   5,   5,    0,   -5 ),   # 'u'
  GFXGlyph(   336,   5,   5,   6,    0,   -5 ),   # 'v'
  GFXGlyph(   340,   5,   5,   6,    0,   -5 ),   # 'w'
  GFXGlyph(   344,   5,   5,   6,    0,   -5 ),   # 'x'
  GFXGlyph(   348,   4,   5,   5,    0,   -5 ),   # 'y'
  GFXGlyph(   351,   4,   5,   5,    0,   -5 ),   # 'z'
  GFXGlyph(   354,   3,   7,   4,    0,   -7 ),   # '{'
  GFXGlyph(   358,   1,   7,   2,    0,   -7 ),   # '|'
  GFXGlyph(   360,   3,   7,   4,    0,   -7 ),   # '}'
  GFXGlyph(   364,   4,   7,   5,    0,   -7 ),   # '~'
]

font5x7Fixed = GFXFont(font5x7FixedBitmaps, font5x7FixedGlyphs, 0x20, 0x7E, 7)

grid = []
for y in range(80):
  row = []
  for x in range(80):
    row.append(' ')
  grid.append(row)

def writePixel(x, y, c):
    global grid
    grid[y][x] = c

def writeFillRect(x, y, w, h, c):
    global grid
    for yy in range(h):
        for xx in range(w):
            writePixel(xx + w, yy + h, c)

def drawChar(font, x, y, c, colour, bg, size_x, size_y):
    c = ord(c) - font.first
    glyph = font.glyph[c]
    bitmap = font.bitmap

    bo = glyph.bitmapOffset
    w = glyph.width
    h = glyph.height
    xo = glyph.xOffset
    yo = glyph.yOffset
    xx = 0
    yy = 0
    bits = 0
    bit = 0
    xo16 = 0
    yo16 = 0

    if size_x > 1 or size_y > 1:
      xo16 = xo
      yo16 = yo

    for yy in range(h):
      for xx in range(w):
        if not (bit & 7):
          bits = bitmap[bo]
          bo += 1
        bit += 1
        if bits & 0x80:
          if size_x == 1 and size_y == 1:
            writePixel(x + xo + xx, y + yo + yy, colour)
          else:
            writeFillRect(x + (xo16 + xx) * size_x, y + (yo16 + yy) * size_y, size_x, size_y, colour)
        bits <<= 1

    return glyph.xAdvance

def drawText(font, x, y, msg, colour, bg, size_x, size_y, wrap = -1):
    cursor_x = 0
    cursor_y = 0
    for c in msg:
        if c == '\n':
            cursor_x = 0;
            cursor_y += size_y * font.yAdvance
        elif c != '\r':
            if ord(c) >= font.first and ord(c) <= font.last:
                glyph = font.glyph[ord(c) - font.first]
                w = glyph.width
                h = glyph.height
                if w > 0 and h > 0: # Is there an associated bitmap?
                    xo = glyph.xOffset
                    if wrap > 0 and ((cursor_x + size_x * (xo + w)) >= wrap):
                        cursor_x = 0;
                        cursor_y += size_y * font.yAdvance
                    drawChar(font, cursor_x, cursor_y, c, colour, bg, size_x, size_y)
                cursor_x += glyph.xAdvance * size_x

if __name__ == "__main__":
  drawText(font5x7Fixed, 0, 0, "Hello World", '#', ' ', 1, 1, 80)

  for row in grid:
    print(''.join(row))

