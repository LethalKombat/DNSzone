# DNS Zone Transfer Vulnerability Scanner

## 📌 Description
This Python script checks whether a domain's **DNS server allows unauthorized Zone Transfers (`AXFR`)**, which can expose sensitive DNS records. If a nameserver permits zone transfers, the domain is **marked as vulnerable**. 

## 🔹 Features
✔️ Queries DNS `NS` (nameserver) records  
✔️ Attempts **Zone Transfers (`AXFR`)**  
✔️ Categorizes targets as **secure or vulnerable**  
✔️ Logs results for future analysis  

## ⚠️ Ethical Disclaimer
🔸 Unauthorized zone transfer attempts may violate security policies.  
🔸 This script is **for educational and security research purposes** in controlled environments.

## 🛠️ Requirements
- Python 3.x
- `dnspython` library

### **📌 Installation**
Install dependencies before running the script:
```bash
pip install dnsZoneTransfer.py
