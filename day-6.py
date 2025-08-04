import streamlit as st
import google.generativeai as genai
import datetime
import pytz


genai.configure(api_key="AIzaSyAE9_isBkWtFQOU8Lv7nHzgGzzKXc2XbEo")


def ask_gemini_about_health(health_query):
    
    restricted_keywords = ["symptoms", "disease", "treatment", "medicine", "doctor", "health", "diagnosis"]
    if not any(keyword in health_query.lower() for keyword in restricted_keywords):
        return "⚠️ Sorry, I can only provide medical-related information. Please refine your query."

    prompt = (
        f"You are an AI assistant specialized in medical guidance. "
        f"For the following query: '{health_query}', provide relevant information such as possible causes, "
        f"preventive measures, and when to seek medical attention. Avoid prescribing medication."
    )

    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest") 
        response = model.generate_content(prompt)
        return response.text if response else "⚠️ Sorry, I couldn't find relevant health details."
    except Exception as e:
        return f"❌ Error: {str(e)}"


def get_health_recommendation():
   
    tz = pytz.timezone("Asia/Kolkata")
    current_time = datetime.datetime.now(tz).strftime("%I:%M %p")  
    hour = datetime.datetime.now(tz).hour

    
    health_tips = {
        6: "🌅 Good morning! Start your day with a glass of warm water. 💧",
        7: "🌞 Time for a healthy breakfast! Include fruits and proteins. 🍎🥚",
        8: "💪 Do some stretching or a short walk for better energy. 🚶",
        9: "📖 If working, take a short break and stretch your muscles. 🧘",
        10: "💧 Time to hydrate! Drink a glass of water. 💦",
        11: "🍵 A healthy snack like nuts or yogurt will boost energy. 🥜🍦",
        12: "🍽️ It's lunchtime! Eat a balanced meal with proteins and greens. 🥗",
        13: "😴 A short 10-minute break can improve productivity. 💤",
        14: "💧 Drink another glass of water to stay hydrated. 🚰",
        15: "🧘‍♂️ If feeling tired, try deep breathing exercises. 🌬️",
        16: "🍏 Eat a fruit or a small snack to avoid energy dips. 🍌",
        17: "🚶 Time for an evening walk! Get some fresh air. 🌳",
        18: "🌇 Wind down, reduce screen time, and relax. 🎧",
        19: "🍲 Have a light and nutritious dinner. 🍛",
        20: "💤 Reduce caffeine intake to sleep better. ☕🚫",
        21: "📖 Read something relaxing or meditate before bed. 🛌",
        22: "🌙 It's bedtime! Aim for 7-8 hours of sleep. 😴"
    }

    
    recommendation = health_tips.get(hour, "💡 Stay healthy! Listen to your body and take care.")
    return f"🕒 {current_time}: {recommendation}"


st.title("🩺 Monty The Medical Chatbot")
st.write("Ask any health-related question, and I'll provide general medical guidance.")


st.subheader("💡 Health Tip for You:")
st.write(get_health_recommendation())


user_query = st.text_input("Enter your medical question here:")

if st.button("Get Advice"):
    if user_query.strip():
        response = ask_gemini_about_health(user_query)
        st.subheader("🩺 AI Response:")
        st.write(response)
    else:
        st.warning("⚠️ Please enter a medical-related question.")




st.markdown("---")
st.markdown("🔬 **Note:** Please consult a doctor for professional advice.")
st.markdown("---")

st.markdown("© 2025 Monty The Medical Chatbot. All rights reserved to Sateesh.", unsafe_allow_html=True)