import os
import platform
import psutil

class MissionComputer:
    def __init__(self):
        self.info_fields = []
        self.load_fields = []
        self.load_settings()

    def load_settings(self):
        try:
            with open("setting.txt", "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("info:"):
                        self.info_fields = [i.strip() for i in line[5:].split(",") if i.strip()]
                    elif line.startswith("load:"):
                        self.load_fields = [i.strip() for i in line[5:].split(",") if i.strip()]
        except FileNotFoundError:
            print("[경고] setting.txt 파일이 없습니다. 모든 항목을 출력합니다.")
            self.info_fields = ["OS", "OS Version", "CPU Type", "CPU Cores", "Memory Size"]
            self.load_fields = ["CPU Usage", "Memory Usage"]

    def get_mission_computer_info(self):
        try:
            os_name = platform.system()
            os_version = platform.version()
            cpu_type = platform.processor()
            cpu_cores = os.cpu_count()
            mem_gb = round(psutil.virtual_memory().total / (1024 ** 3), 2)

            result = {}
            if "OS" in self.info_fields:
                result["OS"] = os_name
            if "OS Version" in self.info_fields:
                result["OS Version"] = os_version
            if "CPU Type" in self.info_fields:
                result["CPU Type"] = cpu_type
            if "CPU Cores" in self.info_fields:
                result["CPU Cores"] = cpu_cores
            if "Memory Size" in self.info_fields:
                result["Memory Size (GB)"] = mem_gb

            print("\n[시스템 정보]")
            print("{")
            for i, (key, value) in enumerate(result.items()):
                comma = "," if i < len(result) - 1 else ""
                print(f'  "{key}": "{value}"{comma}' if isinstance(value, str) else f'  "{key}": {value}{comma}')
            print("}")

        except Exception as e:
            print(f"[오류] 시스템 정보 수집 중 예외 발생: {e}")

    def get_mission_computer_load(self):
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            mem_usage = psutil.virtual_memory().percent

            result = {}
            if "CPU Usage" in self.load_fields:
                result["CPU Usage (%)"] = cpu_usage
            if "Memory Usage" in self.load_fields:
                result["Memory Usage (%)"] = mem_usage

            print("\n[시스템 부하]")
            print("{")
            for i, (key, value) in enumerate(result.items()):
                comma = "," if i < len(result) - 1 else ""
                print(f'  "{key}": {value}{comma}')
            print("}")

        except Exception as e:
            print(f"[오류] 시스템 부하 수집 중 예외 발생: {e}")


if __name__ == "__main__":
    runComputer = MissionComputer()
    runComputer.get_mission_computer_info()
    runComputer.get_mission_computer_load()
