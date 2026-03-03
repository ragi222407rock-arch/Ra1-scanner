import os
import argparse
from fpdf import FPDF

# Argument parser
parser = argparse.ArgumentParser(description="Automated Vulnerability Scanner")
parser.add_argument("-t", "--target", required=True, help="Target domain or IP")

args = parser.parse_args()
target = args.target

print(f"\n[+] Target Selected: {target}")

# Nmap scan
print("\n[+] Running Nmap Scan...")
os.system(f"nmap -sV {target} -oN nmap_result.txt")

# Nikto scan
print("\n[+] Running Nikto Scan...")
os.system(f"nikto -h {target} -o nikto_result.txt")

# Severity analysis
high, medium, low = [], [], []

def analyze(file):
    with open(file, "r", errors="ignore") as f:
        for line in f:
            l = line.lower()
            if "vulnerable" in l or "exploit" in l or "sql" in l:
                high.append(line)
            elif "warning" in l or "outdated" in l:
                medium.append(line)
            else:
                low.append(line)

analyze("nmap_result.txt")
analyze("nikto_result.txt")

# PDF report
print("\n[+] Generating CLI Report...")

pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", "B", 16)
pdf.cell(200, 10, "CLI Vulnerability Report", ln=True, align="C")

pdf.set_font("Helvetica", size=12)
pdf.cell(200, 10, f"Target: {target}", ln=True)
pdf.cell(200, 10, f"High: {len(high)}  Medium: {len(medium)}  Low: {len(low)}", ln=True)

pdf.output("cli_report.pdf")

print("\n✅ CLI Scan Complete! Report saved as cli_report.pdf")
