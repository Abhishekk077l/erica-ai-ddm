# ERICA v2.0 - Main Application Entry Point

import subprocess
import os
from src.hrm.model import HRM
from src.computer_vision.core import ComputerVision

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

    print("ERICA v2.0 is running. Type 'exit' to quit.")

    while True:
        try:
            user_input = input("> ")
            if user_input.lower() == 'exit':
                break

            if "capture screen" in user_input.lower():
                print("Capturing screen...")
                frame = cv.capture_screen()
                print(f"Screen captured. Frame shape: {frame.shape}")
            else:
                response = hrm.query(user_input)
                print(response)
        except (KeyboardInterrupt, EOFError):
            break

    print("Shutting down ERICA v2.0.")

if __name__ == "__main__":
    main()
