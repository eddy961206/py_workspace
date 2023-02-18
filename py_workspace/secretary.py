import whisper
import gradio as gr
import warnings
import openai


warnings.filterwarnings("ignore")

# Use your API key to authenticate
openai.api_key = "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"

model = whisper.load_model("base")

model.device

def transcribe(audio):
    # load audio and pad/trim it to fit 30 seconds
    audio=whisper.load_audio(audio)
    audio=whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)

    # decode the audio
    #options = whisper.DecodingOptions()
    options = whisper.DecodingOptions(fp16=False)
    result = whisper.decode(model, mel, options)
    result_text = result.text

    # Pass the generated text to Audio
    # Use the openai API to generate a response
    response = openai.Completion.create(
        engine="ada",
        prompt=result_text,
        max_tokens=1024,
        n=1,
        temperature=0.5
    ).choices[0].text

    out_result = response
    print(out_result)

    return [result_text, out_result]

output_1 = gr.Textbox(label="Speech to Text")
output_2 = gr.Textbox(label="ChatGPT Output")

gr.Interface(
    title = 'OpenAI Whisper and ChatGPT ASR Gradio Web UI',
    fn=transcribe,
    inputs=[
        gr.inputs.Audio(source="microphone", type="filepath")
    ],

    outputs=[output_1, output_2],
    live=True).launch()