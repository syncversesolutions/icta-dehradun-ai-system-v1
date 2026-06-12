import os
import sys
from pathlib import Path
# ============================================
# PROJECT ROOT
# ============================================
PROJECT_ROOT = (
    Path(__file__).resolve().parent.parent
)
# ============================================
# REGISTER PROJECT ROOT
# ============================================
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(
        str(PROJECT_ROOT)
    )
# ============================================
# RUNTIME ROOT
# ============================================
RUNTIME_ROOT = (
    PROJECT_ROOT /
    "runtime"
)
# ============================================
# RUNTIME DIRECTORIES
# ============================================
RUNTIME_DIRECTORIES = [
    "snapshots",
    "simulations",
    "sessions",
    "exports"
]
# ============================================
# CREATE RUNTIME DIRECTORIES
# ============================================
for directory in RUNTIME_DIRECTORIES:
    path = (
        RUNTIME_ROOT /
        directory
    )
    os.makedirs(
        path,
        exist_ok=True
    )
# ============================================
# INITIALIZATION LOGS
# ============================================
print("\n")
print("=" * 60)
print(
    "ICTA RUNTIME ENVIRONMENT INITIALIZED ✅"
)
print("\nPROJECT ROOT:")
print(PROJECT_ROOT)
print("\nRUNTIME ROOT:")
print(RUNTIME_ROOT)
print("\nRUNTIME DIRECTORIES:")
for directory in RUNTIME_DIRECTORIES:
    print(
        f"• {directory}"
    )
print("\n")
print("=" * 60)