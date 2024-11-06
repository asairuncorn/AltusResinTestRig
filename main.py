from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from rp_controler import start_pump
import os
import threading
import time

# Initialize Flask and Flask-SocketIO
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_default_secret_key')  # Use environment variable or default key
socketio = SocketIO(app, cors_allowed_origins="*")


# Serve the HTML page
@app.route('/')
def index():
    return render_template('index_c5.html')


# Countdown function that runs in a background thread
def countdown_timer(button_id, duration=10):
    seconds = duration
    while seconds > 0:
        # Emit remaining time to the client
        socketio.emit('server_response', {'message': f'Time remaining for Button {button_id}: {seconds} seconds'} )
        print(f"Time remaining for Button {button_id}: {seconds} seconds")  # Print for server logging
        socketio.sleep(1)  # Non-blocking wait
        seconds -= 1

    # Notify client when time is up
    socketio.emit('server_response', {'message': f"Time's up for Button {button_id}!"})
    print(f"Time's up for Button {button_id}!")


# Event handler for button presses
@socketio.on('button_press')
def handle_button_press(data):

    print("Button press event received:", data)  # Log incoming data for debugging
    button_id = data.get("buttonId")
    print("Button press event received:", button_id)
    countdown_timer(button_id, duration=10)

    duration = data.get('duration', 10)  # Default to 10 seconds if not specified

@socketio.on('start_pump')
def handle_pump(data):
    pump_thread = threading.Thread(target=start_pump)
    pump_thread.start()
    print("Pump started:", data)  # Log incoming data for debugging
    button_id = data.get("buttonId")
    print("Button press event received:", button_id)

    countdown_timer(button_id, duration=10)

    duration = data.get('duration', 10)  # Default to 10 seconds if not specified

    # Start the countdown in a new thread
    #countdown_thread = threading.Thread(target=countdown_timer, args=(button_id, duration))
    #countdown_thread.start()


# Run the Flask application with SocketIO


# from flask import Flask, render_template
# from flask_socketio import SocketIO, emit
# import os
# import time
# import threading
#
#
# def countdown_timer(seconds=30):
#     while seconds > 0:
#         print(f"Time remaining: {seconds} seconds")
#         time.sleep(1)  # Wait for 1 second
#         seconds -= 1
#         return seconds
#
#     print("Time's up!")
#
#
# # Initialize Flask and Flask-SocketIO
# app = Flask(__name__)
# app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_default_secret_key')  # Use environment variable or default key
# socketio = SocketIO(app, cors_allowed_origins="*")
#
#
# # Serve the HTML page
# @app.route('/')
# def index():
#     return render_template('indec_c5.html')  # Ensure `index.html` is in the `templates` folder
#
#
# # Event handler for button presses
# @socketio.on('button_press')
# def handle_button_press(data):
#     print("Button press event received:", data)  # Log incoming data for debugging
#     button_id = data
#     seconds = 10
#     while seconds > 0:
#
#         emit('server_response', {'message': 'seconds'})
#         print(f"Time remaining: {seconds} seconds")
#         time.sleep(1)  # Wait for 1 second
#         seconds -= 1




    # # Determine response message based on button_id
    # if button_id.startswith("start_"):
    #     response_message = f"Started process for Bay {button_id.split('_')[1]}"
    # elif button_id.startswith("stop_"):
    #     response_message = f"Stopped process for Bay {button_id.split('_')[1]}"
    # elif button_id.startswith("setTime_"):
    #     response_message = f"Set time for Bay {button_id.split('_')[1]}"
    # else:
    #     response_message = "Unknown command received"
    #
    # print("Sending response:", response_message)  # Log the response being sent
    #emit('server_response', {'message': response_message})


# Run the server using socketio.run for WebSocket support
if __name__ == '__main__':
    print("Starting Flask-SocketIO server...")
    socketio.run(app, host='127.0.0.1', port=5005, debug=True)

# from flask import Flask, render_template
# from flask_socketio import SocketIO
# from flask_cors import CORS
#
# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes
# socketio = SocketIO(app, cors_allowed_origins="*")  # Enable CORS for Socket.IO
#
# # Route to serve your HTML page
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# # Handle button press events from the client
# @socketio.on('button_press')
# def handle_button_press(data):
#     block_id = data['block_id']
#     button_type = data['button_type']
#     print(f"Button pressed in Block {block_id}: {button_type}")
#
# if __name__ == '__main__':
#     socketio.run(app, debug=True, port=5555)
