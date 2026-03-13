import csv
import os

FILE_NAME = "company.csv"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "..", FILE_NAME)
''' 
def load_company():
    data = {}
    if os.path.exists(CSV_PATH):
        with open(CSV_PATH, mode="r", encoding="utf-8", newline="") as file:
            read = csv.DictReader(file)
            print("test read")
           
            for fila in read:
                ruc = fila["ruc"]
                data[ruc] = {
                    "company_name": fila["company_name"],
                    "direcction": fila["direcction"]
                }
                
    return data
'''

def load_company():
    data = {}
    if os.path.exists(CSV_PATH):
        with open(CSV_PATH, mode="r", encoding="utf-8", newline="") as file:
            read = csv.DictReader(file)
            for fila in read:
                # Usamos .get() o verificamos si la fila no está vacía
                if not fila or "ruc" not in fila:
                    continue
                
                ruc = fila["ruc"].strip() # Limpia espacios
                data[ruc] = {
                    "company_name": fila["company_name"],
                    "direcction": fila["direcction"]
                }
    return data


def save_company(data):
    with open(CSV_PATH, mode="w", encoding="utf-8", newline="") as file:
        headers = ["ruc", "company_name", "direcction"]
        write = csv.DictWriter(file, fieldnames=headers)
        write.writeheader()

        for ruc, info in data.items():
            write.writerow({
                "ruc": ruc,
                "company_name": info["company_name"],
                "direcction": info["direcction"]
            })

data = load_company()