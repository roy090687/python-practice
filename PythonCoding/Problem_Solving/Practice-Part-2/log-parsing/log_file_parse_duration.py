# output
# {
#   "T1": {"status": "PASS", "duration": "5m"},
#   "T2": {"status": "FAILED", "duration": "5m"}
# }
from datetime import datetime

def get_result_duration(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    res = {}
    result = {}
    tc_name = None
    start_time = None
    finish_time = None

    for line in lines:
        line = line.strip()
        if line.startswith('[RUN]'):
            tc_name = line.split(" ")[1]
        if line.startswith('Started'):
            start_time = line.split(": ")[1].strip()
            start_time = datetime.strptime(start_time, "%H:%M")
        if line.startswith('Finished'):
            finish_time = line.split(": ")[1].strip()
            finish_time = datetime.strptime(finish_time, "%H:%M")
        if line in ('[PASS]', '[FAILED]', '[SKIPPED]'):
            if tc_name:
                diff = abs(finish_time - start_time)
                minutes = diff.total_seconds()/60
                duration = f"{int(minutes)}m"
                res["status"] = line.strip("[]")
                res["duration"] = duration
                result[tc_name] = res
                res = {}
                tc_name = None
    return result

filepath = "D:\\Udemy Python APIAutomation - RahulShetty\\PythonPracticeAutomation\\PythonCoding\\Problem_Solving\\inputdata\\log1.txt"
output = get_result_duration(filepath)
print(output)
