def main():
    t = int(input())
    my_output = []
    my_input = []
    for i in range(t):
        line = input()
        my_input.append(line)
    for line in my_input:
        arr = line.split(" ")
        a = arr[0]
        b = arr[1]
        c = arr[2]
        if a != b != c:
            my_output.append(1)
        else:
            my_output.append(0)

    for x in my_output:
        print(x)


if __name__ == '__main__':
    main()
