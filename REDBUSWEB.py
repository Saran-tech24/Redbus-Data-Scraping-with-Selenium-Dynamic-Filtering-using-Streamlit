import streamlit as st
import pandas as pd
import mysql.connector
from datetime import time


kerala_list =[]
KERALA_DATA_1=pd.read_csv("C:/Users/Admin/Desktop/REDBUS/ALLROUTELINKS/ALL_K_L.CSV")
for i,r in KERALA_DATA_1.iterrows():
     kerala_list.append(r["routename"])  

AP_list =[]
AP_DATA_1=pd.read_csv("C:/Users/Admin/Desktop/REDBUS/ALLROUTELINKS/ALL_AP_L.CSV")
for i,r in AP_DATA_1.iterrows():
    AP_list.append(r["routename"])

TS_list =[]
TS_DATA_1=pd.read_csv("C:/Users/Admin/Desktop/REDBUS/ALLROUTELINKS/ALL_TS_L.CSV")
for i,r in TS_DATA_1.iterrows():
    TS_list.append(r["routename"])

RS_list=[]
RS_DATA_1=pd.read_csv("C:/Users/Admin/Desktop/REDBUS/ALLROUTELINKS/ALL_RS_L.CSV")
for i,r in RS_DATA_1.iterrows():
    RS_list.append(r["routename"])


SB_list = []
SB_DATA_1=pd.read_csv("C:/Users/Admin/Desktop/REDBUS/ALLROUTELINKS/ALL_SB_L.CSV")
for i,r in SB_DATA_1.iterrows():
    SB_list.append(r["routename"])

AS_list=[]
AS_DATA_1=pd.read_csv("C:/Users/Admin/Desktop/REDBUS/ALLROUTELINKS/ALL_AS_L.CSV")
for i,r in AS_DATA_1.iterrows():
    AS_list.append(r["routename"])


UP_list = []
UP_DATA_1=pd.read_csv("C:/Users/Admin/Desktop/REDBUS/ALLROUTELINKS/ALL_UP_L.CSV")
for i,r in UP_DATA_1.iterrows():
    UP_list.append(r["routename"])



CD_list = []
CD_DATA_1=pd.read_csv("C:/Users/Admin/Desktop/REDBUS/ALLROUTELINKS/ALL_NB_L.CSV")
for i,r in CD_DATA_1.iterrows():
    CD_list.append(r["routename"])


NB_list = []
NB_DATA_1=pd.read_csv("C:/Users/Admin/Desktop/REDBUS/ALLROUTELINKS/ALL_NB_L.CSV")
for i,r in NB_DATA_1.iterrows():
    NB_list.append(r["routename"])

PJ_list = []
PUNJAB_DATA_1=pd.read_csv("C:/Users/Admin/Desktop/REDBUS/ALLROUTELINKS/ALL_PJ_L.CSV")
for i,r in PUNJAB_DATA_1.iterrows():
    PJ_list.append(r["routename"])



st.sidebar.title("welcome to redbus")
menu_option = st.sidebar.selectbox("choose a option:",["Home","BusDetails"])
if menu_option == "Home":
    st.image('C:/Users/Admin/Desktop/redbus.png',use_column_width=True)
    st.markdown("**BOOK BUS TICKETS ONLINE**")
    st.markdown('RedBus is an online platform for booking bus tickets across India and other countries.It offers a convenient way to search, compare, and book bus tickets from various operators. Users can select their preferred routes, choose seats, and pay securely through the website or mobile app. RedBus also provides features like live bus tracking, ratings, and reviews to enhance the travel experience.')
if menu_option == "BusDetails":
    st.image('C:/Users/Admin/Desktop/redbus.png',use_column_width=True)
    states = st.sidebar.selectbox("list of the state",["None","Kerala", "Adhra Pradesh", "Telugana","Rajastan", 
                                "South Bengal", "Assam", "Uttar Pradesh","chandigarh","North Bengal","Punjab"])
    


    if states == "Kerala":
            K = st.sidebar.selectbox("chose the Bus Route" , kerala_list)
            select_type = st.sidebar.selectbox("choose the Bus Type",["None","sleeper","semi-sleepar","oters"])
            select_fare = st.sidebar.selectbox("choose the fare range",["None","500-1000", "1000-2000", "2000 & above"])
            Ratings = st.sidebar.selectbox("chosee the rating",["1-2","3-5"])
            Times = st.sidebar.time_input("select the time") 


            def type_and_fare(bus_type, fare_range,Rating_range):
                mydb = mysql.connector.connect(host="localhost",user="root",password="",database="redbus")
                mycursor = mydb.cursor(buffered=True)

                # Define bus type condition
                if bus_type == "sleeper":
                    bus_type_condition = "Bus_type LIKE '%Sleeper%'"
                elif bus_type == "semi-sleeper":
                    bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
                else:
                    bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"


                # Define fare range based on selection
                if fare_range == "500-1000":
                    fare_min, fare_max = 500, 1000
                elif fare_range == "1000-2000":
                    fare_min, fare_max = 1000, 2000
                else:
                    fare_min, fare_max = 2000, 10000  # assuming a high max value for "2000 and above"  

                # Define rating range
                if Rating_range == "1-2":
                    Rating_min, Rating_max = 1,2
                else:
                    Rating_min, Rating_max = 3,5

                mycursor.execute(f'''
                    SELECT * FROM bus_details 
                    WHERE Price BETWEEN {fare_min} AND {fare_max} AND Ratings BETWEEN {Rating_min} and {Rating_max}
                    AND Route_name = "{K}"
                    AND {bus_type_condition} AND Start_time>='{Times}'
                    ORDER BY Start_time  ASC
                ''')
                out = mycursor.fetchall()
                mydb.close()

                df = pd.DataFrame(out, columns=[
                    "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                    "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
                ])
                return df

            df_result = type_and_fare(select_type, select_fare,Ratings)
            st.dataframe(df_result)
        

    if states == "Adhra Pradesh":
            A = st.sidebar.selectbox("chose the Bus Route" , AP_list)
            select_type = st.sidebar.selectbox("choose the Bus Type",["None","sleeper","semi-sleepar","oters"])
            select_fare = st.sidebar.selectbox("choose the fare range",["None","500-1000", "1000-2000", "2000 & above"])
            Ratings = st.sidebar.selectbox("chosee the rating",["1-2","3-5"])
            Times = st.sidebar.time_input("select the time") 


            def type_and_fare(bus_type, fare_range,Rating_range):
                mydb = mysql.connector.connect(host="localhost",user="root",password="",database="redbus")
                mycursor = mydb.cursor(buffered=True)

                # Define bus type condition
                if bus_type == "sleeper":
                    bus_type_condition = "Bus_type LIKE '%Sleeper%'"
                elif bus_type == "semi-sleeper":
                    bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
                else:
                    bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"


                # Define fare range based on selection
                if fare_range == "500-1000":
                    fare_min, fare_max = 500, 1000
                elif fare_range == "1000-2000":
                    fare_min, fare_max = 1000, 2000
                else:
                    fare_min, fare_max = 2000, 10000  # assuming a high max value for "2000 and above"  


                if Rating_range == "1-2":
                    Rating_min, Rating_max = 1,2
                else:
                    Rating_min, Rating_max = 3,5

                mycursor.execute(f'''
                    SELECT * FROM bus_details 
                    WHERE Price BETWEEN {fare_min} AND {fare_max} AND Ratings BETWEEN {Rating_min} and {Rating_max}
                    AND Route_name = "{A}"
                    AND {bus_type_condition} AND Start_time>='{Times}'
                    ORDER BY Start_time  ASC
                ''')
                out = mycursor.fetchall()
                mydb.close()

                df = pd.DataFrame(out, columns=[
                    "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                    "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
                ])
                return df

            df_result = type_and_fare(select_type, select_fare,Ratings)
            st.dataframe(df_result)


    if states == "Telugana":
        T = st.sidebar.selectbox("chose the Bus Route" ,TS_list)
        select_type = st.sidebar.selectbox("choose the Bus Type",["None","sleeper","semi-sleepar","oters"])
        select_fare = st.sidebar.selectbox("choose the fare range",["None","500-1000", "1000-2000", "2000 & above"])
        Ratings = st.sidebar.selectbox("chosee the rating",["1-2","3-5"])  
        Times = st.sidebar.time_input("select the time") 


        def type_and_fare(bus_type, fare_range,Rating_range):
            mydb = mysql.connector.connect(host="localhost",user="root",password="",database="redbus")
            mycursor = mydb.cursor(buffered=True)

            # Define fare range based on selection
            if fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 10000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"


                if Rating_range == "1-2":
                    Rating_min, Rating_max = 1,2
                else:
                    Rating_min, Rating_max = 3,5

                mycursor.execute(f'''
                    SELECT * FROM bus_details 
                    WHERE Price BETWEEN {fare_min} AND {fare_max} AND Ratings BETWEEN {Rating_min} and {Rating_max}
                    AND Route_name = "{A}"
                    AND {bus_type_condition} AND Start_time>='{Times}'
                    ORDER BY Start_time  ASC
                ''')
                out = mycursor.fetchall()
                mydb.close()

                df = pd.DataFrame(out, columns=[
                    "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                    "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
                ])
                return df

            df_result = type_and_fare(select_type, select_fare,Ratings)
            st.dataframe(df_result)


    if states == "Rajastan":
        R = st.sidebar.selectbox("chose the Bus Route" , RS_list)
        select_type = st.sidebar.selectbox("choose the Bus Type",["None","sleeper","semi-sleepar","oters"])
        select_fare = st.sidebar.selectbox("choose the fare range",["None","500-1000", "1000-2000", "2000 & above"])
        Ratings = st.sidebar.selectbox("chosee the rating",["1-2","3-5"])  
        Times = st.sidebar.time_input("select the time") 


        def type_and_fare(bus_type, fare_range,Rating_range):
            mydb = mysql.connector.connect(host="localhost",user="root",password="",database="redbus")
            mycursor = mydb.cursor(buffered=True)

            # Define fare range based on selection
            if fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"


                if Rating_range == "1-2":
                    Rating_min, Rating_max = 1,2
                else:
                    Rating_min, Rating_max = 3,5

                mycursor.execute(f'''
                    SELECT * FROM bus_details 
                    WHERE Price BETWEEN {fare_min} AND {fare_max} AND Ratings BETWEEN {Rating_min} and {Rating_max}
                    AND Route_name = "{A}"
                    AND {bus_type_condition} AND Start_time>='{Times}'
                    ORDER BY Start_time  ASC
                ''')
                out = mycursor.fetchall()
                mydb.close()

                df = pd.DataFrame(out, columns=[
                    "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                    "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
                ])
                return df

            df_result = type_and_fare(select_type, select_fare,Ratings)
            st.dataframe(df_result)



    if states == "South Bengal":
        S = st.sidebar.selectbox("chose the Bus Route" , SB_list)
        select_type = st.sidebar.selectbox("choose the Bus Type",["None","sleeper","semi-sleepar","oters"])
        select_fare = st.sidebar.selectbox("choose the fare range",["None","500-1000", "1000-2000", "2000 & above"])
        Ratings = st.sidebar.selectbox("chosee the rating",["1-2","3-5"])  
        Times = st.sidebar.time_input("select the time") 


        def type_and_fare(bus_type, fare_range,Rating_range):
            mydb = mysql.connector.connect(host="localhost",user="root",password="",database="redbus")
            mycursor = mydb.cursor(buffered=True)

            # Define fare range based on selection
            if fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 10000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"


                if Rating_range == "1-2":
                    Rating_min, Rating_max = 1,2
                else:
                    Rating_min, Rating_max = 3,5

                mycursor.execute(f'''
                    SELECT * FROM bus_details 
                    WHERE Price BETWEEN {fare_min} AND {fare_max} AND Ratings BETWEEN {Rating_min} and {Rating_max}
                    AND Route_name = "{A}"
                    AND {bus_type_condition} AND Start_time>='{Times}'
                    ORDER BY Start_time  ASC
                ''')
                out = mycursor.fetchall()
                mydb.close()

                df = pd.DataFrame(out, columns=[
                    "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                    "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
                ])
                return df

            df_result = type_and_fare(select_type, select_fare,Ratings)
            st.dataframe(df_result)


    if states == "Assam":
        AS = st.sidebar.selectbox("chose the Bus Route" , AS_list)
        select_type = st.sidebar.selectbox("choose the Bus Type",["None","sleeper","semi-sleepar","oters"])
        select_fare = st.sidebar.selectbox("choose the fare range",["None","500-1000", "1000-2000", "2000 & above"])
        Ratings = st.sidebar.selectbox("chosee the rating",["1-2","3-5"])  
        Times = st.sidebar.time_input("select the time") 


        def type_and_fare(bus_type, fare_range,Rating_range):
            mydb = mysql.connector.connect(host="localhost",user="root",password="",database="redbus")
            mycursor = mydb.cursor(buffered=True)

            # Define fare range based on selection
            if fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 10000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"


                if Rating_range == "1-2":
                    Rating_min, Rating_max = 1,2
                else:
                    Rating_min, Rating_max = 3,5

                mycursor.execute(f'''
                    SELECT * FROM bus_details 
                    WHERE Price BETWEEN {fare_min} AND {fare_max} AND Ratings BETWEEN {Rating_min} and {Rating_max}
                    AND Route_name = "{A}"
                    AND {bus_type_condition} AND Start_time>='{Times}'
                    ORDER BY Start_time  ASC
                ''')
                out = mycursor.fetchall()
                mydb.close()

                df = pd.DataFrame(out, columns=[
                    "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                    "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
                ])
                return df

            df_result = type_and_fare(select_type, select_fare,Ratings)
            st.dataframe(df_result)  


    if states == "Uttar Pradesh":
        UP = st.sidebar.selectbox("chose the Bus Route" , UP_list)
        select_type = st.sidebar.selectbox("choose the Bus Type",["None","sleeper","semi-sleepar","oters"])
        select_fare = st.sidebar.selectbox("choose the fare range",["None","500-1000", "1000-2000", "2000 & above"])
        Ratings = st.sidebar.selectbox("chosee the rating",["1-2","3-5"])  
        Times = st.sidebar.time_input("select the time") 


        def type_and_fare(bus_type, fare_range,Rating_range):
            mydb = mysql.connector.connect(host="localhost",user="root",password="",database="redbus")
            mycursor = mydb.cursor(buffered=True)

            # Define fare range based on selection
            if fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 10000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"


                if Rating_range == "1-2":
                    Rating_min, Rating_max = 1,2
                else:
                    Rating_min, Rating_max = 3,5

                mycursor.execute(f'''
                    SELECT * FROM bus_details 
                    WHERE Price BETWEEN {fare_min} AND {fare_max} AND Ratings BETWEEN {Rating_min} and {Rating_max}
                    AND Route_name = "{A}"
                    AND {bus_type_condition} AND Start_time>='{Times}'
                    ORDER BY Start_time  ASC
                ''')
                out = mycursor.fetchall()
                mydb.close()

                df = pd.DataFrame(out, columns=[
                    "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                    "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
                ])
                return df

            df_result = type_and_fare(select_type, select_fare,Ratings)
            st.dataframe(df_result)


    if states == "chandigarh":
        CD = st.sidebar.selectbox("chose the Bus Route" , CD_list)
        select_type = st.sidebar.selectbox("choose the Bus Type",["None","sleeper","semi-sleepar","oters"])
        select_fare = st.sidebar.selectbox("choose the fare range",["None","500-1000", "1000-2000", "2000 & above"])
        Ratings = st.sidebar.selectbox("chosee the rating",["1-2","3-5"])  
        Times = st.sidebar.time_input("select the time") 


        def type_and_fare(bus_type, fare_range,Rating_range):
            mydb = mysql.connector.connect(host="localhost",user="root",password="",database="redbus")
            mycursor = mydb.cursor(buffered=True)

            # Define fare range based on selection
            if fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 10000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"


                if Rating_range == "1-2":
                    Rating_min, Rating_max = 1,2
                else:
                    Rating_min, Rating_max = 3,5

                mycursor.execute(f'''
                    SELECT * FROM bus_details 
                    WHERE Price BETWEEN {fare_min} AND {fare_max} AND Ratings BETWEEN {Rating_min} and {Rating_max}
                    AND Route_name = "{A}"
                    AND {bus_type_condition} AND Start_time>='{Times}'
                    ORDER BY Start_time  ASC
                ''')
                out = mycursor.fetchall()
                mydb.close()

                df = pd.DataFrame(out, columns=[
                    "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                    "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
                ])
                return df

            df_result = type_and_fare(select_type, select_fare,Ratings)
            st.dataframe(df_result)


    if states == "North Bengal":
        NB = st.sidebar.selectbox("chose the Bus Route" , NB_list)
        select_type = st.sidebar.selectbox("choose the Bus Type",["None","sleeper","semi-sleepar","oters"])
        select_fare = st.sidebar.selectbox("choose the fare range",["None","500-1000", "1000-2000", "2000 & above"])
        Ratings = st.sidebar.selectbox("chosee the rating",["1-2","3-5"]) 
        Times = st.sidebar.time_input("select the time") 


        def type_and_fare(bus_type, fare_range,Rating_range):
            mydb = mysql.connector.connect(host="localhost",user="root",password="",database="redbus")
            mycursor = mydb.cursor(buffered=True)

            # Define fare range based on selection
            if fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 10000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"


                if Rating_range == "1-2":
                    Rating_min, Rating_max = 1,2
                else:
                    Rating_min, Rating_max = 3,5

                mycursor.execute(f'''
                    SELECT * FROM bus_details 
                    WHERE Price BETWEEN {fare_min} AND {fare_max} AND Ratings BETWEEN {Rating_min} and {Rating_max}
                    AND Route_name = "{A}"
                    AND {bus_type_condition} AND Start_time>='{Times}'
                    ORDER BY Start_time  ASC
                ''')
                out = mycursor.fetchall()
                mydb.close()

                df = pd.DataFrame(out, columns=[
                    "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                    "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
                ])
                return df

            df_result = type_and_fare(select_type, select_fare,Ratings)
            st.dataframe(df_result)
        
    if states == "Punjab":
        PJ = st.sidebar.selectbox("chose the Bus Route" , PJ_list)
        select_type = st.sidebar.selectbox("choose the Bus Type",["None","sleeper","semi-sleepar","oters"])
        select_fare = st.sidebar.selectbox("choose the fare range",["None","500-1000", "1000-2000", "2000 & above"])
        Ratings = st.sidebar.selectbox("chosee the rating",["1-2","3-5"])  
        Times = st.sidebar.time_input("select the time") 


        def type_and_fare(bus_type, fare_range,Rating_range):
            mydb = mysql.connector.connect(host="localhost",user="root",password="",database="redbus")
            mycursor = mydb.cursor(buffered=True)

            # Define fare range based on selection
            if fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 10000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"


                if Rating_range == "1-2":
                    Rating_min, Rating_max = 1,2
                else:
                    Rating_min, Rating_max = 3,5

                mycursor.execute(f'''
                    SELECT * FROM bus_details 
                    WHERE Price BETWEEN {fare_min} AND {fare_max} AND Ratings BETWEEN {Rating_min} and {Rating_max}
                    AND Route_name = "{A}"
                    AND {bus_type_condition} AND Start_time>='{Times}'
                    ORDER BY Start_time  ASC
                ''')
                out = mycursor.fetchall()
                mydb.close()

                df = pd.DataFrame(out, columns=[
                    "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                    "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
                ])
                return df

            df_result = type_and_fare(select_type, select_fare,Ratings)
            st.dataframe(df_result)