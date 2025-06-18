import ast
import json
import argparse
import os
import tkinter as tk
from tkinter import filedialog

def python_type_to_json_type(type_str: str):
    if type_str in ("str", "builtins.str"):
        return "string"
    elif type_str in ("int", "builtins.int"):
        return "integer"
    elif type_str in ("float", "builtins.float"):
        return "number"
    elif type_str in ("bool", "builtins.bool"):
        return "boolean"
    elif type_str in ("list", "typing.List"):
        return "array"
    elif type_str in ("dict", "typing.Dict"):
        return "object"
    return "string"

def extract_functions_from_ast(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        source = f.read()
    tree = ast.parse(source, filename=filepath)

    tools = []

    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            name = node.name
            docstring = ast.get_docstring(node) or ""
            parameters = {
                "type": "object",
                "properties": {},
                "required": []
            }

            for i, arg in enumerate(node.args.args):
                if arg.arg == "self":
                    continue
                param_name = arg.arg
                param_type = "string"
                if arg.annotation:
                    param_type = python_type_to_json_type(ast.unparse(arg.annotation))
                parameters["properties"][param_name] = {
                    "type": param_type,
                    "description": f"{param_name} parameter"
                }

            # Determine required args
            num_required = len(node.args.args) - len(node.args.defaults)
            for i, arg in enumerate(node.args.args):
                if arg.arg != "self" and i < num_required:
                    parameters["required"].append(arg.arg)

            tools.append({
                "name": name,
                "description": docstring,
                "parameters": parameters
            })
    return tools

def select_file_gui():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename(
        title="Select a Python file",
        filetypes=[("Python files", "*.py")]
    )

def load_existing_tools(output_path):
    if os.path.exists(output_path):
        with open(output_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def merge_tools(existing, new_tools):
    existing_names = {tool["name"] for tool in existing}
    merged = existing[:]
    added = 0

    for tool in new_tools:
        if tool["name"] not in existing_names:
            merged.append(tool)
            added += 1

    return merged, added

def main():
    parser = argparse.ArgumentParser(description="Extract Gemini tool schemas and append to JSON.")
    parser.add_argument("-f", "--file", help="Path to the Python file")
    parser.add_argument("-o", "--output", default="tools.json", help="Output JSON file (default: tools.json)")
    args = parser.parse_args()

    file_path = args.file or select_file_gui()
    if not file_path:
        print("❌ No file selected. Exiting.")
        return

    new_tools = extract_functions_from_ast(file_path)
    existing_tools = load_existing_tools(args.output)
    merged_tools, added_count = merge_tools(existing_tools, new_tools)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(merged_tools, f, indent=2)

    print(f"✅ {added_count} new tool(s) added to {args.output}")
    print(f"📁 Total tools: {len(merged_tools)}")

if __name__ == "__main__":
    main()
