#Creating a pdf receipt
from fpdf import FPDF
import datetime
def pdfn(task, AN, CN,IB, FB, M,EN,RN,ACT):
 pdf=FPDF()
 pdf.add_page()
 pdf.set_font("Arial", size=21)
 pdf.cell(200,10,txt="Sunrise Chartered Bank",ln=1,align='C')
 dtn=datetime.datetime.now()
 dtn=str(dtn)
 pdf.set_font("Arial", size=16)
 pdf.cell(200,10,txt=dtn,ln=2,align='C')
 pdf.set_font("Arial", size=12)
 pdf.cell(200,10,txt=task,ln=4,align='C')
 pdf.cell(200,10,txt="-"*50,ln=7,align='C')
 pdf.cell(200,10,txt="Account Number: "+str(AN),ln=8,align='L')
 pdf.cell(200,10,txt="Customer Name: "+str(CN),ln=9,align='L')
 pdf.cell(200,10,txt="Initial Balance: "+str(IB),ln=10,align='L')
 pdf.cell(200,10,txt="Final Balance: "+str(FB),ln=11,align='L')
 pdf.cell(200,10,txt=ACT+": "+str(M),ln=12,align='L')
 
 pdf.cell(200,10,txt="Transaction By:",ln=16,align='L')
 pdf.cell(200,10,txt=str(EN),ln=17,align='L')
 pdf.cell(200,10,txt="Manager",ln=16,align='R')
 pdf.cell(200,10,txt="Sandeep Verma",ln=17,align='R')
 pdf.cell(200,10,txt="-"*50,ln=18,align='C')
Page | 15
 pdf.cell(200,10,txt="I,"+str(CN)+" hereby agree that the above transaction was done 
in my presence and understand that",ln=19,align='C')
 pdf.cell(200,10,txt="Bank will not be responsible for any losses or inadvertent 
errors",ln=20,align='C')
 pdf.cell(200,10,txt="Signature:",ln=21,align='L')
 
 out=str(AN)+"_"+RN+"_Receipt_"
 pdf.output(out+".pdf")
