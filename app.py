import os

os.environ["FOOD"]="SPINACH"

def food():
    x = os.environ["FOOD"]
    return x

if __name__ == "__main__":
    result = food()
    print(f"foo_bar={result}")
