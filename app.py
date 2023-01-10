import os

os.environ["FOOD"]="SPINACH"

def food():
    x = os.environ["FOOD"]
    print (x)
    return x

if __name__ == "__main__":
    food()