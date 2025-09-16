import streamlit as st
import pandas as pd
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Local imports
from utils import load_templates, generate_hashtags, add_emojis, export_to_csv

# ---------- CONFIG ----------
st.set_page_config(page_title="ContentCraft AI ✍️", page_icon="✨", layout="wide")

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load templates
templates = load_templates()

# ---------- SIDEBAR ----------
st.sidebar.title("⚙️ Options")
mode = st.sidebar.radio("Choose Mode:", ["Single Prompt", "Bulk CSV"])

content_type = st.sidebar.selectbox("Content Type:", list(templates["content_types"].keys()))
tone = st.sidebar.selectbox("Tone:", templates["tones"])
length = st.sidebar.selectbox("Length:", templates["lengths"])

# ---------- MAIN TITLE ----------
st.title("✨ ContentCraft AI ✍️")
st.write("Generate professional, motivational, or creative content for social media, blogs, and reports.")

# ---------- SINGLE PROMPT MODE ----------
if mode == "Single Prompt":
    topic = st.text_input("Enter your topic/idea:")
    if st.button("Generate Content 🚀"):
        if topic.strip() == "":
            st.warning("Please enter a topic.")
        else:
            prompt = f"""
            Write a {length.lower()} {content_type.replace('_',' ')} 
            in a {tone.lower()} tone about "{topic}".
            """
            try:
                model = genai.GenerativeModel('gemini-2.5-pro')
                response = model.generate_content(prompt)
                generated_text = response.text.strip()

                # Add emojis + hashtags
                final_text = add_emojis(generated_text, mood=tone)
                hashtags = generate_hashtags(topic, count=5)

                st.subheader("📝 Generated Content:")
                st.write(final_text)
                st.markdown(f"**Hashtags:** {hashtags}")

            except Exception as e:
                st.error(f"Error generating content: {e}")

# ---------- BULK CSV MODE ----------
else:
    uploaded_file = st.file_uploader("Upload a CSV file (topic, content_type, tone, length):", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)

        if st.button("Generate Bulk Content 🚀"):
            results = []
            for _, row in df.iterrows():
                prompt = f"""
                Write a {row['length'].lower()} {row['content_type'].replace('_',' ')} 
                in a {row['tone'].lower()} tone about "{row['topic']}".
                """
                try:
                    model = genai.GenerativeModel('gemini-2.5-pro')
                    response = model.generate_content(prompt)
                    text = response.text.strip()
                    text = add_emojis(text, mood=row['tone'])
                    hashtags = generate_hashtags(row['topic'], count=5)

                    results.append({
                        "topic": row['topic'],
                        "content_type": row['content_type'],
                        "tone": row['tone'],
                        "length": row['length'],
                        "content": text,
                        "hashtags": hashtags
                    })
                except Exception as e:
                    results.append({
                        "topic": row['topic'],
                        "content_type": row['content_type'],
                        "tone": row['tone'],
                        "length": row['length'],
                        "content": f"Error: {e}",
                        "hashtags": ""
                    })

            st.success("✅ Bulk content generated!")
            results_df = pd.DataFrame(results)
            st.dataframe(results_df)

            # Export option
            filename = export_to_csv(results, "bulk_generated_content.csv")
            st.download_button(
                label="📥 Download Results as CSV",
                data=open(filename, "rb").read(),
                file_name="bulk_generated_content.csv",
                mime="text/csv"
            )
