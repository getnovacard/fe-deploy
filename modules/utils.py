import os
import random
import string


def create_directory(directory):
    check_dir = os.path.isdir(directory)

    if not check_dir:
        os.makedirs(directory)
        print("created folder : ", directory)
    else:
        print(directory, "folder already exists.")


def get_random_string(length):
    source = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(source) for i in range(length)))
    
    return result_str
