import streamlit as st
from html import escape

st.set_page_config(
    page_title="나를 소개합니다",
    page_icon="🌈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 이 데이터만 바꾸면 페이지의 소개 내용이 함께 바뀝니다.
PROFILE = {
    "name": "Hyowon Wang",
    "headline": "배우고, 만들고, 세상으로 나아가는 사람",
    "intro": "관심사와 성격, 요즘 빠져 있는 것을 자유롭게 소개해 보세요.",
    "affiliation": "학교 · 학과 · 동아리 등 소속을 입력하세요",
    "dream": "앞으로 이루고 싶은 꿈을 적어 보세요.",
    "cover": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=2000&q=85",
}

CLASSES = [
    {"name": "수업 이름을 입력하세요", "term": "2025 · 봄", "note": "기억에 남는 배움이나 프로젝트를 적어 보세요.", "color": "#ffd43b"},
    {"name": "수업 이름을 입력하세요", "term": "2025 · 가을", "note": "새롭게 알게 된 것과 인상 깊었던 순간을 적어 보세요.", "color": "#62d9c2"},
    {"name": "수업 이름을 입력하세요", "term": "2026 · 봄", "note": "직접 만든 결과물이나 도전한 일을 소개해 보세요.", "color": "#ff8b72"},
]

RESEARCH = [
    {"title": "연구 주제를 입력하세요", "note": "연구의 질문, 함께한 사람, 진행 과정과 결과를 소개해 보세요.", "tag": "진행 중"},
    {"title": "프로젝트 또는 탐구 주제를 입력하세요", "note": "작은 실험이나 관심 분야의 탐구도 멋진 연구 경험이 될 수 있어요.", "tag": "기록"},
]

TRAVELS = [
    {"place": "여행한 곳을 입력하세요", "note": "그곳에서 본 풍경이나 기억하고 싶은 일을 적어 보세요.", "icon": "✦", "color": "#ff6e91"},
    {"place": "여행한 곳을 입력하세요", "note": "새로운 장소에서 만난 맛과 사람을 기록해 보세요.", "icon": "◉", "color": "#6957e8"},
    {"place": "여행한 곳을 입력하세요", "note": "언젠가 다시 가고 싶은 이유를 적어 보세요.", "icon": "✳", "color": "#f49a35"},
]

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700;800&family=Gowun+Dodum&display=swap');

    [data-testid="stAppViewContainer"] { background: #fff9ed; color: #17263d; }
    [data-testid="stHeader"] { background: transparent; }
    .block-container { max-width: 1160px; padding: 1.4rem 2rem 4rem; }
    .stMarkdown { font-family: 'Gowun Dodum', 'DM Sans', sans-serif; }
    .topbar { display: flex; justify-content: space-between; align-items: center; gap: 20px; padding: 8px 0 20px; }
    .wordmark { color: #17263d; font: 800 17px 'DM Sans', sans-serif; }
    .navlinks { display: flex; flex-wrap: wrap; gap: 18px; }
    .navlinks a { color: #17263d; font-size: 13px; text-decoration: none; }
    .navlinks a:hover { color: #f04e83; }
    .hero { min-height: 490px; position: relative; display: flex; align-items: end; overflow: hidden; background-size: cover; background-position: center 48%; border-radius: 4px; color: white; }
    .hero::before { content: ''; position: absolute; inset: 0; background: rgba(15, 25, 45, .48); }
    .hero-copy { position: relative; max-width: 790px; padding: 64px 7%; }
    .eyebrow { font: 700 12px 'DM Sans', sans-serif; letter-spacing: 1px; text-transform: uppercase; }
    .hero h1 { margin: 18px 0 14px; color: white; font: 800 66px/1.12 'Gowun Dodum', sans-serif; }
    .hero p { max-width: 620px; margin: 0; color: white; font-size: 19px; line-height: 1.7; }
    .hero-chip { display: inline-block; margin-top: 24px; padding: 9px 14px; background: #ffcf38; color: #17263d; font-size: 13px; font-weight: 700; }
    .ticker { display: flex; justify-content: space-between; gap: 12px; padding: 15px 4px; color: #17263d; font: 700 12px 'DM Sans', sans-serif; }
    .section { padding: 70px 7%; margin-top: 30px; }
    .section-kicker { color: #f04e83; font: 800 12px 'DM Sans', sans-serif; letter-spacing: 1px; text-transform: uppercase; }
    .section h2 { margin: 10px 0 24px; color: #17263d; font: 800 39px/1.2 'Gowun Dodum', sans-serif; }
    .section p { color: #263650; font-size: 17px; line-height: 1.8; }
    .about { background: #ffffff; border-top: 8px solid #ff6e91; }
    .about-grid { display: grid; grid-template-columns: 1.4fr 1fr; gap: 38px; align-items: start; }
    .about-note { padding: 24px; background: #b7f1df; color: #17263d; font-size: 16px; line-height: 1.8; }
    .duo { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; margin-top: 18px; }
    .color-block { min-height: 200px; padding: 28px; }
    .color-block h3 { margin: 0 0 18px; font: 800 24px 'Gowun Dodum', sans-serif; }
    .color-block p { margin: 0; }
    .affiliation { background: #55c8e8; }
    .dream { background: #d3ef5b; }
    .classes { background: #ffe8ad; }
    .item-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; }
    .class-item { min-height: 220px; padding: 22px; color: #17263d; }
    .class-item .term { font: 700 12px 'DM Sans', sans-serif; }
    .class-item h3 { margin: 25px 0 10px; font: 800 20px 'Gowun Dodum', sans-serif; }
    .class-item p { margin: 0; font-size: 14px; }
    .research { background: #f35e50; }
    .research .section-kicker, .research h2, .research p { color: #17263d; }
    .research-list { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; }
    .research-item { padding: 22px 0; border-top: 2px solid #17263d; }
    .research-item h3 { margin: 12px 0; font: 800 21px 'Gowun Dodum', sans-serif; }
    .tag { padding: 5px 9px; background: #17263d; color: white; font: 700 11px 'DM Sans', sans-serif; }
    .research-item p { margin-bottom: 0; font-size: 15px; }
    .travels { background: #d9e8ff; }
    .travel-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; }
    .travel-item { min-height: 220px; padding: 22px; color: white; }
    .travel-icon { font-size: 34px; }
    .travel-item h3 { margin: 25px 0 10px; font: 800 20px 'Gowun Dodum', sans-serif; }
    .travel-item p { margin: 0; color: white; font-size: 14px; }
    .footer { margin-top: 30px; padding: 30px 7%; background: #3157d5; color: white; display: flex; justify-content: space-between; gap: 16px; }
    .footer p { margin: 0; color: white; font-size: 14px; }
    @media (max-width: 720px) {
      .block-container { padding: 1rem 1rem 2rem; }
      .topbar, .ticker, .footer { align-items: flex-start; flex-direction: column; }
      .navlinks { gap: 10px 14px; }
      .hero { min-height: 440px; }
      .hero-copy { padding: 38px 7%; }
      .hero h1 { font-size: 44px; }
      .hero p { font-size: 16px; }
      .section { padding: 42px 7%; }
      .section h2 { font-size: 31px; }
      .about-grid, .duo, .item-grid, .research-list, .travel-grid { grid-template-columns: 1fr; }
      .color-block, .class-item, .travel-item { min-height: auto; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

safe = lambda value: escape(str(value), quote=True)
nav_items = [("소개", "about"), ("소속", "affiliation"), ("꿈", "dream"), ("수업", "classes"), ("연구", "research"), ("여행", "travels")]
nav_html = "".join(f'<a href="#{anchor}">{label}</a>' for label, anchor in nav_items)
class_html = "".join(
    f'<article class="class-item" style="background:{item["color"]}">'
    f'<span class="term">{safe(item["term"])}</span>'
    f'<h3>{safe(item["name"])}</h3><p>{safe(item["note"])}</p></article>'
    for item in CLASSES
)
research_html = "".join(
    f'<article class="research-item"><span class="tag">{safe(item["tag"])}</span>'
    f'<h3>{safe(item["title"])}</h3><p>{safe(item["note"])}</p></article>'
    for item in RESEARCH
)
travel_html = "".join(
    f'<article class="travel-item" style="background:{item["color"]}">'
    f'<span class="travel-icon">{safe(item["icon"])}</span>'
    f'<h3>{safe(item["place"])}</h3><p>{safe(item["note"])}</p></article>'
    for item in TRAVELS
)

st.markdown(
    f"""
    <nav class="topbar"><div class="wordmark">MY COLORFUL WORLD</div><div class="navlinks">{nav_html}</div></nav>
    <header class="hero" style="background-image:url('{safe(PROFILE['cover'])}')">
      <div class="hero-copy"><span class="eyebrow">A LITTLE INTRODUCTION</span>
        <h1>안녕하세요,<br>{safe(PROFILE['name'])}입니다.</h1>
        <p>{safe(PROFILE['headline'])}</p><span class="hero-chip">나의 이야기 · 2026</span>
      </div>
    </header>
    <div class="ticker"><span>ABOUT ME</span><span>STUDY · RESEARCH · TRAVEL</span><span>MADE WITH CURIOSITY</span></div>

    <section class="section about" id="about">
      <span class="section-kicker">01 / ABOUT ME</span><h2>저를 소개합니다</h2>
      <div class="about-grid"><p>{safe(PROFILE['intro'])}</p>
        <div class="about-note">좋아하는 것, 잘하는 것, 요즘 궁금한 것.<br>나를 가장 잘 보여 주는 이야기를 적어 보세요.</div>
      </div>
      <div class="duo">
        <article class="color-block affiliation" id="affiliation"><h3>지금의 소속</h3><p>{safe(PROFILE['affiliation'])}</p></article>
        <article class="color-block dream" id="dream"><h3>나의 꿈</h3><p>{safe(PROFILE['dream'])}</p></article>
      </div>
    </section>

    <section class="section classes" id="classes">
      <span class="section-kicker">02 / THINGS I LEARNED</span><h2>내가 들었던 수업</h2>
      <div class="item-grid">{class_html}</div>
    </section>

    <section class="section research" id="research">
      <span class="section-kicker">03 / QUESTIONS I FOLLOW</span><h2>내가 했던 연구</h2>
      <div class="research-list">{research_html}</div>
    </section>

    <section class="section travels" id="travels">
      <span class="section-kicker">04 / PLACES I HAVE BEEN</span><h2>내가 여행했던 곳</h2>
      <div class="travel-grid">{travel_html}</div>
    </section>
    <footer class="footer"><p>계속 배우고, 새로운 이야기를 만들어 가는 중.</p><p>{safe(PROFILE['name'])} · PERSONAL PAGE</p></footer>
    """,
    unsafe_allow_html=True,
)