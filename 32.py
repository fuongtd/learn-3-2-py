import datetime
import random
import string

# Tạo chuỗi ngẫu nhiên xx
random_chars = ''.join(random.choices(string.ascii_letters, k=2))

# Tạo số ngẫu nhiên yyyy
random_numbers = random.randint(1000, 9999)

# Tạo tên tệp tin xxyyyy.py
file_name = f"{random_chars}{random_numbers}.py"

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
text_to_write = f"Updated on {current_time}."

# Mở tệp tin mới và ghi nội dung vào tệp
with open(file_name, "a") as file:
    file.write(text_to_write + "\n")
