def add10(number):
    return number + 10

if __name__ == "__main__":
    result_iterator = map(add10, range(5))
    for item in result_iterator:
        print(item)