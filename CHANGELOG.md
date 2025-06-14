# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2025-06-14

### Added

- Support for installing the package via pip
- Command line interface with focus and rest period customization
- Resource file handling when running as an installed package
- User-specific configuration and data directories
- Version command line option

### Fixed

- Package structure to support proper installation
- Resource paths for sounds and icons when running as an installed package
- Pygame startup message suppression

### Changed

- Improved documentation and installation instructions
- Updated Python requirement to >=3.12
- Added appdirs dependency for better cross-platform file locations

## [0.1.0] - 2025-06-01

### Features

- Initial release
- Basic Pomodoro timer functionality
- Focus and rest period tracking
- Sound notifications
- Optional Obsidian integration
- Configurable settings
