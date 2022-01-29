def try_me(a,b):
    return a+b

if __name__ == "__main__":
    solution = try_me("1,2,3", " test")
    if solution == "1,2,3 test":
        print(solution)
    else:
        print("not today")
