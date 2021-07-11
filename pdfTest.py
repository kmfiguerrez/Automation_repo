import re

#file_name = 'W11-W12-M1'

def dir_Name(filename):
    # pdf name with basename of Week.
    pdf_name = 'Week '

    # We will get the pattern ie. W11-W12. 
    # Where the part starts with - onwards is optional 
    name = re.compile(r'W(\d)+(-W(\d)+)?')
    # mo variable stands for Math Object.
    mo = name.search(filename)
    # mof stads for modified name.
    mof_name = mo.group() 
    print(mof_name)
    
    # Get the week's numbers ie. 1-2.
    week_number = re.compile(r'[^W]')
    mo1 = week_number.findall(mof_name)
    print(mo1)
    
    # Set the pdf name.
    for c in mo1:
        pdf_name += c

    return pdf_name

#print(dir_Name(file_name))