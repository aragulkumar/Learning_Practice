import pyqrcode

# Replace with your Google Drive Image link
google_drive_image_link = 'https://drive.google.com/file/d/1acIdN2UeuEl7M4iL1kRhvfsxlbLaBSpl/view?usp=sharing'

# Extract file ID safely
file_id = google_drive_image_link.split("/d/")[1].split("/view")[0]

# Create the direct download linkimport pyqrcode
import png  # required for saving as PNG

# Replace with your Google Drive Image link
google_drive_image_link = 'https://drive.google.com/file/d/1acIdN2UeuEl7M4iL1kRhvfsxlbLaBSpl/view?usp=sharing'

# Extract file ID safely
file_id = google_drive_image_link.split("/d/")[1].split("/view")[0]

# Create the direct download link
real = f"https://drive.google.com/uc?id={file_id}&export=download"

# Generate QR code
qr_code = pyqrcode.create(real)

# Save QR code as a PNG file
qr_code.png('C:/Users/Ragul/Pictures/myqrcode11.png', scale=8)

print("QR Code saved successfully!")

real = f"https://drive.google.com/uc?id={file_id}&export=download"

# Generate QR code
qr_code = pyqrcode.create(real)

# Save QR code as a PNG file
qr_code.png('C:/Users/Ragul/Pictures/myqrcode11.png', scale=8)

print("QR Code saved successfully!")
