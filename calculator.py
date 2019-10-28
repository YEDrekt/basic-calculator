import operator

operatorlookup = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

operation = input("İşlemi giriniz: ")

result = 0

elements = []

for z in operation:
    if z is not " ":
        elements.append(z)

for x in range(0, len(elements), 2):
    y = int(elements[x])

    if x == 0:
        result += y
    else:
        op = operatorlookup.get(elements[x-1])
        result = op(result, y)

print("Result: ", result)
