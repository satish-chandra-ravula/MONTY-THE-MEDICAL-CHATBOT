# MONTY-THE-MEDICAL-CHATBOT
MONTY THE MEDICAL CHATBOT
                                          
Introduction
In today’s fast-paced world, access to quick and reliable medical advice is essential. MONTY THE MEDICAL CHATBOT is an AI-powered health assistant designed to provide instant general medical guidance and automated health reminders every 30 minutes. Using Google Gemini AI, this chatbot can answer medical queries, suggest healthy habits, and keep users informed about their well-being.
Whether it's reminding you to stay hydrated, take breaks, or provide general health guidance, Monty acts as a virtual health companion.
Project Description
Monty is a real-time AI medical chatbot built using Streamlit for a simple and user-friendly interface. The chatbot utilizes Google Gemini AI to process medical queries and respond with general guidance. Additionally, it includes a time-based health recommendation system that provides users with wellness tips every 30 minutes, encouraging healthy habits throughout the day.
Key Highlights
 AI-powered medical chatbot 
 Automated health reminders based on the current time 
 Simple & interactive interface with Streamlit
Features
•	AI-Powered Health Advice – Answers user queries related to symptoms, health concerns, and general medical guidance.
•	Time-Based Health Reminders – Suggests healthy activities every 30 minutes (e.g., drinking water, taking breaks, eating snacks).
•	User-Friendly UI – Built with Streamlit for easy access and interaction.
•	Safe & Secure – Does not diagnose or prescribe medicine but provides general guidance.
•	Runs Locally – No need for an external server or database.
Technology Stack
•	Programming Language – Python 
•	Frontend Framework – Streamlit 
•	AI Model – Google Gemini AI (gemini-1.5-pro-latest) 
•	Time Management – datetime & pytz 
Installation & Setup
Follow these steps to set up and run MONTY THE MEDICAL CHATBOT:
Step 1: Install Dependencies
Ensure you have Python 3.8+ installed, then run:
pip install google-generativeai streamlit pytz
Step 2: Set API Key
Replace "YOUR_GEMINI_API_KEY" in the code with your Google Gemini API Key.
Step 3: Run the Application
Save the script as monty_chatbot.py and execute:
streamlit run monty_chatbot.py
How It Works
1.	User enters a medical question in the chat input field.
2.	The Google Gemini AI model processes the query and generates a response.
3.	Every 30 minutes, a health reminder appears based on the current time.
4.	The response and reminder are displayed on the Streamlit UI.
Example Interactions
User Query: "I have a headache. What should I do?"
AI Response:
•	Possible causes: dehydration, stress, lack of sleep.
•	Preventive measures: stay hydrated, get enough rest, avoid screen strain.
•	When to see a doctor: if persistent for more than 3 days or severe pain occurs.
Health Reminder at 10 AM:
•	 "Time to hydrate! Drink a glass of water."
Health Reminder at 3 PM:
•	"Feeling tired? Try deep breathing exercises for relaxation."
Future Enhancements
•	Voice Command Support – Users can speak instead of typing.
•	Multi-Language Support – Responses in different languages.
•	Advanced Symptom Analysis – More detailed AI-driven health insights.
•	Mobile App Integration – Deploy as a mobile app.

Limitations & Disclaimers
 Medical Disclaimer:
•	Monty does not replace professional medical advice. Always consult a doctor for serious health concerns.
•	The chatbot provides general health information but does not diagnose or prescribe medication.
 Technical Limitations:
•	Requires internet access for API calls.
•	Limited to text-based responses (no voice output).


Conclusion
MONTY THE MEDICAL CHATBOT is a simple yet powerful tool for promoting health awareness and providing quick, AI-driven medical advice. With automated health reminders and AI-powered insights, Monty helps users stay informed, hydrated, and healthy throughout the day.
 Try it now and make health a priority! 

