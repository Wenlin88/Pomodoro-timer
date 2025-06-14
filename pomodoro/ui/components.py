"""
Shared UI components for the Pomodoro Timer application.
"""
from PyQt6.QtWidgets import QLabel, QPushButton
from PyQt6.QtCore import Qt

class TimerLabel(QLabel):
    """A label for displaying the timer."""
    
    def __init__(self, text="00:00", parent=None):
        """Initialize the timer label."""
        super().__init__(text, parent)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("font-size: 48px;")

class FocusLabel(QLabel):
    """A label for displaying the focus text."""
    
    def __init__(self, text="", parent=None):
        """Initialize the focus label."""
        super().__init__(text, parent)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setWordWrap(True)
        self.setStyleSheet("font-size: 14px;")
        
class PomodoroButton(QPushButton):
    """A styled button for the Pomodoro Timer."""
    
    def __init__(self, text, parent=None):
        """Initialize the button with text."""
        super().__init__(text, parent)
        # Custom styling can be applied here
