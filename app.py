import streamlit as st
import pandas as pd
import csv
from pathlib import Path

st.set_page_config(page_title="MSD E-Learning Demo", page_icon="🎓", layout="wide")

DATA_DIR = Path("data")
ASSETS_DIR = Path("assets")

@st.cache_data
def load_lessons():
    # lessons.csv: id,title,description,video_url,material
    return pd.read_csv(DATA_DIR / "lessons.csv")

@st.cache_data
def load_quiz():
    # quiz.csv: id,question,option_a,option_b,option_c,correct
    return pd.read_csv(DATA_DIR / "quiz.csv", quoting=csv.QUOTE_MINIMAL)

st.sidebar.title("📚 MSD E-Learning Portal")
page = st.sidebar.radio("Navigation", ["Courses", "Quiz", "Progress"])

# Course page
if page == "Courses":
    st.title("🎥 Ergonomics & MSD Learning Modules")
    try:
        lessons = load_lessons()
    except Exception as e:
        st.error(f"Failed to load lessons.csv: {e}")
        st.stop()

    if lessons.empty:
        st.warning("No lessons found. Please check data/lessons.csv")
    else:
        # If id is missing or has a null value, use the row number as a fallback key
        for idx, row in lessons.reset_index(drop=True).iterrows():
            row_id = str(row["id"]) if ("id" in row and pd.notna(row["id"])) else f"row{idx}"

            with st.expander(f"📘 {row.get('title','(untitled)')}", expanded=False):  # You can also add a key to the expander
                st.write(row.get("description", ""))

                # video
                url = str(row.get("video_url", "") or "").strip()
                if url:
                    st.video(url)

                # Download data (be sure to add a unique key)
                material = str(row.get("material", "") or "").strip()
                if material:
                    file_path = ASSETS_DIR / material
                    if file_path.exists():
                        st.download_button(
                            label="📄 Download Material",
                            data=open(file_path, "rb").read(),
                            file_name=material,
                            key=f"dl_{row_id}",     # unique key
                        )
                    else:
                        st.info(f"Material not found: {material}")

# quiz page
elif page == "Quiz":
    st.title("🧠 Quick Knowledge Check")

    try:
        quiz = load_quiz()
    except Exception as e:
        st.error(f"Failed to load quiz.csv: {e}")
        st.stop()

    if quiz.empty:
        st.warning("No quiz found. Please check data/quiz.csv")
    else:
        score = 0
        answers = {}
        with st.form("quiz_form"):
            for _, row in quiz.iterrows():
                options = [row["option_a"], row["option_b"], row["option_c"]]
                ans = st.radio(
                    row["question"],
                    options,
                    key=f"q_{row['id']}",  # unique key
                )
                answers[row["id"]] = ans
            submitted = st.form_submit_button("Submit")

        if submitted:
            for _, row in quiz.iterrows():
                correct_opt = row[f"option_{row['correct'].lower()}"]
                if answers[row["id"]] == correct_opt:
                    score += 1
            st.success(f"✅ You scored {score}/{len(quiz)}")

            # show correct answer
            with st.expander("Show Answers"):
                for _, row in quiz.iterrows():
                    correct_opt = row[f"option_{row['correct'].lower()}"]
                    st.write(f"- {row['question']} → **{row['correct']}** ({correct_opt})")

# Progress Page (Example Description)
else:
    st.title("📊 Learning Progress")
    st.write("This demo uses CSV-only storage. You can extend it to:")
    st.markdown("""
- ✅ Sync to **Google Sheets** (for multi-device update)  
- ✅ Host videos on **YouTube** / company Drive  
- ✅ Export quiz results to CSV / Sheets  
    """)
    st.info("Tip: Track completion by appending a local CSV per user email/session in a real deployment.")
