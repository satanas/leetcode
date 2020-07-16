def fruits_into_baskets(fruits):
    basket = {}
    window_fruits = 0
    max_fruits = 0
    window_start = 0

    for window_end in range(0, len(fruits)):
        fruit = fruits[window_end]
        basket[fruit] = True
        window_fruits += 1

        if len(basket.keys()) <= 2:
            max_fruits = max(max_fruits, window_fruits)
        else:
            while len(basket.keys()) > 2:
                window_fruits -= 1
                del basket[fruits[window_start]]
                window_start += 1

            max_fruits = max(max_fruits, window_fruits)
    return max_fruits


if __name__ == "__main__":
    print(fruits_into_baskets(['A', 'B', 'C', 'A', 'C']))
    print(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']))