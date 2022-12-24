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
        fmt = st.radio("Output style", unit_format.keys())
        prec = st.radio("Output decimals", (2, 4, 6, 8), index=1, horizontal=True)

    st.markdown("""
    # Unit conversion

    Use the input field to convert units. The quantity on the left is converted
    to the units on the right separated by the word "to". See examples below
    for more information.
    """)

    st.subheader("Input")

    user_input = st.text_input("x", label_visibility="collapsed", value="2.54 cm to m")
    x, y = user_input.split(" to ")
    x1, x2 = x.split(" ")

    st.subheader("Output")

    ureg = pint.UnitRegistry()
    output = ureg.Quantity(float(x1), x2).to(y)
    st.markdown(f"{output:0.{prec}f{unit_format[fmt]}}")

    st.markdown("""
    ---

    Below are some examples for the input. Notice the quantity on the left is
    converted to the units on the right which are separated by the word "to".

    Convert from centimeters to meters:
    > 2.54 cm to m

    Convert from Fahrenheit to Celsius:
    > 45 degF to degC

    Convert from miles per hour to kilometers per hour:
    > 80 mph to kph

    Convert from square meters per second to square feet per hour:
    > 4 m^2/s to ft^2/hr \n
    > 4 meters^2/second to feet^2/hour

    Units can be spelled out or abbreviated. For example, meter can be input
    as meter, meters, or m which is demonstrated below.

    - centimeter = centimeters = cm
    - meter = meters = m
    - foot = feet = ft
    - yard = yards = yd
    """)

    st.markdown("This unit converter is built with [Pint](https://pint.readthedocs.io/en/stable/).")


if __name__ == "__main__":
    main()
