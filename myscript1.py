def process_devops_logs(file_path):
    # التحقق من وجود الملف أولاً (ممارسة أمنية ممتازة في الـ DevOps)
    if not os.path.exists(file_path):
        print(f"❌ خطأ: الملف {file_path} غير موجود!")
        return

    print("=== بدء فحص ملف البيانات وفلترة الصلاحيات ===")
    
    # فتح الملف وقراءته بأمان
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            # تنظيف السطر من أي مسافات أو سطور فارغة في النهاية
            clean_line = line.strip()
            if not clean_line:
                continue
            
            # تقطيع السطر بناءً على العلامة الفاصلة |
            # النتيجة ستكون قائمة: [الدور، الإيميل، رقم الموبايل]
            user_data = clean_line.split("|")
            
            role = user_data[0]
            email = user_data[1]
            phone = user_data[2]
            
            # --- تطبيق فكرة الاقتطاع (Slicing) ---
            
            # 1. اقتطاع نطاق الإيميل (Domain) بعد علامة @
            email_domain = email.split("@")[1]
            
            # 2. اقتطاع كود شبكة الموبايل (أول 3 أرقام)
            phone_code = phone[0:3]
            
            # --- الجمل الشرطية لاتخاذ قرار نظام الأتمتة (DevOps Decision) ---
            print(f"\n👤 المستخدم: {email} | الدور: {role}")
            
            # فحص الإيميل للسماح بالوصول للسيرفرات أو الـ Pipeline
            if email_domain in ["company.com", "devops-team.xyz"]:
                print(f"   🔓 حالة الإيميل: مسموح بالدخول (النطاق: {email_domain})")
            else:
                print(f"   🔒 حالة الإيميل: [محظور] نطاق خارجي أو شخصي!")
                
            # فحص شبكة الموبايل لتحديد مسار إرسال رسائل التحقق التلقائية (SMS OTP)
            if phone_code == "010":
                print("   📱 بوابة الرسائل: توجيه عبر شبكة (Vodafone)")
            elif phone_code == "011":
                print("   📱 بوابة الرسائل: توجيه عبر شبكة (Etisalat)")
            elif phone_code == "012":
                print("   📱 بوابة الرسائل: توجيه عبر شبكة (Orange)")
            elif phone_code == "015":
                print("   📱 بوابة الرسائل: توجيه عبر شبكة (WE)")
            else:
                print("   📱 بوابة الرسائل: شبكة غير مدعومة لإرسال كود التحقق")

# تشغيل الدالة وتمرير الملف لها
process_devops_logs("employees.txt")
Use code with caution.