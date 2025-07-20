# if you want to visualise on UI, use this file and run manually in your local
import streamlit as st
import os
import json

# Load matches from the generated file
MATCH_FILE = "job_matches/weekly_matches.json"

def load_matches():
    if os.path.exists(MATCH_FILE):
        with open(MATCH_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def main():
    st.set_page_config(page_title="Job Match Viewer", layout="centered")
    st.title("🔍 Weekly Job Matches")

    matches = load_matches()

    if not matches:
        st.warning("No matches found. Run the matcher script first.")
        return

    for job in matches:
        with st.expander(f"📄 {job['file']} — Fit Score: {job['fit_score']}"):
            st.markdown(f"**✅ Matched Skills:** {', '.join(job['matched_skills']) or 'None'}")
            st.markdown(f"**❌ Missing Skills:** {', '.join(job['missing_skills']) or 'None'}")
            st.progress(job['fit_score'])

if __name__ == "__main__":
    main()
