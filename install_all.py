import os
import sys
from core.loader import ToolLoader
from core.installer import ToolInstaller

def main():
    print("⚔️ RedTeam-Arsenal: Bulk Installer")
    print("==================================")
    
    loader = ToolLoader()
    installer = ToolInstaller()
    tools = loader.get_all_tools()
    
    for category, tool_list in tools.items():
        print(f"\n[*] Processing Category: {category}")
        for tool in tool_list:
            tool_name = tool['name']
            confirm = input(f"Install {tool_name}? (y/n): ").lower()
            if confirm == 'y':
                installer.install(category, tool_name.lower().replace(' ', '_'))

if __name__ == "__main__":
    main()
