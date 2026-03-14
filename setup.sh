#!/bin/bash

# RedTeam-Arsenal Setup Script
echo "⚔️ Setting up RedTeam-Arsenal..."

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "[-] Python 3 is not installed. Please install it first."
    exit 1
fi

# Install requirements
echo "[*] Installing dependencies..."
pip3 install -r requirements.txt

# Set permissions
chmod +x arsenal.py

echo "[+] Setup complete! Run 'python3 arsenal.py --help' to get started."
