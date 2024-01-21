import os

try:
    server_port = int(os.environ.get('SERVER_PORT', ''))
except ValueError:
    server_port = 7860

root_path = os.environ.get('ROOT_PATH', '')

import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="textbox", outputs="textbox")
    
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0",
                server_port=server_port,
                root_path=root_path)