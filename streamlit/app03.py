import streamlit as st

def binary_to_decimal(binary_num):
    return int(binary_num, 2)

def decimal_to_binary(decimal_num):
    return bin(decimal_num).replace("0b", "")

def main():
    st.title("Binary Calculator")

    operation = st.selectbox("Choose operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

    num1 = st.text_input("Enter the first binary number:")
    num2 = st.text_input("Enter the second binary number:")

    if st.button("Calculate"):
        if num1 and num2:
            decimal_num1 = binary_to_decimal(num1)
            decimal_num2 = binary_to_decimal(num2)

            if operation == "Addition":
                result = decimal_to_binary(decimal_num1 + decimal_num2)
            elif operation == "Subtraction":
                result = decimal_to_binary(decimal_num1 - decimal_num2)
            elif operation == "Multiplication":
                result = decimal_to_binary(decimal_num1 * decimal_num2)
            elif operation == "Division":
                if decimal_num2 != 0:
                    result = decimal_to_binary(decimal_num1 // decimal_num2)
                else:
                    result = "Cannot divide by zero"

            st.write(f"The result of {operation.lower()} {num1} and {num2} is: {result}")
        else:
            st.warning("Please enter both binary numbers")

if __name__ == "__main__":
    main()

