import re

def parse_log_line(line):
    # Парсинг рядка логу у словник за компонентами: дата, час, рівень, повідомлення
    match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)', line)
    if match:
        return {
            'datetime': match.group(1),
            'level': match.group(2),
            'message': match.group(3)
        }
    return None

def load_logs(file_path):
    # Завантаження логів з файлу
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                log_entry = parse_log_line(line)
                if log_entry:
                    logs.append(log_entry)
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
    return logs

def filter_logs_by_level(logs, level):
    # Фільтрація логів за рівнем
    return [log for log in logs if log['level'].lower() == level.lower()]

def count_logs_by_level(logs):
    #Підрахунок записів за рівнем логування
    levels = ['INFO', 'DEBUG', 'ERROR', 'WARNING']
    counts = {level: 0 for level in levels}
    for log in logs:
        if log['level'] in counts:
            counts[log['level']] += 1
    return counts

def display_log_counts(counts):
    # Форматуємо та виводимо результати підрахунку у вигляді таблиці
    print(f"{'Рівень логування':<17} | {'Кількість':<9}")
    print("-" * 26)
    for level, count in counts.items():
        print(f"{level:<17} | {count:<9}")

def main():
    # Вказуємо шлях до файлу логів
    file_path = r"C:\Users\golos\OneDrive\Рабочий стол\Projects\First_repo\Тема-8\log_file.txt"
    
    log_level = None  # Рівень логування
    logs = load_logs(file_path)
    if not logs:
        print("Логи не були завантажені або файл порожній.")
        return

    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)

    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        if filtered_logs:
            print(f"\nДеталі логів для рівня '{log_level.upper()}':")
            for log in filtered_logs:
                print(f"{log['datetime']} - {log['message']}")
        else:
            print(f"Не знайдено жодного запису для рівня {log_level.upper()}.")

if __name__ == "__main__":
    main()
