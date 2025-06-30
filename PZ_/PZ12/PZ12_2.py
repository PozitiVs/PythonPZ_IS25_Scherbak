#составить генератор  yield, который преобразует все буквенные символы в заглавные
from functools import partial

def char_processor(func, text):
    yield from map(func, text)

uppercase_gen = partial(char_processor, str.upper)

text = "Hello, Functional 123!"
result = uppercase_gen(text)

print(''.join(uppercase_gen(text)))  