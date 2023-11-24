from urllib.parse import urlencode
def generate_whatsapp_link(phone_number, message):
    base_url = "https://api.whatsapp.com/send"
    params = {
        "phone": phone_number,
        "text": message,
    }

    # Construct the URL with parameters
    whatsapp_url = f"{base_url}?{urlencode(params)}"

    return whatsapp_url


# Example usage
phone_number = "+918960608001"  # Replace with the desired phone number
message = "Hello, how can I help you?"  # Replace with your desired pre-filled message

whatsapp_link = generate_whatsapp_link(phone_number, message)

print("WhatsApp Link:", whatsapp_link)


import qrcode

def generate_qr_code(data, file_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)

# Example usage
whatsapp_link = "https://api.whatsapp.com/send?phone=%2B918960608001&text=Welcome%20to%20Dimension%20Zero%21"
qr_code_file_path = "whatsapp_qr_code.png"

generate_qr_code(whatsapp_link, qr_code_file_path)
print(f"QR Code generated and saved to {qr_code_file_path}")
