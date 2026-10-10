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

# The 9 Travellers
GROUP = ["Andy", "Meg", "Hannah", "Jo", "Laila", "Molly", "Ethan", "Robyn", "Amber"]

# ---------------------------------------------------------
# FLIGHT COUNTDOWNS (NATIVE STREAMLIT TICKING LIVE)
# ---------------------------------------------------------
st.subheader("🛫 Flight Countdowns")

flights = [
    {
        "name": "1. Heathrow to Phuket",
        "flight": "Virgin Atlantic VS214",
        "ref": "D48RHT",
        "route": "LHR to HKT",
        "depart_local": "17 Mar 2027, 16:10 GMT",
        "depart_dt": datetime(2027, 3, 17, 16, 10, tzinfo=timezone.utc)
    },
    {
        "name": "2. Phuket to Singapore",
        "flight": "Singapore Airlines SQ739",
        "ref": "5OBEZB",
        "route": "HKT to Singapore",
        "depart_local": "25 Mar 2027, 20:25 ICT",
        "depart_dt": datetime(2027, 3, 25, 20, 25, tzinfo=timezone(timedelta(hours=7)))
    },
    {
        "name": "3. Singapore to Brisbane",
        "flight": "Singapore Airlines SQ255",
        "ref": "5OBEZB",
        "route": "Singapore to Brisbane",
        "depart_local": "26 Mar 2027, 00:55 SGT",
        "depart_dt": datetime(2027, 3, 26, 0, 55, tzinfo=timezone(timedelta(hours=8)))
    },
    {
        "name": "4. Brisbane to Heathrow (TBD)",
        "flight": "TBD",
        "ref": "TBD",
        "route": "BNE to LHR",
        "depart_local": "07 Apr 2027, 12:00 AEST (TBD)",
        "depart_dt": datetime(2027, 4, 7, 12, 0, tzinfo=timezone(timedelta(hours=10)))
    }
]

@st.fragment(run_every="1s")
def render_flight_cards():
    now_utc = datetime.now(timezone.utc)
    cols = st.columns(4)
    
    for idx, flight in enumerate(flights):
        with cols[idx]:
            diff = flight["depart_dt"] - now_utc
            total_seconds = int(diff.total_seconds())
            
            if total_seconds > 0:
                days = total_seconds // 86400
                hours = (total_seconds % 86400) // 3600
                mins = (total_seconds % 3600) // 60
                secs = total_seconds % 60
                countdown_str = f"{days}d {hours}h {mins}m {secs}s"
            else:
                countdown_str = "Departed"

            with st.container(border=True):
                st.metric(label=flight["name"], value=countdown_str)
                st.markdown(f"**Route:** {flight['route']}")
                st.markdown(f"**Flight:** {flight['flight']}")
                st.markdown(f"**Departure:** {flight['depart_local']}")
                st.caption(f"Ref: {flight['ref']}")

render_flight_cards()

st.divider()

# ---------------------------------------------------------
# TABS SECTION
# ---------------------------------------------------------
THB_TO_GBP = 0.022
AUD_TO_GBP = 0.52

tab_adventurers, tab_itinerary, tab_expenses, tab_stays, tab_activities, tab_vax = st.tabs([
    "🎭 Adventurers",
    "📅 Itinerary",
    "💰 Expenses",
    "📍 Stays & Travel",
    "🙋 Activities",
    "💉 Vaccinations"
])

# TAB 1: ADVENTURERS
with tab_adventurers:
    st.subheader("The Holiday Crew")
    st.caption("9 Travellers ready for Thailand & Australia")

    crew = [
        {"name": "Andy", "icon": "🤡", "role": "Trip Commissioner", "vibe": "Spreadsheets, transfers and morning coffee runs"},
        {"name": "Meg", "icon": "🌸", "role": "Chief Coordinator", "vibe": "Keeping the peace and spotting beach sunset spots"},
        {"name": "Hannah", "icon": "✨", "role": "Sunshine Seeker", "vibe": "First by the pool, last to leave the beach"},
        {"name": "Jo", "icon": "🌴", "role": "Relaxation Specialist", "vibe": "Chilled poolside drinks and finding great food"},
        {"name": "Laila", "icon": "🌊", "role": "Wave Watcher", "vibe": "Exploring the shorelines and coastal walks"},
        {"name": "Molly", "icon": "☀️", "role": "Holiday Adventurer", "vibe": "Up for boat trips, markets and day tours"},
        {"name": "Ethan", "icon": "🏄‍♂️", "role": "Coast Cruiser", "vibe": "Ready for theme park rides and ocean swims"},
        {"name": "Robyn", "icon": "🍧", "role": "Chief Fun Officer", "vibe": "Ice cream tracker and water slide explorer"},
        {"name": "Amber", "icon": "🐬", "role": "Wildlife Scout", "vibe": "Spotting dolphins, kangaroos and koalas"}
    ]

    cols_av = st.columns(3)
    for i, member in enumerate(crew):
        with cols_av[i % 3]:
            with st.container(border=True):
                st.markdown(f"## {member['icon']} {member['name']}")
                st.markdown(f"**Role:** {member['role']}")
                st.caption(member["vibe"])

# TAB 2: ITINERARY
with tab_itinerary:
    st.subheader("Trip Timeline")
    timeline_data = [
        {"Date": "17 Mar", "Stage": "VS214 departs London Heathrow 16:10"},
        {"Date": "18 Mar", "Stage": "Arrive Phuket 11:25, private van to The Sands Khao Lak"},
        {"Date": "19 - 24 Mar", "Stage": "Khao Lak beach, night markets and boat tours"},
        {"Date": "25 Mar", "Stage": "SQ739 departs Phuket 20:25, lands Singapore 23:35"},
        {"Date": "26 Mar", "Stage": "SQ255 departs Singapore 00:55, lands Brisbane 10:45, transfer to Surfers Paradise"},
        {"Date": "27 Mar - 6 Apr", "Stage": "Gold Coast stay, family visits and day trips"},
        {"Date": "07 Apr", "Stage": "Fly Brisbane back to London Heathrow (TBD ~12:00)"}
    ]
    st.dataframe(pd.DataFrame(timeline_data), use_container_width=True, hide_index=True)

# TAB 3: EXPENSES
with tab_expenses:
    st.subheader("Quick Expense Converter & Logger")
    with st.form("spend_form", clear_on_submit=True):
        col_a, col_b = st.columns(2)
        with col_a:
            payer = st.selectbox("Paid by", GROUP)
            item = st.text_input("Item", placeholder="e.g. Minibus transfer, dinner tab")
        with col_b:
            curr = st.selectbox("Currency", ["THB", "AUD", "GBP"])
            val = st.number_input("Amount", min_value=0.0, step=1.0)
        
        submit = st.form_submit_button("Record Cost")
        if submit and val > 0:
            conv = val * THB_TO_GBP if curr == "THB" else (val * AUD_TO_GBP if curr == "AUD" else val)
            st.success(f"Recorded {val:,.2f} {curr} (~£{conv:,.2f} GBP) paid by {payer} for {item}")

# TAB 4: STAYS & TRAVEL
with tab_stays:
    st.subheader("Addresses & Access Info")
    with st.expander("🏨 The Sands Khao Lak (18 - 25 March)", expanded=True):
        st.markdown("**English:** 10/185 Moo 7, Khuk Khak, Takuapa, Phang Nga 82220")
        st.markdown("**Thai Driver Card:** เดอะแซนด์ เขาหลัก บาย กะตะธานี 10/185 หมู่ 7 ต.คึกคัก อ.ตะกั่วป่า จ.พังงา")
        st.info("Airport transfer: 75 to 90 minutes north from Phuket Airport (HKT).")
    with st.expander("🏄 Surfers Paradise Base"):
        st.markdown("**Location:** Gold Coast, Queensland")
        st.markdown("**Transfer:** 85 km south from Brisbane Airport via M1 motorway.")

# TAB 5: ACTIVITIES
with tab_activities:
    st.subheader("Excursion Headcounts")
    outing = st.selectbox("Outing", ["Currumbin Sanctuary", "Theme Parks", "Burleigh Heads Lunch", "Broadwater Boat Hire"])
    people = st.multiselect("Who is going?", GROUP, default=["Andy"])
    st.metric(label=f"Total head count for {outing}", value=f"{len(people)} of 9")

# TAB 6: VACCINATIONS
with tab_vax:
    st.subheader("Travel Health & Vaccination Checklist")
    st.caption("UK NHS / Fitfortravel general advice. Check with your GP or travel clinic 6 to 8 weeks prior to departure.")

    col_thai, col_aus = st.columns(2)
    with col_thai:
        with st.container(border=True):
            st.markdown("### 🇹🇭 Thailand (Khao Lak)")
            st.markdown("**Standard recommended for most travellers:**")
            st.markdown("- **Hepatitis A** (food and water borne)")
            st.markdown("- **Tetanus** (check booster is up to date)")
            st.markdown("- **Typhoid** (usually recommended for rural dining or extended stays)")
            st.divider()
            st.markdown("**Consider for some travellers:**")
            st.markdown("- **Hepatitis B**")
            st.markdown("- **Rabies** (avoid feeding stray beach dogs or monkeys)")
            st.markdown("- **Dengue / Mosquito precautions:** Khao Lak has low malaria risk, but high strength DEET insect repellent is essential for dengue.")

    with col_aus:
        with st.container(border=True):
            st.markdown("### 🇦🇺 Australia (Queensland)")
            st.markdown("**Standard routine UK boosters:**")
            st.markdown("- **MMR** (Measles, Mumps, Rubella)")
            st.markdown("- **Tetanus, Diphtheria & Polio**")
            st.divider()
            st.markdown("**Health reminders:**")
            st.markdown("- **No specific exotic travel vaccines required.**")
            st.markdown("- **Sun Protection:** Queensland UV index is severe. Pack SPF 50+ broad spectrum sunscreen, hats and rash vests.")
            st.markdown("- **Reciprocal Healthcare:** UK citizens are eligible for essential treatment via Medicare under the reciprocal healthcare agreement, but comprehensive travel insurance remains essential.")