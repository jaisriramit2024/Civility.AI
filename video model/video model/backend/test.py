#!/usr/bin/env python3
"""
Simple test to verify the backend is working
"""

import sys
from pathlib import Path

# Add backend to path
backend_path = Path(__file__).parent
sys.path.insert(0, str(backend_path))

def test_imports():
    """Test that all required modules can be imported."""
    print("\n" + "=" * 60)
    print("Backend Import Testing")
    print("=" * 60 + "\n")

    modules = [
        "fastapi",
        "uvicorn",
        "torch",
        "cv2",
        "mediapipe",
        "ffmpeg",
    ]

    print("Testing imports:")
    failed = []
    for module in modules:
        try:
            __import__(module)
            print(f"✓ {module}")
        except ImportError as e:
            print(f"✗ {module}: {e}")
            failed.append(module)

    if failed:
        print(f"\n❌ Failed to import: {', '.join(failed)}")
        print("\nInstall missing packages with:")
        print(f"  pip install -r requirements.txt")
        return False

    print("\n✓ All imports successful!")
    print("\n" + "=" * 60 + "\n")
    return True


def test_directories():
    """Test that required directories exist."""
    print("Testing directories:")
    required_dirs = [
        backend_path / "uploads",
        backend_path / "frames",
        backend_path / "pipeline",
    ]

    for dir_path in required_dirs:
        if dir_path.exists():
            print(f"✓ {dir_path.name}/")
        else:
            print(f"✗ {dir_path.name}/ - MISSING")
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"  Created: {dir_path.name}/")

    return True


if __name__ == "__main__":
    success = test_imports() and test_directories()
    sys.exit(0 if success else 1)
