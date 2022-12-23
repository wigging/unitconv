import streamlit as st
import pint


def main():

    unit_format = {
        "Default": "D",
        "Short default": "~D",
        "Pretty": "P",
        "Short pretty": "~P",
        "Compact": "C",
        "Short compact": "~C"
    }

    with st.sidebar:
        st.header("Settings")
        fmt = st.radio("Format", unit_format.keys())
        prec = st.radio("Float digits", (2, 4, 6, 8), index=1, horizontal=True)

    st.subheader("Unit conversion")

    user_input = st.text_input("x", label_visibility="collapsed", value="2.54 cm to m")
    x, y = user_input.split(" to ")
    x1, x2 = x.split(" ")

    ureg = pint.UnitRegistry()
    output = ureg.Quantity(float(x1), x2).to(y)
    st.markdown(f"{output:0.{prec}f{unit_format[fmt]}}")

    st.markdown("---")
    st.markdown("")

    st.markdown("""
    Input the following to convert from centimeters to meters:
    > 2.54 cm to m

    Input the following to convert from Fahrenheit to Celsius:
    > 45 degF to degC
    """)

    st.write("""
    Units can be expressed as shown below.

    - centimeter = centimeters = cm</li>
    - meter = meters = m
    - foot = feet = ft
    - yard = yards = yd
    """, unsafe_allow_html=True)

    st.markdown("This unit converter is built with [Pint](https://pint.readthedocs.io/en/stable/).")


if __name__ == "__main__":
    main()
