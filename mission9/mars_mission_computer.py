import time
import threading
import multiprocessing
import os
import platform
import psutil

class MissionComputer:
    def __init__(self, name=""):
        self.name = name
        self.running = True

    def get_mission_computer_info(self):
        while self.running:
            try:
                os_name = platform.system()
                os_version = platform.version()
                cpu_type = platform.processor()
                cpu_cores = os.cpu_count()
                mem_size = round(psutil.virtual_memory().total / (1024 ** 3), 2)

                print(f"\n[{self.name} 시스템 정보]")
                print("{")
                print(f'  "OS": "{os_name}",')
                print(f'  "OS Version": "{os_version}",')
                print(f'  "CPU Type": "{cpu_type}",')
                print(f'  "CPU Cores": {cpu_cores},')
                print(f'  "Memory Size (GB)": {mem_size}')
                print("}")
            except Exception as e:
                print(f"[{self.name} 시스템 정보 오류] {e}")
            time.sleep(20)

    def get_mission_computer_load(self):
        while self.running:
            try:
                cpu_usage = psutil.cpu_percent(interval=1)
                mem_usage = psutil.virtual_memory().percent

                print(f"\n[{self.name} 시스템 부하]")
                print("{")
                print(f'  "CPU Usage (%)": {cpu_usage},')
                print(f'  "Memory Usage (%)": {mem_usage}')
                print("}")
            except Exception as e:
                print(f"[{self.name} 시스템 부하 오류] {e}")
            time.sleep(20)

    def get_sensor_data(self):
        counter = 0
        total_temp = 0
        try:
            while self.running:
                temp = round(20 + 10 * (time.time() % 1), 2)
                humid = round(50 + 10 * (time.time() % 1), 2)
                print(f"\n[{self.name} 센서 데이터]")
                print("{")
                print(f'  "Temperature": {temp},')
                print(f'  "Humidity": {humid}')
                print("}")
                total_temp += temp
                counter += 1

                if counter == 60:
                    avg = round(total_temp / 60, 2)
                    print(f"[{self.name} 센서 5분 평균 온도]: {avg}")
                    counter = 0
                    total_temp = 0

                time.sleep(5)
        except Exception as e:
            print(f"[{self.name} 센서 오류] {e}")

def run_with_threads():
    comp = MissionComputer("Thread컴퓨터")
    t1 = threading.Thread(target=comp.get_mission_computer_info)
    t2 = threading.Thread(target=comp.get_mission_computer_load)
    t3 = threading.Thread(target=comp.get_sensor_data)

    t1.start()
    t2.start()
    t3.start()

    try:
        input("엔터를 누르면 쓰레드 실행 중지...\n")
        comp.running = False
        t1.join()
        t2.join()
        t3.join()
    except KeyboardInterrupt:
        comp.running = False


def process_info():
    MissionComputer("프로세스1").get_mission_computer_info()

def process_load():
    MissionComputer("프로세스2").get_mission_computer_load()

def process_sensor():
    MissionComputer("프로세스3").get_sensor_data()

def run_with_processes():
    p1 = multiprocessing.Process(target=process_info)
    p2 = multiprocessing.Process(target=process_load)
    p3 = multiprocessing.Process(target=process_sensor)

    p1.start()
    p2.start()
    p3.start()

    try:
        input("엔터를 누르면 프로세스 종료...\n")
        p1.terminate()
        p2.terminate()
        p3.terminate()
    except KeyboardInterrupt:
        p1.terminate()
        p2.terminate()
        p3.terminate()


if __name__ == "__main__":
    mode = input("실행 모드를 선택하세요 (1: Thread / 2: Process): ").strip()

    if mode == "1":
        run_with_threads()
    elif mode == "2":
        run_with_processes()
    else:
        print("잘못된 입력입니다.")
