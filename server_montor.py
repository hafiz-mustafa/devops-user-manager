# 1. دالة ترجع Integer: تحسب الاستهلاك الإجمالي للـ RAM
def get_total_ram(used: int, docker: int) -> int:
    total = used + docker
    return total

# 2. دالة ترجع String: تصيغ تقرير حالة الخادم
def get_status_report(server_name: str, total_ram: int) -> str:
    report = f"Server [{server_name}] current RAM usage is: {total_ram} GB."
    return report

# 3. دالة ترجع Boolean: تتحقق هل شارف الخادم على الانهيار (الحد الأقصى 12)
def is_server_overloaded(total_ram: int) -> bool:
    if total_ram >= 12:
        return True
    else:
        return False

# ==========================================
# تشغيل المتغيرات وتجربة النظام (Basic & Bonus Inputs)
# ==========================================
srv_name = "DevOps-Prod-Server"
used_ram = 7    # المتغير الأول
docker_ram = 6  # المتغير الثاني (مجموعهما 13 أي أكبر من 12)

# 1. استدعاء الدالة الرقمية
total_consumption = get_total_ram(used_ram, docker_ram)
print("--- 1. Total RAM (Integer) ---")
print(f"Total: {total_consumption} GB\n")

# 2. استدعاء الدالة النصية
server_report = get_status_report(srv_name, total_consumption)
print("--- 2. Server Report (String) ---")
print(server_report + "\n")

# 3. استدعاء الدالة المنطقية
critical_status = is_server_overloaded(total_consumption)
print("--- 3. Overload Alert (Boolean) ---")
print(f"Is the server in danger Alert?: {critical_status}")

# ==========================================
# التعديل الجديد: طباعة تحذير مخصص للـ DevOps
# ==========================================
if critical_status == True:
    print("🚨 WARNING: Server is in critical condition! Action required!")
else:
    print("🟢 System Check: Server status is stable.")