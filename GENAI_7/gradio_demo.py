import gradio as gr

def add_number(n1, n2):
    return n1 + n2

#define gradio interface

demo = gr.Interface(
    fn=add_number,
    inputs=['number', 'number'],
    outputs = 'number'
)

#launch
demo.launch(server_name="0.0.0.0", server_port = 7860)