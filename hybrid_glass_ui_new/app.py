import base64
import textwrap

import streamlit as st

from hybrid_llm_init import create_router
from hybrid_llm.web.web_qa_local import answer_with_google_local


# ============== PAGE CONFIG ==============
st.set_page_config(
    page_title="Hybrid AI – Google + Local Mistral",
    page_icon="🤖",
    layout="wide",
)


# ============== BACKGROUND + GLASS CSS ==============
def set_background(image_file: str):
    try:
        with open(image_file, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        # agar image na mile to simple gradient
        encoded = ""

    css = f"""
    <style>
    html, body, [data-testid="stAppViewContainer"] {{
        background: radial-gradient(circle at top, #071b2f 0, #02030a 45%, #000000 100%);
        color: #f5f5f5;
    }}

    .glass-card {{
        background: rgba(15, 23, 42, 0.75);
        border-radius: 18px;
        padding: 20px 24px;
        margin-bottom: 14px;
        border: 1px solid rgba(148, 163, 184, 0.35);
        box-shadow: 0 18px 45px rgba(0, 0, 0, 0.6);
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
    }}

    .card-title {{
        font-size: 20px;
        font-weight: 700;
        color: #38bdf8;
        margin-bottom: 8px;
    }}

    .card-body {{
        font-size: 16px;
        line-height: 1.6;
        color: #e5e7eb;
        white-space: pre-wrap;
    }}

    .source-link {{
        color: #22d3ee;
        text-decoration: none;
        font-size: 14px;
    }}

    .source-box {{
        margin-top: 4px;
        padding: 6px 10px;
        border-radius: 10px;
        background: rgba(15, 118, 110, 0.27);
        font-size: 14px;
    }}

    .mode-button > button {{
        width: 100%;
        border-radius: 999px !important;
        border: 1px solid rgba(148, 163, 184, 0.5);
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.9), rgba(15, 23, 42, 0.4));
        color: #e5e7eb !important;
        font-weight: 600;
    }}

    .mode-button > button:hover {{
        border-color: #38bdf8;
        box-shadow: 0 0 18px rgba(56, 189, 248, 0.7);
    }}

    .title-glow {{
        text-align: center;
        color: #e0f2fe;
        text-shadow: 0 0 18px rgba(56, 189, 248, 0.9);
        font-weight: 800;
        letter-spacing: 0.06em;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


set_background("assets/bg.png")


def glass_card(title: str, body: str):
    st.markdown(
        f"""
        <div class="glass-card">
            <div class="card-title">{title}</div>
            <div class="card-body">{body}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============== HEADER ==============
st.markdown(
    "<h1 class='title-glow'>🤖 HYBRID AI – GOOGLE + LOCAL MISTRAL</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align:center;color:#9ca3af;'>Choose a mode: Google-only, Local-only, Compare, or Hybrid Summary.</p>",
    unsafe_allow_html=True,
)
st.markdown("<br/>", unsafe_allow_html=True)

# ============== INPUT ==============
question = st.text_input(
    "Your question:",
    placeholder="e.g. What is the latest update on the India AI Act?",
)

st.markdown("<br/>", unsafe_allow_html=True)

# ============== MODE BUTTONS ==============
col1, col2, col3, col4 = st.columns(4)

with col1:
    google_btn = st.container()
    with google_btn:
        btn_google = st.button("🌐 Google Answer", key="google_mode")
with col2:
    local_btn = st.container()
    with local_btn:
        btn_local = st.button("💻 Local Answer", key="local_mode")
with col3:
    compare_btn = st.container()
    with compare_btn:
        btn_compare = st.button("⚖️ Compare", key="compare_mode")
with col4:
    hybrid_btn = st.container()
    with hybrid_btn:
        btn_hybrid = st.button("🧬 Hybrid Summary", key="hybrid_mode")

# style mode buttons
st.markdown(
    """
    <script>
    const containers = window.parent.document.querySelectorAll('.mode-button');
    </script>
    """,
    unsafe_allow_html=True,
)


def ensure_question() -> bool:
    if not question or not question.strip():
        st.error("Pehle question likh na boss 😄")
        return False
    return True


# ============== HANDLERS ==============
if btn_google or btn_local or btn_compare or btn_hybrid:
    if not ensure_question():
        st.stop()

    router = create_router(mode="local")

    # 1️⃣ GOOGLE MODE
    if btn_google:
        with st.spinner("Google se data laa raha hu + Mistral se summarize kar raha hu..."):
            result = answer_with_google_local(question, router)

        glass_card("🌐 Google-based Answer (via Mistral)", result["answer"])

        st.markdown("<h3 style='color:#38bdf8;margin-top:10px;'>Sources (Google)</h3>", unsafe_allow_html=True)
        for i, src in enumerate(result["sources"], start=1):
            title = src.get("title", "")
            snippet = src.get("snippet", "")
            link = src.get("link", "")
            body = textwrap.dedent(
                f"""[{i}] {title}

{snippet}

🔗 {link}
"""
            )
            glass_card("Source", body)

    # 2️⃣ LOCAL ONLY MODE
    if btn_local:
        with st.spinner("Sirf local Mistral se answer nikal raha hu..."):
            out = router.answer(question)

        glass_card("💻 Local-only Answer (Mistral)", out.get("response", ""))

    # 3️⃣ COMPARE MODE
    if btn_compare:
        with st.spinner("Google + Local dono ka answer nikal ke compare kar raha hu..."):
            web_result = answer_with_google_local(question, router)
            local_out = router.answer(question)

        col_left, col_right = st.columns(2)
        with col_left:
            glass_card("🌐 Google-based Answer", web_result["answer"])
        with col_right:
            glass_card("💻 Local-only Answer", local_out.get("response", ""))

    # 4️⃣ HYBRID SUMMARY MODE
    if btn_hybrid:
        with st.spinner("Google + Local dono ko mila ke ek smart summary bana raha hu..."):
            web_result = answer_with_google_local(question, router)
            local_out = router.answer(question)

            hybrid_prompt = f"""
You are a helpful AI assistant.

User question:
{question}

There are two candidate answers:

[Answer A - from Google search, summarized by an LLM]
{web_result['answer']}

[Answer B - from local LLM only]
{local_out.get('response', '')}

TASK:
- Combine both answers.
- If they agree, give a single clean answer.
- If they differ, explain briefly and then give your best final answer.
- Answer in 1–3 short paragraphs.
"""
            hybrid = router.answer(hybrid_prompt)

        glass_card("🧬 Hybrid Summary (Google + Local)", hybrid.get("response", ""))

        st.markdown("<h3 style='color:#38bdf8;margin-top:10px;'>Key Sources (Google)</h3>", unsafe_allow_html=True)
        for i, src in enumerate(web_result["sources"], start=1):
            title = src.get("title", "")
            link = src.get("link", "")
            snippet = src.get("snippet", "")
            body = f"[{i}] {title}\n\n{snippet}\n\n🔗 {link}"
            glass_card("Source", body)
