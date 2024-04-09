def value_chain(*args):
  for i in args:
        if i is isinstance(i,(str,bytes)):
            yield i
            return
        try:
            yield from i
        except:
            yield i


v=('afasdf','hhjjkj')
print(type(v))
print(list(value_chain(v)))