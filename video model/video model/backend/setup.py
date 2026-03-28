#!/usr/bin/env python3
"""
Setup script to initialize the deepfake detection backend
Run this once before starting the application
"""

import os
import sys
from pathlib import Path

def setup():
    """Initialize backend directories and check setup."""
    print("\n" + "=" * 60)
    print("Deepfake Detection - Backend Setup")
    print("=" * 60 + "\n")

    base_dir = Path(__file__).parent
    
    # Create necessary directories
    dirs_to_create = [
        base_dir / "uploads",
        base_dir / "frames",
    ]

    print("Creating directories:")
    for dir_path in dirs_to_create:
        dir_path.mkdir(exist_ok=True)
        print(f"✓ {dir_path.name}/")

    print("\nBackend is ready!")
    print("\nTo start the server, run:")
    print("  uvicorn main:app --reload --port 8000")
    print("\nOr use the startup script:")
    print("  start.bat (Windows)")
    print("  start.sh (macOS/Linux)")
    print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    try:
        setup()
    except Exception as e:
        print(f"Error during setup: {e}", file=sys.stderr)
        sys.exit(1)
