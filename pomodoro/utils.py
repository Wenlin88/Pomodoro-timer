"""
Utilities for the Pomodoro Timer application.
"""
import os
import sys
import importlib.resources as resources
import logging

logger = logging.getLogger(__name__)


def get_resource_path(resource_name):
    """
    Get the appropriate path for a resource file.
    Works both when running from source and when installed as a package.
    
    Args:
        resource_name: Resource name/path (e.g., 'icons/pomodoro.png')
    
    Returns:
        str: Absolute path to the resource
    """
    # Split the resource name into directory and filename
    parts = os.path.normpath(resource_name).split(os.sep)
    resource_dir = parts[0]  # 'icons' or 'sounds'
    resource_file = os.path.join(*parts[1:]) if len(parts) > 1 else parts[0]    # First try to find the resource in the package data
    try:
        # Try using importlib.resources (Python 3.9+)
        path = resources.files('pomodoro').joinpath(f"../{resource_name}")
        if path.is_file():
            return str(path)
    except (ImportError, AttributeError, FileNotFoundError):
        pass
    
    # Fall back to looking in standard locations relative to the module
    try:
        package_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        resource_path = os.path.join(package_dir, resource_name)
        
        if os.path.exists(resource_path):
            return resource_path
    except Exception as e:
        logger.warning(f"Error finding resource {resource_name}: {e}")
    
    # Last resort - try relative to current directory
    if os.path.exists(resource_name):
        return os.path.abspath(resource_name)
    
    logger.warning(f"Resource not found: {resource_name}")
    return resource_name  # Return the original path as a fallback
