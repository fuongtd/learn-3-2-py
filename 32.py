import os
import random
import string
import datetime

random_chars = ''.join(random.choices(string.ascii_lowercase, k=2))
random_numbers = ''.join(random.choices(string.digits, k=4))
file_name = f"{random_chars}{random_numbers}.py"

code_directory = "./code"

if not os.path.exists(code_directory):
    os.makedirs(code_directory)

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

text_to_write = f"Updated on {current_time}."

file_path = os.path.join(code_directory, file_name)

with open(file_path, "a") as file:
    file.write(text_to_write + "\n")
