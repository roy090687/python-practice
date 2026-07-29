import json

def read_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        return lines

def get_codes_from_log(file):
    all_lines = read_file(file)
    log_status = {}
    for line in all_lines:
        line = line.strip()
        words = line.split()
        code = words[2]
        if code not in log_status:
            log_status[code] = 1
        else:
            log_status[code] += 1

    return log_status

def get_messages_from_log(file):
    all_lines = read_file(file)
    messages = []
    for line in all_lines:
        line = line.strip()
        words = line.split()
        description = " ".join(words[3:])
        messages.append(description)
    return messages

print("------------ Total Lines -----------")
total_lines = len(read_file("log.txt"))
print(total_lines)

print("------------ Print Code Counts -----------")
codes = get_codes_from_log("log.txt")
for code, count in codes.items():
    print(code, ":", count)

print("------------ Print Messages -----------")
messages = get_messages_from_log("log.txt")
print(json.dumps(messages, indent=2))

