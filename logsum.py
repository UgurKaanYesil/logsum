import argparse

parser = argparse.ArgumentParser()
parser.add_argument("logFile", help="file name to be read")

args = parser.parse_args()

def is_valid_line(line):
    parts = line.split(maxsplit=3)
    if len(parts) != 4:
        return False

    date_parts = parts[0].split("-")
    if len(date_parts) != 3 or not all(part.isdigit() for part in date_parts):
        return False

    time_parts = parts[1].split(":")
    if len(time_parts) != 3 or not all(part.isdigit() for part in time_parts):
        return False

    if parts[2] not in {"ERROR", "WARN", "INFO"}:
        return False

    return True


error_num = 0
info_num = 0
warn_num = 0
mismatch_num = 0

error_messages = {}

with open(args.logFile, "r", encoding="utf-8") as f:

    for line in f:
        line = line.strip()

        if not is_valid_line(line):
            mismatch_num += 1
            continue

        parts = line.split(maxsplit=3)
        log_type = parts[2]

        if log_type == "ERROR":
            error_num += 1

            message = parts[3]

            if message in error_messages:
                error_messages[message] += 1
            else:
                error_messages[message] = 1

        elif log_type == "INFO":
            info_num += 1

        elif log_type == "WARN":
            warn_num += 1

print(f"Total number of errors: {error_num}")
print(f"Total number of info: {info_num}")
print(f"Total number of warn: {warn_num}")
print(f"Total number of mismatch log: {mismatch_num}")

sorted_errors = sorted(
    error_messages.items(),
    key=lambda item: item[1],
    reverse=True
)

print("\nTop 5 error messages:")

for message, count in sorted_errors[:5]:
    print(f"{message} : {count}")