
def to_camel_case(text):
    s = text.replace("-", " ").replace("_", " ")
    s = s.split()
    if len(text) == 0:
        return text
    return s[0] + ''.join(i.capitalize() for i in s[1:])

nome = 'MARCIO LUCAS MOTA CAMINHA'
print(f'Meu nome é {to_camel_case(nome)}')