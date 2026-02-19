from datetime import datetime

file_path = "C:\\Users\dparh\\Documents\\GitHub\\Homework--Dmytro-Parkhomenko\\homework_module5\\logs_file.txt"

def parse_log_line(line: str) -> dict:
    log_components = {}
    levels = {"WARNING", "DEBUG", "INFO", "ERROR"}

    formatted_line = line.split()

    for component in formatted_line:
        #adding date to a dictionary
        log_components['date'] = formatted_line[0]
        #adding level to a dictionary
        if component in levels:
            log_components['level'] = formatted_line[2]
        
        log_components['time'] = formatted_line[1]
        log_components['msg'] = " ".join(formatted_line[3:])
        
    return log_components

def load_logs(file_path: str) -> list:

    with open(file_path, "r") as file:
        logs = []

        for line in file:
            formatted_log = parse_log_line(line)
            logs.append(formatted_log)
    
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log and log.get("level") == level.upper()]

def count_logs_by_level(logs: list) -> dict:
    logs_count = {}
    

    for entry in logs:
        level = entry.get('level')

        if level in logs_count:
            logs_count['level'] += 1
        else:
            logs_count['level'] = 1
    
    return logs_count

def display_log_counts(count: dict):
    print(f"ERROR | {count_logs_by_level(all_logs)}")
    print(f"WARNING | {count_logs_by_level()}")

all_logs = load_logs(file_path)
errors_messages = filter_logs_by_level(all_logs, "WARNING")
counted_logs = count_logs_by_level(all_logs)

print(load_logs(file_path))
print(f"{errors_messages}")
print(f"{counted_logs}")