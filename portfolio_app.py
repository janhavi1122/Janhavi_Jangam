import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Janhavi Jangam | Data Scientist", page_icon="🧠", layout="wide")

# ---------- BACKGROUND STYLE ----------
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1557683316-973673baf926");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: white;
}
[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0);
}
h1, h2, h3, h4 {
    color: #FFFFFF;
}
.stMarkdown {
    color: white;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<h1 style='text-align: center; font-size: 3.5em;'>Hi, I'm Janhavi Santosh Jangam 👩‍💻</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #c4f0ff;'>Data Scientist | ML Engineer | GenAI Developer</h3>", unsafe_allow_html=True)
st.markdown("---")

# ---------- ABOUT ME ----------
with st.container():
    st.subheader("🚀 About Me")
    st.write("""
        I'm **Janhavi Santosh Jangam**, a highly motivated and enthusiastic Data Scientist with over 2 years of practical experience working at **Sanjivani Artificial Intelligence Lab**, 
        under the mentorship of **Dr. Radhakrishna Naik (Senior Data Scientist)**.

        I've actively worked on various real-world AI/ML projects ranging from traditional regression models to advanced GenAI applications using tools like **LangChain, OpenAI, and FastAPI**.

        📌 **Internships**:
        - **Oasis Infobyte** – Performed machine learning tasks such as Sales Prediction, Car Price Prediction, and Stock Forecasting.
        - **Cognifyz Technologies** – Worked on customer analytics, feature engineering, and geospatial data analysis.
        - **PRASUNET** – Focused on advanced NLP & generative AI projects during July 2024.
        - Completed 10+ mini-projects and hackathons during my academic and internship tenure.

        💡 I am passionate about creating intelligent systems that solve real-world problems, whether it's through predictive analytics, NLP, computer vision, or generative AI models.
        I also love deploying my work using **Streamlit** and **FastAPI** for real-time interactive usage.
    """)

# ---------- PROJECTS ----------
st.subheader("💼 Projects")
st.markdown("""
1. **🧾 Sales Prediction**  
   - Developed regression models using Scikit-learn to predict retail sales.  
   - Included EDA, feature selection, and model evaluation.  
   - Deployed using Streamlit.  
   - [GitHub](https://github.com/)

2. **🚗 Car Price Prediction**  
   - Built ML pipeline for predicting used car prices.  
   - Addressed missing values, outliers, and applied multiple regression techniques.  
   - [GitHub](https://github.com/)

3. **🧠 LangChain Q&A App**  
   - Created a robust app using LangChain + OpenAI to extract answers from PDF/Word files.  
   - Used FAISS vector store and deployed via FastAPI, LangServe, and LangSmith.  
   - [GitHub](https://github.com/)

4. **📈 Stock Price Prediction**  
   - Forecasted Google stock prices using models like LSTM, KNN, Linear Regression, and Random Forest.  
   - Plotted trend graphs with Matplotlib and Seaborn.  
   - [GitHub](https://github.com/)

5. **🔌 Load Forecasting using ARIMA**  
   - Utilized ARIMA for energy load prediction from real-time datasets.  
   - Tuned hyperparameters (p,d,q) and validated performance using AIC/BIC.  
   - [GitHub](https://github.com/)
""")

# ---------- SKILLS ----------
st.subheader("🧰 Skills")

skill_sets = {
    "📊 Programming": "Python, SQL, HTML",
    "📚 ML & Stats": "Scikit-learn, XGBoost, Regression, Classification",
    "🧠 Deep Learning": "TensorFlow, Keras, CNN, LSTM",
    "🗣️ NLP & GenAI": "spaCy, NLTK, Transformers, LangChain, LangServe, LangSmith, LLM",
    "📈 Time Series": "ARIMA, LSTM, Prophet",
    "🚀 Deployment": "Streamlit, FastAPI, Uvicorn",
    "🧰 Tools & IDEs": "VS Code, Git, Jupyter, Google Colab",
    "🔍 Data Viz & EDA": "Matplotlib, Seaborn, Plotly"
}

skill_cols = st.columns(2)
for i, (key, val) in enumerate(skill_sets.items()):
    with skill_cols[i % 2]:
        st.markdown(f"**{key}**")
        st.write(val)

# ---------- RESUME ----------
st.markdown("### 📄 Resume & Certifications")
st.markdown("- 📎 [Download Resume](https://your-link.com)")
st.markdown("- ✅ Certifications: Oasis Infobyte, Cognifyz, Prasunet, Coursera, Kaggle")

# ---------- CONTACT ----------
st.markdown("### 📬 Get In Touch")
st.markdown("📞 **Phone:** 7756047085")
st.markdown("📧 **Email:** janhavijangam1122@gmail.com")
st.markdown("🌐 [LinkedIn](https://www.linkedin.com/in/janhavi-jangam-12b7a8228) | [GitHub](https://github.com/janhavi1122)")

# ---------- FOOTER ----------
st.markdown("---")
st.markdown("<p style='text-align: center; color: white;'>Made with ❤️ using Streamlit | © 2025 Janhavi Santosh Jangam</p>", unsafe_allow_html=True)
