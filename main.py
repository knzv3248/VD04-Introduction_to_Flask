from datetime import datetime
from  flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    cur_data = datetime.now().strftime("%Y-%m-%d")
    cur_time = datetime.now().strftime("%H:%M:%S")
    print(cur_data, cur_time)
    return  f"Сегодня {cur_data}. Текущее время - {cur_time}"


if __name__ == '__main__':
    app.run()