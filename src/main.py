# ERICA v2.0 - Main Application Entry Point

import subprocess
import os
import time
from src.hrm.model import HRM
from src.computer_vision.core import ComputerVision
from src.orchestra.core import Orchestra

def install_voice_dependencies():
    """
    Installs the Node.js dependencies for the voice processing module.
    """
    script_path = "src/voice_processing/install_node_deps.sh"
    if not os.path.exists("src/voice_processing/node_modules"):
        print("Voice processing dependencies not found. Installing...")
        try:
            subprocess.run(["bash", script_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error installing voice processing dependencies: {e}")
            exit(1)
        except FileNotFoundError:
            print(f"Error: The script at {script_path} was not found.")
            exit(1)

def main():
    """
    Main function to run ERICA v2.0.
    """
    print("Initializing ERICA v2.0...")

    install_voice_dependencies()

    hrm = HRM()
    cv = ComputerVision()
    orchestra = Orchestra()
    orchestra.start()

    print("ERICA v2.0 is running. Type 'exit' to quit.")
    print("You can add tasks to the queue by typing 'task: <task description>'.")

    try:
        while True:
            user_input = input("> ")
            if user_input.lower() == 'exit':
                break

            if user_input.lower().startswith("task:"):
                task_description = user_input[5:].strip()
                # This is a dummy task. In a real application, we would
                # parse the task description and create a real task.
                def dummy_task():
                    print(f"Starting task: {task_description}")
                    time.sleep(2)
                    print(f"Finished task: {task_description}")
                orchestra.add_task(dummy_task)
                print(f"Task '{task_description}' added to the queue.")
            elif "capture screen" in user_input.lower():
                print("Capturing screen...")
                frame = cv.capture_screen()
                print(f"Screen captured. Frame shape: {frame.shape}")
            else:
                response = hrm.query(user_input)
                print(response)

    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        orchestra.stop()
        print("Shutting down ERICA v2.0.")

if __name__ == "__main__":
    main()
