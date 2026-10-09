# Question 5

def is_prime(n):
    found = False

    for factor in range(2, n):
        if n % factor == 0:
            found = True

    return found

def main():
    n = int(input("Enter an integer: "))

    if n < 2:
        print(n, "is not prime.")
    else:
        found = is_prime(n)

        if found:
            print(n, "is not prime.")
        else:
            print(n, "is prime.")

main()
