"""
UI components for the Pomodoro Timer application.
This file is a compatibility layer that imports from the ui package.
"""
# Re-export the classes from the ui package
from pomodoro.ui.main_window import PomodoroTimer
from pomodoro.ui.config_dialog import PomodoroConfigDialog

# Export the same classes for backward compatibility
__all__ = ['PomodoroTimer', 'PomodoroConfigDialog']
