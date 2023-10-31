import numpy as np
import gradio as gr


def flip_text(x):
    return x[:: -1]

def flip_image(x):
    return np.fliplr(x)


with gr.Blocks() as demo:
    gr.Markdown("Flip text or Image files demo")
    with gr.Tab("Flip text"):
        text_Input = gr.Textbox()
        text_Output = gr.Textbox()
        text_Button = gr.Button("Flip")
    with gr.Tab("Flip Image"):
        with gr.Row():
            image_input = gr.Image()
            image_output = gr.Image()
        image_Button = gr.Button("Flip Image")

    #with gr.Accordion("Open for More !"):
    #    gr.Markdown("Look at me")

    text_Button.click(flip_text , inputs= text_Input , outputs=text_Output)
    image_Button.click(flip_image, inputs= image_input , outputs=image_output)

demo.launch(share = True)

