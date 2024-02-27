import streamlit as st

st.image('https://www.teachernu.com/wp-content/uploads/2018/12/%E0%B8%9A%E0%B8%A7%E0%B8%81%E0%B8%A5%E0%B8%9A%E0%B9%80%E0%B8%A5%E0%B8%82%E0%B8%90%E0%B8%B2%E0%B8%99.png')
st.sidebar.subheader('เลขฐานขอดนิยม')
menu_option = st.sidebar.radio("คำนวณเลขฐาน", ['เลขฐาน2', 'เลขฐาน3', 'เลขฐาน8', 'เลขฐาน16'])
def set_background(image_url):
    image_url_str = f'url("{image_url}")'
    css = f"""
    <style>
    .stApp {{
        background-image: {image_url_str};
        background-size: cover;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


##ใช้งานตรงนี้
set_background("")
def decimal_to_binary(decimal_num):
    return bin(decimal_num).replace("0b", "")
def binary_to_decimal(binary_num):
    return int(binary_num, 2)

def main():
    if menu_option == 'เลขฐาน2':
        st.title("แปลงเลขฐานสอง")

        option = st.selectbox("เลือกตัวเลือก:", ["ทศนิยมเป็นเลขฐานสอง", "ไบนารีเป็นทศนิยม"])

        if option == "ทศนิยมเป็นเลขฐานสอง":
            decimal_num = st.number_input("ป้อนเลขทศนิยม:", value=0, step=1)
            if st.button('แปลงเลข'):
                binary_num = decimal_to_binary(decimal_num)
                st.write(f"การแสดงทศนิยมของ {decimal_num} คือ: {binary_num}")
        elif option == "ไบนารีเป็นทศนิยม":
            binary_num = st.text_input("ป้อนเลขทศนิยม:")
            if st.button('แปลงเลข'):
                decimal_num = binary_to_decimal(binary_num)
                st.write(f"การแสดงทศนิยมของ {binary_num} คือ: {decimal_num}")
    if menu_option == 'เลขฐาน3':
        st.title("แปลงเลขฐานสาม")

        option = st.selectbox("เลือกตัวเลือก:", ["ทศนิยมเป็นฐานสาม", "ฐานสามเป็นทศนิยม"])

        if option == "ทศนิยมเป็นฐานสาม":
         decimal_num = st.number_input("ป้อนเลขทศนิยม:", value=0, step=1)
         if st.button('แปลงเลข'):
            ternary_num = decimal_to_ternary(decimal_num)
            st.write(f"การแสดงทศนิยมของ {decimal_num} คือ: {ternary_num}")
        elif option == "ฐานสามเป็นทศนิยม":
         ternary_num = st.text_input("ป้อนเลขฐานสาม:")
         if st.button('แปลงเลข'):
            decimal_num = ternary_to_decimal(ternary_num)
            st.write(f"การแสดงทศนิยมของ {ternary_num} คือ: {decimal_num}")

    if menu_option == 'เลขฐาน8':
         st.title("แปลงเลขฐานแปด")

         option = st.selectbox("เลือกตัวเลือก:", ["ทศนิยมเป็นฐานแปด", "ฐานแปดเป็นทศนิยม"])

         if option == "ทศนิยมเป็นฐานแปด":
           decimal_num = st.number_input("ป้อนเลขทศนิยม:", value=0, step=1)
           if st.button('แปลงเลข'):
                octal_num = decimal_to_octal(decimal_num)
                st.write(f"การแสดงทศนิยมของ {decimal_num} คือ: {octal_num}")
         elif option == "ฐานแปดเป็นทศนิยม":
            octal_num = st.text_input("ป้อนเลขฐานแปด:")
            if st.button('แปลงเลข'):
                decimal_num = octal_to_decimal(octal_num)
                st.write(f"การแสดงทศนิยมของ {octal_num} คือ: {decimal_num}")

    if menu_option == 'เลขฐาน16':
        st.title("แปลงเลขฐานสิบหก")

        option = st.selectbox("เลือกตัวเลือก:", ["ทศนิยมเป็นฐานสิบหก", "ฐานสิบหกเป็นทศนิยม"])

        if option == "ทศนิยมเป็นฐานสิบหก":
         decimal_num = st.number_input("ป้อนเลขทศนิยม:", value=0, step=1)
         if st.button('แปลงเลข'):
            hexadecimal_num = decimal_to_hexadecimal(decimal_num)
            st.write(f"การแสดงทศนิยมของ {decimal_num} คือ: {hexadecimal_num}")
        elif option == "ฐานสิบหกเป็นทศนิยม":
         hexadecimal_num = st.text_input("ป้อนเลขฐานสิบหก:")
         if st.button('แปลงเลข'):
            decimal_num = hexadecimal_to_decimal(hexadecimal_num)
            st.write(f"การแสดงทศนิยมของ {hexadecimal_num} คือ: {decimal_num}")
     




if __name__ == "__main__":
    main()
