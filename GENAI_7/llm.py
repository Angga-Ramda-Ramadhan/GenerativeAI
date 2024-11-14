# Import necessary packages
from ibm_watson_machine_learning.foundation_models import Model
# Model and project settings
import gradio as gr

model_id = "meta-llama/llama-2-13b-chat"  # Directly specifying the LLAMA2 model
# Set credentials to use the model
my_credentials = {
    "url": "https://us-south.ml.cloud.ibm.com"
}
# Set necessary parameters
gen_parms = {
    "max_new_tokens": 256,  # Specifying the max tokens you want to generate
    "temperature": 0.1    # Specifying the temperature which controls the randomness of the token generated
}
project_id = "skills-network"  # Specifying project_id as provided
space_id = None
verify = False
# Initialize the model
model = Model(model_id, my_credentials, gen_parms, project_id, space_id, verify)

def bot(prompt):
    generated_response = model.generate(prompt)
    generated_text = generated_response["results"][0]["generated_text"]
    # Print the generated response
    return generated_text

chat_application = gr.Interface(
    fn = bot,
    allow_flagging="never",
    inputs=gr.Textbox(label="Input", lines=2, placeholder="Type your question here..."),
    outputs = gr.Textbox(label="Ouput"),
    title = "Watsonx.ai CHatbot",
    description = "Ask any question and the chatbot will try to answer."
)

#launch the app

chat_application.launch()