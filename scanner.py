import os
from fpdf import FPDF

target = input("Enter target: ")

print("\n[+] Running Nmap Scan...")
os.system(f"nmap -sV {target} -oN nmap_result.txt")

print("\n[+] Running Nikto Scan...")
os.system(f"nikto -h {target} -o nikto_result.txt")

print("\n[+] Analyzing Results...")

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

print("[+] Generating Professional PDF Report...")

pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", "B", 16)
pdf.cell(200, 10, "Vulnerability Assessment Report", ln=True, align="C")

# Summary
pdf.set_font("Helvetica", size=12)
pdf.cell(200, 10, f"Target: {target}", ln=True)
pdf.cell(200, 10, f"High: {len(high)}  Medium: {len(medium)}  Low: {len(low)}", ln=True)

# High severity
pdf.add_page()
pdf.set_text_color(255, 0, 0)
pdf.cell(200, 10, "High Severity Findings", ln=True)
pdf.set_text_color(0, 0, 0)
for i in high[:50]:
    pdf.multi_cell(0, 8, i)

# Medium severity
pdf.add_page()
pdf.set_text_color(255, 165, 0)
pdf.cell(200, 10, "Medium Severity Findings", ln=True)
pdf.set_text_color(0, 0, 0)
for i in medium[:50]:
    pdf.multi_cell(0, 8, i)

# Low severity
pdf.add_page()
pdf.set_text_color(0, 0, 255)
pdf.cell(200, 10, "Low Severity Findings", ln=True)
pdf.set_text_color(0, 0, 0)
for i in low[:50]:
    pdf.multi_cell(0, 8, i)

pdf.output("pro_report.pdf")

print("\n✅ Pro Report Generated: pro_report.pdf")
