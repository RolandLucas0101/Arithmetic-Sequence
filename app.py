import streamlit as st

def generate_arithmetic_sequence(first_term, common_difference, num_terms):
    """
    Generate an arithmetic sequence given the first term, common difference, and number of terms.
    
    Args:
        first_term (float): The first term of the sequence
        common_difference (float): The common difference between consecutive terms
        num_terms (int): The number of terms to generate
    
    Returns:
        list: The arithmetic sequence as a list of numbers
    """
    sequence = []
    for i in range(num_terms):
        term = first_term + (i * common_difference)
        sequence.append(term)
    return sequence

def generate_geometric_sequence(first_term, common_ratio, num_terms):
    """
    Generate a geometric sequence given the first term, common ratio, and number of terms.
    
    Args:
        first_term (float): The first term of the sequence
        common_ratio (float): The common ratio between consecutive terms
        num_terms (int): The number of terms to generate
    
    Returns:
        list: The geometric sequence as a list of numbers
    """
    sequence = []
    for i in range(num_terms):
        term = first_term * (common_ratio ** i)
        sequence.append(term)
    return sequence

def calculate_geometric_series_sum(first_term, common_ratio, num_terms):
    """
    Calculate the sum of a finite geometric series.
    
    Args:
        first_term (float): The first term of the series
        common_ratio (float): The common ratio between consecutive terms
        num_terms (int): The number of terms in the series
    
    Returns:
        float: The sum of the geometric series
    """
    if common_ratio == 1:
        return first_term * num_terms
    else:
        return first_term * (1 - common_ratio ** num_terms) / (1 - common_ratio)

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Sequence Generator",
        page_icon="🔢",
        layout="centered"
    )
    
    # Main title and description
    st.title("🔢 Sequence Generator")
    st.markdown("Generate arithmetic or geometric sequences with their properties and calculations.")
    
    # Sequence type selection
    sequence_type = st.selectbox(
        "Choose Sequence Type",
        ["Arithmetic", "Geometric"],
        help="Select the type of sequence you want to generate"
    )
    
    # Create input section
    st.header("Input Parameters")
    
    # Create three columns for better layout
    col1, col2, col3 = st.columns(3)
    
    with col1:
        first_term = st.number_input(
            "First Term",
            value=1.0,
            step=1.0,
            help="The first number in the sequence"
        )
    
    with col2:
        if sequence_type == "Arithmetic":
            common_difference = st.number_input(
                "Common Difference",
                value=1.0,
                step=1.0,
                help="The constant difference between consecutive terms"
            )
            common_ratio = None
        else:  # Geometric
            common_ratio = st.number_input(
                "Common Ratio",
                value=2.0,
                step=0.1,
                help="The constant ratio between consecutive terms"
            )
            common_difference = None
    
    with col3:
        num_terms = st.number_input(
            "Number of Terms",
            min_value=1,
            max_value=1000,
            value=10,
            step=1,
            help="How many terms to generate (1-1000)"
        )
    
    # Add some spacing
    st.markdown("---")
    
    # Validate inputs and generate sequence
    if st.button("Generate Sequence", type="primary"):
        try:
            # Input validation
            if num_terms <= 0:
                st.error("Number of terms must be a positive integer.")
                return
            
            if num_terms > 1000:
                st.error("Number of terms cannot exceed 1000 for performance reasons.")
                return
            
            # Generate the sequence based on type
            if sequence_type == "Arithmetic":
                sequence = generate_arithmetic_sequence(first_term, common_difference, int(num_terms))
                formula = f"a_n = {first_term} + (n-1) × {common_difference}"
                sequence_sum = sum(sequence)
            else:  # Geometric
                sequence = generate_geometric_sequence(first_term, common_ratio, int(num_terms))
                formula = f"a_n = {first_term} × {common_ratio}^(n-1)"
                sequence_sum = calculate_geometric_series_sum(first_term, common_ratio, int(num_terms))
            
            # Display results
            st.header(f"Generated {sequence_type} Sequence")
            
            # Show sequence information
            st.info(f"**Sequence Formula:** {formula}")
            
            # Display the sequence in a nice format
            if len(sequence) <= 50:
                # For shorter sequences, display in a more readable format
                sequence_str = ", ".join([str(term) for term in sequence])
                st.success(f"**Sequence:** {sequence_str}")
            else:
                # For longer sequences, display in columns
                st.success(f"**First 10 terms:** {', '.join([str(term) for term in sequence[:10]])}")
                st.success(f"**Last 10 terms:** {', '.join([str(term) for term in sequence[-10:]])}")
            
            # Show additional information
            st.markdown("### Sequence Details")
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("First Term", sequence[0])
            
            with col2:
                st.metric("Last Term", sequence[-1])
            
            with col3:
                if sequence_type == "Geometric":
                    st.metric("Series Sum", f"{sequence_sum:.6f}")
                else:
                    st.metric("Sum of Terms", sum(sequence))
            
            with col4:
                st.metric("Total Terms", len(sequence))
            
            # Display full sequence in expandable section
            with st.expander("View Full Sequence"):
                # Display sequence in a table format for better readability
                sequence_data = []
                for i, term in enumerate(sequence, 1):
                    sequence_data.append({
                        "Term Position (n)": i,
                        "Term Value": term
                    })
                
                st.dataframe(sequence_data, use_container_width=True)
                
                # Option to download as CSV
                import io
                import csv
                
                output = io.StringIO()
                writer = csv.writer(output)
                writer.writerow(["Term Position", "Term Value"])
                for i, term in enumerate(sequence, 1):
                    writer.writerow([i, term])
                
                csv_data = output.getvalue()
                if sequence_type == "Arithmetic":
                    filename = f"arithmetic_sequence_{first_term}_{common_difference}_{num_terms}.csv"
                else:
                    filename = f"geometric_sequence_{first_term}_{common_ratio}_{num_terms}.csv"
                
                st.download_button(
                    label="Download as CSV",
                    data=csv_data,
                    file_name=filename,
                    mime="text/csv"
                )
        
        except Exception as e:
            st.error(f"An error occurred while generating the sequence: {str(e)}")
    
    # Add information section
    st.markdown("---")
    
    if sequence_type == "Arithmetic":
        st.markdown("### About Arithmetic Sequences")
        st.markdown("""
        An arithmetic sequence is a sequence of numbers where each term after the first is obtained by adding a constant value (common difference) to the previous term.
        
        **Formula:** a_n = a_1 + (n-1) × d
        
        Where:
        - a_n = nth term
        - a_1 = first term
        - d = common difference
        - n = position of the term
        """)
        
        # Example section
        with st.expander("Examples"):
            st.markdown("""
            **Example 1:** First term = 2, Common difference = 3, Number of terms = 5
            - Sequence: 2, 5, 8, 11, 14
            
            **Example 2:** First term = 10, Common difference = -2, Number of terms = 6  
            - Sequence: 10, 8, 6, 4, 2, 0
            
            **Example 3:** First term = 1.5, Common difference = 0.5, Number of terms = 4
            - Sequence: 1.5, 2.0, 2.5, 3.0
            """)
    else:
        st.markdown("### About Geometric Sequences")
        st.markdown("""
        A geometric sequence is a sequence of numbers where each term after the first is obtained by multiplying the previous term by a constant value (common ratio).
        
        **Sequence Formula:** a_n = a_1 × r^(n-1)
        
        **Series Sum Formula:** 
        - If r ≠ 1: S_n = a_1 × (1 - r^n) / (1 - r)
        - If r = 1: S_n = n × a_1
        
        Where:
        - a_n = nth term
        - a_1 = first term
        - r = common ratio
        - n = position of the term
        - S_n = sum of first n terms
        """)
        
        # Example section
        with st.expander("Examples"):
            st.markdown("""
            **Example 1:** First term = 2, Common ratio = 3, Number of terms = 4
            - Sequence: 2, 6, 18, 54
            - Sum: 80
            
            **Example 2:** First term = 100, Common ratio = 0.5, Number of terms = 5  
            - Sequence: 100, 50, 25, 12.5, 6.25
            - Sum: 193.75
            
            **Example 3:** First term = 1, Common ratio = 2, Number of terms = 6
            - Sequence: 1, 2, 4, 8, 16, 32
            - Sum: 63
            """)

if __name__ == "__main__":
    main()
