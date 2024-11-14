from helpers import productHelper # type: ignore


if __name__ == "__main__":
    
    file_path = 'Products.txt'
    
    
    products = productHelper.create_item_from_text(file_path)
    
    
    total_balance = productHelper.get_total_balance(products)
    
    print(f"Toplam bakiye (KDV dahil): {total_balance:.2f} TL")