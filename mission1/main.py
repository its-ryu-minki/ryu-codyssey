log_file_path = 'mission_computer_main.log'
problem_log_path = 'problem.md'

try:
    with open(log_file_path, 'r') as file:
        lines = file.readlines()

    header = lines[0].strip()
    data_lines = lines[1:]
    data_lines.reverse()

    print(header)
    for line in data_lines:
        print(line.strip())

    # 문제 로그 필터링
    problem_logs = [line.strip() for line in data_lines if 'Oxygen tank' in line]

    # Markdown 파일로 저장
    with open(problem_log_path, 'w') as pfile:
        pfile.write("Problem Logs\n\n")
        pfile.write("| Timestamp | Event | Message |\n")
        pfile.write("|---|---|---|\n")
        for log in problem_logs:
            parts = log.split(',', 2)  # timestamp, event, message 분리
            if len(parts) == 3:
                timestamp, event, message = parts
                pfile.write(f"| {timestamp.strip()} | {event.strip()} | {message.strip()} |\n")

    print(f"\n[!] 문제 로그 Markdown 파일로 저장 완료: {problem_log_path}")

except FileNotFoundError:
    print(f"'{log_file_path}' 없음")
except PermissionError:
    print("거부됨")
except Exception as e:
    print(f"예상치 못한 에러: {e}")
