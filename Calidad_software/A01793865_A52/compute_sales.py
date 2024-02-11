"Programa para realizar calculo de ventas por tickect"
import json
import time
import sys


def load_json_file(file_path):
    "define los archivos a ser cargados"
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e_n:
        print(f"Error loading {file_path}: {e_n}")
        return None


def compute_total_cost(price_catalogue, sales_records):
    "calcula los costos totales"
    total_cost = 0

    for sale in sales_records:
        sale_id = sale.get('SALE_ID', '')
        product = sale.get('Product', '')
        quantity = sale.get('Quantity', 0)

        if isinstance(product, str):
            product_id = product
        elif isinstance(product, dict):
            product_id = product.get('product', '')
        else:
            print("Error: Unexpected structure for Product")
        mat_prod = [item for item in price_catalogue
                    if item.get('title') == product_id]

        if mat_prod:
            # Assuming there's only one matching product, use the first one
            cost_per_item = mat_prod[0]['price']
            total_cost += quantity * cost_per_item
        else:
            print(f"Error: Product ID {product_id} not found in {sale_id}.")

    return total_cost


def main():
    "funcion principal"
    if len(sys.argv) != 3:
        print("Usage: python importjson.py price.json sales.json")
        sys.exit(1)

    start_time = time.time()

    price_catalogue_file = sys.argv[1]
    sales_record_file = sys.argv[2]

    price_catalogue = load_json_file(price_catalogue_file)
    sales_records = load_json_file(sales_record_file)

    if price_catalogue is None or sales_records is None:
        sys.exit(1)

    total_cost = compute_total_cost(price_catalogue, sales_records)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Total Cost: ${total_cost:.2f}")
    print(f"Time Elapsed: {elapsed_time:.4f} seconds")

    with open('SalesResults.txt', 'w') as results_file:
        results_file.write(f"Total Cost: ${total_cost:.2f}\n")
        results_file.write(f"Time Elapsed: {elapsed_time:.4f} seconds\n")


if __name__ == "__main__":
    main()
