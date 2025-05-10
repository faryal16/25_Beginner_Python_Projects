import qrcode
import cv2

def create_qr_code(data, filename="qr_code.png"):
    qr =qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color = "black", back_color= "white")
    img.save(filename)
    print(f"QR Code saved as {filename}")
    
def read_qr_code(filename):
    img = cv2.imread(filename)
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(img)
    
    if data:
        print("QR Code Data:", data)
        
    else:
        print("No QR Code detected")
        
if __name__ == "__main__":
    data_input = input("Enter data to encode in QR Code: ")
    create_qr_code(data_input)
    
    print("\nReading the QR Code...")
    read_qr_code("qr_code.png")