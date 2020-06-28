'''
Find the absolute minimum difference and the pairs of numbers that have the same
absolute minimum difference. Print the pairs in sorted order.
'''

def main():
    num = list(map(int, input('Enter the elements:\n').strip().split()))
    num.sort()
    print(num)
    abs_min = num[1] - num[0]
    pairs = [(num[0], num[1])]
    for i in range(2, len(num)):
        current_min = num[i] - num[i-1]
        if abs_min >= current_min:
            if abs_min > current_min:
                pairs.pop()
            pairs.append((num[i-1], num[i]))
            abs_min = current_min
    print(f"\nThe absolute minimum difference is {abs_min}.")
    print("And the pair(s) with the difference is(are):")
    for pair in pairs:
        print(pair)

if __name__ == '__main__':
    main()