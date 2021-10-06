
# x = input().split()
# x = [int(x[i]) for i in range(len(x))]

def make_list():
    return lambda x: [i for i in range(x)]


prod = make_list()

print(prod(10))
