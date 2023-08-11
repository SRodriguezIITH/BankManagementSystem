We are already accustomed to python standard libraries like math(), 
random() and datetime(). Now, we will briefly discuss some installed 
modules which overall increase the program efficiency and decrease code 
length. 

To install any module, type the following in the command prompt:
 pip install <module_name>

NOTE: import <module> before writing their functions

1. time Module
This is used to create a time delay between certain processes. Used to 
simulate a load screen bar or exit process.
>>>time.sleep(<delay>) will stop interpreter for <delay> seconds.

2. emoji Module
This is used to print emoticons (UX interface) in certain outputs. This 
module prints the respective emoticon based on given common local 
data repository CLDR name which is also associated to a UNICODE.
For eg: print (emoji.emojize(“:grinning_face:”)) #Output: 

3. fpdf Module
This is used to create a pdf based on given data. In this project, we will 
use this
Syntax:
pdf = FPDF() #Store FPDF function from fpdf
pdf.addpage() #Add a blank page to pdf
pdf.set_font(“<font_name>”,size=<int>)
pdf.cell(200,10,txt=”<Text to be printed in pdf>”)
pdf.output(“File_name.pdf”
