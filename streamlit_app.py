import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(
    page_title="Holiday 2027",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("☀️ Holiday Hub")
st.caption("9 Travellers | Khao Lak & Surfers Paradise")

# ---------------------------------------------------------
# LIVE TICKING JAVASCRIPT COUNTDOWN
# ---------------------------------------------------------
st.subheader("🛫 Live Flight Countdowns")

countdown_html = """
<style>
  .countdown - grid {
    display: grid;
    grid - template - columns: repeat(auto - fit, minmax(240px, 1fr));
    gap: 16px;
    font - family: - apple - system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans - serif;
  }
  .card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border - radius: 10px;
    padding: 16px;
    box - shadow: 0 1px 3px rgba(0,0,0,0.05);
  }
  .title {
    font - size: 14px;
    font - weight: 600;
    color: #475569;
    margin - bottom: 6px;
  }
  .timer {
    font - size: 26px;
    font - weight: 700;
    color: #0f172a;
    letter - spacing: - 0.5px;
    margin - bottom: 12px;
  }
  .detail {
    font - size: 13px;
    color: #334155;
    margin: 3px 0;
  }
  .ref {
    font - size: 12px;
    color: #94a3b8;
    margin - top: 8px;
  }
</style>

<div class="countdown - grid">
  <div class="card">
    <div class="title">1. Heathrow to Phuket</div>
    <div class="timer" id="timer - lhr">Loading...</div>
    <div class="detail"><strong>Route:</strong> LHR &rarr; HKT</div>
    <div class="detail"><strong>Flight:</strong> Virgin Atlantic VS214</div>
    <div class="detail"><strong>Departure:</strong> 17 Mar 2027, 16:10 GMT</div>
    <div class="ref">Ref: D48RHT</div>
  </div>

  <div class="card">
    <div class="title">2. Phuket to Singapore</div>
    <div class="timer" id="timer - sin">Loading...</div>
    <div class="detail"><strong>Route:</strong> HKT &rarr; SIN</div>
    <div class="detail"><strong>Flight:</strong> Singapore Airlines SQ739</div>
    <div class="detail"><strong>Departure:</strong> 25 Mar 2027, 20:25 ICT</div>
    <div class="ref">Ref: 5OBEZB</div>
  </div>

  <div class="card">
    <div class="title">3. Singapore to Brisbane</div>
    <div class="timer" id="timer - bne">Loading...</div>
    <div class="detail"><strong>Route:</strong> SIN &rarr; BNE</div>
    <div class="detail"><strong>Flight:</strong> Singapore Airlines SQ255</div>
    <div class="detail"><strong>Departure:</strong> 26 Mar 2027, 00:55 SGT</div>
    <div class="ref">Ref: 5OBEZB</div>
  </div>
</div>

<script>
  const flights = [
    { id: "timer - lhr", date: new Date("2027 - 03 - 17T16:10:00Z").getTime() },
    { id: "timer - sin", date: new Date("2027 - 03 - 25T20:25:00+07:00").getTime() },
    { id: "timer - bne", date: new Date("2027 - 03 - 26T00:55:00+08:00").getTime() }
  ];

  function updateCountdowns() {
    const now = new Date().getTime();
    flights.forEach(f => {
      const distance = f.date - now;
      const el = document.getElementById(f.id);
      if (distance < 0) {
        el.innerHTML = "Departed";
      } else {
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);
        el.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;
      }
    });
  }

  updateCountdowns();
  setInterval(updateCountdowns, 1000);
</script>
"""

# Render the countdown widget
components.html(countdown_html, height=230)

st.divider()

# ---------------------------------------------------------
# TABS SECTION
# ---------------------------------------------------------
THB_TO_GBP = 0.022
AUD_TO_GBP = 0.52

tab_itinerary, tab_expenses, tab_stays, tab_activities = st.tabs([
    "📅 Itinerary",
    "💰 Expenses",
    "📍 Stays & Travel",
    "🙋 Activities"
])

with tab_itinerary:
    st.subheader("Trip Timeline")
    timeline_data = [
        {"Date": "17 Mar", "Stage": "VS214 departs London Heathrow 16:10"},
        {"Date": "18 Mar", "Stage": "Arrive Phuket 11:25, private van to The Sands Khao Lak"},
        {"Date": "19 - 24 Mar", "Stage": "Khao Lak beach, night markets and boat tours"},
        {"Date": "25 Mar", "Stage": "SQ739 departs Phuket 20:25, lands Singapore 23:35"},
        {"Date": "26 Mar", "Stage": "SQ255 departs Singapore 00:55, lands Brisbane 10:45, transfer to Surfers Paradise"},
        {"Date": "27 Mar - 6 Apr", "Stage": "Gold Coast stay, family visits and day trips"},
        {"Date": "07 Apr", "Stage": "Fly Brisbane back to London Heathrow"}
    ]
    st.dataframe(pd.DataFrame(timeline_data), use_container_width=True, hide_index=True)

with tab_expenses:
    st.subheader("Quick Expense Converter & Logger")
    with st.form("spend_form", clear_on_submit=True):
        col_a, col_b = st.columns(2)
        with col_a:
            payer = st.selectbox("Paid by", ["Andy", "Meghann", "Other"])
            item = st.text_input("Item", placeholder="e.g. Minibus transfer, grocery run")
        with col_b:
            curr = st.selectbox("Currency", ["THB", "AUD", "GBP"])
            val = st.number_input("Amount", min_value=0.0, step=1.0)
        
        submit = st.form_submit_button("Record Cost")
        if submit and val > 0:
            conv = val * THB_TO_GBP if curr == "THB" else (val * AUD_TO_GBP if curr == "AUD" else val)
            st.success(f"Recorded {val:,.2f} {curr} (~£{conv:,.2f} GBP) paid by {payer} for {item}")

with tab_stays:
    st.subheader("Addresses & Access Info")
    with st.expander("🏨 The Sands Khao Lak (18 - 25 March)", expanded=True):
        st.markdown("**English:** 10/185 Moo 7, Khuk Khak, Takuapa, Phang Nga 82220")
        st.markdown("**Thai Driver Card:** เดอะแซนด์ เขาหลัก บาย กะตะธานี 10/185 หมู่ 7 ต.คึกคัก อ.ตะกั่วป่า จ.พังงา")
        st.info("Airport transfer: 75 to 90 minutes north from Phuket Airport (HKT).")
    with st.expander("🏄 Surfers Paradise"):
        st.markdown("**Location:** Gold Coast, Queensland")
        st.markdown("**Transfer:** 85 km south from Brisbane Airport via M1 motorway.")

with tab_activities:
    st.subheader("Excursion Headcounts")
    outing = st.selectbox("Outing", ["Currumbin Sanctuary", "Theme Parks", "Burleigh Heads Lunch", "Broadwater Boat Hire"])
    people = st.multiselect("Who is going?", ["Andy", "Meghann", "Robyn", "Adult 4", "Adult 5", "Adult 6", "Adult 7", "Child 2", "Child 3"], default=["Andy"])
    st.metric(label=f"Total head count for {outing}", value=f"{len(people)} of 9")