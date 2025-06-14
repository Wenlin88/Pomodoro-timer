"""
Main entry point for the Pomodoro Timer application.
"""
import os
import sys
import logging
from PyQt6.QtWidgets import QApplication

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("pomodoro.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def main():
    """Main entry point for the application."""
    try:
        # Import components
        from pomodoro.config import Config
        from pomodoro.sound import SoundManager
        from pomodoro.notes import NotesManager
        from pomodoro.session import SessionManager
        from pomodoro.ui import PomodoroTimer
        
        # Create configuration
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
        config = Config(config_path)
        
        # Create managers
        sound_manager = SoundManager(config)
        notes_manager = NotesManager(config)
        session_manager = SessionManager()
        
        # Create and show the main window
        app = QApplication(sys.argv)
        app.setApplicationName("Pomodoro Timer")
        
        # Create icons directory if it doesn't exist
        icons_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons")
        if not os.path.exists(icons_dir):
            os.makedirs(icons_dir)
            
        # Create sounds directory if it doesn't exist
        sounds_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sounds")
        if not os.path.exists(sounds_dir):
            os.makedirs(sounds_dir)
        
        # Create the main window
        window = PomodoroTimer(config, sound_manager, notes_manager, session_manager)
        window.show()
        
        # Run the application
        sys.exit(app.exec())
    except Exception as e:
        logger.exception(f"Application error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
