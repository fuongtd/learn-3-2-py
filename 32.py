import datetime
import random
import string

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

text_to_write = f"Updated on {current_time}."

random_chars = ''.join(random.choices(string.ascii_letters, k=2))
random_nums = ''.join(random.choices(string.digits, k=4))
file_name = f"{random_chars}{random_nums}.py"

with open(file_name, "a") as file:
    file.write(text_to_write + "\n")
