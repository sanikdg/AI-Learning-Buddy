%%writefile app.py

import streamlit as st
import google.generativeai as genai

# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="📘",
    layout="wide"
)

# ==================================================
# GEMINI API CONFIGURATION
# ==================================================

# Replace with your NEW Gemini API Key
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

.main{
    background-color:#F5F7FA;
}

h1,h2,h3{
    color:#1F4E79;
}

.stButton>button{
    width:100%;
    height:50px;
    border-radius:10px;
    font-size:16px;
    font-weight:bold;
}

.response-box{
    background:#FFFFFF;
    padding:20px;
    border-radius:12px;
    border:1px solid #E0E0E0;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("⚙️ AI Learning Buddy")

persona = st.sidebar.text_input(
    "AI Persona",
    value="Code Coach"
)

topic = st.sidebar.selectbox(
    "Choose Learning Topic",
    [
        "Machine Learning",
        "Operating Systems",
        "Database Management System (DBMS)",
        "Computer Networks",
        "Python Programming",
        "Data Structures",
        "Artificial Intelligence"
    ]
)

st.sidebar.markdown("---")

st.sidebar.success("✅ Gemini API Connected")

# ==================================================
# MAIN PAGE
# ==================================================

st.title("📘 AI Learning Buddy")

st.write("""
Welcome to **AI Learning Buddy**!

This application uses **Google Gemini AI** to help students learn concepts in a simple and interactive way.

### Features
- 🤖 Ask AI
- 📖 Explain Topic
- 🌍 Real-Life Examples
- 📝 Quiz Generator
- 💡 Study Tips
""")

st.header("💬 Ask Your Question")

question = st.text_input(
    "Enter your question"
)

# ==================================================
# BUTTONS
# ==================================================

col1, col2 = st.columns(2)

with col1:
    explain = st.button("📖 Explain Topic")

with col2:
    example = st.button("🌍 Real-Life Example")

col3, col4 = st.columns(2)

with col3:
    quiz = st.button("📝 Quiz")

with col4:
    tips = st.button("💡 Study Tips")

ask = st.button("🚀 Ask AI")

# ==================================================
# GEMINI FUNCTION
# ==================================================

def get_response(prompt):
    try:
        with st.spinner("🤖 Gemini is thinking..."):
            response = model.generate_content(prompt)
            return response.text
    except Exception as e:
        return f"⚠️ Error: {e}"

st.divider()
# ==================================================
# ASK AI
# ==================================================

if ask:

    if question.strip() == "":
        st.warning("⚠️ Please enter a question.")
    else:

        prompt = f"""
You are an AI tutor named {persona}.

Your task is to teach students in a simple and beginner-friendly way.

Topic:
{topic}

Student Question:
{question}

Instructions:
- Explain in simple language.
- Give examples whenever possible.
- Use bullet points if needed.
- Keep the explanation easy to understand.
"""

        answer = get_response(prompt)

        st.subheader("🤖 AI Response")
        st.markdown(answer)

# ==================================================
# EXPLAIN TOPIC
# ==================================================

if explain:

    prompt = f"""
You are {persona}.

Explain the topic '{topic}' from scratch.

Include:

1. Definition
2. Why it is important
3. Key Concepts
4. Advantages
5. Disadvantages
6. Applications
7. Interview Questions
8. Summary

Explain everything in simple language suitable for beginners.
"""

    answer = get_response(prompt)

    st.subheader("📖 Topic Explanation")
    st.markdown(answer)

# ==================================================
# REAL LIFE EXAMPLES
# ==================================================

if example:

    prompt = f"""
Give 5 real-life examples of {topic}.

For each example explain:

• Where it is used
• Why it is useful
• How it works

Keep the explanation simple.
"""

    answer = get_response(prompt)

    st.subheader("🌍 Real-Life Examples")
    st.markdown(answer)

# ==================================================
# QUIZ
# ==================================================

if quiz:

    prompt = f"""
Generate a quiz on {topic}.

Create 5 Multiple Choice Questions.

Each question should contain:

Question

A)

B)

C)

D)

At the end provide the correct answers separately.

Difficulty:
Beginner to Intermediate.
"""

    answer = get_response(prompt)

    st.subheader("📝 Quiz")
    st.markdown(answer)

# ==================================================
# STUDY TIPS
# ==================================================

if tips:

    prompt = f"""
Give the best study plan for learning {topic}.

Include:

• Daily Study Plan
• Best YouTube Resources
• Books
• Websites
• Common Mistakes
• Revision Strategy
• Interview Preparation Tips
• Practice Suggestions

Keep everything beginner friendly.
"""

    answer = get_response(prompt)

    st.subheader("💡 Study Tips")
    st.markdown(answer)
    # ==================================================
# QUICK LEARNING CARDS
# ==================================================

st.divider()

st.header("📚 Quick Learning Guide")

col1, col2 = st.columns(2)

with col1:

    st.info("""
### 🤖 Machine Learning

• Supervised Learning

• Unsupervised Learning

• Reinforcement Learning

• Classification

• Regression
""")

with col2:

    st.info("""
### 💻 Computer Science Subjects

• Operating Systems

• Database Management System

• Computer Networks

• Python Programming

• Data Structures

• Artificial Intelligence
""")

# ==================================================
# HOW TO USE
# ==================================================

st.divider()

st.header("📖 How to Use this Application")

st.markdown("""
1️⃣ Select an AI Persona.

2️⃣ Choose a learning topic.

3️⃣ Ask your own question.

4️⃣ Or use the feature buttons:

- 📖 Explain Topic

- 🌍 Real-Life Example

- 📝 Quiz

- 💡 Study Tips

The AI will generate beginner-friendly responses using Google Gemini.
""")

# ==================================================
# FEATURES
# ==================================================

st.divider()

st.header("✨ Features")

feature1, feature2, feature3 = st.columns(3)

with feature1:
    st.success("""
### 🤖 AI Tutor

Ask any question and receive simple, easy-to-understand explanations.
""")

with feature2:
    st.success("""
### 📝 Quiz Generator

Generate multiple-choice quizzes instantly for practice.
""")

with feature3:
    st.success("""
### 💡 Smart Study Tips

Receive study plans, resources, interview tips, and revision strategies.
""")

# ==================================================
# TECHNOLOGIES USED
# ==================================================

st.divider()

st.header("🛠 Technologies Used")

st.markdown("""
- Python

- Streamlit

- Google Gemini API

- Google Colab

- ngrok
""")

# ==================================================
# FOOTER
# ==================================================

st.divider()

st.markdown("""
---
### 🎓 AI Learning Buddy

Developed using **Python**, **Streamlit**, and **Google Gemini API**.

This application provides an interactive AI-powered learning experience by helping students understand concepts, generate quizzes, view real-life examples, and receive study tips.

**Project Developed for AI Empower Her**
""")
