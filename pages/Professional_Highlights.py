import streamlit as st
from pathlib import Path
import base64

st.set_page_config(
    page_title="Professional Highlights | Dhairya Dosi",
    page_icon="📸",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- DARK THEME CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    [data-testid="stAppViewContainer"],
    [data-testid="stApp"],
    .main,
    section[data-testid="stSidebar"],
    [data-testid="stSidebar"] > div {
        background-color: #0d1117 !important;
    }
    header[data-testid="stHeader"] {
        background-color: #0d1117 !important;
    }
    [data-testid="stSidebar"] {
        background-color: #161b22 !important;
        border-right: 1px solid #21262d !important;
    }
    [data-testid="stSidebar"] > div {
        background-color: #161b22 !important;
    }
    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
        color: #e6edf3 !important;
    }
    .main p, .main li, .main span, .main div,
    .main h1, .main h2, .main h3, .main h4, .main h5, .main h6,
    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] li,
    [data-testid="stMarkdownContainer"] span,
    [data-testid="stMarkdownContainer"] strong,
    [data-testid="stMarkdownContainer"] em {
        color: #e6edf3 !important;
    }
    [data-testid="stSidebar"] * {
        color: #c9d1d9 !important;
    }
    [data-testid="stSidebar"] a {
        color: #58a6ff !important;
    }
    .main a, [data-testid="stMarkdownContainer"] a {
        color: #58a6ff !important;
        text-decoration: none;
    }
    .main a:hover, [data-testid="stMarkdownContainer"] a:hover {
        color: #79c0ff !important;
        text-decoration: underline;
    }
    .main .block-container {
        padding-top: 2rem;
        max-width: 1100px;
    }
    h1, h2, h3 { font-weight: 700; }
    hr { border-color: #21262d !important; }
    [data-testid="stCaptionContainer"] p { color: #8b949e !important; }

    .section-header {
        font-size: 1.5rem;
        font-weight: 700;
        color: #f0f6fc !important;
        border-bottom: 3px solid #58a6ff;
        padding-bottom: 0.4rem;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    .slideshow-container {
        position: relative;
        max-width: 100%;
        margin: 1.5rem auto;
        overflow: hidden;
        border-radius: 12px;
        border: 1px solid #21262d;
        background: #161b22;
    }
    .slideshow-container img {
        width: 100%;
        max-height: 550px;
        object-fit: contain;
        display: block;
        margin: 0 auto;
        background: #0d1117;
    }
    .slide-caption {
        text-align: center;
        padding: 0.8rem 1rem;
        background: #161b22;
        color: #c9d1d9 !important;
        font-size: 0.95rem;
        font-weight: 500;
        border-top: 1px solid #21262d;
    }
    .slide-counter {
        text-align: center;
        color: #8b949e !important;
        font-size: 0.8rem;
        padding-bottom: 0.5rem;
        background: #161b22;
    }

    .thumb-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
        gap: 1rem;
        margin-top: 1.5rem;
    }
    .thumb-card {
        background: #161b22;
        border: 1px solid #21262d;
        border-radius: 10px;
        overflow: hidden;
        transition: transform 0.2s, border-color 0.2s;
        cursor: pointer;
    }
    .thumb-card:hover {
        transform: translateY(-3px);
        border-color: #58a6ff;
    }
    .thumb-card img {
        width: 100%;
        height: 180px;
        object-fit: cover;
    }
    .thumb-card .thumb-label {
        padding: 0.5rem 0.7rem;
        font-size: 0.8rem;
        color: #b1bac4 !important;
        text-align: center;
        border-top: 1px solid #21262d;
    }
</style>
""", unsafe_allow_html=True)


def get_image_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


# Use the parent of 'pages/' folder (i.e., the project root)
SLIDE_DIR = Path(__file__).parent.parent

slideshow_images = [
    ("1776577306945.jpeg", "Airbus Structures Road Show — A350F Cargo Door Mechanism Demonstration"),
    ("1776577306908.jpeg", "Coastal Surveillance UAV — Propulsion & Landing Gear Design, RGD Lab IIT Madras"),
    ("1776577306924.jpeg", "Stereo Vision Drone Assembly — Research Lab Work"),
    ("1776577306874.jpeg", "Advertisement Drone development — Systems Integration & Wiring"),
    ("1776577306980.jpeg", "IIT Madras 61st Convocation — M.Tech Aerospace Engineering"),
    ("1776577307017.jpeg", "ATAGS Artillery System — Defence Engineering Expo"),
    ("1776577306967.jpeg", "LCA Tejas (Navy) — Aero India / Defence Airshow"),
    ("1776577306956.jpeg", "Coronado Telescope — Academic Exploration at IIA Bangalore"),
    ("1776577306861.jpeg", "RC Fixed-Wing Aircraft — Flight Testing & Prototyping"),
    ("1776577307004.jpeg", "Drone Piloting — Field Testing & Research"),
    ("1776577306992.jpeg", "With Prof. H.S.N Murthy — IIT Madras Convocation"),
]

# Filter to existing images
slideshow_images = [(f, c) for f, c in slideshow_images if (SLIDE_DIR / f).exists()]

# --- HEADER ---
st.page_link("app.py", label="⬅️ Back to Main Page", icon="🏠")
st.markdown("# 📸 Professional Highlights")
st.markdown("*A visual journey through key career moments — Dhairya Dosi*")
st.markdown("---")

if not slideshow_images:
    st.warning("No images found.")
    st.stop()

# --- SLIDESHOW ---
if "slide_idx" not in st.session_state:
    st.session_state.slide_idx = 0

total = len(slideshow_images)
idx = st.session_state.slide_idx % total
img_file, caption = slideshow_images[idx]

img_b64 = get_image_base64(SLIDE_DIR / img_file)
ext = img_file.rsplit(".", 1)[-1].lower()
mime = "image/jpeg" if ext in ("jpg", "jpeg") else f"image/{ext}"

st.markdown(
    f"""<div class="slideshow-container">
        <img src="data:{mime};base64,{img_b64}" alt="{caption}"/>
        <div class="slide-caption">{caption}</div>
        <div class="slide-counter">{idx + 1} / {total}</div>
    </div>""",
    unsafe_allow_html=True,
)

nav_col1, nav_col2, nav_col3 = st.columns([1, 2, 1])
with nav_col1:
    if st.button("⬅️ Previous", use_container_width=True):
        st.session_state.slide_idx = (idx - 1) % total
        st.rerun()
with nav_col3:
    if st.button("Next ➡️", use_container_width=True):
        st.session_state.slide_idx = (idx + 1) % total
        st.rerun()

# --- THUMBNAIL GRID ---
st.markdown("---")
st.markdown('<div class="section-header">🖼️ All Photos</div>', unsafe_allow_html=True)

thumbs_html = '<div class="thumb-grid">'
for i, (img_f, cap) in enumerate(slideshow_images):
    tb64 = get_image_base64(SLIDE_DIR / img_f)
    short_cap = cap.split("—")[0].strip() if "—" in cap else cap[:40]
    thumbs_html += f'''<div class="thumb-card">
        <img src="data:image/jpeg;base64,{tb64}" alt="{cap}"/>
        <div class="thumb-label">{short_cap}</div>
    </div>'''
thumbs_html += '</div>'

st.markdown(thumbs_html, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("---")
st.markdown(
    '<div style="text-align:center;color:#8b949e;font-size:0.82rem;">Dhairya Dosi © 2026</div>',
    unsafe_allow_html=True,
)
