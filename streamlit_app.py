import streamlit as st
import pandas as pd
from datetime import datetime, timezone, timedelta

st.set_page_config(
    page_title="Holiday 2027",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("☀️ Holiday Hub")
st.caption("9 Travellers | Khao Lak & Surfers Paradise")

# ---------------------------------------------------------
# FLIGHT COUNTDOWNS
# ---------------------------------------------------------
st.subheader("🛫 Flight Countdowns")

now_utc = datetime.now(timezone.utc)

flights = [
    {
        "name": "1. Heathrow to Phuket",
        "flight": "Virgin Atlantic VS214",
        "ref": "D48RHT",
        "route": "LHR -> HKT",
        "depart_local": "17 Mar 2027, 16:10 GMT",
        "depart_dt": datetime(2027, 3, 17, 16, 10, tzinfo=timezone.utc)
    },
    {
        "name": "2. Phuket to Singapore",
        "flight": "Singapore Airlines SQ739",
        "ref": "5OBEZB",
        "route": "HKT -> SIN",
        "depart_local": "25 Mar 2027, 20:25 ICT",
        "depart_dt": datetime(2027, 3, 25, 20, 25, tzinfo=timezone(timedelta(hours=7)))
    },
    {
        "name": "3. Singapore to Brisbane",
        "flight": "Singapore Airlines SQ255",
        "ref": "5OBEZB",
        "route": "SIN -> BNE",
        "depart_local": "26 Mar 2027, 00:55 SGT",
        "depart_dt": datetime(2027, 3, 26, 0, 55, tzinfo=timezone(timedelta(hours=8)))
    }
]

cols = st.columns(3)

for idx, flight in enumerate(flights):
    with cols[idx]:
        diff = flight["depart_dt"] - now_utc
        if diff.total_seconds() > 0:
            days = diff.days
            hours = diff.seconds // 3600
            mins = (diff.seconds % 3600) // 60
            countdown_str = f"{days}d {hours}h {mins}m"
        else:
            countdown_str = "Departed"

        with st.container(border=True):
            st.metric(label=flight["name"], value=countdown_str)
            st.markdown(f"**Route:** {flight['route']}")
            st.markdown(f"**Flight:** {flight['flight']}")
            st.markdown(f"**Departure:** {flight['depart_local']}")
            st.caption(f"Ref: {flight['ref']}")

st.divider()

# ---------------------------------------------------------
# TABS SECTION
# ---------------------------------------------------------
# Exchange rate reference values
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