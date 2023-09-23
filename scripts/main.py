from modules import scripts
import gradio as gr
from lib_free_u import global_state, unet


class FreeUScript(scripts.Script):
    def title(self):
        return "Free U"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        with gr.Accordion(open=False, label="Free U"):
            enabled = gr.Checkbox(
                label="Enable",
                value=False,
            )
            with gr.Accordion(open=True, label="Block 1"):
                b1 = gr.Slider(
                    label="Backbone 1 Scale",
                    minimum=0,
                    maximum=2,
                    value=1,
                )
                s1 = gr.Slider(
                    label="Skip 1 Scale",
                    minimum=0,
                    maximum=2,
                    value=1,
                )
            with gr.Accordion(open=True, label="Block 2"):
                b2 = gr.Slider(
                    label="Backbone 2 Scale",
                    minimum=0,
                    maximum=2,
                    value=1,
                )
                s2 = gr.Slider(
                    label="Skip 2 Scale",
                    minimum=0,
                    maximum=2,
                    value=1,
                )

        return enabled, b1, s1, b2, s2

    def process(self, p, enabled: bool, b1: float, s1: float, b2: float, s2: float):
        global_state.enabled = enabled
        global_state.backbone_factors[:] = b1, b2
        global_state.skip_factors[:] = s1, s2


unet.patch_model()