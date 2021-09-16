def func(input_char, i = 0):
    if i == len(input_char):
        print("".join(input_char))
    for j in range(i, len(input_char)):
        string = [char for char in input_char]
        string[i], string[j] = string[j], string[i]
        func(string, i + 1)
print("Enter the symbols: ")
s = input()
print(func(s))
