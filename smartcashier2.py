def calculate_final_price(product, price, tax):
    tax_amount = price * tax
    final_price = price + tax_amount
    return final_price # قمنا بإرجاع القيمة بدلاً من طباعتها

# عند استدعاء البرنامج في الأسفل:
product_name = input("Plz Enter Product Name: ")
product_price = float(input("Plz Enter Price: "))

# قمنا بحفظ القيمة العائدة من الدالة داخل متغير اسمه checkout_price
checkout_price = calculate_final_price(product_name, product_price, 0.14)

# الآن يمكننا طباعتها براحتنا أو عمل عمليات أخرى عليها
print(f"Total price to pay at cashier: {checkout_price} EGP")