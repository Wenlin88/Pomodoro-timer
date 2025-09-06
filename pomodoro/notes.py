"""
Notes integration module for the Pomodoro Timer application.
Handles integration with Obsidian and other note-taking systems.
"""
import datetime
import logging
import os
import sys
import subprocess
import urllib.parse
import webbrowser

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

    def _open_obsidian_url(self, url: str) -> None:
        """Open an Obsidian URL without inheriting the console when possible.

        On Windows, prefer ShellExecute via os.startfile or a detached process
        to avoid Obsidian (Electron) updater logs appearing in our console.
        """
        try:
            if sys.platform.startswith("win"):
                try:
                    os.startfile(url)  # type: ignore[attr-defined]
                    return
                except Exception:
                    creationflags = 0x00000008 | 0x00000010  # DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP
                    with open(os.devnull, "w") as devnull:
                        subprocess.Popen(
                            ["cmd", "/c", "start", "", url],
                            stdout=devnull,
                            stderr=devnull,
                            creationflags=creationflags,
                        )
                    return
            elif sys.platform == "darwin":
                with open(os.devnull, "w") as devnull:
                    subprocess.Popen(["open", url], stdout=devnull, stderr=devnull)
                return
            else:
                # Linux/Unix
                with open(os.devnull, "w") as devnull:
                    subprocess.Popen(["xdg-open", url], stdout=devnull, stderr=devnull)
                return
        except Exception:
            # Fallback to webbrowser if platform-specific approach fails
            webbrowser.open(url)

    def record_pomodoro_session(
        self,
        *,
        focus_text: str,
        success: bool | None,
        early: bool = False,
        planned_minutes: int | None = None,
        actual_minutes: int | None = None,
        status: str | None = None,
    ) -> bool:
        """Append a session entry to a dated Markdown file using Obsidian Advanced URI.

        Uses obsidian://adv-uri with mode=append to write into a file
        "YYYY-MM-DD - Pomodoro Sessions.md" under the configured
        `sessions_notes_path` in the given `vault_name`.
        """
        if not self.enabled:
            return False
        try:
            date_str = datetime.datetime.now().strftime("%Y-%m-%d")
            time_str = datetime.datetime.now().strftime("%H:%M")
            if status is None:
                if success is None:
                    status_str = ""
                else:
                    status_str = "success" if success else ("early stop" if early else "failed")
            else:
                status_str = status
            details: list[str] = []
            if planned_minutes is not None:
                details.append(f"planned {planned_minutes}m")
            if actual_minutes is not None:
                details.append(f"actual {actual_minutes}m")
            detail_str = f" ({', '.join(details)})" if details else ""
            focus_desc = focus_text or "(no description)"
            if status_str:
                line = f"- {time_str} – {focus_desc} — {status_str}{detail_str}"
            else:
                line = f"- {time_str} – {focus_desc}{detail_str}"

            sessions_subpath = (self.obsidian_settings or {}).get("sessions_notes_path") or ""
            filepath = f"{sessions_subpath}/{date_str} - Pomodoro Sessions.md" if sessions_subpath else f"{date_str} - Pomodoro Sessions.md"
            vault = (self.obsidian_settings or {}).get("vault_name") or ""
            if not vault:
                logger.warning("Obsidian vault_name not set; cannot record session via Advanced URI")
                return False

            url = (
                "obsidian://adv-uri?vault="
                + urllib.parse.quote(vault)
                + "&filepath="
                + urllib.parse.quote(filepath)
                + "&data="
                + urllib.parse.quote(line)
                + "&mode=append&silent=true"
            )
            self._open_obsidian_url(url)
            logger.info("Recorded session to Obsidian via Advanced URI")
            return True
        except Exception as e:
            logger.error(f"Error recording session to Obsidian via Advanced URI: {e}")
            return False

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
            
            self._open_obsidian_url(url)
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
            
            self._open_obsidian_url(url)
            logger.info(f"Opened weekly note for {week_str}")
            return True
        except Exception as e:
            logger.error(f"Error opening weekly note: {e}")
            return False
