# Core Computer Vision functionality

import pyautogui
import numpy as np
import cv2

class ComputerVision:
    """
    Provides core computer vision capabilities, such as screen capture and analysis.
    """

    def capture_screen(self) -> np.ndarray:
        """
        Captures the entire screen and returns it as a numpy array in BGR format.
        """
        screenshot = pyautogui.screenshot()
        # Convert the PIL image to a numpy array
        frame = np.array(screenshot)
        # Convert RGB to BGR
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        return frame
