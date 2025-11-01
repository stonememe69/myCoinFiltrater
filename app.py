import streamlit as st
import pandas as pd

st.set_page_config(page_title="Hidden Gem Finder", layout="wide")

st.title("💎 Hidden Gem Filter App")
st.markdown("Use this app to systematically score crypto coins and find potential hidden gems.")

# Initialize session state
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=[
        "Coin", "Sector", "Market Context", "Sector Flow", "Smart Money",
        "Exchange Flow", "Volume & OI", "Chart Setup", "OBV Strength",
        "Social Buzz", "Liquidity", "Contract Safety", "Final Score", "Notes"
    ])

st.sidebar.header("🧠 How to Use")
st.sidebar.write("""
1. Enter a coin name & sector  
2. Score each metric from 1 (weak) → 5 (strong)  
3. Press **Add Coin** to store result  
4. Compare and download your final filtered list
""")

# Input section
st.subheader("🔍 Coin Information")
coin_name = st.text_input("Coin Name / Symbol")
sector = st.text_input("Sector (e.g., AI, DeFi, Gaming)")

# Scoring sliders
st.subheader("📊 Scoring Metrics (1–5)")
cols = st.columns(3)

with cols[0]:
    market_context = st.slider("Market Context", 1, 5, 3)
    sector_flow = st.slider("Sector Flow", 1, 5, 3)
    smart_money = st.slider("Smart Money Inflow", 1, 5, 3)
    exchange_flow = st.slider("Exchange Flow (Outflows Bullish)", 1, 5, 3)

with cols[1]:
    volume_oi = st.slider("Volume & Open Interest", 1, 5, 3)
    chart_setup = st.slider("Chart Structure", 1, 5, 3)
    obv_strength = st.slider("OBV & Volume Strength", 1, 5, 3)

with cols[2]:
    social_buzz = st.slider("Social Buzz (Narrative Stage)", 1, 5, 3)
    liquidity = st.slider("Liquidity / Volume", 1, 5, 3)
    contract_safety = st.slider("Contract & Security", 1, 5, 3)

notes = st.text_area("📝 Notes (optional)", placeholder="Observations, key levels, or narrative notes...")

# Compute final score
scores = [market_context, sector_flow, smart_money, exchange_flow, volume_oi,
          chart_setup, obv_strength, social_buzz, liquidity, contract_safety]
final_score = round(sum(scores) / len(scores), 2)
st.metric("Final Confluence Score", f"{final_score}/5")

# Button to add data
if st.button("➕ Add Coin"):
    new_row = {
        "Coin": coin_name,
        "Sector": sector,
        "Market Context": market_context,
        "Sector Flow": sector_flow,
        "Smart Money": smart_money,
        "Exchange Flow": exchange_flow,
        "Volume & OI": volume_oi,
        "Chart Setup": chart_setup,
        "OBV Strength": obv_strength,
        "Social Buzz": social_buzz,
        "Liquidity": liquidity,
        "Contract Safety": contract_safety,
        "Final Score": final_score,
        "Notes": notes
    }
    st.session_state.data = pd.concat([st.session_state.data, pd.DataFrame([new_row])], ignore_index=True)
    st.success(f"Added {coin_name} ✅")

# Display results
st.subheader("📈 Coin Scores Table")
if not st.session_state.data.empty:
    st.dataframe(st.session_state.data, use_container_width=True)
else:
    st.info("No coins added yet.")

# Chart
if not st.session_state.data.empty:
    st.subheader("📊 Score Comparison")
    chart_data = st.session_state.data[["Coin", "Final Score"]].set_index("Coin")
    st.bar_chart(chart_data)

# Download button
if not st.session_state.data.empty:
    csv = st.session_state.data.to_csv(index=False)
    st.download_button("⬇️ Download Results (CSV)", csv, "hidden_gem_scores.csv", "text/csv")
