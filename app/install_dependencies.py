import subprocess
import sys

# ============================================
# ICTA DASHBOARD DEPENDENCY INSTALLER
# ============================================

packages = [

    "streamlit",

    "streamlit-autorefresh",

    "pyngrok",

    "requests"
]

# ============================================
# INSTALL PACKAGES
# ============================================

for package in packages:

    print(f"\nInstalling {package}...")

    subprocess.check_call([

        sys.executable,

        "-m",

        "pip",

        "install",

        "-q",

        package
    ])

print("\nAll dashboard dependencies installed ✅")