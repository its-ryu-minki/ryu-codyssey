import numpy as np

file1 = 'mars_base_main_parts-001.csv'
file2 = 'mars_base_main_parts-002.csv'
file3 = 'mars_base_main_parts-003.csv'

arr1 = np.genfromtxt(file1, delimiter=',', skip_header=1, usecols=1)
arr2 = np.genfromtxt(file2, delimiter=',', skip_header=1, usecols=1)
arr3 = np.genfromtxt(file3, delimiter=',', skip_header=1, usecols=1)

parts = np.concatenate((arr1, arr2, arr3))
mean_value = np.mean(parts)
weaker_parts = parts[parts < 50]

try:
    np.savetxt('parts_to_work_on.csv', weaker_parts.reshape(-1, 1), delimiter=',', fmt='%.2f')
except Exception as e:
    print('파일 저장 중 오류 발생:', e)

parts2 = np.loadtxt('parts_to_work_on.csv', delimiter=',')
parts3 = np.transpose(parts2)
print(parts3)