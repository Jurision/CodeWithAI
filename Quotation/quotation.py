import pandas as pd
import pytesseract
from PIL import Image
import os
import re

# Get all image files in the same directory
current_dir = os.path.dirname(os.path.abspath(__file__))
image_files = [f for f in os.listdir(current_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))]

# Loop through all image files and extract text
for image_file in image_files:
    image_path = os.path.join(current_dir, image_file)
    image = Image.open(image_path)

    # Use OCR to extract text
    extracted_text = pytesseract.image_to_string(image)
    print(f"Extracted Text from {image_file}:\n{extracted_text}")

    # Split the extracted text into lines and filter out empty or irrelevant lines
    lines = [line.strip() for line in extracted_text.splitlines() if line.strip() and re.search(r'\d+', line)]

    # Initialize lists for storing extracted data from the current image
    quantities = []
    unit_prices_cny = []
    total_prices_cny = []

    # Extract data assuming each line contains Quantity, Unit Price, and Total Price in that order
    for line in lines:
        parts = re.findall(r'\d+\.\d+|\d+', line)
        if len(parts) == 3:
            quantities.append(int(parts[0]))
            unit_prices_cny.append(float(parts[1]))
            total_prices_cny.append(float(parts[2]))

    # Creating a DataFrame with the extracted data
    if quantities and unit_prices_cny and total_prices_cny:
        data = {
            "Quantity": quantities,
            "Unit Price (CNY)": unit_prices_cny,
            "Total Price (CNY)": total_prices_cny
        }

        df = pd.DataFrame(data)

        # Conversion rate
        conversion_rate = 0.94 / 6.9

        # Calculating Unit Price and Total Price in USD
        df["Unit Price (USD)"] = (df["Unit Price (CNY)"] * conversion_rate).round(2)
        df["Total Price (USD)"] = (df["Unit Price (USD)"] * df["Quantity"]).round(2)

        # Dropping CNY columns for final display as per instructions
        df_final = df[["Quantity", "Unit Price (USD)", "Total Price (USD)"]]

        # Displaying the dataframe to the user
        print(df_final.to_string(index=False))

        # Exporting the dataframe to an Excel file named after the image file
        output_file_name = f"{os.path.splitext(image_file)[0]}.xlsx"
        output_path = os.path.join(current_dir, output_file_name)
        df_final.to_excel(output_path, index=False)
        print(f"Data has been exported to {output_path}")
    else:
        print(f"Error: Could not extract valid data from the text in {image_file}.")
