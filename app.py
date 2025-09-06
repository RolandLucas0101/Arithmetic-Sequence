import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def generate_arithmetic_sequence(a1: float, d: float, n: int):
    """Generate an arithmetic sequence."""
    return [a1 + (i * d) for i in range(n)]

def sum_arithmetic_sequence(a1: float, d: float, n: int):
    """Calculate the sum of the first n terms of an arithmetic sequence."""
    return (n / 2) * (2 * a1 + (n - 1) * d)

# Streamlit app layout
st.set_page_config(page_title="Arithmetic Sequence Generator", page_icon="➗")

st.title("📐 Arithmetic Sequence Generator")

st.markdown(
    """
    Enter the first term, the common difference, and the number of terms.  
    This app will generate the arithmetic sequence, display the formula, 
    show the sum of terms, plot the sequence, and let you download it as CSV.
    """
)

# Inputs
a1 = st.number_input("First term (a₁):", value=1.0, step=1.0)
d = st.number_input("Common difference (d):", value=1.0, step=1.0)
n = st.number_input("Number of terms (n):", value=10, min_value=1, step=1)

if st.button("Generate Sequence"):
    sequence = generate_arithmetic_sequence(a1, d, n)
    st.success(f"Here are the {n} terms of your sequence:")
    st.write(sequence)

    # Formula display
    st.subheader("📖 General Term Formula")
    st.latex(r"a_n = a_1 + (n-1)d")
    st.write(f"In your case:  aₙ = {a1} + (n-1)({d})")

    # Show in table form
    st.subheader("📊 Sequence Table")
    df = pd.DataFrame({
        "n": range(1, n+1),
        "aₙ": sequence
    })
    st.dataframe(df, use_container_width=True)

    # Plot the sequence
    st.subheader("📈 Sequence Chart")
    fig, ax = plt.subplots()
    ax.plot(df["n"], df["aₙ"], marker="o", linestyle="-", color="b")
    ax.set_xlabel("Term number (n)")
    ax.set_ylabel("Value (aₙ)")
    ax.set_title("Arithmetic Sequence")
    st.pyplot(fig)

    # Sum of sequence
    st.subheader("➕ Sum of First n Terms")
    st.latex(r"S_n = \\frac{n}{2}\\big(2a_1 + (n-1)d\\big)")
    Sn = sum_arithmetic_sequence(a1, d, n)
    st.write(f"For your inputs: Sₙ = {Sn}")

    # Download button for CSV
    st.subheader("💾 Download Sequence Data")
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download sequence as CSV",
        data=csv,
        file_name="arithmetic_sequence.csv",
        mime="text/csv"
    )
