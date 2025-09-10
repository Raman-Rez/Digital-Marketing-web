import streamlit as st
import pandas as pd

# تنظیمات کلی صفحه
st.set_page_config(
    page_title="دیجیتال مارکتینگ",
    page_icon="🚀",
    layout="wide"
)

# CSS سفارشی برای زیبایی بیشتر
st.markdown(
    """
    <style>
    .main {
        background-color: #fafafa;
        font-family: "Tahoma";
    }
    h1, h2, h3 {
        color: #E63946;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# هدر
st.image("https://source.unsplash.com/1200x400/?digital,marketing", use_container_width=True)
st.title("🚀 آژانس دیجیتال مارکتینگ ما")
st.write("کمک می‌کنیم کسب‌وکار شما در دنیای آنلاین بدرخشد ✨")

# منو
menu = st.sidebar.radio("منو", ["🏠 خانه", "📌 خدمات ما", "🔍 تحلیل کلیدواژه", "📞 تماس با ما"])

# صفحه خانه
if menu == "🏠 خانه":
    st.header("خانه 🏠")
    st.write("""
    خوش آمدید به آژانس دیجیتال مارکتینگ ما!  
    ما تخصص داریم در:
    - 📈 سئو و بهینه‌سازی سایت
    - 📱 مدیریت شبکه‌های اجتماعی
    - 🎯 تبلیغات آنلاین
    - ✍️ تولید محتوا
    """)

# صفحه خدمات
elif menu == "📌 خدمات ما":
    st.header("خدمات ما 📌")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📈 SEO")
        st.write("ارتقاء رتبه سایت شما در گوگل")
        st.subheader("📱 شبکه‌های اجتماعی")
        st.write("مدیریت اینستاگرام، لینکدین و ...")

    with col2:
        st.subheader("🎯 تبلیغات آنلاین")
        st.write("کمپین‌های گوگل ادز و تبلیغات کلیکی")
        st.subheader("✉️ ایمیل مارکتینگ")
        st.write("ارسال ایمیل‌های هدفمند برای جذب مشتری")

# ابزار تحلیل کلیدواژه
elif menu == "🔍 تحلیل کلیدواژه":
    st.header("🔍 تحلیل ساده کلیدواژه")

    keywords_input = st.text_area("کلیدواژه‌ها را وارد کنید (با کاما جدا کنید):", "دیجیتال مارکتینگ, سئو, تبلیغات آنلاین")

    if st.button("تحلیل کن"):
        keywords = [k.strip() for k in keywords_input.split(",")]
        data = {
            "کلیدواژه": keywords,
            "میانگین جستجو (تخمینی)": [len(k)*100 for k in keywords],
            "سختی (1-100)": [min(100, len(k)*10) for k in keywords]
        }
        df = pd.DataFrame(data)
        st.dataframe(df)

# صفحه تماس با ما
elif menu == "📞 تماس با ما":
    st.header("📞 تماس با ما")

    col1, col2 = st.columns(2)

    with col1:
        st.text_input("نام شما:")
        st.text_input("ایمیل شما:")
        st.text_area("پیام شما:")
        if st.button("ارسال"):
            st.success("✅ پیام شما ارسال شد!")

    with col2:
        st.info("📧 ایمیل: raman.rez.2000@gmail.com") 
        st.info("پیج اینستاگرام: New._.Business._.Online")