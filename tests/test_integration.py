import subprocess
import sys

def test_python_in_docker():
    result = subprocess.run(
        [sys.executable, "-c", "print('Hello from Docker!')"],
        capture_output=True, text=True
    )
    assert "Hello from Docker!" in result.stdout