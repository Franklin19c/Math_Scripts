def find_primes(n_min, n_max):
    result = []
    for a in range(int(n_min),int(n_max)+1):
        has_factor = False
        for b in range (2,a):
            if a % b == 0:
                has_factor = True
                break
        if not has_factor:
            print(a)
    print(result)

min = input("Min number(>1): ")
max = input("Max number: ")

find_primes(min,max)
