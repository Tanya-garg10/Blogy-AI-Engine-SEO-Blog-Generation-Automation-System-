import streamlit as st
from utils.prompt_engine import generate_blog, generate_strategy
from utils.seo_validator import calculate_seo_score
from utils.formatter import format_blog
from utils.serp_gap import get_serp_gap_insights
from utils.helpers import save_blog_to_file, word_count, estimate_readability

st.set_page_config(page_title="Blogy AI Engine Prototype", page_icon="🚀", layout="wide")

st.title("🚀 Blogy AI Engine Prototype")
st.write("Generate SEO-optimized blogs with strategy, validation, and platform formatting.")

keyword = st.text_input("Enter Target Keyword", placeholder="e.g. Best AI Blog Automation Tool in India")

col1, col2 = st.columns(2)

with col1:
    audience = st.selectbox("Target Audience", ["Startups", "Marketers", "Founders", "Businesses", "Agencies"])

with col2:
    platform = st.selectbox("Publishing Platform", ["Medium", "LinkedIn", "WordPress", "Dev.to", "Hashnode"])

generate = st.button("Generate Blog")

if generate:
    if not keyword.strip():
        st.warning("Please enter a keyword.")
    else:
        try:
            with st.spinner("Generating SEO strategy..."):
                strategy = generate_strategy(keyword, audience)

            with st.spinner("Generating blog..."):
                blog = generate_blog(keyword, audience)

            score = calculate_seo_score(blog, keyword)
            formatted_blog = format_blog(blog, platform)
            gaps = get_serp_gap_insights(keyword)
            total_words = word_count(blog)
            readability = estimate_readability(blog)

            save_blog_to_file(blog)

            st.success("Blog generated successfully.")

            metric1, metric2, metric3 = st.columns(3)
            with metric1:
                st.metric("SEO Score", f"{score}/100")
            with metric2:
                st.metric("Word Count", total_words)
            with metric3:
                st.metric("Readability", readability)

            tab1, tab2, tab3, tab4 = st.tabs([
                "SEO Strategy",
                "Generated Blog",
                "Formatted Output",
                "SERP Gap Insights"
            ])

            with tab1:
                st.subheader("SEO Strategy")
                st.write(strategy)

            with tab2:
                st.subheader("Generated Blog")
                st.write(blog)

            with tab3:
                st.subheader(f"Formatted for {platform}")
                st.write(formatted_blog)

            with tab4:
                st.subheader("SERP Gap Insights")
                for gap in gaps:
                    st.write(f"• {gap}")

            st.download_button(
                label="Download Blog as TXT",
                data=blog,
                file_name="generated_blog.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"Error: {e}")