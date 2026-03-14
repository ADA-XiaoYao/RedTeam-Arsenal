import os
import yaml

class ToolLoader:
    def __init__(self, tools_dir="tools"):
        self.tools_dir = tools_dir

    def get_all_tools(self):
        tools_list = {}
        if not os.path.exists(self.tools_dir):
            return tools_list
        for category in os.listdir(self.tools_dir):
            cat_path = os.path.join(self.tools_dir, category)
            if os.path.isdir(cat_path):
                tools_list[category] = []
                for tool_file in os.listdir(cat_path):
                    if tool_file.endswith(".yaml"):
                        with open(os.path.join(cat_path, tool_file), 'r') as f:
                            # Use safe_load_all to handle multiple tools in one file
                            for tool in yaml.safe_load_all(f):
                                if tool:
                                    tools_list[category].append(tool)
        return tools_list
