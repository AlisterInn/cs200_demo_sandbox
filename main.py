def func1():
    lst = []
    print('Enter numbers one at a time. Enter 0 to stop.')
    x = int(input('num:'))
    while x != 0:
        lst.append(x)
        x = int(input('num:'))
    return lst

def func2(data):
    print('Here is the data:')
    print(data)

    choice = ''
    while True:
        choice = input('Select an option. 1-sum  2-min  3-max  4-quit: ')
        if choice == '1':
            print('The sum is',sum(data))
        elif choice == '2':
            print('Min value:', min(data), '- at index:', data.index(min(data)))
        elif choice == '3':
            print('Max value:', max(data), '- at index:', data.index(max(data)))
        elif choice == '4':
            print('Goodbye')
            return

def main():
    print("Hello, World!")
    data = func1()
    func2(data)

if __name__ == "__main__":
    main()