import streamlit as st

st.set_page_config(page_title="Unit Converter", layout="centered")

st.title("🔄 Unit Converter")

# Main categories
conversion_type = st.selectbox("Select Conversion Type", [
    "Length", "Weight", "Temperature"
])

def length_converter(value, from_unit, to_unit):
    length_units = {
        "Meters": 1,
        "Kilometers": 1000,
        "Centimeters": 0.01,
        "Miles": 1609.34,
        "Feet": 0.3048,
        "Inches": 0.0254
    }
    value_in_meters = value * length_units[from_unit]
    return value_in_meters / length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495
    }
    value_in_kg = value * weight_units[from_unit]
    return value_in_kg / weight_units[to_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else value + 273.15
    if from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    if from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32

value = st.number_input("Enter Value", format="%.4f")

if conversion_type == "Length":
    units = ["Meters", "Kilometers", "Centimeters", "Miles", "Feet", "Inches"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    result = length_converter(value, from_unit, to_unit)

elif conversion_type == "Weight":
    units = ["Kilograms", "Grams", "Pounds", "Ounces"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    result = weight_converter(value, from_unit, to_unit)

elif conversion_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    result = temperature_converter(value, from_unit, to_unit)

if value:
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
