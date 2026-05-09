
import os
import sys

print("=== DEBUG START: EXTREME DEBUG ===")
print(f"System Check: Python {sys.version}")
print(f"ENV CHECK: DEEPSEEK_API_KEY present: {os.getenv('DEEPSEEK_API_KEY') is not None}")
print("=== DEBUG END ===")
