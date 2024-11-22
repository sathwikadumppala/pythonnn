import streamlit as st

# Function to calculate R1 and X1
def Tran_Eff(VSC, ISC, WSC):
    ZSC = VSC / ISC
    R1 = WSC / (ISC ** 2)  # WSC / ISC^2 gives the resistance in ohms
    X1 = (ZSC ** 2 - R1 ** 2) ** 0.5  # Reactance in ohms
    return R1 / 1000, X1 / 1000  # Convert both to kilo ohms

# Streamlit UI
st.title("Transformer Winding Resistance and Reactance Calculator")

# Input fields for VSC, ISC, WSC
VSC = st.number_input("Enter Short Circuit Voltage (VSC) in Volts:", min_value=0.0)
ISC = st.number_input("Enter Short Circuit Current (ISC) in Amperes:", min_value=0.0)
WSC = st.number_input("Enter Short Circuit Power (WSC) in Watts:", min_value=0.0)

# Calculate R1 and X1 when button is pressed
if st.button("Calculate R1 and X1"):
    if ISC == 0:
        st.error("ISC cannot be zero.")
    elif VSC <= 0 or WSC <= 0:
        st.error("VSC and WSC must be positive values.")
    else:
        R1, X1 = Tran_Eff(VSC, ISC, WSC)
        st.write(f"Calculated Winding Resistance (R1): {R1:.3f} kΩ")
        st.write(f"Calculated Reactance (X1): {X1:.3f} kΩ")
