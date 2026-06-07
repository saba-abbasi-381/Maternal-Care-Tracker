import streamlit as st
from maternal import SmartMaternalCareTracker

st.title("Smart Maternal Care Tracker🧑‍⚕️")
st.header("Smart care for every hearbeat of motherhood♥️!")

last_date = st.date_input("Enter your last menstural date: ")
current_date = st.date_input("Select current date: ")

p = SmartMaternalCareTracker(last_date, current_date)

user_choice = st.sidebar.selectbox("Services ", [
    "Complete Summary",
    "Gestational Age",
    "Trimester",
    "Scan Schadule",
    "Monitoring Alerts",
    "Edd(expected date of delivery)",
    
])

if st.button("View"):
    if not last_date or not current_date:
        st.warning("Please Enter dates.")
    
    else:    
        if p.lmp > p.today:
            st.error("Invalid dates!") 
        else:
            weeks, days = p.g_age_calc()
            
            if p.days == 0:
                st.info("Today is recorded as the first day of the last menstrual period (LMP).")
            
            elif p.weeks < 4:
                st.info("Pregnancy tests may not yet be reliable. Consider testing after a missed period.")    
            
            elif 4 <= p.weeks <= 6:
                st.info("You can take a pregnancy test now for more reliable results.")
            
            else:
                trimester = p.trimester()
                scan = p.scan_scheduler()
                risk = p.monitoring_alerts()
                edd = p.edd_detector()

                if user_choice == "Complete Summary":
                    st.write(f"""
                        G.age : {weeks}weeks+{days}days
                        \nTrimester : {trimester}
                        \nScan info : {scan}
                        \nMonitoring Alerts : {risk}
                        \nEDD : {edd}
                    """)
                
                elif user_choice == "Gestational Age":
                    st.write(
                        f"G.age : {weeks}weeks+{days}days"
                    )

                elif user_choice == "Trimester":
                    st.write(
                        f"Trimester : {trimester}"
                    )
                
                elif user_choice == "Scan Schadule":
                    st.write(
                        f"Scan info : {scan}"
                    )
                    
                elif user_choice == "Monitoring Alerts":    
                    st.write(
                        f"Monitoring Alerts : {risk}"
                    )
                
                elif user_choice == "Edd(expected date of delivery)":
                    st.write(
                        f"EDD : {edd}"
                    )

                    

