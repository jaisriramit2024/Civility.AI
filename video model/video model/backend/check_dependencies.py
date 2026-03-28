#!/usr/bin/env python3
"""
Quick verification script to ensure all dependencies are available
Run this before starting the application
"""

import sys
import subprocess

def check_package(package_name: str, import_name: str = None) -> bool:
    """Check if a Python package is installed."""
    import_name = import_name or package_name
    try:
        __import__(import_name)
        print(f"✓ {package_name}")
        return True
    except ImportError:
        print(f"✗ {package_name} - MISSING")
        return False


def check_command(cmd: str) -> bool:
    """Check if a command is available in PATH."""
    try:
        result = subprocess.run(
            [cmd, "--version"],
            capture_output=True,
            timeout=5,
            check=False,
        )
        if result.returncode == 0:
            print(f"✓ {cmd}")
            return True
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    print(f"✗ {cmd} - NOT FOUND in PATH")
    return False


def main():
    print("\n" + "=" * 60)
    print("Deepfake Detection - Dependency Checker")
    print("=" * 60 + "\n")

    # Python packages
    print("Python Packages:")
    required = [
        ("fastapi", "fastapi"),
        ("uvicorn", "uvicorn"),
        ("torch", "torch"),
        ("torchvision", "torchvision"),
        ("timm", "timm"),
        ("opencv-python", "cv2"),
        ("mediapipe", "mediapipe"),
        ("pillow", "PIL"),
        ("ffmpeg-python", "ffmpeg"),
        ("aiofiles", "aiofiles"),
        ("numpy", "numpy"),
    ]

    missing_packages = []
    for package, import_name in required:
        if not check_package(package, import_name):
            missing_packages.append(package)

    # External commands
    print("\nExternal Commands:")
    commands = ["python", "ffmpeg", "node", "npm"]
    missing_commands = []
    for cmd in commands:
        if not check_command(cmd):
            missing_commands.append(cmd)

    # Summary
    print("\n" + "=" * 60)
    if missing_packages:
        print(f"Missing Python packages: {', '.join(missing_packages)}")
        print("\nInstall with:")
        print(f"pip install {' '.join(missing_packages)}")
    if missing_commands:
        print(f"Missing commands: {', '.join(missing_commands)}")
    if not missing_packages and not missing_commands:
        print("✓ All dependencies are installed!")
    print("=" * 60 + "\n")

    return len(missing_packages) == 0 and len(missing_commands) == 0


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
