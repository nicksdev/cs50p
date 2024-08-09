from project import pdf_check, extract, resize_file

def test_pdf_check():
    assert pdf_check("test.pdf") == True

def test_extract():
    assert type(extract("test.pdf")) == str 

def test_resize_file():
    assert len(resize_file("test.txt")) <= 3000 