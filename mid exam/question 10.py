def defensive_fulfillment(a,b):
    if type(a) == type(b):
        answer = a + b
    else:
        answer = None
    return answer

def main():
    print(defensive_fulfillment([1,2], [3,4]))
    print(defensive_fulfillment([1,2], "3,4"))


if __name__ == "__main__":
    main()
