import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

st.title("📊 Data Processing & Visualization App")

st.write("Developed By Junaid Ul Haque Sheikh")

# File Upload
file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])
if file:
    file_ext = file.name.split(".")[-1]
    if file_ext == "csv":
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)
    
    st.write("### Data Preview", df.head())
    
    # Fill missing values
    numeric_cols = df.select_dtypes(include=["number"]).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    st.write("Missing values filled!")
    
    # Column selection
    st.subheader("Select Columns to Keep")
    columns = st.multiselect(f"Choose Columns for {file.name}", df.columns, default=df.columns)
    df = df[columns]
    
    # Visualization
    st.subheader("📈 Data Visualization")
    if st.checkbox(f"Show Visualization for {file.name}"):
        chart_type = st.selectbox("Select Chart Type", ["Line", "Bar", "Histogram"])
        x_axis = st.selectbox("Select X-axis", df.columns)
        y_axis = st.selectbox("Select Y-axis", df.columns)
        
        fig, ax = plt.subplots()
        if chart_type == "Line":
            df.plot(x=x_axis, y=y_axis, kind="line", ax=ax)
        elif chart_type == "Bar":
            df.plot(x=x_axis, y=y_axis, kind="bar", ax=ax)
        else:
            df[y_axis].plot(kind="hist", ax=ax, bins=20)
        
        st.pyplot(fig)
    
    # File Download
    st.subheader("📥 Download Processed File")
    buffer = io.BytesIO()
    conversion_type = st.selectbox("Convert File To", ["CSV", "Excel"])
    
    if conversion_type == "CSV":
        df.to_csv(buffer, index=False)
        file_name = file.name.replace(file_ext, "csv")
        mime_type = "text/csv"
    else:
        df.to_excel(buffer, index=False)
        file_name = file.name.replace(file_ext, "xlsx")
        mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    
    buffer.seek(0)
    st.download_button(
        label=f"📥 Download {file.name} as {conversion_type}",
        data=buffer,
        file_name=file_name,
        mime=mime_type
    )
    
    st.success("🎉 All files processed!")
