from dotenv import load_dotenv
import os
import requests
import streamlit as st

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


# Function to generate meal plan
def generate_meal_plan(user_id, age, weight, height, goal, activity_level, cuisine, restrictions):
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
                        "text": "You are a professional world-class personal trainer and dietician. Your job is to craft a personalized meal plan for the user based on the information they provide you with. Estimate the number of calories the user should eat and provide the number of calories for each meal. Provide exact instructions and ingredients, along with measurements and repeat it for each day of the week. The output should be only HTML code for a table that contains the meal plan. The rows should be the days of the week and the columns should be the meals of the day. DO NOT OUTPUT MARKDOWN, ONLY THE HTML CODE AND NOTHING ELSE BEFORE OR AFTER IT. FOR EXAMPLE, DONT INCLUDE ```html BEFORE THE CODE. Put the ingredients in bullet points and put the instructions in a numbered list. Make the instructions concise and brief - if needed, combine multiple steps into one step and include calories and protein for each meal"
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"Gender: {gender}\nAge: {age}\nWeight: {weight} kgs\nHeight: {height} cm\nGoal: {goal}\nActivity level: {activity_level}\nPreferred Cuisine: {cuisine}\nDietary Restrictions: {restrictions}"
                    }
                ]
            }
        ],
        "max_tokens": 4000,
        "temperature": 0
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    meal_plan_content = response.json().get("choices")[0].get("message").get("content")
    print(meal_plan_content)
    st.markdown(meal_plan_content, unsafe_allow_html=True)

# Streamlit app
st.set_page_config(
    page_title="Meal Plan Builder",
    page_icon="🍳",
)

st.title("MealFit - Personalized Meal Plan Builder")


st.write("Provide your information to generate a personalized meal plan.")
with st.form(key="user_input", clear_on_submit=False):
    gender = st.text_input("What's your gender?")
    age = st.text_input("What's your age?")
    weight = st.text_input("What's your weight in kgs?")
    height = st.text_input("What's your height in cm?")
    goal = st.text_input("What's your current fitness goal?")
    activity_level = st.text_input("What's your activity level? (sedentary, lightly active, somewhat active, highly active, athlete)")
    cuisine = st.text_input("What's your preferred cuisine? (optional)")
    restrictions = st.text_input("Any dietary restrictions? (optional)")
    submit = st.form_submit_button("Generate Meal Plan")
if submit:
    generate_meal_plan(gender, age, weight, height, goal, activity_level, cuisine, restrictions)
