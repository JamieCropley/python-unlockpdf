import pikepdf
print("Enter PDF file or / and directory to unlock!")
try:
    pdf = pikepdf.open(input(),password='PASSWORDHERE')
except Exception:
    print("File invalid!")
else:
    pdf.save('book_without_pass.pdf')
    print("PDF File Unlocked!")