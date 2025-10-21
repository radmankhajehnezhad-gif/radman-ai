import gradio as gr
import os
import json

# فایل ذخیره سوال و جواب‌ها
db_file = "qa_db.json"

# بارگذاری دیتابیس در صورت وجود
if os.path.exists(db_file):
    with open(db_file, "r", encoding="utf-8") as f:
        qa_db = json.load(f)
else:
    qa_db = {}

# تابع پاسخگویی
def radman_ai(user_input):
    # اگر جواب موجود است برگردان
    if user_input in qa_db:
        return f"جواب قبلی: {qa_db[user_input]}"
    
    # در غیر این صورت پاسخ واقعی بده (فعلاً نمونه)
    # می‌تونی این بخش را با یک مدل واقعی یا API هوش مصنوعی جایگزین کنی
    answer = f"این پاسخ واقعی برای: {user_input}"
    
    # ذخیره سوال و جواب
    qa_db[user_input] = answer
    with open(db_file, "w", encoding="utf-8") as f:
        json.dump(qa_db, f, ensure_ascii=False, indent=4)
    
    return answer

# رابط گرافیکی
with gr.Blocks() as demo:
    gr.Markdown("""
    # 🤖 رادمان AI با حافظه
    سوال خود را وارد کنید و رادمان جواب واقعی ذخیره شده را برمی‌گرداند.
    """)
    
    with gr.Row():
        user_input = gr.Textbox(label="پیام شما", placeholder="پیام خود را وارد کنید...")
        submit_btn = gr.Button("ارسال")
    
    output = gr.Textbox(label="پاسخ رادمان")

    submit_btn.click(fn=radman_ai, inputs=user_input, outputs=output)

demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 8080)),
    share=False
)
