# Завдання 1
# Розроблення програми з таймером, що підраховує
# час. Використати JSON для збереження стану таймера
# (наприклад, поточний час) у файлі. При перезапуску
# програми відновити час збереженого стану
import json
import time


class Timer:
    def __init__(self, filename='timer_state.json'):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False
        self.filename = filename
        self.load_state()

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time
            print("Таймер запущено.")

    def stop(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False
            self.save_state()
            print("Таймер зупинено.")

    def reset(self):
        self.elapsed_time = 0
        self.start_time = time.time()
        self.save_state()
        print("Таймер скинуто.")

    def save_state(self):
        state = {
            'start_time': self.start_time,
            'elapsed_time': self.elapsed_time,
        }
        with open(self.filename, 'w') as file:
            json.dump(state, file)
        print("Стан таймера збережено.")

    def load_state(self):
        try:
            with open(self.filename, 'r') as file:
                state = json.load(file)
                self.start_time = state['start_time']
                self.elapsed_time = state['elapsed_time']
                if self.running:
                    self.start_time = time.time() - self.elapsed_time
                    self.start()
                print("Стан таймера завантажено.")
        except (FileNotFoundError, json.JSONDecodeError):
            print("Файл стану не знайдено. Створення нового таймера.")
            self.reset()

    def get_time(self):
        if self.running:
            return time.time() - self.start_time
        return self.elapsed_time

    def __str__(self):
        current_time = self.get_time()
        return time.strftime("%H:%M:%S", time.gmtime(current_time))


timer = Timer()
timer.start()
time.sleep(5)
print(str(timer))
timer.stop()
