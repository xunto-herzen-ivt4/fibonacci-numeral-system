import fibonacci_ns

for i in range(0, 20):
    tmp = fibonacci_ns.convert(i)
    print(i, "|", tmp)
    print(tmp, "|", fibonacci_ns.convert_to_dec(tmp))
    print("\n")