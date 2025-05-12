import streamlit as st

st.set_page_config(layout="wide", page_title="📊 Аналитика задач с отклонениями")

st.title("📈 Дашборд: Аналитика задач с отклонениями по ОСП(2024–2025)")
st.markdown("Автор: **Анатолий, Data Science, BIA Technologies**", unsafe_allow_html=True)

st.divider()

# === Раздел: Холдинг ===
import streamlit as st

st.set_page_config(layout="wide", page_title="📊 Аналитика задач с отклонениями")

st.title("📈 Дашборд: Аналитика задач с отклонениями по ОСП (2024–2025)")
st.markdown("Автор: **Анатолий, Data Science, BIA Technologies**", unsafe_allow_html=True)
st.divider()

# === Раздел: Холдинг ===
st.subheader("Холдинг (ежемесячно)")
with open("monthly_holding.html", "r", encoding="utf-8") as f:
    st.components.v1.html(f.read(), height=600, scrolling=True)

st.subheader("Холдинг (еженедельно)")
with open("weekly_holding.html", "r", encoding="utf-8") as f:
    st.components.v1.html(f.read(), height=600, scrolling=True)

st.divider()

# === Раздел: Регионы ===
st.subheader("Регионы (ежемесячно)")
with open("monthly_region.html", "r", encoding="utf-8") as f:
    st.components.v1.html(f.read(), height=600, scrolling=True)

st.subheader("Регионы (еженедельно)")
with open("weekly_region.html", "r", encoding="utf-8") as f:
    st.components.v1.html(f.read(), height=600, scrolling=True)

st.divider()

# === Раздел: Топ ОСП ===
st.subheader("🏢 Топ-ОСП по отклонениям (ежемесячно)")
with open("top_osp_monthly.html", "r", encoding="utf-8") as f:
    st.components.v1.html(f.read(), height=600, scrolling=True)

st.divider()

# === Раздел: Сентимент ===
st.subheader("🧠 Сентимент по задачам (ежемесячно)")
with open("sentiment_full.html", "r", encoding="utf-8") as f:
    st.components.v1.html(f.read(), height=600, scrolling=True)

st.divider()

# === Раздел: Категории ===
st.subheader("🔥 Топ-20 категорий проблем (суммарно)")
with open("top20_categories.html", "r", encoding="utf-8") as f:
    st.components.v1.html(f.read(), height=600, scrolling=True)

st.subheader("📍 Топ-10 категорий по регионам")
with open("top10_categories_by_region.html", "r", encoding="utf-8") as f:
    st.components.v1.html(f.read(), height=600, scrolling=True)

st.subheader("📈 Динамика категорий по месяцам")
with open("top10_categories_trend.html", "r", encoding="utf-8") as f:
    st.components.v1.html(f.read(), height=600, scrolling=True)


st.divider()
st.markdown("© Роман Анатолий, 2025.")
