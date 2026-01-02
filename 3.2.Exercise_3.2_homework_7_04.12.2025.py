def filter_logs(logs, filter_func):
    return [log for log in logs if filter_func(log)]

logs = [
    {"level": "INFO", "message": "Test started"},
    {"level": "ERROR", "message": "Login failed"},
    {"level": "WARNING", "message": "Timeout occurred"}
]

error_logs = filter_logs(logs, lambda log: log['level'] == 'ERROR')
print("Ошибки:", error_logs)
