import argparse

parser = argparse.ArgumentParser()
parser.add_argument("logFile", help="file name to be read")

args = parser.parse_args()

error_num = 0
info_num = 0
warn_num = 0
mismatch_num = 0

error_messages = {}

with open(args.logFile, "r", encoding="utf-8") as f:

    for line in f:

        if "ERROR" in line:
            error_num += 1

            message = line.split("ERROR")[1].strip()

            if message in error_messages:
                error_messages[message] += 1
            else:
                error_messages[message] = 1

        elif "INFO" in line:
            info_num += 1

        elif "WARN" in line:
            warn_num += 1

        else:
            mismatch_num += 1


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
    print(f"{message}: {count}")