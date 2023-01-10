import os

os.environ["FOOD"]="SPINACH"

def food():
    x = os.environ["FOOD"]
    print (x)
    return x

import os
name = 'my_name'
value = 'my_value'


if __name__ == "__main__":
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'{name}={value}', file=fh)
