import os
import gradio as gr

def video_identity(video):
    return video


demo = gr.Interface(video_identity,
                    gr.Video(),
                    "playable_video",
                    loop = True,
                    examples=["/tmp/index.m3u8"],
                    )

if __name__ == "__main__":
    demo.launch()
