import gradio as gr
from transformers import pipeline
import os
import json

memory_file = "memory.json"
if os.path.exists(memory_file):
    with open(memory_file, "r", encoding="utf-8") as f:
        memory = json.load(f)
else:
    memory = {}

generator = pipeline("text2text-generation", model="google/flan-t5-small")

def radman_ai(user_input):
    answer = generator(user_input, max_length=100)[0]['generated_text']
    memory[user_input] = answer
    with open(memory_file, "w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=False, indent=4)
    return answer

with gr.Blocks() as demo:
    gr.Markdown("""# 🤖 رادمان AI واقعی
سوال خود را بپرس و جواب طبیعی بگیر.""")
    with gr.Row():
        user_input = gr.Textbox(label="پیام شما", placeholder="پیام خود را وارد کنید...")
        submit_btn = gr.Button("ارسال")
    output = gr.Textbox(label="پاسخ رادمان")
    submit_btn.click(fn=radman_ai, inputs=user_input, outputs=output)

demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 8080)), share=False)
