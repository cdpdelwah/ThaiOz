import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Holiday 2027",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("☀️ Holiday Hub")
st.caption("9 Travellers | Khao Lak & Surfers Paradise")

# Exchange rate reference constants
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
        {"Date": "17 Mar", "Stage": "Fly Heathrow to Phuket (HKT)"},
        {"Date": "18 Mar", "Stage": "Arrive HKT, 80 min private van to The Sands Khao Lak"},
        {"Date": "19 - 24 Mar", "Stage": "Khao Lak beach, night markets and boat tours"},
        {"Date": "25 Mar", "Stage": "Transfer to HKT, fly via Singapore to Brisbane (BNE)"},
        {"Date": "26 Mar", "Stage": "Land in Brisbane, transfer south to Surfers Paradise"},
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