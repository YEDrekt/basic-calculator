import operator

operatorlookup = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

operation = input("İşlemi giriniz: ")

elements = []

if " " in operation:
    elements = operation.split(" ")
else:
    elements = operation

result = 0

for x in range(0, len(elements), 2):
    y = int(elements[x])

    if x == 0:
        result += y
    else:
        op = operatorlookup.get(elements[x-1])
        result = op(result, y)

print("Result: ", result)
