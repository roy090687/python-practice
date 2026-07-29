# {
#   "T1": {"status": "PASS", "logs": ["connecting", "sending request"]},
#   "T2": {"status": "FAILED", "logs": ["connecting", "timeout"]}
# }

from pathlib import Path

def get_result_log_status(filename):
    with open(filename) as f:
        lines = f.readlines()

    result = {}
    res = {}
    logs = []
    tc_name = None

    for line in lines:
        line = line.strip()
        if line.startswith('[RUN]'):
            tc_name = line.split(" ")[1]
        if line.startswith('log'):
            logs.append(line.split(":")[1].strip())
        if line in ('[PASS]', '[FAILED]', '[SKIPPED]'):
            if tc_name:
                status = line.strip("[]")
                res["status"] = status
                res["logs"] = logs
                result[tc_name] = res
                res = {}
                logs = []
                tc_name = None
    return result

base_dir = Path(__file__).parent
filepath = base_dir.parent.parent / "inputdata" / "log3.txt"

output = get_result_log_status(filepath)
print(output)




