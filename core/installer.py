import os
import subprocess
import platform
import yaml

class ToolInstaller:
    def __init__(self, tools_dir="tools"):
        self.tools_dir = tools_dir
        self.os_type = platform.system().lower()

    def load_tool_config(self, category, tool_name):
        config_path = os.path.join(self.tools_dir, category, f"{tool_name}.yaml")
        if not os.path.exists(config_path):
            return None
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)

    def install(self, category, tool_name):
        config = self.load_tool_config(category, tool_name)
        if not config:
            print(f"[-] Configuration for {tool_name} not found.")
            return False

        install_cmd = config.get('install_command', {}).get(self.os_type)
        if not install_cmd:
            print(f"[-] No installation command found for {self.os_type}.")
            return False

        print(f"[*] Installing {tool_name} via: {install_cmd}")
        try:
            subprocess.run(install_cmd, shell=True, check=True)
            print(f"[+] {tool_name} installed successfully.")
            return True
        except subprocess.CalledProcessError as e:
            print(f"[-] Failed to install {tool_name}: {e}")
            return False
