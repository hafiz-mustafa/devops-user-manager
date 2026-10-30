# 1️⃣ تعريف الدالة بدون بارامترات
def show_welcome_message():
    print("Welcome to DevOps Supermarket")

# 2️⃣ تعريف الدالة مع بارامترات
def calculate_final_price(product, price, tax):
    tax_amount = price * tax
    final_price = price + tax_amount
    print(f"The final price for {product} after tax is: {final_price} EGP")

# ---- جزء تشغيل البرنامج واستدعاء الدوال في الأسفل ----

# استدعاء دالة الترحيب (تأكد من الحروف والأقواس)
show_welcome_message()

# استقبال المدخلات من المستخدم
product_name = input("Plz Enter Product Name: ")
product_price = float(input("Plz Enter Price: "))

# استدعاء دالة الحساب وتمرير المدخلات لها مع نسبة ضريبة 14% مثلاً (0.14)
calculate_final_price(product_name, product_price, 0.14)