from flask import Flask, render_template, jsonify
import os
import yaml

app = Flask(__name__)

TOOLS_DIR = "../tools"

def get_tools():
    tools_list = {}
    if not os.path.exists(TOOLS_DIR):
        return tools_list
    for category in os.listdir(TOOLS_DIR):
        cat_path = os.path.join(TOOLS_DIR, category)
        if os.path.isdir(cat_path):
            tools_list[category] = []
            for tool_file in os.listdir(cat_path):
                if tool_file.endswith(".yaml"):
                    with open(os.path.join(cat_path, tool_file), 'r') as f:
                        tools_list[category].append(yaml.safe_load(f))
    return tools_list

@app.route('/')
def index():
    return render_template('index.html', tools=get_tools())

@app.route('/api/tools')
def api_tools():
    return jsonify(get_tools())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
