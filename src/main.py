# ERICA v2.0 - Main Application Entry Point

from src.hrm.model import HRM
from src.computer_vision.core import ComputerVision

def main():
    """
    Main function to run ERICA v2.0.
    """
    print("Initializing ERICA v2.0...")
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
