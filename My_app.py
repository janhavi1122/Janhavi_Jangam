import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Janhavi Jangam | Data Scientist", page_icon="🧠", layout="wide")

# ---------- BACKGROUND STYLE ----------
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #0F2027;
    background-image: linear-gradient(to right, #2C5364, #203A43, #0F2027);
    color: white;
}
[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0);
}
h1, h2, h3, h4, h5, h6 {
    color: #00FFFF;
}
.stMarkdown, .stText, .stSubheader {
    color: white;
}
a {
    color: #FFDD00 !important;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<h1 style='text-align: center; font-size: 3.5em;'>Hi, I'm Janhavi Santosh Jangam 👩‍💻</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #c4f0ff;'>Data Scientist | AIML Engineer | GenAI Developer</h3>", unsafe_allow_html=True)
st.markdown("---")

# ---------- ABOUT ME ----------
with st.container():
    st.subheader("🚀 About Me")
    st.write("""
        I'm **Janhavi Santosh Jangam**, a Data Scientist and Machine Learning Engineer specializing in developing scalable AI solutions leveraging advanced statistical modeling, machine learning, and deep learning techniques.

        My expertise spans:
        - **Supervised & Unsupervised Learning:** Regression, classification, clustering, and anomaly detection.
        - **Deep Learning Architectures:** CNNs, LSTMs, and transformers applied to time-series forecasting, NLP, and computer vision.
        - **Natural Language Processing & Generative AI:** Implementing state-of-the-art transformer models, LangChain pipelines, and retrieval-augmented generation (RAG).
        - **Data Engineering & Deployment:** Building end-to-end pipelines, optimizing feature engineering, and deploying ML models with FastAPI, Streamlit, Docker, and LangServe.
        - **Model Monitoring & Experiment Tracking:** Utilizing LangSmith and MLFlow for model versioning, debugging, and performance analysis.

        I've contributed to over 15 real-world projects including sales forecasting, car price prediction, document-based Q&A systems, stock market prediction, load forecasting, and computer vision applications such as YOLOv8-based damage detection.

        I am passionate about transforming complex datasets into actionable insights and production-ready applications that drive business value.

        Currently, I am further enhancing my skills in generative AI, model interpretability, and scalable ML operations to push the boundaries of AI-driven solutions.
    """)


# ---------- PROJECTS ----------
st.subheader("💼 Projects")
st.markdown("""
### 1. **🧾 Sales Prediction**
- Built predictive regression models (Linear, Ridge, Lasso, Decision Tree) on sales data.
- Carried out advanced **EDA**, feature engineering, and correlation analysis.
- Created an intuitive **Streamlit dashboard** for exploring predictions based on user input.
- Metrics: **RMSE, MAE, R-squared**.
- 🔗 [GitHub](https://github.com/janhavi1122/Oasis_Task5_sales_prediction)

### 2. **🚗 Car Price Prediction**
- End-to-end pipeline for predicting used car prices based on mileage, fuel type, seller type, etc.
- Treated missing data, removed outliers (IQR), and scaled features.
- Deployed regression models: **Linear, Random Forest, Decision Tree**.
- Explained model decisions with **feature importance plots**.
- 🔗 [GitHub](https://github.com/janhavi1122/Oasis_Task3_Car_price_prediction)

### 3. **🧠 LangChain Q&A App**
- Created a document-based QA system using **LangChain + OpenAI** for PDF/Word files.
- Embedded documents using **streanlit + OpenAIEmbeddings**.
- Deployed backend using **streamlit**, served via **LangServe**, monitored via **LangSmith**.
- Can answer questions contextually, using **retrieval-augmented generation (RAG)**.

### 4. **📈 Stock Price Prediction**
- Forecasted **Google stock prices** using **LSTM, KNN, Linear Regression, Random Forest**.
- Performed **hyperparameter tuning** and visualized future trends with **Seaborn**.
- Included lag features, moving averages, and stationarity tests.
- 🔗 [GitHub](https://github.com/janhavi1122/Stock-price-prediction)

### 5. **🔌 Load Forecasting using ARIMA**
- Used **ARIMA** to forecast energy consumption patterns from real-time datasets.
- Conducted ADF tests, AIC/BIC score tuning, residual analysis.
- Compared ARIMA with **LSTM** for long-term energy forecasting.
- 🔗 [GitHub](https://github.com/janhavi1122/Load-forecasting-using-ML-LSTM-)

### 6. **🛠️ Car Damage Detection using YOLOv8**
- Built a **YOLOv8-powered real-time app** to detect and localize car damages.
- Used **OpenCV** to draw bounding boxes and extract region features.
- Created an **interactive Streamlit UI** to upload images and generate annotated results.
- Exports **PDF report** with **FPDF** containing damage details, confidence scores, and visuals.
- 🔗 [GitHub](https://github.com/janhavi1122/Janhavi_Jangam)
""")

# ---------- SKILLS ----------
st.subheader("🧰 Skills")

skill_sets = {
    "📊 Programming": "Python, SQL, HTML",
    "📚 ML & Stats": "Scikit-learn, XGBoost, Regression, Classification, Clustering",
    "🧠 Deep Learning": "TensorFlow, Keras, CNN, LSTM, Transfer Learning",
    "🗣️ NLP & GenAI": "spaCy, NLTK, Transformers, HuggingFace, LangChain, LangServe, LangSmith",
    "📈 Time Series": "ARIMA, SARIMA, Prophet, LSTM",
    "🚀 Deployment": "Streamlit, FastAPI, Uvicorn, Docker",
    "🧰 Tools & IDEs": "VS Code, Git, Jupyter, Google Colab, PyCharm",
    "🔍 Data Viz & EDA": "Matplotlib, Seaborn, Plotly, Power BI",
    "🧪 Testing & Monitoring": "LangSmith, MLFlow, Cross-Validation, A/B Testing",
    "📦 Version Control": "Git, GitHub, GitLab",
    "🔍 ML Utilities": "GridSearchCV, Pipelines, Feature Scaling, OneHotEncoder"
}

skill_cols = st.columns(2)
for i, (key, val) in enumerate(skill_sets.items()):
    with skill_cols[i % 2]:
        st.markdown(f"**{key}**")
        st.write(val)

# ---------- RESUME ----------
st.markdown("### 📄 Resume & Certifications")
st.markdown("- 📎 [Download Resume](https://your-link.com)")
st.markdown("- ✅ **Certifications**: Oasis Infobyte, Cognifyz, Prasunet, Coursera, Kaggle, DeepLearning.AI")

# ---------- CONTACT ----------
st.markdown("### 📬 Get In Touch")
st.markdown("📞 **Phone:** 7756047085")
st.markdown("📧 **Email:** janhavijangam1122@gmail.com")
st.markdown("🌐 [LinkedIn](https://www.linkedin.com/in/janhavi-jangam-12b7a8228) | [GitHub](https://github.com/janhavi1122)")

# ---------- FOOTER ----------
st.markdown("---")
st.markdown("<p style='text-align: center; color: #CCCCCC;'>Made with ❤️ using Streamlit | © 2025 Janhavi Santosh Jangam</p>", unsafe_allow_html=True)
