import gradio as gr

def fallback_reply(prompt, history):
    p = prompt.strip().lower()
    if not p:
        ans = "سلام! من رادمان هستم؛ چه کمکی از من ساخته است؟"
    elif any(w in p for w in ["سلام","درود","خوبی"]):
        ans = "سلام! من رادمان هستم. چطور می‌تونم کمکت کنم؟"
    elif "تمرین" in p or "ورزش" in p:
        ans = "برای تمرین منظم، روزانه ۳۰–۶۰ دقیقه برنامه‌ریزی کن. اگر می‌خوای برات برنامه تمرینی ساده می‌سازم."
    elif "بسکتبال" in p:
        ans = "برای بسکتبال روی مهارت‌های دریبل، پرتاب و دفاع کار کن. دوست داری برنامه تمرین بدهم؟"
    elif "رپ" in p or "آهنگ" in p:
        ans = "موضوع و سبک بده تا یک بیت رپ فارسی برات بنویسم."
    elif "ممنون" in p or "مرسی" in p:
        ans = "خواهش می‌کنم! هر وقت خواستی من اینجام."
    else:
        ans = "متاسفم، جواب دقیقی ندارم اما می‌تونم کمکت کنم متن بنویسی یا ایده بدهم — دقیق‌تر بپرس؟"
    return ans, history + [("user", prompt), ("assistant", ans)]

def respond(prompt, history):
    return fallback_reply(prompt, history)

css = """
body { background-color: #0b0f13; color: #e6eef6; }
.gradio-container { background: #0b0f13; }
.main { background: linear-gradient(180deg, #071018, #0b0f13); padding: 18px; border-radius: 12px; }
.header { font-size: 24px; font-weight: 700; color: #e6eef6; margin-bottom: 8px; }
.footer { color:#9aa7b2; font-size:13px; margin-top:10px; }
"""

with gr.Blocks(css=css, title='رادمان AI — دستیار فارسی', theme=None) as demo:
    gr.Markdown("""
    <div class='main'>
      <div class='header'>رادمان AI 🤖</div>
      <div class='footer'>دستیار شخصی فارسی — سازنده: امیر علی قجر</div>
    </div>
    "", elem_id="top")
    chatbot = gr.Chatbot(elem_id="chatbox", label="چت با رادمان")
    with gr.Row():
        txt = gr.Textbox(show_label=False, placeholder="پیام خود را بنویس و Enter بزن...", elem_id="input_txt")
    state = gr.State([])
    def submit_fn(message, history):
        if not message or not message.strip():
            return gr.update(value=""), history
        out, new_history = respond(message, history)
        bot = []
        u = None
        for role, text in new_history:
            if role=='user':
                u = text
            else:
                bot.append((u, text))
                u = None
        return "", bot, new_history
    txt.submit(submit_fn, inputs=[txt, state], outputs=[txt, chatbot, state])
    btn = gr.Button("ارسال")
    btn.click(submit_fn, inputs=[txt, state], outputs=[txt, chatbot, state])

if __name__ == '__main__':
    demo.launch(server_name='0.0.0.0', server_port=int(os.environ.get('PORT',8080)))
