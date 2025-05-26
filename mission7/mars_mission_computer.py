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
        except:
            pass

        return self.env_values


class MissionComputer:
    def __init__(self):
        self.env_values = {
            'mars_base_internal_temperature': 0.0,
            'mars_base_external_temperature': 0.0,
            'mars_base_internal_humidity': 0.0,
            'mars_base_external_illuminance': 0.0,
            'mars_base_internal_co2': 0.0,
            'mars_base_internal_oxygen': 0.0
        }
        self.history = {key: [] for key in self.env_values}
        self.ds = DummySensor()

    def update_env_values(self):
        self.ds.set_env()
        current = self.ds.get_env()

        for key in self.env_values:
            value = current[key]
            if value is not None:
                self.env_values[key] = value
                self.history[key].append(value)
                if len(self.history[key]) > 60:
                    self.history[key].pop(0)

    def print_env_values(self):
        print("{")
        for key in self.env_values:
            print(f'  "{key}": {round(self.env_values[key], 3)}')
        print("}")

    # Bonus
    def print_average(self):
        print("\n=== Averages ===")
        for key in self.history:
            values = self.history[key]
            if values:
                total = 0.0
                for v in values:
                    total += v
                avg = total / len(values)
                print(f"{key}: {round(avg, 3)}")
        print("==========================\n")

    def get_sensor_data(self):
        interval = 5
        next_average_time = time.time() + 300  # Bonus

        try:
            while True:
                loop_start = time.time()

                self.update_env_values()
                self.print_env_values()

                elapsed = time.time()

                if elapsed >= next_average_time:
                    self.print_average()  # Bonus
                    next_average_time += 300

                sleep_time = max(0, interval - (time.time() - loop_start))
                time.sleep(sleep_time)

        # Bonus
        except KeyboardInterrupt:
            print("System stopped....")


if __name__ == "__main__":
    RunComputer = MissionComputer()
    RunComputer.get_sensor_data()
