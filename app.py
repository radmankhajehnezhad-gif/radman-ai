import gradio as gr
import os

# تعریف تابع پاسخگویی رادمان AI
def radman_ai(user_input):
    # اینجا می‌تونی هوش مصنوعی یا منطق پاسخگویی خودت را اضافه کنی
    # فعلاً نمونه ساده است
    response = f"رادمان می‌گه: {user_input}"
    return response

# ساخت رابط گرافیکی با Gradio
with gr.Blocks() as demo:
    gr.Markdown("""
    # 🤖 رادمان AI
    خوش آمدید! سوال خود را وارد کنید و رادمان پاسخ می‌دهد.
    """)
    
    with gr.Row():
        user_input = gr.Textbox(label="پیام شما", placeholder="پیام خود را وارد کنید...")
        submit_btn = gr.Button("ارسال")
    
    output = gr.Textbox(label="پاسخ رادمان")

    submit_btn.click(fn=radman_ai, inputs=user_input, outputs=output)

# اجرا روی Render
demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 8080)),
    share=False
)
