import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

st.set_page_config(page_title="Sales Prediction Dashboard", layout="wide")

st.markdown("""<style>
*{color:#fff!important;font-weight:600!important}
h1{color:#00D4FF!important;font-size:2rem!important;font-weight:900!important;text-shadow:0 0 15px rgba(0,212,255,.4);border-bottom:2px solid #00D4FF;padding-bottom:8px}
h2{color:#FFD700!important;font-size:1.1rem!important;font-weight:800!important;border-left:4px solid #FFD700;padding-left:12px;margin:18px 0 8px 0!important;background:linear-gradient(90deg,rgba(255,215,0,.06),transparent)}
p{color:#d0d0d0!important;font-weight:500!important;font-size:.92rem!important;line-height:1.5}
.stDataFrame{border:1px solid #1e3a5f!important;border-radius:10px!important;overflow:hidden}
.stDataFrame td{color:#fff!important;font-weight:600!important;background:#111827!important;padding:6px 12px!important;border-bottom:1px solid #1e293b!important}
.stDataFrame th{color:#00D4FF!important;font-weight:800!important;background:#0f172a!important;padding:8px 12px!important;text-transform:uppercase;letter-spacing:.5px;font-size:.8rem!important}
.stDataFrame tr:hover td{background:#1e293b!important}
[data-testid="stAlert"]{background:#111827!important;border:1px solid #1e3a5f!important;border-radius:10px!important;padding:12px 16px!important}
[data-testid="stAlertInfo"]{border-left:4px solid #00D4FF!important}
[data-testid="stAlertSuccess"]{border-left:4px solid #00FF88!important}
[data-testid="stAlertWarning"]{border-left:4px solid #FFD700!important}
[data-testid="stAlert"] p{color:#fff!important;font-weight:700!important;font-size:.9rem!important}
.main .block-container{background:#09090b!important;padding-top:20px!important}
section[data-testid="stSidebar"]{background:linear-gradient(180deg,#09090b,#111827)!important;border-right:1px solid #1e3a5f!important}
section[data-testid="stSidebar"] h2{color:#00D4FF!important;font-size:1.1rem!important;text-align:center;border-bottom:1px solid #1e3a5f!important;border-left:none!important;background:none!important;padding-bottom:8px!important}
section[data-testid="stSidebar"] label{color:#ccc!important;font-weight:600!important;font-size:.82rem!important}
.stSelectbox [data-baseweb="select"]{background:#111827!important;border:1px solid #1e3a5f!important;border-radius:8px!important;color:#fff!important}
.stSelectbox [data-baseweb="select"] span{color:#fff!important;font-weight:600!important}
.stSlider [data-baseweb="slider-handle"]{background:#00D4FF!important;box-shadow:0 0 8px rgba(0,212,255,.5)!important}
.stSlider [data-baseweb="slider-track"]{background:#1e293b!important}
.stPlotlyChart{border:1px solid #1e3a5f!important;border-radius:10px!important;overflow:hidden}
hr{border:none!important;height:1px!important;background:linear-gradient(90deg,transparent,#1e3a5f,transparent)!important;margin:20px 0!important}
.stElementContainer img{border-radius:10px!important;border:1px solid #1e3a5f!important}
::-webkit-scrollbar{width:6px;height:6px}
::-webkit-scrollbar-track{background:#09090b}
::-webkit-scrollbar-thumb{background:#1e3a5f;border-radius:10px}
::-webkit-scrollbar-thumb:hover{background:#00D4FF}
.card{background:linear-gradient(135deg,#111827,#0f172a);border:1px solid #1e3a5f;border-radius:12px;padding:18px 20px;box-shadow:0 2px 12px rgba(0,0,0,.3)}
.card-cyan{border-left:4px solid #00D4FF}
.card-green{border-left:4px solid #00FF88}
.card-gold{border-left:4px solid #FFD700}
.card-red{border-left:4px solid #FF6B6B}
.card-purple{border-left:4px solid #A78BFA}
.card-blue{border-left:4px solid #60A5FA}
.card-title{font-size:.95rem;font-weight:800;margin-bottom:4px}
.card-text{font-size:.82rem;font-weight:500;color:#a0a0a0!important;line-height:1.5}
.hero{background:linear-gradient(135deg,#052e16,#064e3b);border:1px solid #00FF88;border-radius:14px;padding:22px 28px;text-align:center;box-shadow:0 0 25px rgba(0,255,136,.12)}
.hero-label{color:#6ee7b7!important;font-size:.75rem!important;font-weight:700!important;text-transform:uppercase;letter-spacing:2px;margin:0}
.hero-value{color:#00FF88!important;font-size:2.6rem!important;font-weight:900!important;text-shadow:0 0 18px rgba(0,255,136,.4);margin:6px 0!important}
.hero-sub{color:#6ee7b7!important;font-size:.82rem!important;font-weight:600!important;margin:0}
.hero-zero{color:#4b5563!important;font-size:2.6rem!important;font-weight:900!important;margin:6px 0!important}
.budget-header{color:#FFD700!important;font-size:.78rem!important;font-weight:800!important;text-transform:uppercase;letter-spacing:2px;margin:0 0 12px 0!important;text-align:center;padding-bottom:10px;border-bottom:1px solid #1e3a5f}
.budget-total{background:linear-gradient(135deg,#111827,#0f172a);border:1px solid #1e3a5f;border-radius:10px;padding:14px 16px;text-align:center;margin-top:14px}
.budget-total-label{color:#888!important;font-size:.72rem!important;font-weight:700!important;text-transform:uppercase;letter-spacing:1.5px;margin:0}
.budget-total-value{color:#00D4FF!important;font-size:1.6rem!important;font-weight:900!important;margin:4px 0 0 0!important;text-shadow:0 0 10px rgba(0,212,255,.3)}
.empty-hint{color:#4b5563!important;font-size:.85rem!important;font-weight:600!important;text-align:center;margin-top:14px!important;font-style:italic}
</style>""", unsafe_allow_html=True)

df = pd.read_csv("Advertising.csv").drop_duplicates().dropna()

segment_map = {"Youth": 1, "Adults": 2, "Professionals": 3}
platform_map = {"Instagram": 1, "Facebook": 2, "TV": 3, "YouTube": 4}

df["Segment"] = np.random.randint(1, 4, size=len(df))
df["Platform"] = np.random.randint(1, 5, size=len(df))

X = df[["TV", "Radio", "Newspaper", "Segment", "Platform"]]
y = df["Sales"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression().fit(X_train, y_train)
predictions = model.predict(X_test)
r2 = r2_score(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)

# ─── Sidebar: Slider Inputs (default 0) ───
st.sidebar.markdown('<p class="budget-header">Ad Budget Allocation</p>', unsafe_allow_html=True)

tv = st.sidebar.slider("TV Budget", 0, 300, 0, step=1)
radio = st.sidebar.slider("Radio Budget", 0, 50, 0, step=1)
newspaper = st.sidebar.slider("Newspaper Budget", 0, 120, 0, step=1)

segment = st.sidebar.selectbox("Target Segment", ["Youth", "Adults", "Professionals"])
platform = st.sidebar.selectbox("Platform", ["Instagram", "Facebook", "TV", "YouTube"])

total_budget = tv + radio + newspaper
st.sidebar.markdown(
    f'<div class="budget-total"><p class="budget-total-label">Total Budget</p><p class="budget-total-value">{total_budget}</p></div>',
    unsafe_allow_html=True
)

segment_value = segment_map[segment]
platform_value = platform_map[platform]

# ─── Prediction ───
future_sales = model.predict(
    np.array([[tv, radio, newspaper, segment_value, platform_value]])
)[0]

st.title("Sales Prediction Dashboard :")

if total_budget == 0:
    st.markdown(f"""
    <div class="hero" style="border-color:#1e3a5f;box-shadow:none;background:linear-gradient(135deg,#111827,#0f172a)">
      <p class="hero-label" style="color:#6b7280!important">Predicted Sales</p>
      <p class="hero-zero">0.00</p>
      <p class="hero-sub" style="color:#4b5563!important">Slide the budget to see prediction</p>
    </div>""", unsafe_allow_html=True)
else:
    st.markdown(f"""
    <div class="hero">
      <p class="hero-label">Predicted Sales</p>
      <p class="hero-value">{future_sales:.2f}</p>
      <p class="hero-sub">Units Expected | Budget: {total_budget} | R2: {r2:.2f}</p>
    </div>""", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
with m1:
    st.info(f"**R2 Score:** {r2:.2f}")
with m2:
    st.info(f"**MAE:** {mae:.2f}")
with m3:
    st.info(f"**Rows:** {df.shape[0]}")
with m4:
    st.info(f"**Columns:** {df.shape[1]}")

st.markdown("<hr>", unsafe_allow_html=True)

d1, d2, d3 = st.columns([1, 1, 1])
with d1:
    st.subheader("Data Preview")
    st.dataframe(df.head(), use_container_width=True, height=220)
with d2:
    st.subheader("Correlation")
    fig, ax = plt.subplots(figsize=(3.2, 2.6))
    fig.patch.set_facecolor("#09090b")
    ax.set_facecolor("#09090b")
    sns.heatmap(
        df.corr(), annot=True, cmap="Blues", ax=ax,
        linewidths=0.4, linecolor="#1e3a5f",
        annot_kws={"color": "black", "size": 7}, cbar=False
    )
    ax.tick_params(colors="#fff", labelsize=6)
    st.pyplot(fig)
with d3:
    st.subheader("Feature Impact")
    coefficients = abs(model.coef_)
    impact_percentage = (coefficients / coefficients.sum()) * 100
    imp = pd.DataFrame({
        "Feature": X.columns,
        "Impact %": impact_percentage.round(2)
    })
    st.dataframe(imp, use_container_width=True, height=220)

st.markdown("<hr>", unsafe_allow_html=True)
st.subheader("Advertising vs Sales")

c1, c2, c3 = st.columns(3)
bg = "#09090b"
grid_c = "#1e293b"
base_cfg = {
    "plot_bgcolor": bg, "paper_bgcolor": bg,
    "font": {"color": "#fff", "family": "Arial", "size": 10},
    "title_font": {"color": "#FFD700", "size": 12, "family": "Arial Black"},
    "xaxis_title_font": {"color": "#ccc", "size": 10},
    "yaxis_title_font": {"color": "#ccc", "size": 10},
    "xaxis_tickfont": {"color": "#aaa", "size": 8},
    "yaxis_tickfont": {"color": "#aaa", "size": 8},
    "xaxis": {"gridcolor": grid_c, "linecolor": grid_c},
    "yaxis": {"gridcolor": grid_c, "linecolor": grid_c},
    "margin": {"t": 35, "b": 30, "l": 40, "r": 10},
    "title_x": 0.5, "height": 240
}

with c1:
    f1 = px.scatter(df, x="TV", y="Sales", trendline="ols")
    f1.update_layout(**base_cfg, title_text="TV vs Sales")
    f1.update_traces(marker=dict(color="#00D4FF", size=6), line=dict(color="#FFD700", width=2))
    st.plotly_chart(f1, use_container_width=True)
with c2:
    f2 = px.scatter(df, x="Radio", y="Sales", trendline="ols")
    f2.update_layout(**base_cfg, title_text="Radio vs Sales")
    f2.update_traces(marker=dict(color="#00FF88", size=6), line=dict(color="#FFD700", width=2))
    st.plotly_chart(f2, use_container_width=True)
with c3:
    f3 = px.scatter(df, x="Newspaper", y="Sales", trendline="ols")
    f3.update_layout(**base_cfg, title_text="Newspaper vs Sales")
    f3.update_traces(marker=dict(color="#FF6B6B", size=6), line=dict(color="#FFD700", width=2))
    st.plotly_chart(f3, use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.subheader("Quick Insights")

i1, i2 = st.columns(2)
with i1:
    if total_budget == 0:
        st.info("Slide the budget to get insights")
    elif tv > radio and tv > newspaper:
        st.info("TV has highest impact on sales")
    elif radio > tv:
        st.info("Radio campaigns performing strongly")
    else:
        st.info("Balanced advertising strategy")
with i2:
    if total_budget == 0:
        st.info("No budget allocated yet")
    elif future_sales > 20:
        st.success("High sales growth expected")
    else:
        st.warning("Consider increasing ad budget")

st.markdown("<hr>", unsafe_allow_html=True)
st.subheader("Strategy Overview")

s1, s2, s3 = st.columns(3)

seg_data = {
    "Youth": ("Youth Segment", "#00D4FF", "card-cyan", "Youth responds best to social media ads like Instagram Reels and TikTok."),
    "Adults": ("Adults Segment", "#FFD700", "card-gold", "Adults respond well to TV and Facebook. Combine traditional and digital."),
    "Professionals": ("Professionals", "#00FF88", "card-green", "Professionals prefer premium campaigns via LinkedIn and email marketing.")
}
plat_data = {
    "Instagram": ("Instagram", "#A78BFA", "card-purple", "Best for younger audiences. Reels and Stories drive highest engagement."),
    "Facebook": ("Facebook", "#60A5FA", "card-blue", "Balanced reach across demographics. Great for retargeting campaigns."),
    "TV": ("TV", "#00FF88", "card-green", "Broadest reach for brand awareness. Ideal for mass-market campaigns."),
    "YouTube": ("YouTube", "#FF6B6B", "card-red", "Video ads boost engagement. Pre-roll and Shorts drive conversions.")
}

sv, sc, scls, stxt = seg_data[segment]
s1.markdown(f'<div class="card {scls}"><p class="card-title" style="color:{sc}">{sv}</p><p class="card-text">{stxt}</p></div>', unsafe_allow_html=True)

pv, pc, pcls, ptxt = plat_data[platform]
s2.markdown(f'<div class="card {pcls}"><p class="card-title" style="color:{pc}">{pv}</p><p class="card-text">{ptxt}</p></div>', unsafe_allow_html=True)

if total_budget == 0:
    s3.markdown('<div class="card" style="border-left:4px solid #4b5563"><p class="card-title" style="color:#6b7280">Waiting for Input</p><p class="card-text">Slide the budget to get a personalized strategy recommendation.</p></div>', unsafe_allow_html=True)
elif future_sales > 20 and tv > 100:
    s3.markdown('<div class="card card-green"><p class="card-title" style="color:#00FF88">Increase TV Spend</p><p class="card-text">TV is driving strong results. Double down for maximum growth.</p></div>', unsafe_allow_html=True)
elif radio > 30:
    s3.markdown('<div class="card card-cyan"><p class="card-title" style="color:#00D4FF">Radio Working</p><p class="card-text">Radio generating strong engagement. Maintain spend and test TV.</p></div>', unsafe_allow_html=True)
else:
    s3.markdown('<div class="card card-gold"><p class="card-title" style="color:#FFD700">Balance Strategy</p><p class="card-text">Shift more budget to TV. It shows strongest correlation with sales.</p></div>', unsafe_allow_html=True)

st.markdown("""<hr><div style="text-align:center;padding:10px 0">
<p style="color:#444!important;font-size:.78rem!important;font-weight:600!important;letter-spacing:1px">
Built by Nitish Kumar | ML | Python
</p></div>""", unsafe_allow_html=True)
