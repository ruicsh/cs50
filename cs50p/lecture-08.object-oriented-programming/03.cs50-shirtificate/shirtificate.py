import sys

from fpdf import FPDF


def main():
    if len(sys.argv) != 2:
        sys.exit()

    name = sys.argv[1]

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", style="B", size=32)
    pdf.cell(0, 10, "CS50 shirtificate", align="C")
    pdf.image("shirtificate.png", x=0, y=50, w=210)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(0, 150)
    pdf.cell(0, 10, f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")


main()
