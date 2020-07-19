from functools import reduce

def find_happy_number(num):
    numbers = []

    while True:
        sqr_sum = reduce(lambda x, y: x + y, [pow(int(x), 2) for x in str(num)])
        if sqr_sum == 1:
            return True
        elif sqr_sum in numbers:
            return False
        else:
            numbers.append(sqr_sum)
            num = sqr_sum
        
    return False


def main():
  print(find_happy_number(23))
  print(find_happy_number(12))


main()