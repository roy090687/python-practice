# Log Analyzer: Count error codes and show top 3
from pathlib import Path

def getTopThreeLogErrorCounts(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    error_count = {}
    for line in lines:
        line = line.strip()
        words = line.split()
        for word in words:
            if word.startswith("ERROR"):
                error_code = word
                error_count[error_code] = error_count.get(error_code, 0) + 1

    print(error_count.items())  # dict_items([('ERROR404', 5), ('ERROR500', 4), ('ERROR403', 3), ('ERROR401', 2), ('ERROR502', 2), ('ERROR408', 1)])
    sorted_items = sorted(error_count.items(), key=lambda x: x[1], reverse=True)
    print("Sorting method: ", sorted_items)

    # manual for loop [alternative way]
    items = list(error_count.items())  # Convert to List of Tuples first
    print(items)
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if items[i][1] < items[j][1]:
                items[i], items[j] = items[j], items[i]
    print("Manual Sorting: ", items)

    print("------- Top 3 Error With Counts --------")
    for code, count in sorted_items[:3]:
        print(code, ":", count)


base_dir = Path(__file__).parent
filepath = base_dir.parent.parent / "inputdata" / "logfile1.txt"
getTopThreeLogErrorCounts(filepath)
