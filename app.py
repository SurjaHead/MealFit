from dotenv import load_dotenv
import os
import requests
import streamlit as st

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def generate_meal_plan(age, weight, height, goal, activity_level):
    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }
    payload = {
    "model": "gpt-4o",
    "messages": [
        {
        "role": "system",
        "content": [
            {
            "type": "text",
            "text": "You are a professional world-class personal trainer and dietician. Your job is to craft a personalized meal plan for the user based on the information they provide you with. Estimate the number of calories the user should eat and provide the number of calories for each meal. Provide exact instructions and ingredients, along with measurements and repeat it for each day of the week. "
            }
        ]
        }, 
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"Gneder: {gender}\nAge: {age}\nWeight: {weight} kgs\nHeight: {height}cm\nGoal: {goal}\nActivity level:{activity_level}"
                }
            ]
        }
    ],
    "max_tokens": 4000,
    "temperature": 0
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

        # print(response.json())
    st.write(response.json().get("choices")[0].get("message").get("content"))



st.set_page_config(
    page_title="Meal Plan Builder",
    page_icon="🍳",
)

st.title("Meal Plan Builder")
st.write("This app uses OpenAI's GPT-4 model to generate recipes based on the ingredients in the image you upload.")
with st.form(key="user_input", clear_on_submit=False):
    st.write("Generating meal plan...")
    gender = st.text_input("What's your gender?")
    age = st.number_input("What's your age?")
    weight = st.number_input("What's your weight in kgs?")
    height = st.number_input("What's your height in cm?")
    goal = st.text_input("What's your current fitness goal?")
    activity_level = st.text_input("What's your activity leve? (sedentary, lightly active, somewhat active, highly active, athlete)")
    submit = st.form_submit_button("Generate Meal Plan")
if submit:
    generate_meal_plan(age, weight, height, goal, activity_level)
# OpenAI API Key


# Function to save the image


