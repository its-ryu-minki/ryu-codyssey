import random
import time


class DummySensor:
    def __init__(self):
        self.env_values = {
            'mars_base_internal_temperature': None,
            'mars_base_external_temperature': None,
            'mars_base_internal_humidity': None,
            'mars_base_external_illuminance': None,
            'mars_base_internal_co2': None,
            'mars_base_internal_oxygen': None
        }

    def set_env(self):
        self.env_values['mars_base_internal_temperature'] = random.uniform(18, 30)
        self.env_values['mars_base_external_temperature'] = random.uniform(0, 21)
        self.env_values['mars_base_internal_humidity'] = random.uniform(50, 60)
        self.env_values['mars_base_external_illuminance'] = random.uniform(500, 715)
        self.env_values['mars_base_internal_co2'] = random.uniform(0.02, 0.1)
        self.env_values['mars_base_internal_oxygen'] = random.uniform(4, 7)

    def get_env(self):
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        log_line = [now]
        for key in self.env_values:
            log_line.append(str(round(self.env_values[key], 3)))

        try:
            with open("env_log.txt", "a") as log_file:
                log_file.write(', '.join(log_line) + "\n")
        except Exception as e:
            print("로그 저장 오류:", e)

        return self.env_values


ds = DummySensor()
ds.set_env()
env_data = ds.get_env()
print(env_data)
