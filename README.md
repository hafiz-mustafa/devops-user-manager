# DevOps Identity & Role-Based Access Control (RBAC) Simulator

A production-ready Python automation script designed to simulate identity management, log parsing, and user privilege assignment. This project mimics real-world infrastructure security workflows where access level states are enforced dynamically based on employee organizational departments.

## 🚀 Key Features Implemented
* **Automated Data Seeding:** Self-generates structured flat-text configuration logs (`employees_raw.txt`) upon script runtime execution.
* **Log Parsing & Extraction:** Dynamically parses tokenized raw text data using string-splitting algorithms.
* **RBAC Authorization Logic:** Evaluates infrastructure access rules using explicit Boolean logic to isolate tech and non-tech tiers.
* **Modern Python Formatting:** Built using native strict Type Hinting (`variable: type -> output`) for secure, predictable execution.

## ⚙️ How It Works
1. **File Seeding:** The system verifies if the text logs exist; if not, it automatically compiles a standard pipeline-delimited identity matrix.
2. **Parsing Pipeline:** Extracts user attributes (`Name`, `Email`, `Phone`, `Department`).
3. **Privilege Assignment:** Checks compliance lists. Departments like **DevOps**, **Backend**, and **Site Reliability** are assigned high-level cluster administration rights (`GRANTED`), while other departments default to safe standard access (`DENIED`).

## 💻 Tech Stack
* **Language:** Python 3.x
* **Core Libraries:** `os` (Native system path evaluation)
* **Design Pattern:** Functional programming with clean PEP 8 coding standards.

---
*Created as part of practical DevOps & Automation engineering exploration.*
