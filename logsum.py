error_num = 0

with open("app.log", "r", encoding="utf-8") as f:
    for line in f:
        if "ERROR" in line:
            error_num += 1

print(f"Total number of errors: {error_num}")