with open('mission_computer_main.log', 'r') as file:
    lines = file.readlines()

log_list = []
for line in lines:
    parts = line.strip().split(',', 1)
    if len(parts) == 2:
        date_time = parts[0].strip()
        log_content = parts[1].strip()
        log_list.append([date_time, log_content])

print("Original Log List:")
for item in log_list:
    print(item)

log_list.sort(reverse=True, key=lambda x: x[0])

print("\nSorted Log List (Descending):")
for item in log_list:
    print(item)

log_dict = {}
for item in log_list:
    log_dict[item[0]] = item[1]

search_str = input("\n검색할 문자열을 입력: ")

print(f"\n[검색 결과: '{search_str}' 포함 로그]")
found = False
for key in log_dict:
    if search_str in log_dict[key]:
        print(f"{key}: {log_dict[key]}")
        found = True

if not found:
    print("해당 문자열이 포함된 로그가 없습니다.")

with open('mission_computer_main.json', 'w') as json_file:
    json_file.write('{\n')
    count = 0
    total = len(log_dict)
    for key in log_dict:
        json_line = f'  "{key}": "{log_dict[key]}"'
        count += 1
        if count != total:
            json_line += ','
        json_line += '\n'
        json_file.write(json_line)
    json_file.write('}\n')

print("\nJSON 파일 저장 완료: mission_computer_main.json")
