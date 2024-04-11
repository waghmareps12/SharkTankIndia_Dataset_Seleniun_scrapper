from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

row_data = {"Company":[],
"Description": [],
"Ask": [],
"Deal":[],
"Investment by": [],
"Website": [],
"Instagram": [],
"Twitter": [],
"LinkedIn": [],
"Founder 1": [],
"Founder 2": [],
"Founder 3": [],
"Founder 4": []
}
# Define the target URL
url = "https://sharktankindia.com/"

# Initialize the webdriver (adapt for your browser)
driver = webdriver.Chrome()

# Open the UR
driver.get(url)

# Wait for the page to load (adjust wait time as needed)
driver.implicitly_wait(10)

# Find all tables with the desired class using XPath
tables = driver.find_elements(By.XPATH, "//table[@class='notion-collection-table']")

# Process each table
for table in tables:
    # Extract table rows
    rows = table.find_elements(By.TAG_NAME, "tr")
    for row in rows:

        # Extract table cells within each row
        cells = row.find_elements(By.TAG_NAME, "td")
        # Process cell data (text or other elements)

        for cell in cells:
            cell_data = cell.text.strip()
            if cells.index(cell) == 0:
                row_data["Company"].append(cell_data)
            elif cells.index(cell) == 1:
                row_data["Description"].append(cell_data)
            elif cells.index(cell) == 2:
                row_data["Ask"].append(cell_data)
            elif cells.index(cell) == 3:
                row_data["Deal"].append(cell_data)
            elif cells.index(cell) == 4:
                row_data["Investment by"].append(cell_data)
            elif cells.index(cell) == 5:
                row_data["Website"].append(cell_data)
            elif cells.index(cell) == 6:
                row_data["Instagram"].append(cell_data)
            elif cells.index(cell) == 7:
                row_data["Twitter"].append(cell_data)
            elif cells.index(cell) == 8:
                row_data["LinkedIn"].append(cell_data)
            elif cells.index(cell) == 9:
                row_data["Founder 1"].append(cell_data)
            elif cells.index(cell) == 10:
                row_data["Founder 2"].append(cell_data)
            elif cells.index(cell) == 11:
                row_data["Founder 3"].append(cell_data)
            elif cells.index(cell) == 12:
                row_data["Founder 4"].append(cell_data)
            else:
                pass
            print(cell_data)
            
# Close the browser window
driver.quit()
dataset = pd.DataFrame(row_data)
dataset.to_excel('SharkTankIndia_Dataset_Selenium.xlsx', index= False)