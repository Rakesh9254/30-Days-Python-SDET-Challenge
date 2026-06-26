# Intermediate / QA-Focused Example: sdet_info.py
# This script prints system and execution information.
# QA Engineers use this kind of script to verify the environment 
# where their automation tests are running.

import sys
import os

print("--- Test Environment Details ---")
print(f"Python Version: {sys.version.split(' ')[0]}")
print(f"Current Working Directory: {os.getcwd()}")
print("--------------------------------")
print("Environment is ready for Automation Testing!")
