import requests
from bs4 import BeautifulSoup
import re

def extract_pricings(pricing_table):
    # Extract table rows
    rows = pricing_table.select("tr")

    # Extract headers and data rows
    header_row = rows[0]
    data_rows = rows[1:]

    # Extract header titles (Model, Prompt, Completion)
    headers = [cell.get_text().strip() for cell in header_row.select("td")]

    pricing = []
    
    # Iterate over each data row
    for index, row in enumerate(data_rows):
        price_obj = {}
        cells = row.select("td")
        
        # Extract the model name, prompt price, and completion price from the cells
        model = cells[0].get_text().replace("Ã\x97", "x")
        price_obj[headers[0]] = str(model)
        for index2, cell in enumerate(cells[1:]):
            price_obj[headers[index2+1]] = float(re.sub(r"[^0-9.]", "", cell.get_text()))
            

        # Add the data to the pricing list
        pricing.append(price_obj)
    return pricing

def extractInstructGPT(div):
    res = []
    names = div.select(".f-heading-5")
    prices = div.select(".pt-spacing-4")
    for name, price in zip(names, prices):
        model_name = name.get_text().strip()
        model_price = re.sub(r"[^0-9.]", "", price.get_text())
        res.append({
            "Model": model_name,
            "Usage": model_price
            })
    return res

def fetch_pricing_data(url="https://openai.com/pricing"):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    pricing = {}

    pricing_divs = soup.select(".mt-spacing-7")
    for div in pricing_divs:
        
        model_name_element = div.select_one("h3.f-heading-3")

        # If a model name element is not found, skip this div
        if model_name_element is None:
            continue

        model_name = model_name_element.get_text().strip()
        if model_name == "InstructGPT": #Exceptional case, displays differently
            pricing[model_name] = extractInstructGPT(div)
            continue

        # Locate the table containing the pricing data within the current div
        pricing_table = div.select_one("table")

        # If a pricing table is not found, skip this div
        if pricing_table is None:
            continue
        pricing[model_name] = extract_pricings(pricing_table)
    return pricing

if __name__=="__main__":
    print(fetch_pricing_data())