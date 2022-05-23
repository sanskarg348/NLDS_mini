from fpdf import FPDF
from main import Main

code = Main()
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', size=15)
pdf.cell(200, 10, txt="Exam Shedule for the Year 1 - 4", ln=1, align='C')
c = 2
for i,j in code.colors.items():
    date, time = code.slots[j].split('#')
    pdf.cell(75, 10, txt=f'{i}', ln=c, align='C')
    pdf.cell(250, 0, txt=f'{date}', ln=c, align='C')
    pdf.cell(350, 0, txt=f'{time}', ln=c, align='C')
    c += 1

pdf.output("schedule.pdf")


