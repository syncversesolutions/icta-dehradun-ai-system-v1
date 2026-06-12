import subprocess
import sys
import time

from pyngrok import ngrok

from google.colab import userdata

# ============================================
# NGROK AUTH
# ============================================

NGROK_AUTH_TOKEN = userdata.get(
    "NGROK_AUTH_TOKEN"
)

if not NGROK_AUTH_TOKEN:

    raise ValueError(

        "NGROK_AUTH_TOKEN not found"
    )

ngrok.set_auth_token(
    NGROK_AUTH_TOKEN
)

# ============================================
# APP CONFIG
# ============================================

APP_PATH = (

    "/content/drive/MyDrive/project_cd/app/app.py"
)

PORT = 8502

# ============================================
# START STREAMLIT
# ============================================

print(
    "\nStarting ICTA dashboard..."
)

process = subprocess.Popen([

    sys.executable,

    "-m",

    "streamlit",

    "run",

    APP_PATH,

    "--server.port",

    str(PORT)
])

time.sleep(5)

print(
    "\nStreamlit server started ✅"
)

# ============================================
# START NGROK
# ============================================

tunnel = ngrok.connect(PORT)

print("\n")
print("=" * 60)

print("ICTA DASHBOARD LIVE")

print("=" * 60)

print(f"\nPublic URL:\n{tunnel.public_url}")

print("\n")
print("=" * 60)

# ============================================
# KEEP RUNTIME ACTIVE
# ============================================

try:

    while True:

        time.sleep(60)

except KeyboardInterrupt:

    print(
        "\nStopping dashboard..."
    )

    ngrok.kill()

    process.terminate()

    process.wait()

    print(
        "\nDashboard stopped ✅"
    )