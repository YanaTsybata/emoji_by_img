import gradio as gr
from deepface import DeepFace
import json


def read_json():
    with open('emoji.json', 'r', encoding='utf8') as f:
        data_emoji = json.load(f)
        return data_emoji


def emotion_analysis(image):
    try:
        analyze = DeepFace.analyze(image, actions=['emotion'])
        return analyze[0]['dominant_emotion']
    except Exception as e:
        return f"An Error occurred: {str(e)}"


def emotion_to_emoji(emotion, emoji_dict):
    return emoji_dict[emotion.lower()] if emotion.lower() in emoji_dict else emoji_dict["Unknown"]


def main_process(image):
    try:
        # emotion analysis
        detected_emotion = emotion_analysis(image)
        emoji_dict = read_json()
        matched_emoji = emotion_to_emoji(detected_emotion, emoji_dict)
        # Emoji size
        results = f"Detected emotion: {detected_emotion}</p><p style='font-size:72px;'> {matched_emoji}</p>"
        return results
    except Exception as e:
        return f"An Error occurred{str(e)}"


iface = gr.Interface(
    fn=main_process,
    inputs=gr.Image(),
    outputs=gr.HTML(),
    title=" ",
    description=" "
)

iface.launch()
