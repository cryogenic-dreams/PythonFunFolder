"""
This program is inspired by the Eratostenes' sieve.
"""
def sieve (number):
    """
    @type number: integer
    @param number: number > 0
    @rtype: list
    @return: list of the primes until number.
    """
    i = 2
    cont = 0
    primes = []
    while i <= number:
        while cont < len(primes) and i % primes[cont] != 0:
            cont = cont + 1
        if cont == len(primes):
            primes.append(i)
        cont = 0
        i = i + 1
    return primes
    
answer = "y"
while answer in ["y", "Y"]:
    number = int(raw_input("Give me a number: "))
    while number < 0:
        print "The number must be positive."
        number = int(raw_input("Give me a number: "))
    list1 = sieve(number)
    list2 = []
    while number != 1:
        i = 0
        while number % list1[i] != 0:
            i = i + 1
        list2.append(list1[i])
        number = number / list1[i]
    print "Prime factors: ", list2
    answer = raw_input("Repeat? (y/n): ")
        
