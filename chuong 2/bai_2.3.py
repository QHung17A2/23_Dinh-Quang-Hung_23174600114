import xml.dom.minidom

# Đọc file XML
doc = xml.dom.minidom.parse('sample.xml')

# Tìm tất cả các phần tử "staff"
staffs = doc.getElementsByTagName('staff')

# Duyệt qua từng phần tử "staff" và in thông tin
for staff in staffs:
    id = staff.getAttribute('id')
    name = staff.getElementsByTagName('name')[0].childNodes[0].data
    salary = staff.getElementsByTagName('salary')[0].childNodes[0].data
    print(f"ID: {id}, Name: {name}, Salary: {salary}")
