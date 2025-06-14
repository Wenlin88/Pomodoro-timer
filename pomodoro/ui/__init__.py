"""
UI components for the Pomodoro Timer application.
"""

# Import and re-export the components
from .main_window import PomodoroTimer
from .config_dialog import PomodoroConfigDialog

# Define what's available when importing from this package
__all__ = ['PomodoroTimer', 'PomodoroConfigDialog']
