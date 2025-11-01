import streamlit as st
import pandas as pd

st.set_page_config(page_title="💎 Hidden Gem Pipeline", layout="wide")

st.title("💎 Hidden Gem Discovery Pipeline")
st.markdown("""
Systematic pipeline to filter **raw coins → profitable setups**  
Follow the stages, verify data using the linked tools, and mark ✅ or ❌ based on factual signals.
""")

# Initialize storage
if "coins" not in st.session_state:
    st.session_state.coins = []

# --- Input section ---
st.sidebar.header("🪙 Add New Coin")
coin_name = st.sidebar.text_input("Coin Name / Symbol")
sector = st.sidebar.text_input("Sector (e.g. AI, DeFi, Gaming)")
notes = st.sidebar.text_area("Notes or Key Narrative Points")

# --- Pipeline Stages ---
st.divider()
st.subheader("🔍 Stage 1 — Discovery Layer")
st.markdown("""
**Goal:** Find early tokens with growing activity & liquidity.  
**Tools:** [Birdeye](https://birdeye.so), [DEXTools](https://www.dextools.io/), [DexCheck](https://dexcheck.ai), [Kaito AI](https://kaito.ai)
""")
stage1 = st.radio("Stage 1: Found via early discovery platforms with $100k+ volume & $200k+ LP?", ["❌ No", "✅ Yes"], index=0)

st.divider()
st.subheader("💰 Stage 2 — Smart Money Validation")
st.markdown("""
**Goal:** Verify whales or smart wallets accumulating.  
**Tools:** [Arkham](https://arkhamintelligence.com), [Nansen](https://www.nansen.ai), [Santiment](https://santiment.net), [DeFiLlama](https://defillama.com)
""")
stage2 = st.radio("Stage 2: Smart money inflow confirmed (accumulation >24h)?", ["❌ No", "✅ Yes"], index=0)

st.divider()
st.subheader("📊 Stage 3 — On-Chain Activity Check")
st.markdown("""
**Goal:** Confirm user activity & fee growth.  
**Tools:** [Artemis](https://app.artemis.xyz/), [Token Terminal](https://tokenterminal.com/), [Santiment](https://santiment.net)
""")
stage3 = st.radio("Stage 3: On-chain metrics trending up (active users / fees / TVL)?", ["❌ No", "✅ Yes"], index=0)

st.divider()
st.subheader("📈 Stage 4 — Technical Setup Validation")
st.markdown("""
**Goal:** Ensure chart is coiling for breakout.  
**Tools:** [TradingView](https://tradingview.com), [Loris.tools](https://loris.tools), [Coinalyze](https://coinalyze.net), [Laevitas](https://laevitas.ch)
""")
stage4 = st.radio("Stage 4: Structure shows breakout base (rising OI + healthy funding)?", ["❌ No", "✅ Yes"], index=0)

st.divider()
st.subheader("🧠 Stage 5 — Sentiment & Narrative Momentum")
st.markdown("""
**Goal:** Confirm early narrative traction, not peak hype.  
**Tools:** [Santiment](https://santiment.net), [LunarCrush](https://lunarcrush.com), [Kaito.ai](https://kaito.ai), [Twitter Search](https://x.com/search)
""")
stage5 = st.radio("Stage 5: Narrative forming (rising mentions, moderate buzz)?", ["❌ No", "✅ Yes"], index=0)

st.divider()
st.subheader("💦 Stage 6 — Liquidity & Safety Check")
st.markdown("""
**Goal:** Verify liquidity & contract safety.  
**Tools:** [Dexscreener](https://dexscreener.com), [GoPlus](https://gopluslabs.io), [RugDoc](https://rugdoc.io)
""")
stage6 = st.radio("Stage 6: Liquidity > $200k, verified contract, no honeypot?", ["❌ No", "✅ Yes"], index=0)

# --- Compute Result ---
st.divider()
passes = [stage1, stage2, stage3, stage4, stage5, stage6].count("✅ Yes")
progress = int((passes / 6) * 100)

if passes == 6:
    verdict = "🚀 Potential Hidden Gem (Strong Confluence)"
elif passes >= 4:
    verdict = "⚡ Worth Monitoring (Medium Confluence)"
else:
    verdict = "❌ Weak Setup (Skip)"

st.subheader("🧩 Pipeline Summary")
st.progress(progress / 100)
st.write(f"**{passes}/6 stages passed** — {verdict}")

# --- Add coin to list ---
if st.sidebar.button("➕ Add Coin to List"):
    if coin_name:
        st.session_state.coins.append({
            "Coin": coin_name,
            "Sector": sector,
            "Passes": passes,
            "Progress (%)": progress,
            "Verdict": verdict,
            "Notes": notes
        })
        st.sidebar.success(f"{coin_name} added to list ✅")
    else:
        st.sidebar.warning("Please enter a coin name first.")

# --- Display Saved Coins ---
st.divider()
st.subheader("📋 Filtered Coin List")

if st.session_state.coins:
    df = pd.DataFrame(st.session_state.coins)
    st.dataframe(df, use_container_width=True)

    csv = df.to_csv(index=False)
    st.download_button("⬇️ Download Results (CSV)", csv, "hidden_gem_pipeline.csv", "text/csv")
else:
    st.info("No coins added yet. Use the sidebar to add your first coin!")
