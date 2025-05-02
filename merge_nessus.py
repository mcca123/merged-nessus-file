import xml.etree.ElementTree as ET

def merge_nessus(file1, file2, output_file):
    tree1 = ET.parse(file1)
    tree2 = ET.parse(file2)

    root1 = tree1.getroot()
    root2 = tree2.getroot()

    # ค้นหา <Report> ในไฟล์แรกและไฟล์ที่สอง
    report1 = root1.find("Report")
    report2 = root2.find("Report")

    if report1 is not None and report2 is not None:
        for item in report2.findall("ReportHost"):
            report1.append(item)  # เพิ่มโฮสต์จากไฟล์ที่สองเข้าไปในไฟล์แรก

    tree1.write(output_file)
    print(f"ไฟล์รวมกันเสร็จแล้ว: {output_file}")

# เรียกใช้ฟังก์ชัน
merge_nessus("file1.nessus", "file2.nessus", "merged.nessus")
