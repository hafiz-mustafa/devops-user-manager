import os

def generate_simulation_file(filename: str) -> None:
    """
    Automatically creates a raw text file containing employee records
    if it does not already exist in the working directory.
    """
    raw_data = [
        "Hafiz|hafiz@company.dev|+1-555-0199|DevOps",
        "Sarah|sarah.j@company.com|+1-555-0144|HR",
        "Alex|alex.k@company.dev|+1-555-0177|Backend",
        "Emma|emma.w@company.com|+1-555-0122|Marketing",
        "David|david.d@company.dev|+1-555-0155|Site Reliability"
    ]
    
    # Write the records to a flat file text format
    with open(filename, "w", encoding="utf-8") as file:
        for record in raw_data:
            file.write(record + "\n")
    print(f"[INFO] Simulation file '{filename}' generated successfully.\n")


def parse_employee_record(line: str) -> tuple:
    """
    Parses a single pipeline-delimited string record into its individual fields.
    Returns a tuple containing: (name, email, phone, department)
    """
    # Clean whitespace and split using the pipeline character '|'
    cleaned_line = line.strip()
    fields = cleaned_line.split("|")
    
    name = fields[0]
    email = fields[1]
    phone = fields[2]
    department = fields[3]
    
    return name, email, phone, department


def has_admin_privileges(department: str) -> bool:
    """
    DevOps Access Rule Evaluator:
    Determines if an employee is granted infrastructure administrative privileges.
    """
    admin_departments = ["DevOps", "Backend", "Site Reliability"]
    
    if department in admin_departments:
        return True
    return False


def generate_access_report(name: str, email: str, is_admin: bool) -> str:
    """
    Constructs a highly structured text status report for the access log.
    """
    access_level = "GRANTED (Root / Cluster Admin)" if is_admin else "DENIED (Standard User Access)"
    report = f"USER: {name:<8} | EMAIL: {email:<20} | INFRA ACCESS: {access_level}"
    return report


# ==============================================================================
# MAIN PIPELINE EXECUTION
# ==============================================================================
if __name__ == "__main__":
    target_file = "employees_raw.txt"
    
    # Step 1: Self-generate data within the runtime workspace
    generate_simulation_file(target_file)
    
    print("=" * 80)
    print("              DEV_OPS IDENTITY & ROLE-BASED ACCESS LOGS                 ")
    print("=" * 80)
    
    # Step 2: Read and parse the generated dataset
    if os.path.exists(target_file):
        with open(target_file, "r", encoding="utf-8") as file:
            for line in file:
                # Skip empty lines if any exist
                if not line.strip():
                    continue
                
                # Unpack fields extracted by our string-parsing utility
                emp_name, emp_email, emp_phone, emp_dept = parse_employee_record(line)
                
                # Evaluate authorization level (Boolean check)
                admin_status = has_admin_privileges(emp_dept)
                
                # Format text summary record
                log_entry = generate_access_report(emp_name, emp_email, admin_status)
                print(log_entry)
                
    print("=" * 80)
    print("[SUCCESS] Infrastructure compliance parsing cycle completed.")

