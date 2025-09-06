# Changelog

All notable changes to this project will be documented in this file.

## [0.3.1] - 2025-09-06

### Added

- Log start/rest/pause/resume events to sessions log
- Obsidian entries for resume and app exit
- Early-exit events recorded to sessions log and Obsidian

### Changed

- Obsidian appends use silent mode (no focus/tab switch)
- Non-completion Obsidian entries no longer show "success"
- Removed logging of opening Daily/Weekly notes to sessions

## [0.2.1] - 2025-06-14

### Changed

- Removed "Focus:" prefix from the focus text display

## [0.2.0] - 2025-06-14

### Added

- Default configuration file is now created under `~/.pomodoro/config.json` if none exists
- Dialog to set focus and rest durations before each session
- Prompt to record whether a focus session succeeded or failed
- Session logs now include success or failure information

## [0.1.0] - 2025-06-14

### Added

- Initial release of the Pomodoro Timer
