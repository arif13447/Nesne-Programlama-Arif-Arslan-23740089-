class ProductHelper:
    @staticmethod
    def create_item_from_text(file_path):
        products = []
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                name = parts[0].strip()
                price = float(parts[1].strip())
                quantity = int(parts[2].strip()) if len(parts) > 2 else 1
                
                product = product(name, price, quantity)
                products.append(product)
        return products

    @staticmethod
    def get_total_balance(products):
        total_balance = sum(product.get_total_price() for product in products)
        total_balance_with_tax = total_balance * 1.20  
        return total_balance_with_tax