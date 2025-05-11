import streamlit as st
import qrcode
import io  # To convert PIL image to byte stream

# Function to create QR Code
def create_qr_code(data, filename="qr_code.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    return img

# Function to read QR Code (optional, for QR code reading)
def read_qr_code(filename):
    import cv2
    img = cv2.imread(filename)
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(img)
    
    if data:
        return f"QR Code Data: {data}"
    else:
        return "No QR Code detected"

# Streamlit run function
def run():
    st.title("QR Code Generator & Reader")
    
    # Input section: User enters data for QR Code
    data_input = st.text_input("Enter data to encode in QR Code:")

    if st.button("Generate QR Code"):
        if data_input:
            # Create QR code and convert it to a byte object for Streamlit to display
            qr_image = create_qr_code(data_input)

            # Save image to a BytesIO buffer instead of directly to disk
            img_byte_array = io.BytesIO()
            qr_image.save(img_byte_array, format='PNG')
            img_byte_array.seek(0)  # Rewind the byte array to the start

            # Display the generated QR code with a fixed width (200px)
            st.image(img_byte_array, caption="Generated QR Code", width=200)
            st.success("QR Code has been generated successfully!")
        else:
            st.error("Please enter some data to generate a QR code.")

    # Option to upload a QR code image to read
    uploaded_file = st.file_uploader("Upload a QR Code image to read", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # Display the uploaded image with a fixed width (200px)
        st.image(uploaded_file, caption="Uploaded QR Code", width=200)
        
        # Save the uploaded file temporarily to process it
        with open("uploaded_qr.png", "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Read QR Code from uploaded image
        result = read_qr_code("uploaded_qr.png")
        st.write(result)

# Run the Streamlit app
if __name__ == "__main__":
    run()
