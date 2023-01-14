import os

os.environ["FOOD"]="SPINACH"

def meal(my_drink):
    """Take as input a beverage from the user"""
    my_env_var = os.environ["FOOD"]
    user_input = my_drink
    my_data = {"env_var": my_env_var,
               "user_input": user_input}
    return my_data

if __name__ == "__main__":
    result = meal("Sweet Tea")
    print(f"env_var={result['env_var']}")
    print(f"user_input={result['user_input']}")
