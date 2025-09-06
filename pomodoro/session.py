"""
Session management module for the Pomodoro Timer application.
Handles tracking and logging completed pomodoro sessions.
"""
import datetime
import os
import logging

logger = logging.getLogger(__name__)

class SessionManager:
    """Manager for tracking and logging pomodoro sessions."""
    
    def __init__(self, log_file=None):
        """
        Initialize the session manager.
        
        Args:
            log_file: Path to the session log file (defaults to pomodoro_sessions.log in current directory)
        """
        self.log_file = log_file or "pomodoro_sessions.log"
        
        # Create directory for log file if it doesn't exist
        log_dir = os.path.dirname(self.log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
            
        self.session_count = self._get_session_count()

    def _get_session_count(self):
        """
        Get the current session count from the log file.
        
        Returns:
            int: Number of sessions found in the log file
        """
        try:
            if not os.path.exists(self.log_file):
                return 0
                
            with open(self.log_file, "r") as file:
                return sum(1 for line in file if "Session" in line and "completed" in line)
        except Exception as e:
            logger.error(f"Error reading session count: {e}")
            return 0
    
    def log_session(self, focus_text="", success=True):
        """
        Log a completed pomodoro session.

        Args:
            focus_text: Text describing what was focused on during the session
            success: Whether the session was completed successfully

        Returns:
            int: Updated session count
        """
        try:
            self.session_count += 1
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            with open(self.log_file, "a") as file:
                log_entry = f"Session {self.session_count} completed at {timestamp}"
                if focus_text:
                    log_entry += f" - {focus_text}"
                log_entry += " - success" if success else " - failed"
                file.write(log_entry + "\n")
                
            logger.info(f"Logged session {self.session_count}")
            return self.session_count
        except Exception as e:
            logger.error(f"Error logging session: {e}")
            return self.session_count

    def log_event(self, message: str) -> None:
        """Append a non-counting event entry to the sessions log.

        Used to mirror Obsidian actions (start/rest/pause/resume)
        without affecting the completed-session counter.
        """
        try:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(self.log_file, "a") as file:
                file.write(f"Event at {timestamp} - {message}\n")
        except Exception as e:
            logger.error(f"Error logging event: {e}")

    def get_session_count(self):
        """
        Get the current session count.
        
        Returns:
            int: Current session count
        """
        return self.session_count

    def get_daily_stats(self):
        """
        Get statistics for sessions completed today.
        
        Returns:
            dict: Statistics including count and focus areas
        """
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        count = 0
        focus_areas = set()
        
        try:
            if not os.path.exists(self.log_file):
                return {"count": 0, "focus_areas": []}
                
            with open(self.log_file, "r") as file:
                for line in file:
                    if today in line and "Session" in line and "completed" in line:
                        count += 1
                        if " - " in line:
                            focus = line.split(" - ", 1)[1].strip()
                            focus_areas.add(focus)
            
            return {"count": count, "focus_areas": list(focus_areas)}
        except Exception as e:
            logger.error(f"Error getting daily stats: {e}")
            return {"count": 0, "focus_areas": []}
