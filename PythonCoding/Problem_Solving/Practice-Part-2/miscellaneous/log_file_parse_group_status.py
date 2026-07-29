# output:
# {
#   "PASS": ["T1", "T3"],
#   "FAILED": ["T2"],
#   "SKIPPED": ["T4"]
# }

from pathlib import Path

def get_result_group_status(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    result = {}
    tc_name = None
    for line in lines:
        line = line.strip()
        if line.startswith("[RUN]"):
            tc_name = line.split(" ")[1]
        if line in ('[PASS]', '[FAILED]', '[SKIPPED]'):
            if tc_name:
                status = line.strip("[]")
                if status not in result:
                    result[status] = []
                result[status].append(tc_name)
    return result

base_dir = Path(__file__).parent  # current script folder
print("PATH", base_dir)
print(base_dir.parent)
filepath = base_dir.parent.parent / "inputdata" / "log2.txt"

output = get_result_group_status(filepath)
print(output)
