import datetime

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

text_to_write = f"Updated on {current_time}."

with open("system.py", "w") as file:
    file.write(text_to_write)
