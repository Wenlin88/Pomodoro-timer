"""
Notes integration module for the Pomodoro Timer application.
Handles integration with Obsidian and other note-taking systems.
"""
import webbrowser
import datetime
import logging
import urllib.parse

logger = logging.getLogger(__name__)

class NotesManager:
    """Manager for integrating with note-taking systems."""

    def __init__(self, config):
        """
        Initialize the notes manager.
        
        Args:
            config: Application configuration
        """
        self.config = config
        self.enabled = config.is_obsidian_enabled()
        self.obsidian_settings = config.get_obsidian_settings()

    def is_enabled(self):
        """Check if note-taking integration is enabled."""
        return self.enabled

    def open_daily_note(self):
        """Open today's daily note in Obsidian."""
        if not self.enabled:
            logger.info("Notes integration is disabled")
            return False
            
        try:
            vault = self.obsidian_settings["vault_name"]
            path = self.obsidian_settings["daily_notes_path"]
            date_str = datetime.datetime.now().strftime("%Y-%m-%d")
            
            # Construct the URL with proper encoding
            file_path = f"{path}/{date_str}"
            encoded_path = urllib.parse.quote(file_path)
            url = f"obsidian://open?vault={vault}&file={encoded_path}"
            
            webbrowser.open(url)
            logger.info(f"Opened daily note for {date_str}")
            return True
        except Exception as e:
            logger.error(f"Error opening daily note: {e}")
            return False

    def open_weekly_note(self):
        """Open this week's weekly note in Obsidian."""
        if not self.enabled:
            logger.info("Notes integration is disabled")
            return False
            
        try:
            vault = self.obsidian_settings["vault_name"]
            path = self.obsidian_settings["weekly_notes_path"]
            
            # Week note format: YYYY-WXX where XX is the week number
            week_str = datetime.datetime.now().strftime("%Y-W%V")
            
            # Construct the URL with proper encoding
            file_path = f"{path}/{week_str}"
            encoded_path = urllib.parse.quote(file_path)
            url = f"obsidian://open?vault={vault}&file={encoded_path}"
            
            webbrowser.open(url)
            logger.info(f"Opened weekly note for {week_str}")
            return True
        except Exception as e:
            logger.error(f"Error opening weekly note: {e}")
            return False
