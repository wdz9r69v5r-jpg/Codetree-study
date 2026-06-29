n = int(input())

def print_n_rect(N):
    num = 0
    for _ in range(N):
        for _ in range(N):
            num = num + 1
            if (num > 9):
                num = 1
            print(num, "", end = "")
        print()

print_n_rect(n)