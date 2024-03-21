from flask import Flask, render_template
import serial

app = Flask(__name__)
arduino_port = '/dev/ttyACM0' #Arduinoのポート
baud_rate = 9600 #シリアル通信のボーレート

ser = serial.Serial(arduino_port, baud_rate)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_sound_value', methods=['GET'])
def get_sound_value():
    try:
        sound_value = ser.readline().decode('utf-8').strip()
        return sound_value
    except Exception as e:
        print("Error:", e)
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
