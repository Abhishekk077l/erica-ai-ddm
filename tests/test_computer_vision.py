# Tests for the Computer Vision module

import unittest
from unittest.mock import patch, MagicMock
import numpy as np
import sys
from PIL import Image

# Mock pyautogui before it is imported by any other module
sys.modules['pyautogui'] = MagicMock()

from src.computer_vision.core import ComputerVision


class TestComputerVision(unittest.TestCase):

    def setUp(self):
        self.cv = ComputerVision()

    def test_capture_screen(self):
        """
        Tests the screen capture functionality with pyautogui mocked.
        """
        # Create a dummy image for the mock to return
        dummy_image = Image.new('RGB', (100, 100), color = 'red')
        sys.modules['pyautogui'].screenshot.return_value = dummy_image

        frame = self.cv.capture_screen()
        self.assertIsInstance(frame, np.ndarray)
        self.assertTrue(len(frame.shape) == 3) # Height, Width, Channels
        self.assertEqual(frame.shape[0], 100)
        self.assertEqual(frame.shape[1], 100)
        self.assertTrue(frame.shape[2] == 3) # BGR channels
        sys.modules['pyautogui'].screenshot.assert_called_once()


if __name__ == '__main__':
    unittest.main()
