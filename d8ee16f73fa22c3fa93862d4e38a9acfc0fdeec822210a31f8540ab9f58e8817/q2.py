import math


def check(n, m, k):
    if n % m != 0:
        return -1
    c = 0
    i = 0
    while n % m == 0:
        n = int(n / m)
        m = m * m
        c += int(math.pow(2, i))
        i += 1
    if n == 1:
        return c
    if n < k:
        return -1
    else:
        re = check(n, k, k)
        if re == -1:
            return -1
        else:
            return c + re


def isPrime(n):
    # Corner cases
    if n <= 1:
        return False
    if n <= 3:
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True


def main():
    t = int(input())
    my_input = []
    my_output = []
    for i in range(t):
        line = input()
        my_input.append(line)

    for line in my_input:
        line = line.split(" ")
        n = int(line[0])
        m = int(line[1])
        if n == 1 or m == 1 or n == 0 or m == 0:
            my_output.append(0)
            continue
        r = check(n, m, m)
        # print(r)
        if isPrime(r):
            my_output.append(1)
        else:
            my_output.append(0)

    for x in my_output:
        if x == 1:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
