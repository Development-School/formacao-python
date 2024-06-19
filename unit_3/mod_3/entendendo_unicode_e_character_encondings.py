
# Entendendo Unicode e os Character Encodings ▼
# Ref.: (https://docs.python.org/3/howto/unicode.html)

print("-----------------------------------------------")

import unicodedata

u = chr(233) + chr(0x0bf2) + chr(3972) + chr(6000) + chr(13231)

for i, c in enumerate(u):
    print(i, '%04x' % ord(c), unicodedata.category(c), end=" ")
    print(unicodedata.name(c))

# 0 00e9 Ll LATIN SMALL LETTER E WITH ACUTE
# 1 0bf2 No TAMIL NUMBER ONE THOUSAND
# 2 0f84 Mn TIBETAN MARK HALANTA
# 3 1770 Lo TAGBANWA LETTER SA
# 4 33af So SQUARE RAD OVER S SQUARED

print("-----------------------------------------------")

# Get numeric value of second character
print(unicodedata.numeric(u[1]))
# 1000.0

print("-----------------------------------------------")

def compare_strs(s1, s2):
    def NFD(s):
        return unicodedata.normalize('NFD', s)

    return NFD(s1) == NFD(s2)

single_char = 'ê'
multiple_chars = '\N{LATIN SMALL LETTER E}\N{COMBINING CIRCUMFLEX ACCENT}'
print('length of first string=', len(single_char))
print('length of second string=', len(multiple_chars))
print(compare_strs(single_char, multiple_chars))

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")
