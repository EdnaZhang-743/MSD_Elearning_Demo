# MSD E-Learning Demo

A lightweight, low-code Streamlit prototype of an e-learning management system (LMS) for musculoskeletal disorder (MSD) and ergonomics training.

It allows learners to watch training videos, take quick quizzes, and track progress — all without any database setup.

---

## 🚀 Quick Start 

Follow these steps to get the application running on your local machine.

#### 1. Environment Setup
Clone or download the repository:
```bash
git clone https://github.com/EdnaZhang-743/MSD_Elearning_Demo.git
cd MSD_Elearning_Demo
```
(Optional) Create a virtual environment：
```bash
python -m venv .venv
```
*   For Windows:
    ```bash
    .venv\Scripts\activate
    ```
*   For macOS/Linux:
    ```bash
    source .venv/bin/activate
    ```
Install dependencies：
```bash
pip install streamlit pandas

# or

pip install -r requirements.txt
```

#### 2. Run the App 
```bash
streamlit run app.py
```
Then open your browser at 👉 http://localhost:8501

---

## 🧭 How to Use

Left Sidebar Navigation

#### 1 – Courses 
view learning modules with YouTube videos and downloadable materials.

#### 2 – Quiz
take a short knowledge check with automatic scoring.

#### 3 – Progress
review data-flow explanation and extension ideas (e.g., sync to Google Sheets).

---

## 📁 Project Structure
```bash
MSD_Elearning_Demo/
├─ app.py
├─ data/
│  ├─ lessons.csv     # course list
│  └─ quiz.csv        # quiz questions
└─ assets/
   └─ guide.pdf       # example downloadable material
```
lessons.csv
Column	Description
id	Unique course ID
title	Lesson name
description	Short text shown under the lesson
video_url	YouTube video link
material	File name in /assets folder

Example

id,title,description,video_url,material
1,Lifting Techniques,Basic lifting and posture training for manual handling,https://www.youtube.com/watch?v=dQw4w9WgXcQ,guide.pdf
2,Pushing & Pulling,How to safely push or pull objects to reduce MSD risk,https://www.youtube.com/watch?v=3fumBcKC6RE,guide.pdf
3,Repetitive Tasks,Reduce upper-limb strain and fatigue with micro-breaks and neutral posture,https://www.youtube.com/watch?v=K4TOrB7at0Y,guide.pdf

quiz.csv
Column	Description
id	Unique question ID
question	Question text
option_a/b/c	Three options
correct	Correct answer (A/B/C)

Example

id,question,option_a,option_b,option_c,correct
1,"What is the safest back posture for lifting?","Keep back straight","Bend and twist","Hold breath",A
2,"When pushing loads, what should you prioritize?","Use leg strength","Pull with arms","Lean backward",A
3,"To reduce repetitive strain, you should:","Work longer hours","Take regular micro-breaks","Ignore discomfort",B

---

## 🧩 Extension Ideas

✅ Sync results to Google Sheets for shared progress
✅ Add login by user email and save scores per learner
✅ Host on Streamlit Cloud or Render for live demo
✅ Use local or Google Sheets-based storage for real data tracking
