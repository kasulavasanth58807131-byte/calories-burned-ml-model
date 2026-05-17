import streamlit as st
import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# ── Page Config ─────────────────────────────────────────────
st.set_page_config(
    page_title="Calories Burned Predictor",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Load Model & Data ────────────────────────────────────────
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

@st.cache_data
def load_data():
    with open("df.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()
df    = load_data()

# ── Custom CSS ───────────────────────────────────────────────
st.markdown("""
<style>
    .main-title {
        font-size: 2.4rem;
        font-weight: 800;
        background: linear-gradient(90deg, #FF6B6B, #FF8E53);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        color: #888;
        font-size: 1rem;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #1e1e2e, #2a2a3e);
        border-radius: 16px;
        padding: 1.2rem 1.5rem;
        text-align: center;
        border: 1px solid #3a3a5c;
    }
    .metric-value {
        font-size: 2.2rem;
        font-weight: 800;
        color: #FF6B6B;
    }
    .metric-label {
        font-size: 0.85rem;
        color: #aaa;
        margin-top: 0.2rem;
    }
    .result-box {
        background: linear-gradient(135deg, #FF6B6B, #FF8E53);
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        margin-top: 1rem;
        box-shadow: 0 8px 32px rgba(255,107,107,0.3);
    }
    .result-box h1 {
        color: white;
        font-size: 3.5rem;
        font-weight: 900;
        margin: 0;
    }
    .result-box p {
        color: rgba(255,255,255,0.85);
        font-size: 1.1rem;
        margin-top: 0.5rem;
    }
    .stButton > button {
        background: linear-gradient(90deg, #FF6B6B, #FF8E53);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        font-weight: 700;
        width: 100%;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255,107,107,0.4);
    }
    .info-badge {
        display: inline-block;
        background: #2a2a3e;
        border-radius: 8px;
        padding: 0.3rem 0.8rem;
        font-size: 0.8rem;
        color: #FF8E53;
        font-weight: 600;
        margin: 0.2rem;
        border: 1px solid #FF8E53;
    }
</style>
""", unsafe_allow_html=True)

# ── Header ───────────────────────────────────────────────────
st.markdown('<div class="main-title">🔥 Calories Burned Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Predict how many calories you burn during exercise using Machine Learning</div>', unsafe_allow_html=True)

# ── Dataset KPIs ─────────────────────────────────────────────
k1, k2, k3, k4 = st.columns(4)
with k1:
    st.markdown(f"""<div class="metric-card">
        <div class="metric-value">{len(df):,}</div>
        <div class="metric-label">Training Records</div>
    </div>""", unsafe_allow_html=True)
with k2:
    st.markdown(f"""<div class="metric-card">
        <div class="metric-value">99.95%</div>
        <div class="metric-label">Model Accuracy (R²)</div>
    </div>""", unsafe_allow_html=True)
with k3:
    st.markdown(f"""<div class="metric-card">
        <div class="metric-value">~1.0</div>
        <div class="metric-label">Mean Abs. Error (cal)</div>
    </div>""", unsafe_allow_html=True)
with k4:
    st.markdown(f"""<div class="metric-card">
        <div class="metric-value">XGBoost</div>
        <div class="metric-label">Best Model</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Two Columns: Input + Result ───────────────────────────────
left, right = st.columns([1, 1], gap="large")

with left:
    st.subheader("📋 Enter Your Details")

    gender = st.radio("Gender", ["Male", "Female"], horizontal=True)

    c1, c2 = st.columns(2)
    with c1:
        age    = st.slider("Age (years)", 10, 100, 30)
        height = st.slider("Height (cm)", 140, 220, 170)
        weight = st.slider("Weight (kg)", 30, 150, 70)
    with c2:
        duration   = st.slider("Exercise Duration (min)", 1, 60, 20)
        heart_rate = st.slider("Heart Rate (bpm)", 60, 200, 100)
        body_temp  = st.slider("Body Temperature (°C)", 36.0, 42.0, 40.0, step=0.1)

    predict_btn = st.button("🔥 Predict Calories Burned")

with right:
    st.subheader("🎯 Prediction Result")

    if predict_btn:
        gender_enc = 0 if gender == "Male" else 1
        input_data = pd.DataFrame([[gender_enc, age, height, weight,
                                    duration, heart_rate, body_temp]],
                                  columns=["Gender", "Age", "Height", "Weight",
                                           "Duration", "Heart_Rate", "Body_Temp"])
        prediction = model.predict(input_data)[0]

        st.markdown(f"""
        <div class="result-box">
            <h1>{prediction:.1f}</h1>
            <p>Estimated Calories Burned 🔥</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Context — compare to dataset percentile
        pct = (df["Calories"] < prediction).mean() * 100
        if pct >= 75:
            level, emoji = "High Burn 🚀", "You're burning more than most!"
        elif pct >= 40:
            level, emoji = "Moderate Burn 💪", "Solid workout effort!"
        else:
            level, emoji = "Low Burn 🧘", "Light activity — great for recovery!"

        st.info(f"**{level}** — {emoji}  \nYou're burning more calories than **{pct:.0f}%** of users in the dataset.")

        # Equivalent foods
        st.markdown("**🍕 That's equivalent to burning off:**")
        foods = {
            "🍎 Apples":      int(prediction / 52),
            "🍫 Chocolates":  int(prediction / 55),
            "🥤 Sodas (250ml)": int(prediction / 105),
            "🍕 Pizza slices": int(prediction / 285),
        }
        fc1, fc2 = st.columns(2)
        for i, (food, qty) in enumerate(foods.items()):
            (fc1 if i % 2 == 0 else fc2).metric(food, f"{max(qty,0)}")
    else:
        st.markdown("""
        <div style='text-align:center; padding:3rem; color:#666;'>
            <div style='font-size:4rem'>🏋️</div>
            <p style='margin-top:1rem'>Fill in your details on the left<br>and click <b>Predict</b> to see your result</p>
        </div>
        """, unsafe_allow_html=True)

# ── EDA Section ───────────────────────────────────────────────
st.markdown("---")
st.subheader("📊 Dataset Insights")

tab1, tab2, tab3 = st.tabs(["Distributions", "Correlations", "Calories by Group"])

with tab1:
    cols_to_plot = ["Age", "Height", "Weight", "Duration", "Heart_Rate", "Body_Temp", "Calories"]
    fig, axes = plt.subplots(2, 4, figsize=(16, 6))
    fig.patch.set_facecolor("#0E1117")
    for i, col in enumerate(cols_to_plot):
        ax = axes[i // 4][i % 4]
        ax.hist(df[col], bins=30, color="#FF6B6B", edgecolor="#0E1117", alpha=0.85)
        ax.set_title(col, color="white", fontsize=10, fontweight="bold")
        ax.set_facecolor("#1a1a2e")
        ax.tick_params(colors="#888", labelsize=7)
        for spine in ax.spines.values():
            spine.set_edgecolor("#333")
    # Gender bar
    ax = axes[1][3]
    gender_counts = df["Gender"].map({0: "Male", 1: "Female"}).value_counts()
    ax.bar(gender_counts.index, gender_counts.values,
           color=["#4C72B0", "#FF6B6B"], edgecolor="#0E1117")
    ax.set_title("Gender", color="white", fontsize=10, fontweight="bold")
    ax.set_facecolor("#1a1a2e")
    ax.tick_params(colors="#888", labelsize=8)
    for spine in ax.spines.values():
        spine.set_edgecolor("#333")
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

with tab2:
    fig, ax = plt.subplots(figsize=(9, 6))
    fig.patch.set_facecolor("#0E1117")
    ax.set_facecolor("#1a1a2e")
    numeric_df = df.select_dtypes(include=np.number).drop(columns=["User_ID"])
    sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", cmap="RdYlGn",
                linewidths=0.5, ax=ax, annot_kws={"size": 9})
    ax.set_title("Feature Correlation Heatmap", color="white", fontsize=13, fontweight="bold")
    ax.tick_params(colors="white", labelsize=9)
    st.pyplot(fig)
    plt.close()

with tab3:
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.patch.set_facecolor("#0E1117")
    plot_configs = [
        ("Duration", "Calories", "Duration vs Calories"),
        ("Heart_Rate", "Calories", "Heart Rate vs Calories"),
        ("Age", "Calories", "Age vs Calories"),
    ]
    colors_g = df["Gender"].map({0: "#4C72B0", 1: "#FF6B6B"})
    for ax, (xcol, ycol, title) in zip(axes, plot_configs):
        ax.scatter(df[xcol], df[ycol], c=colors_g, alpha=0.2, s=5)
        ax.set_xlabel(xcol, color="#aaa", fontsize=9)
        ax.set_ylabel(ycol, color="#aaa", fontsize=9)
        ax.set_title(title, color="white", fontsize=10, fontweight="bold")
        ax.set_facecolor("#1a1a2e")
        ax.tick_params(colors="#888", labelsize=8)
        for spine in ax.spines.values():
            spine.set_edgecolor("#333")
    import matplotlib.patches as mpatches
    axes[2].legend(
        handles=[mpatches.Patch(color="#4C72B0", label="Male"),
                 mpatches.Patch(color="#FF6B6B", label="Female")],
        fontsize=8, facecolor="#1a1a2e", labelcolor="white"
    )
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

# ── Footer ────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style='text-align:center; color:#555; font-size:0.85rem; padding: 1rem 0'>
    Built with ❤️ using <b>Streamlit</b> · Model: <b>XGBoost</b> · Dataset: 15,000 exercise records · R² = 0.9995
</div>
""", unsafe_allow_html=True)
