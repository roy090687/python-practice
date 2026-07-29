from pathlib import Path

class ProdExecution:

    def get_result_log_prod(self, filename):
        with open(filename) as f:
            lines = f.readlines()
        result = {}
        for line in lines:
            line = line.strip()
            if "[" in line and "]" in line:
                log_status = line.split("]")[0].split("[")[1].strip()
                if log_status in ('INFO', 'ERROR', 'WARN'):
                    result[log_status] = result.get(log_status, 0) + 1
        return result

base_dir = Path(__file__).parent
filepath = base_dir.parent.parent / "inputdata" / "log4.txt"

prod_log = ProdExecution()
log_status_count = prod_log.get_result_log_prod(filepath)
for key, count in log_status_count.items():
    print(f"{key} : {count}")









