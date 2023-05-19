from subprocess import Popen
import time

def run_flask():
    Popen(["python", "app.py"])

def run_streamlit():
    Popen(["streamlit", "run", "streamlit_app.py"])

if __name__ == "__main__":
    run_flask()
    time.sleep(3)  # Wait for Flask server to start
    run_streamlit()
