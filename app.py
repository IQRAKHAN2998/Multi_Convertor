import streamlit as st

# App Title
st.title("Multi-Converter (Unit + Currency)")

# Conversion Type Selection
conversion_type = st.radio("Select Conversion Type:", ["Length", "💰Currency"])

if conversion_type == "Length":
    # Length Conversion
    st.subheader("Length Converter")

    units = ["Centimeter", "Meter", "Kilometer", "Inch", "Foot"]
    
    amount = st.number_input("Enter the value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("Convert from:", units)
    to_unit = st.selectbox("Convert to:", units)

    conversion_factors = {
        "Centimeter": {"Meter": 0.01, "Kilometer": 0.00001, "Inch": 0.393701, "Foot": 0.0328084, "Centimeter": 1},
        "Meter": {"Centimeter": 100, "Kilometer": 0.001, "Inch": 39.3701, "Foot": 3.28084, "Meter": 1},
        "Kilometer": {"Centimeter": 100000, "Meter": 1000, "Inch": 39370.1, "Foot": 3280.84, "Kilometer": 1},
        "Inch": {"Centimeter": 2.54, "Meter": 0.0254, "Kilometer": 0.0000254, "Foot": 0.0833333, "Inch": 1},
        "Foot": {"Centimeter": 30.48, "Meter": 0.3048, "Kilometer": 0.0003048, "Inch": 12, "Foot": 1},
    }

    if st.button("Convert Length"):
        converted_value = amount * conversion_factors[from_unit][to_unit]
        st.success(f"{amount} {from_unit} = 📏{converted_value:.4f} {to_unit}")

elif conversion_type == "Currency":
    # Currency Conversion
    st.subheader("Currency Converter")

    currencies = ["USD", "PKR", "EUR", "GBP", "INR"]
    
    amount = st.number_input("Enter amount:", min_value=0.0, format="%.2f")
    from_currency = st.selectbox("Convert from:", currencies)
    to_currency = st.selectbox("Convert to:", currencies)

    # Dummy conversion rates (You can replace these with real-time API data)
    exchange_rates = {
        "USD": {"PKR": 278.50, "EUR": 0.92, "GBP": 0.79, "INR": 82.50, "USD": 1},
        "PKR": {"USD": 0.0036, "EUR": 0.0033, "GBP": 0.0028, "INR": 0.30, "PKR": 1},
        "EUR": {"USD": 1.09, "PKR": 301.00, "GBP": 0.86, "INR": 89.90, "EUR": 1},
        "GBP": {"USD": 1.27, "PKR": 349.00, "EUR": 1.16, "INR": 104.50, "GBP": 1},
        "INR": {"USD": 0.012, "PKR": 3.30, "EUR": 0.011, "GBP": 0.0096, "INR": 1},
    }

    if st.button("Convert Currency"):
        converted_value = amount * exchange_rates[from_currency][to_currency]
        st.success(f"{amount} {from_currency} =  💰{converted_value:.2f} {to_currency}")
