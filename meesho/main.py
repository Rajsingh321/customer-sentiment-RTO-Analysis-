import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="RTO & Customer Sentiment Analysis | Raj Singh", layout="wide")

# --- Custom Title ---
st.markdown("""
    <h1 style='text-align: center; font-size: 42px; color: #262730;'>
        📦 Customer Sentiment & RTO Analysis – E-commerce
    </h1>
    <h3 style='text-align: center; font-weight: 400; color: #555;'>
        Reducing Returns and Improving Delivery Experience with Data
    </h3>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- Problem Statement ---
st.markdown("## 🧩 Problem Statement", unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 25px; text-align: justify;'>
High Return-to-Origin (RTO) rates in e-commerce lead to increased costs, blocked inventory, and poor customer experience due to failed deliveries, rejections, and quality issues.  
These RTOs damage both operational efficiency and brand trust. Addressing them is essential for sustainable growth.
</p>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- Objective ---
st.markdown("## 🎯 Objective", unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 25px; text-align: justify;'>
The objective of this project is to deeply analyze patterns related to Return-to-Origin (RTO) and customer sentiment within an e-commerce environment.  
By exploring return reasons, customer feedback, delivery behavior, and regional distribution, the goal is to uncover the underlying causes behind undelivered and returned orders.  
This analysis aims to generate meaningful insights that help reduce RTO rates, streamline logistics, improve customer satisfaction, and support better decision-making for operations and marketing teams.
</p>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- Dataset Overview ---
st.markdown("## 🗃 Dataset Overview", unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 25px;'>         
- 3,000+ order records<br>
- 10 key columns: Order ID, Category, Sales, Profit, Sentiment, Return Reason, Pincode, Return Days, Delivery Status<br>
- Covers return behaviors, customer experience, and delivery outcomes<br>
- Enables deep analysis of return trends and feedback patterns
</p>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- Analysis Process ---
st.markdown("## 🔍 Analysis Process", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

# --- Data Analysis ---
with col1:
    st.markdown("""
        <div style='background-color: #ffffff; border: 1px solid #eee; border-radius: 12px; padding: 24px; text-align: center;'>
            <div style='font-size: 36px;'>📊</div>
            <h4 style='margin-top: 10px;'>Data Analysis</h4>
            <p style='color: #555; font-size: 20px;'>
                Cleaned and explored return data, categories, and regions to find high-return areas and patterns.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
# --- Sentiment Analysis ---
with col2:
    st.markdown("""
        <div style='background-color: #ffffff; border: 1px solid #eee; border-radius: 12px; padding: 24px; text-align: center;'>
            <div style='font-size: 36px;'>💬</div>
            <h4 style='margin-top: 10px;'>Sentiment Analysis</h4>
            <p style='color: #555; font-size: 20px;'>
                Analyzed product reviews to classify feedback and link sentiment with return and product issues.
            </p>
        </div>
    """, unsafe_allow_html=True)

# --- Dashboard Creation ---
with col3:
    st.markdown("""
        <div style='background-color: #ffffff; border: 1px solid #eee; border-radius: 12px; padding: 24px; text-align: center;'>
            <div style='font-size: 36px;'>📈</div>
            <h4 style='margin-top: 10px;'>Dashboard Creation</h4>
            <p style='color: #555; font-size: 20px;'>
                Built an interactive Streamlit dashboard to visualize RTO, sentiment, return reasons, and locations.
            </p>
        </div>
    """, unsafe_allow_html=True)
    with open("files/meesho_RTO_Analysis.pbix", "rb") as f:
        st.download_button("See Dashboard", f, file_name="meesho_RTO_Analysis.pbix", key="See Dashboard")

# --- Data Storytelling ---
with col4:
    st.markdown("""
        <div style='background-color: #ffffff; border: 1px solid #eee; border-radius: 12px; padding: 24px; text-align: center;'>
            <div style='font-size: 36px;'>🗣</div>
            <h4 style='margin-top: 10px;'>Data Storytelling</h4>
            <p style='color: #555; font-size: 20px;'>
                Designed a presentation to explain insights, connect problems, and guide business decisions on RTO.
            </p>
        </div>
    """, unsafe_allow_html=True)
    #with open("files/rto_data_presentation.pptx", "rb") as f:
        #st.download_button("See Presentation", f, file_name="rto_data_presentation.pptx", key="rto_story_download")

st.markdown("<hr>", unsafe_allow_html=True)

# --- Key Insights ---
st.markdown("## 📊 Key Insights", unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 20px;'>
✅ <b>Total sales</b> amounted to <b>$9 million</b>.<br>
✅ <b>Total profit</b> recorded was <b>$351K</b>.<br>
✅ <b>The average RTO rate</b> across orders is <b>23.5%</b>.<br>
✅ <b>Average return time</b> is <b>12 days</b>.<br>
✅ <b>74.9% of customer sentiment</b> is <b>positive</b>.<br>
✅ <b>23.5% of customer sentiment</b> is <b>negative</b>.<br>
✅ <b>General negative feedback = 70.93%</b>of all negative responses.<br>
✅ <b>Product broken/damaged = 12.5%</b>, <b>incomplete product = 6.1%</b>, <b>poor quality= 5.52%</b>.<br>
✅ <b>Pincode 9</b> has the highest return <b>count (50)</b>, followed by 6 and 8 (38 each), 10 (35), and 1 (33).
</p>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- Visuals ---
st.markdown("## 📸 Dashboard Visuals", unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 20px;'>
All key insights are presented through an interactive Streamlit dashboard that includes KPIs, charts, and visual breakdowns of RTO patterns and customer sentiment.
</p>
""", unsafe_allow_html=True)

st.image("files/dashboard.jpg", caption="RTO Dashboard Overview", use_column_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- Business Recommendations ---
st.markdown("## 📌 Business Recommendations", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <p style='font-size: 20px;'> 
    1. Apply stricter quality checks on high-return categories like Electronics and Home & Kitchen.<br>
    2. Audit delivery operations in top return pincodes to reduce RTO from regional failures.<br>
    3. Use product-level sentiment to flag low-performing SKUs and underperforming suppliers.<br>
    4. Set automated return reason alerts to pause problematic products and notify operations.
    </p>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <p style='font-size: 20px;'>
    5. Improve packaging for fragile items to reduce damage-related returns.<br>
    6. Promote prepaid orders through incentives to reduce COD-based RTO.<br>
    7. Provide sellers with real-time return insights to drive accountability and improvements.<br>
    8. Benchmark courier partners by RTO performance and optimize delivery assignments.
    </p>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- Conclusion ---
st.markdown("## 🧠 Conclusion", unsafe_allow_html=True)

st.markdown("""
<p style='font-size: 20px; text-align: justify;'>
<b>Problem:</b> High RTO rates and negative customer sentiment were driving operational losses and hurting delivery efficiency.<br><br>
<b>Solving Approach:</b> I analyzed return reasons, customer feedback, product categories, and regional patterns using real-world-style data to identify the root causes behind failed deliveries.<br><br>
<b>Solution:</b> The insights led to clear, actionable strategies—improving product quality, targeting high-RTO regions, optimizing packaging, and using sentiment analytics—to reduce returns and improve overall business performance.
</p>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- Tools Used + Links ---
st.markdown("## 🛠 Tools & Links", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <p style='font-size: 20px;'>         
    - Python: pandas,for data cleaning and analysis<br>
    - Streamlit: for dashboard creation and frontend interface<br>
    - Excel: quick data validation<br>
    - Canva / PowerPoint: for storytelling and presentation slides
    </p>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <p style='font-size: 20px;'> 
    🔗 <a href="https://github.com/Rajsingh321/customer-sentiment-RTO-Analysis-/blob/main/meesho/main.py" target="_blank">GitHub Repository</a><br>
    🔗 <a href="https://www.linkedin.com/in/rajsinghsendhav" target="_blank">LinkedIn</a><br>
    🔗 <a href="https://rajsingh-sendhav-data-analytics-portfolio-x5kgg6xfxmkqdex5sbdq.streamlit.app/" target="_blank">Portfolio Website</a>
    </p>
    """, unsafe_allow_html=True)

    st.download_button("📄 See Resume", "files/Rajsingh_DataAnalyst_Resume.pdf", file_name="Rajsingh_Data_Analyst_Resume.pdf", key="See Resume")
