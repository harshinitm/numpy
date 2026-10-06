import base64

encoded = input("Enter Base64 string: ")
decoded = base64.b64decode(encoded.encode())
print("Decoded Text:", decoded.decode())
