# 1. النوع الأول: Function ترجع قيمة رقمية (Integer) لحساب الراتب الإجمالي
def calculate_total_salary(basic: int, bonus: int) -> int:
    salary = basic + bonus
    return salary

# 2. النوع الثاني: Function ترجع قيمة نصية (String) لطباعة تقرير الموظف
def generate_employee_report(name: str, total_salary: int) -> str:
    report = f"Employee {name} has a total salary of: {total_salary} USD."
    return report

# 3. النوع الثالث: Function ترجع قيمة منطقية (Boolean) للتحقق من استحقاق الحوافز
def check_bonus_eligibility(total_salary: int) -> bool:
    if total_salary < 5000:
        return True
    else:
        return False

# تشغيل المتغيرات (Basic & Bonus) وطباعة النتائج
emp_name = "Hafiz"
basic_salary = 3000
bonus_amount = 1500

# حساب الراتب الإجمالي
total = calculate_total_salary(basic_salary, bonus_amount)
print("--- 1. Integer Output ---")
print(f"Total Salary: {total}\n")

# إنشاء التقرير النصي
final_report = generate_employee_report(emp_name, total)
print("--- 2. String Output ---")
print(final_report + "\n")

# التحقق المنطقي
is_eligible = check_bonus_eligibility(total)
print("--- 3. Boolean Output ---")
print(f"Is eligible for DevOps allowance? {is_eligible}")