from fpdf import FPDF

def create_pdf(nmap_file, nikto_file):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    # Title
    pdf.cell(200, 10, txt="Vulnerability Scan Report", ln=True, align="C")

    # Nmap Result
    pdf.cell(200, 10, txt="Nmap Scan Result:", ln=True)
    with open(nmap_file, "r") as f:
        for line in f:
            pdf.multi_cell(0, 8, line)

    # Nikto Result
    pdf.add_page()
    pdf.cell(200, 10, txt="Nikto Scan Result:", ln=True)
    with open(nikto_file, "r") as f:
        for line in f:
            pdf.multi_cell(0, 8, line)

    pdf.output("scan_report.pdf")

# Run function
create_pdf("nmap_result.txt", "nikto_result.txt")
