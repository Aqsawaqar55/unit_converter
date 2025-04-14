import streamlit as st

st.set_page_config(page_title="Unit Converter", layout="centered")

st.title("🔄 Unit Converter")

# Conversion categories and units
conversion_categories = {
    "Length": {
        "units": ["Meter", "Kilometer", "Mile", "Foot"],
        "conversion": {
            ("Meter", "Kilometer"): lambda x: x / 1000,
            ("Meter", "Mile"): lambda x: x / 1609.34,
            ("Meter", "Foot"): lambda x: x * 3.28084,
            ("Kilometer", "Meter"): lambda x: x * 1000,
            ("Kilometer", "Mile"): lambda x: x / 1.60934,
            ("Kilometer", "Foot"): lambda x: x * 3280.84,
            ("Mile", "Meter"): lambda x: x * 1609.34,
            ("Mile", "Kilometer"): lambda x: x * 1.60934,
            ("Mile", "Foot"): lambda x: x * 5280,
            ("Foot", "Meter"): lambda x: x / 3.28084,
            ("Foot", "Kilometer"): lambda x: x / 3280.84,
            ("Foot", "Mile"): lambda x: x / 5280,
        }
    },
    "Weight": {
        "units": ["Kilogram", "Gram", "Pound", "Ounce"],
        "conversion": {
            ("Kilogram", "Gram"): lambda x: x * 1000,
            ("Kilogram", "Pound"): lambda x: x * 2.20462,
            ("Kilogram", "Ounce"): lambda x: x * 35.274,
            ("Gram", "Kilogram"): lambda x: x / 1000,
            ("Gram", "Pound"): lambda x: x / 453.592,
            ("Gram", "Ounce"): lambda x: x / 28.3495,
            ("Pound", "Kilogram"): lambda x: x / 2.20462,
            ("Pound", "Gram"): lambda x: x * 453.592,
            ("Pound", "Ounce"): lambda x: x * 16,
            ("Ounce", "Kilogram"): lambda x: x / 35.274,
            ("Ounce", "Gram"): lambda x: x * 28.3495,
            ("Ounce", "Pound"): lambda x: x / 16,
        }
    },
    "Temperature": {
        "units": ["Celsius", "Fahrenheit", "Kelvin"],
        "conversion": {
            ("Celsius", "Fahrenheit"): lambda x: (x * 9/5) + 32,
            ("Celsius", "Kelvin"): lambda x: x + 273.15,
            ("Fahrenheit", "Celsius"): lambda x: (x - 32) * 5/9,
            ("Fahrenheit", "Kelvin"): lambda x: (x - 32) * 5/9 + 273.15,
            ("Kelvin", "Celsius"): lambda x: x - 273.15,
            ("Kelvin", "Fahrenheit"): lambda x: (x - 273.15) * 9/5 + 32,
        }
    }
}

# Select category
category = st.selectbox("Select a category", list(conversion_categories.keys()))
units = conversion_categories[category]["units"]

# Select units
from_unit = st.selectbox("From", units)
to_unit = st.selectbox("To", units)

# Input value
value = st.number_input(f"Enter value in {from_unit}", step=0.01)

# Convert
if from_unit == to_unit:
    result = value
else:
    conversion_func = conversion_categories[category]["conversion"].get((from_unit, to_unit))
    if conversion_func:
        result = conversion_func(value)
    else:
        result = "Conversion not defined"

# Output
st.markdown(f"### Result: `{result} {to_unit}`")
