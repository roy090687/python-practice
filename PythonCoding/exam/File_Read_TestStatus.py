#output data:
#{'T1':{status: 'PASS'}, 'T2':{status: 'FAIL'}, 'T4':{status: 'SKIP'}...}

def get_result(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    res = {}
    result = {}
    tc_name = None
    for line in lines:
        line = line.strip()
        if line.startswith('[RUN]'):
            tc_name = line.split(" ")[1]
        if line in ('[PASS]', '[FAILED]', '[SKIPPED]'):
            if tc_name:
                res['status'] = line.strip("[]")
                result[tc_name] = res
                tc_name = None
                res = {}

    return result

output = get_result('run.txt')
print(output)

