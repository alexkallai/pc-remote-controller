import qrcode
import socket


def prepare_qr_code_info(HOST, PORT):
    IP_ADDRESSES = socket.gethostbyname_ex(socket.gethostname())[2]
    print(f"""
    The remote mouse website is available at the following IP address(es):
    {IP_ADDRESSES}, 
    at PORT NUMBER: {PORT}
    The hostname is: {socket.gethostname()}
    To connect, be on the SAME network as this computer and type into your browser the following: 

    IP:PORT NUMBER

    e.g.:
    {IP_ADDRESSES[-1]}:{PORT}
    (NOTE: the website must be in mobile/tablet mode to work.)
    """)
    for IP in IP_ADDRESSES:
        qrcode_printer(IP, PORT)

def qrcode_printer(IP, PORT_NUMBER):
    text = f"{IP}:{PORT_NUMBER}"
    print(f"QR code for {text}")
    qr = qrcode.QRCode()
    qr.add_data(text)
    qr.print_ascii()