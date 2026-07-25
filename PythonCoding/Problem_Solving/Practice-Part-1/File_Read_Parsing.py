def parse_file_results(filename):
    results = []
    with open(filename, 'r') as f:
        lines = f.readlines()

    current = {}

    for line in lines:
        line = line.strip()
        if line.startswith("TEST"):
            current["test"] = line.split(":")[1].strip()
        elif line.startswith("STATUS"):
            current["status"] = line.split(":")[1].strip()
        elif line.startswith("DATA"):
            current["data"] = line.split(":")[1].strip()
            print(current)
            results.append(current)
            current = {}
    return results

parsed = parse_file_results("C:/Users/SNEHASISH/OneDrive/Desktop/results.txt")

print("================ Result ================")
for entry in parsed:
    print(f"Test Name  : {entry['test']}")
    print(f"Status  : {entry['status']}")
    print(f"Data  : {entry['data']}")
    print("------------------------------------")





