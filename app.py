import streamlit as st
import random
import pickle

# ---------------- UI STYLE ---------------- #

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');

[data-testid="stAppViewContainer"]{
background-color:#F5F7FB;
font-family:'Inter',sans-serif;
}

h1,h2,h3{
color:#1F2937;
}

p,label,div{
color:#374151;
}

input{
background:white !important;
color:#111827 !important;
}

.stButton>button{
background-color:#4A6CF7;
color:white;
border-radius:10px;
padding:10px 20px;
border:none;
font-weight:500;
}

.stButton>button:hover{
background-color:#3A56D4;
}

.stProgress > div > div{
background-color:#7C3AED;
}

</style>
""", unsafe_allow_html=True)

# ---------------- MODEL ---------------- #

with open("lie_detector_model.pkl","rb") as f:
    model = pickle.load(f)

# ---------------- TITLE ---------------- #

st.title("🧠 AI Mind Reader Game")

st.write("Answer questions and the AI will analyze your behavior.")

# ---------------- QUESTIONS ---------------- #

questions = [

"Do you usually start assignments early?",
"Do you often delay tasks until the last moment?",
"Do you check your phone while studying?",
"Do you sleep later than you planned?",
"Do you sometimes skip workouts?",
"Do you drink enough water daily?",
"Do you feel stressed before exams?",
"Do you scroll social media before sleeping?",
"Do you get distracted easily while studying?",
"Do you follow a strict routine?",
"Do you sometimes lie to avoid trouble?",
"Do you keep promises you make to yourself?",
"Do you feel guilty after procrastinating?",
"Do you stay focused for long periods?"

]

# ---------------- SESSION STATE ---------------- #

if "traits" not in st.session_state:

    st.session_state.traits = {
        "procrastination":0,
        "discipline":0,
        "phone_addiction":0
    }

if "game_running" not in st.session_state:
    st.session_state.game_running = True

if "question_count" not in st.session_state:
    st.session_state.question_count = 0

# ---------------- GAME STOPPED ---------------- #

if not st.session_state.game_running:

    st.success("🧠 AI Analysis Complete")

    traits = st.session_state.traits

    st.write(f"### 📊 Questions answered: {st.session_state.question_count}")

    if traits["procrastination"] > 2:
        st.write("⚠️ You tend to procrastinate under pressure.")

    if traits["phone_addiction"] > 1:
        st.write("📱 Your phone distracts you more than you realize.")

    if traits["discipline"] > 2:
        st.write("💪 You are quite disciplined.")

    accuracy = random.randint(75,95)

    st.write(f"### Mind Reading Accuracy: {accuracy}%")

    st.progress(accuracy)

    if st.button("Restart Game"):
        st.session_state.clear()
        st.rerun()

# ---------------- GAME RUNNING ---------------- #

else:

    st.write(f"### Questions answered: {st.session_state.question_count}")

    question = random.choice(questions)

    st.subheader(question)

    answer = st.text_input("Your answer")

    if st.button("Analyze Answer"):

        prediction = model.predict([answer])[0]
        probs = model.predict_proba([answer])[0]

        truth_prob = probs[list(model.classes_).index("truth")]
        lie_prob = probs[list(model.classes_).index("lie")]

        st.write("### AI Analysis")

        st.write(f"Lie probability: {lie_prob:.2f}")
        st.progress(int(lie_prob*100))

        st.write(f"Truth probability: {truth_prob:.2f}")
        st.progress(int(truth_prob*100))

        if "sometimes" in answer or "often" in answer:
            st.session_state.traits["procrastination"] += 1

        if "always" in answer:
            st.session_state.traits["discipline"] += 1

        if "phone" in answer:
            st.session_state.traits["phone_addiction"] += 1

        if prediction == "lie":
            st.error("🚨 Lie detected!")
        else:
            st.success("🙂 Seems truthful")

        st.session_state.question_count += 1

    col1, col2 = st.columns(2)

    if col1.button("Next Question"):
        st.rerun()

    if col2.button("Stop Game"):
        st.session_state.game_running = False
        st.rerun()