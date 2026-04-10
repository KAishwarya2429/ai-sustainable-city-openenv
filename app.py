import gradio as gr
import requests

API_URL = "http://127.0.0.1:7860"

def reset_env():
    r = requests.post(API_URL + "/reset")
    return r.json()

def step_env(action):
    r = requests.post(API_URL + "/step", json={"action": action})
    return r.json()

with gr.Blocks() as demo:
    gr.Markdown("# 🌍 AI Pollution OpenEnv")

    btn1 = gr.Button("Reset Environment")
    output1 = gr.Textbox()

    btn1.click(reset_env, outputs=output1)

    action = gr.Slider(0, 2, step=1, label="Action (0=none,1=reduce,2=strong)")
    btn2 = gr.Button("Step Environment")
    output2 = gr.Textbox()

    btn2.click(step_env, inputs=action, outputs=output2)

demo.launch(server_name="0.0.0.0", server_port=7860)