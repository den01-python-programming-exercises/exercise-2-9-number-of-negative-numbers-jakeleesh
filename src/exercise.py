def main():
    #write your code below this line
    count = 0
    while True:
        num = int(input("Give a number:"))
        if (num < 0):
            count += 1
        elif (num == 0):
            break
    print("Number of negative numbers: " + str(count))

if __name__ == '__main__':
    main()
