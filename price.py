def get_summ(one, two, delimiter='&'):
  fun = f"{one}{delimiter}{two}"
  return fun

a = get_summ("Learn", "python")
print(a.upper())

