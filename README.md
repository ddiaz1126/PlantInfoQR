# **PlantInfoQR**

**PlantInfoQR** is a simple tool that generates QR codes for plants based on a CSV file of **Plant Names** and their respective **URLs**. The URLs should point to Google Docs (manually created) containing detailed information about each plant.

## **File Structure**

### **PlantDatabase.csv**
- A CSV file downloaded from a Google Sheet containing **Plant Names** and their corresponding **URLs**.
- **URLs** point to Google Docs with plant information.

### **plantQRCreator.py**
- A Python script that orchestrates the generation of a **QR code** for each row in the CSV file.

### **qr_codes (folder)**
- A folder that contains the **QR code files (output)** for each plant.
- The **QR codes** are generated based on the URLs in the CSV file.

## **How to Use**

1. **Prepare the CSV File:**  
   Make sure the **PlantDatabase.csv** file contains two columns: **Plant Name** and **URL**.

2. **Run the Script:**  
   Execute the **plantQRCreator.py** script to create the **QR codes**.

3. **Check the Output Folder:**  
   All generated QR code images will be saved inside the **qr_codes** folder.

## **Dependencies**
- **Python 3.x**
- **qrcode** library (for generating QR codes)
- **Pillow** library (for image manipulation)

You can install the dependencies by running:
```bash
pip install qrcode[pil] pillow
