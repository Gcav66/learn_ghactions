import os

os.environ["FOOD"]="SPINACH"

def food():
    x = os.environ["FOOD"]
    #print (x)
    return x

import os
name = 'my_name'
value = 'my_value'


if __name__ == "__main__":
    result = food()
    #print(f'::set-output name=FOOD::{result}')
    print("foo_bar=yellow")
