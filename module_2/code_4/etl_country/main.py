from tasks.extract import extract
from tasks.transform import transform
from tasks.load import load
from tabulate import tabulate

def main():
    data = extract()
    data_transform = transform(data)
    headers = ['country','capital','population','region']
    print(tabulate(data_transform,headers=headers,tablefmt='grid'))
    result = load(data_transform)
    print(f'{result} records stored in the database')

if __name__ == "__main__":
    main()