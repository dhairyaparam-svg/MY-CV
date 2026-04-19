import streamlit as st
from pathlib import Path
import base64

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Curriculum Vitae | Dhairya Dosi",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- DARK THEME CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200');

    .material-symbols-rounded {
        font-family: 'Material Symbols Rounded' !important;
    }

    /* Hide default Streamlit page navigation */
    [data-testid="stSidebarNav"] {
        display: none !important;
    }

    /* Dark background everywhere */
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

    /* Default text color - bright white/light gray for readability */
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
    [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h5 {
        color: #f0f6fc !important;
    }
    [data-testid="stSidebar"] strong {
        color: #f0f6fc !important;
    }

    /* Links - cyan/teal for pop on dark */
    .main a, [data-testid="stMarkdownContainer"] a,
    [data-testid="stSidebar"] a {
        color: #58a6ff !important;
        text-decoration: none;
    }
    .main a:hover, [data-testid="stMarkdownContainer"] a:hover,
    [data-testid="stSidebar"] a:hover {
        color: #79c0ff !important;
        text-decoration: underline;
    }

    .main .block-container {
        padding-top: 2rem;
        max-width: 1100px;
    }
    h1, h2, h3 {
        font-weight: 700;
    }

    /* Section headers */
    .section-header {
        font-size: 1.5rem;
        font-weight: 700;
        color: #f0f6fc !important;
        border-bottom: 3px solid #58a6ff;
        padding-bottom: 0.4rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }

    /* Experience cards */
    .experience-card {
        background: #161b22 !important;
        border-left: 4px solid #58a6ff;
        padding: 1.2rem 1.5rem;
        border-radius: 0 8px 8px 0;
        margin-bottom: 1rem;
        border: 1px solid #21262d;
        border-left: 4px solid #58a6ff;
    }
    .experience-card h4 {
        margin: 0 0 0.3rem 0;
        color: #58a6ff !important;
        font-size: 1.1rem;
    }
    .experience-card .org {
        font-weight: 600;
        color: #b1bac4 !important;
        font-size: 0.95rem;
    }
    .experience-card .dates {
        color: #8b949e !important;
        font-size: 0.85rem;
        margin-bottom: 0.5rem;
    }
    .experience-card ul {
        margin: 0.4rem 0 0 0;
        padding-left: 1.2rem;
    }
    .experience-card li {
        margin-bottom: 0.3rem;
        color: #c9d1d9 !important;
        font-size: 0.92rem;
        line-height: 1.5;
    }

    /* Project cards */
    .project-card {
        background: #161b22 !important;
        border: 1px solid #21262d;
        padding: 1.2rem 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.3);
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .project-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 16px rgba(88,166,255,0.15);
        border-color: #58a6ff;
    }
    .project-card h4 {
        margin: 0 0 0.5rem 0;
        color: #f0f6fc !important;
    }
    .project-card p {
        color: #b1bac4 !important;
        font-size: 0.92rem;
        line-height: 1.6;
    }
    .project-card a {
        color: #58a6ff !important;
        text-decoration: none;
    }
    .project-card a:hover {
        text-decoration: underline;
        color: #79c0ff !important;
    }

    /* Skill tags */
    .skill-tag {
        display: inline-block;
        background: #1f6feb;
        color: #ffffff !important;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        margin: 0.2rem;
        font-size: 0.82rem;
        font-weight: 500;
    }
    .skill-tag-alt {
        display: inline-block;
        background: #238636;
        color: #ffffff !important;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        margin: 0.2rem;
        font-size: 0.82rem;
        font-weight: 500;
    }
    .skill-tag-eng {
        display: inline-block;
        background: #8957e5;
        color: #ffffff !important;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        margin: 0.2rem;
        font-size: 0.82rem;
        font-weight: 500;
    }

    /* Patent cards */
    .patent-card {
        background: #1c1e24 !important;
        border-left: 4px solid #d29922;
        border: 1px solid #30363d;
        border-left: 4px solid #d29922;
        padding: 1.2rem 1.5rem;
        border-radius: 0 8px 8px 0;
        margin-bottom: 1rem;
    }
    .patent-card h4 {
        color: #e3b341 !important;
        margin: 0 0 0.3rem 0;
    }
    .patent-card p {
        color: #b1bac4 !important;
    }

    /* Education table */
    .edu-table {
        width: 100%;
        border-collapse: collapse;
    }
    .edu-table th {
        background: #1f6feb;
        color: #ffffff !important;
        padding: 0.7rem 1rem;
        text-align: left;
        font-size: 0.9rem;
    }
    .edu-table td {
        padding: 0.6rem 1rem;
        border-bottom: 1px solid #21262d;
        font-size: 0.9rem;
        color: #c9d1d9 !important;
    }
    .edu-table tr:nth-child(even) {
        background: #161b22;
    }
    .edu-table tr:nth-child(odd) {
        background: #0d1117;
    }

    /* Achievement badges */
    .achievement-badge {
        background: #0d2818 !important;
        border-left: 4px solid #3fb950;
        padding: 0.7rem 1rem;
        border-radius: 0 6px 6px 0;
        margin-bottom: 0.5rem;
        font-size: 0.92rem;
        color: #56d364 !important;
    }

    /* Contact links */
    .contact-link {
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        background: #21262d !important;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        color: #58a6ff !important;
        text-decoration: none;
        font-size: 0.88rem;
        font-weight: 500;
        margin: 0.2rem;
        border: 1px solid #30363d;
        transition: background 0.2s, border-color 0.2s;
    }
    .contact-link:hover {
        background: #30363d !important;
        border-color: #58a6ff;
    }

    /* Sidebar photo */
    .sidebar-photo {
        border-radius: 50%;
        border: 4px solid #58a6ff;
        width: 180px;
        height: 180px;
        object-fit: cover;
        margin: 0 auto;
        display: block;
    }

    /* Cert items */
    .cert-item {
        background: #0d2039 !important;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        margin-bottom: 0.4rem;
        font-size: 0.9rem;
        border-left: 3px solid #58a6ff;
        color: #b1bac4 !important;
    }

    .activity-item {
        padding: 0.4rem 0;
        font-size: 0.92rem;
    }
    .divider {
        height: 1px;
        background: #21262d;
        margin: 0.5rem 0;
    }

    /* Streamlit horizontal rule */
    hr {
        border-color: #21262d !important;
    }

    /* Caption text */
    [data-testid="stCaptionContainer"] p {
        color: #8b949e !important;
    }
</style>
""", unsafe_allow_html=True)


# --- HELPER: load photo as base64 ---
def get_image_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


PHOTO_PATH = Path(__file__).parent / "Dhairya-Dosi-2.webp"

# ========================
#  SIDEBAR
# ========================
with st.sidebar:
    if PHOTO_PATH.exists():
        img_b64 = get_image_base64(PHOTO_PATH)
        st.markdown(
            f'<img src="data:image/webp;base64,{img_b64}" class="sidebar-photo"/>',
            unsafe_allow_html=True,
        )
    st.markdown("## Dhairya Dosi")
    st.caption("Aerospace Engineer | IIT Gandhinagar")

    st.markdown("---")
    st.markdown("##### 📬 Contact")
    st.markdown("📧 dhairya.param@iitgn.ac.in")
    st.markdown(
        "[🔗 LinkedIn](https://in.linkedin.com/in/dhairya-dosi-b9040112b)"
    )
    st.markdown(
        "[💻 GitHub](https://github.com/dhairyaparam-svg)"
    )
    st.markdown(
        "[📚 ResearchGate](https://www.researchgate.net/profile/Dhairya-Dosi-2)"
    )
    st.markdown(
        "[📸 Pictures/Videos](/Pictures_Videos)"
    )

    st.markdown("---")
    st.markdown("##### 🏅 Highlights")
    st.markdown("**AIR 32** – GATE AE 2022")
    st.markdown("**1 Patent** (Airbus)")
    st.markdown("**3+ Publications** (IEEE, ASME)")

    st.markdown("---")
    st.markdown("##### 🎓 Memberships")
    st.markdown("AIAA Member")

# ========================
#  MAIN CONTENT
# ========================

# --- HEADER ---
st.markdown("# ✈️ Dhairya Dosi")
st.markdown(
    "*Aerospace Engineer · Indian Institute of Technology Gandhinagar*"
)
st.markdown(
    '<div style="display:flex;flex-wrap:wrap;gap:0.3rem;margin-bottom:1rem;">'
    '<a class="contact-link" href="mailto:dhairya.param@iitgn.ac.in">📧 Email</a>'
    '<a class="contact-link" href="https://in.linkedin.com/in/dhairya-dosi-b9040112b" target="_blank">🔗 LinkedIn</a>'
    '<a class="contact-link" href="https://github.com/dhairyaparam-svg" target="_blank">💻 GitHub</a>'
    '<a class="contact-link" href="https://www.researchgate.net/profile/Dhairya-Dosi-2" target="_blank">📚 ResearchGate</a>'
    "</div>",
    unsafe_allow_html=True,
)

# ========================
# EDUCATION
# ========================
st.markdown('<div class="section-header">🎓 Education</div>', unsafe_allow_html=True)

st.markdown("""
<table class="edu-table">
<tr><th>Program</th><th>Institution</th><th>CGPA / %</th><th>Year</th></tr>
<tr><td>M.Tech (Aerospace Engineering)</td><td>IIT Madras</td><td>8.59</td><td>2024</td></tr>
<tr><td>B.E (Aerospace Engineering)</td><td>Chandigarh University</td><td>6.57</td><td>2021</td></tr>
<tr><td>Class XII</td><td>Govt. Sr. Sec. School, Bagidora</td><td>84%</td><td>2016</td></tr>
<tr><td>Class X</td><td>Govt. Sr. Sec. School, Bagidora</td><td>77%</td><td>2014</td></tr>
</table>
""", unsafe_allow_html=True)

st.markdown("")
st.markdown('<div class="achievement-badge">🏆 <b>Scholarship for Meritorious Students</b>, BSER Ajmer (2016)</div>', unsafe_allow_html=True)
st.markdown('<div class="achievement-badge">🏆 <b>All India Rank 32</b> in GATE (AE)-2022 — Scored 742/1000</div>', unsafe_allow_html=True)

# ========================
# PROJECTS
# ========================
st.markdown('<div class="section-header">🔬 Projects</div>', unsafe_allow_html=True)

projects = [
    {
        "title": "Vision-based Guidance of Autonomous Vehicles (M.Tech Project)",
        "desc": (
            "Experiments on vision-based methods to detect, identify and track UAVs using thermal camera. "
            "Combines YOLO-based object detection with feature matching for real-time tracking. "
            "Introduced a novel clustering algorithm to segment thermal image features. "
            "Implemented image processing technologies for material characterization in GNC."
        ),
        "pub": 'Paper published in IEEE ETAAV 2025: <a href="https://ieeexplore.ieee.org/document/11213400" target="_blank">10.1109/ETAAV66793.2025.11213400</a>',
    },
    {
        "title": "Aerodynamic & Structural Design of Bird Strike Prevention UAV",
        "desc": (
            "Designed a UAV with nose-mounted ultrasonic speakers to clear sensitive areas of bird flocks. "
            "Created autonomous mission profiles to detect flocks at altitude and deter them."
        ),
        "pub": 'Report on ResearchGate DOI: <a href="https://doi.org/10.13140/RG.2.2.32015.70567" target="_blank">10.13140/RG.2.2.32015.70567</a>',
    },
    {
        "title": "Optimization of Front Landing Gear for 15–25 kg UAV",
        "desc": (
            "Designed the CAD geometry of a suspension gear. Performed multi-parameter FEA analysis and selected "
            "optimal parameters using a Lyapunov-inspired cost function. Used regression analysis to characterize "
            "the landing gear for different weight categories."
        ),
        "pub": "Accepted for publication in ASME-IMECE India 2026 Conference",
    },
    {
        "title": "Sliding-Mode-Control Guidance for Precision Soft Landing on Asteroid",
        "desc": (
            'Enhanced and implemented guidance algorithms for precision soft landing (based on DOI: <a href="https://doi.org/10.2514/1.A35412" target="_blank">10.2514/1.A35412</a>). '
            "Developed range-dependent sliding mode constants to minimize propellant consumption."
        ),
        "pub": '<a href="https://slidingmodeguidence.streamlit.app/" target="_blank">Live Demo</a>',
    },
    {
        "title": "PB-2 Rayleigh-Ritz Method for Arbitrary Plate Analysis",
        "desc": (
            'Tool to determine natural frequencies for a plate of any arbitrary shape for all modes of vibration, '
            'based on DOI: <a href="https://doi.org/10.1016/0141-0296(93)90017-X" target="_blank">10.1016/0141-0296(93)90017-X</a>.'
        ),
        "pub": '<a href="https://pb2-method.streamlit.app/" target="_blank">Live Demo</a>',
    },
    {
        "title": "Open Source Flight Simulator (B.Tech Project)",
        "desc": (
            "Designed a short-haul air taxi and determined all aerodynamic, inertial, propulsive, and control parameters. "
            "Used linearized state-space methods to simulate aircraft motion with open-source model on GitHub."
        ),
        "pub": 'Paper published in IJIRSET — DOI: <a href="https://www.ijirset.com/upload/2023/january/27_Design_NC1.pdf" target="_blank">10.15680/IJIRSET.2023.1201027</a>',
    },
    {
        "title": "Solution to Overheating of Laser Range Finders",
        "desc": (
            "Extended overhaul interval of LRF cooling systems in MI-35 helicopters by implementing copper heat pipes "
            "and modifying housing for improved heat dissipation."
        ),
        "pub": None,
    },
]

for i in range(0, len(projects), 2):
    cols = st.columns(2)
    for j, col in enumerate(cols):
        idx = i + j
        if idx < len(projects):
            p = projects[idx]
            pub_html = f'<p style="color:#58a6ff;font-size:0.85rem;margin-top:0.5rem;">📄 {p["pub"]}</p>' if p["pub"] else ""
            with col:
                st.markdown(
                    f"""<div class="project-card">
                        <h4>{p["title"]}</h4>
                        <p>{p["desc"]}</p>
                        {pub_html}
                    </div>""",
                    unsafe_allow_html=True,
                )

# ========================
# SKILLS
# ========================
st.markdown('<div class="section-header">🛠️ Skills & Certifications</div>', unsafe_allow_html=True)

sk1, sk2, sk3 = st.columns(3)

with sk1:
    st.markdown("**🖥️ Software**")
    for s in ["MATLAB", "SolidWorks", "FreeCAD", "CATIA v5", "SimSolid", "Canva", "Google Workspace"]:
        st.markdown(f'<span class="skill-tag">{s}</span>', unsafe_allow_html=True)
    st.markdown("")
    st.markdown("**💻 Languages**")
    for s in ["Embedded C", "Python", "Arduino"]:
        st.markdown(f'<span class="skill-tag-alt">{s}</span>', unsafe_allow_html=True)

with sk2:
    st.markdown("**⚙️ Frameworks**")
    for s in ["Simulink", "DBSCAN", "Ardupilot", "CUDA", "LaTeX"]:
        st.markdown(f'<span class="skill-tag-alt">{s}</span>', unsafe_allow_html=True)
    st.markdown("")
    st.markdown("**🚀 Aerospace**")
    for s in ["Aerospace Structures", "GNC", "UAVs", "Flight Testing"]:
        st.markdown(f'<span class="skill-tag-eng">{s}</span>', unsafe_allow_html=True)

with sk3:
    st.markdown("**🔧 Engineering**")
    for s in ["Product Design", "Prototyping", "Structural Load Analysis", "Conceptual Design", "Computer Vision"]:
        st.markdown(f'<span class="skill-tag-eng">{s}</span>', unsafe_allow_html=True)
    st.markdown("")
    st.markdown("**🌟 Core Competencies**")
    for s in ["Problem Solving", "Creativity", "Mentoring", "IP Management", "Publication Management"]:
        st.markdown(f'<span class="skill-tag">{s}</span>', unsafe_allow_html=True)

st.markdown("")
st.markdown("**📜 Certifications**")
cert_c1, cert_c2, cert_c3 = st.columns(3)
with cert_c1:
    st.markdown('<div class="cert-item">Drone Systems and Controls — <em>NPTEL</em></div>', unsafe_allow_html=True)
with cert_c2:
    st.markdown('<div class="cert-item">Aerospace Controls and Systems Design — <em>Udemy</em></div>', unsafe_allow_html=True)
with cert_c3:
    st.markdown('<div class="cert-item">Aerospace Structures and Materials — <em>TU Delft</em></div>', unsafe_allow_html=True)

st.markdown("")
st.markdown("**📖 Key Coursework**")
coursework = [
    "Approximate Methods of Structural Analysis", "Aeroelasticity",
    "Aerospace Systems Estimation and Control", "Linear Differential Operators",
    "Principles of Guidance of Autonomous Vehicles", "Flight Mechanics",
]
cw_cols = st.columns(3)
for idx_cw, c in enumerate(coursework):
    with cw_cols[idx_cw % 3]:
        st.markdown(f"- {c}")

# ========================
# PROFESSIONAL EXPERIENCE
# ========================
st.markdown('<div class="section-header">💼 Professional Experience</div>', unsafe_allow_html=True)

experiences = [
    {
        "title": "Program Associate - 2",
        "org": "Center for Research Commercialization, IIT Gandhinagar",
        "dates": "Dec 2025 – Present",
        "bullets": [
            'Research on Affordable Multirotor systems for <a href="https://dronenavigatorsmc.streamlit.app/" target="_blank">Long-Range Medical Delivery</a>',
            "Unified Energy-Optimal Trajectory Planning for Electric VTOL Systems Using Direct Shooting and NLP *(IEEE-SPACE 2026)*",
            "Geometric Path Optimization for UAV Missions with Minimal Battery/HESS Swaps",
            "Hierarchical Motion Planning Framework for Time-Efficient UAV Navigation Using 3D-GSE and Conical Sampling *(IEEE-SPACE 2026)*",
            "Optimal guidance of multirotor aircraft using sliding mode control with range-augmented coefficients",
            "Development of National Center For Research Commercialization Portal (NCRC Portal)",
        ],
    },
    {
        "title": "Structural Design Intern",
        "org": "Airbus India Private Limited",
        "dates": "Jan 2025 – Jul 2025",
        "bullets": [
            "Developed 3D-printed prototype of A350 Freighter Main Deck Cargo Door",
            "Designed Universal Door Stopper concepts",
            "Introduced proxy folder solution to resolve storage issues in SQCDP",
            "Automated data extraction from large documents using feature clustering",
        ],
    },
    {
        "title": "Senior Project Engineer",
        "org": "RGD Lab, IIT Madras",
        "dates": "Jun 2024 – Dec 2024",
        "bullets": [
            "Developed propulsion and landing gear systems for an 18 kg coastal surveillance UAV",
            "Designed GNC systems for Smart 155mm Ammunition (details under NDA)",
        ],
    },
    {
        "title": "Teacher",
        "org": "SDRK College, Bagidora",
        "dates": "Nov 2020 – Dec 2021",
        "bullets": [
            "Taught high school mathematics; developed public speaking skills",
        ],
    },
    {
        "title": "Summer Intern",
        "org": "Indian Air Force",
        "dates": "Jul 2019 – Aug 2019",
        "bullets": [
            "Investigated and resolved overheating issues in MI-35 helicopter laser range finders",
        ],
    },
]

for exp in experiences:
    bullets_html = "".join(f"<li>{b}</li>" for b in exp["bullets"])
    st.markdown(
        f"""<div class="experience-card">
            <h4>{exp["title"]}</h4>
            <div class="org">{exp["org"]}</div>
            <div class="dates">📅 {exp["dates"]}</div>
            <ul>{bullets_html}</ul>
        </div>""",
        unsafe_allow_html=True,
    )

# ========================
# PATENTS
# ========================
st.markdown('<div class="section-header">💡 Innovations / Patents</div>', unsafe_allow_html=True)

patents = [
    {
        "title": "Magnetic Angular Bushes for Load Transfer Between Non-Parallel Surfaces",
        "org": "Airbus India Private Limited",
        "date": "Jun 2025",
        "desc": (
            "Designed a bushing for a door stopper allowing alignment to arbitrary orientations. "
            "The magnet ensures the default no-load orientation preventing clashes during operation. "
            'Defensive patent published at <a href="https://www.researchdisclosure.com/database/RD740118" target="_blank">Questel Research</a>.'
        ),
    },
    {
        "title": "Dynamical Spherical Connector (DSC): Tammes Solution Based Spherical Moment-less Joint",
        "org": "Airbus India Private Limited",
        "date": "Jul 2025",
        "desc": (
            "Designed an adaptable joint for A350 next-gen fuselage cabin (NICER) enabling moment-less motion "
            "of links for smart truss structures. Tammes problem solved with N joints for maximum degrees of motion. "
            "Airbus IDD Ref: 21692 — **Patent Applied**."
        ),
    },
]

for pat in patents:
    st.markdown(
        f"""<div class="patent-card">
            <h4>🔒 {pat["title"]}</h4>
            <div style="font-weight:600;color:#e3b341;font-size:0.9rem;">{pat["org"]} · {pat["date"]}</div>
            <p style="margin-top:0.5rem;font-size:0.92rem;color:#b1bac4;">{pat["desc"]}</p>
        </div>""",
        unsafe_allow_html=True,
    )

# ========================
# ACTIVITIES
# ========================
st.markdown('<div class="section-header">🏆 Co-Curricular Activities</div>', unsafe_allow_html=True)

act_col1, act_col2 = st.columns(2)

with act_col1:
    st.markdown("**🏠 Open Houses**")
    st.markdown("Structures Road Show, Airbus India — Demonstrated A350F Main Deck Cargo Door, educational skit")

    st.markdown("**🔧 Workshops**")
    st.markdown("Quadcopter Workshop Volunteer, IIT Madras — Supervised drone assembly and soldering")

    st.markdown("**📢 Conferences**")
    st.markdown("Presented paper at IEEE – ETAAV 2025, IISc Bangalore")

with act_col2:
    st.markdown("**🏅 Competitions**")
    st.markdown("- 🥉 3rd place — Ice Bucket Challenge, Tech Invent 2018")
    st.markdown("- 🥈 2nd place — Robowars, Tech Kriti 2020")
    st.markdown("- Smart Toilet Startup Fundraising")

    st.markdown("**👨‍🏫 Mentorship**")
    st.markdown("Guided undergraduates in UAV landing gear optimization")

st.markdown('<div class="section-header">🎯 Extra-Curricular Activities</div>', unsafe_allow_html=True)

extra_col1, extra_col2 = st.columns(2)

with extra_col1:
    st.markdown("🛩️ **Drone Piloting** — Practical drone flying for research and workshops")
    st.markdown("🖥️ **PC Building** — Assembled and upgraded desktop computers; designed a fluid cooling loop for a laptop")
    st.markdown("💍 **Jewelry Design** — CAD modeling and 3D printing of jewelry prototypes")

with extra_col2:
    st.markdown("🎵 **Music Production & DJing** — Released dubstep EP *\"Aadhar Card\"* on SoundCloud")
    st.markdown("🤝 **Community Involvement** — Taught drone piloting, member of Kunthu Jain Navyuvak Mandal, volunteered in NYSAA IIT Gandhinagar medical camp")

# --- FOOTER ---
st.markdown("---")
st.markdown(
    '<div style="text-align:center;color:#8b949e;font-size:0.82rem;">Built with Streamlit · Dhairya Dosi © 2026</div>',
    unsafe_allow_html=True,
)
