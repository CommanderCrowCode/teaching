# คู่มือการแปลงข้อมูลแบบไม่เป็นระเบียบเป็นข้อมูล Tidy Data

## ตัวอย่าง: ข้อมูลลงทะเบียนนักศึกษา

### ปัญหาข้อมูลที่ไม่เป็นระเบียบ (Untidy Data)

ไฟล์ `untidy_student_registration.csv` มีปัญหาต่อไปนี้:

1. **การรวมเซลล์ของคณะ** - คณะไม่ถูกระบุในทุกแถว แต่ใช้การรวมเซลล์แทน
2. **คำนำหน้า ชื่อ และนามสกุลรวมกัน** - ข้อมูลรวมกันในคอลัมน์เดียว
3. **รหัสวิชา ชื่อวิชา และหน่วยกิตรวมกัน** - ข้อมูลรวมกันในคอลัมน์เดียว
4. **วิชาขยายในแนวนอน** - นักศึกษาหนึ่งคนมีการลงทะเบียนหลายวิชาในแถวเดียว

### ขั้นตอนการแปลงเป็น Tidy Data

#### ขั้นตอนที่ 1: แก้ไขปัญหาการรวมเซลล์ของคณะ

1. สร้างสำเนา Sheet ใหม่
2. คัดลอกข้อมูลทั้งหมดจาก Sheet เดิม
3. ในคอลัมน์คณะ ให้ระบุชื่อคณะในทุกแถวที่เกี่ยวข้อง:
   - แถวที่ 2-6: "วิทยาศาสตร์"
   - แถวที่ 7-9: "วิศวกรรมศาสตร์"
   - แถวที่ 10-11: "การจัดการ"

#### ขั้นตอนที่ 2: แยกคำนำหน้า ชื่อ และนามสกุล

1. เพิ่มคอลัมน์ "คำนำหน้า", "ชื่อ", และ "นามสกุล" หลังคอลัมน์ "รหัสนักศึกษา"
2. ใช้ Data > Split text to columns หรือสูตร เพื่อแยกข้อมูล:
   - ใช้ Text to Columns โดยเลือก Delimiter เป็น Space
   - หรือใช้ฟังก์ชัน SPLIT ใน Google Sheets: `=SPLIT(C2, " ")`

#### ขั้นตอนที่ 3: แยกรหัสวิชา ชื่อวิชา และหน่วยกิต

1. สำหรับแต่ละคอลัมน์วิชา (วิชาลงทะเบียน 1, 2, 3):
   - ใช้ Text to Columns แยกข้อมูลโดยใช้ Space เป็นตัวแบ่ง
   - หรือใช้ฟังก์ชัน:
     - รหัสวิชา: `=LEFT(D2, 6)` (ดึงตัวอักษร 6 ตัวแรก)
     - ชื่อวิชา: `=MID(D2, 8, FIND("(", D2) - 9)` (ดึงข้อความระหว่างตำแหน่งที่ 8 จนถึงเครื่องหมายวงเล็บ)
     - หน่วยกิต: `=VALUE(MID(D2, FIND("(", D2) + 1, FIND(" ", D2, FIND("(", D2)) - FIND("(", D2) - 1))` (ดึงตัวเลขหน่วยกิตจากวงเล็บ)

#### ขั้นตอนที่ 4: แปลงโครงสร้างข้อมูลให้ 1 แถว = 1 การลงทะเบียน 1 วิชา

1. สร้าง Sheet ใหม่สำหรับข้อมูล Tidy Data
2. สร้างคอลัมน์ทั้งหมดที่จำเป็น: รหัสนักศึกษา, คำนำหน้า, ชื่อ, นามสกุล, คณะ, รหัสวิชา, ชื่อวิชา, หน่วยกิต
3. คัดลอกข้อมูลจาก Sheet ที่แปลงแล้ว โดยแยกแต่ละวิชาให้อยู่คนละแถว:
   - นักศึกษา 1 คน ที่ลงทะเบียน 3 วิชาจะกลายเป็น 3 แถวในข้อมูล Tidy
   - ข้อมูลของนักศึกษา (รหัส, คำนำหน้า, ชื่อ, นามสกุล, คณะ) จะซ้ำกันในแต่ละแถว
   - แต่ละแถวจะมีข้อมูลเฉพาะของวิชา (รหัสวิชา, ชื่อวิชา, หน่วยกิต) ที่แตกต่างกัน

### ประโยชน์ของข้อมูลที่ปรับเป็น Tidy Data

เมื่อปรับเป็น Tidy Data แล้ว คุณสามารถทำสิ่งต่อไปนี้ได้อย่างง่ายดาย:

1. **การกรองข้อมูล** - กรองเฉพาะวิชาที่ต้องการ หรือเฉพาะนักศึกษาของคณะที่ต้องการ
2. **การคำนวณสถิติ** - คำนวณจำนวนนักศึกษาที่ลงทะเบียนในแต่ละวิชา หรือจำนวนหน่วยกิตเฉลี่ยที่นักศึกษาลงทะเบียน
3. **การสร้าง Pivot Table** - สร้างรายงานสรุปข้อมูลการลงทะเบียนตามคณะหรือตามรายวิชา
4. **การสร้างกราฟ** - แสดงผลข้อมูลการลงทะเบียนในรูปแบบกราฟได้หลากหลาย

### ฟังก์ชันที่มีประโยชน์สำหรับการวิเคราะห์ข้อมูล Tidy

หลังจากปรับข้อมูลให้เป็น Tidy Data แล้ว คุณสามารถใช้ฟังก์ชันเหล่านี้ได้:

1. `COUNTIFS(range1, criteria1, range2, criteria2, ...)` - นับจำนวนตามเงื่อนไขหลายเงื่อนไข
2. `SUMIFS(sum_range, range1, criteria1, range2, criteria2, ...)` - รวมค่าตามเงื่อนไขหลายเงื่อนไข
3. `AVERAGEIFS(average_range, range1, criteria1, range2, criteria2, ...)` - หาค่าเฉลี่ยตามเงื่อนไขหลายเงื่อนไข
4. `FILTER(range, condition1, [condition2, ...])` - กรองข้อมูลตามเงื่อนไข
5. `QUERY(data, query, [headers])` - ใช้คำสั่งคล้าย SQL เพื่อดึงข้อมูล

## ตัวอย่างคำถามที่สามารถวิเคราะห์ได้ง่ายจากข้อมูล Tidy:

1. มีนักศึกษากี่คนที่ลงทะเบียนวิชาภาษาไทย (001101)?
2. คณะใดมีจำนวนการลงทะเบียนมากที่สุด?
3. นักศึกษาชายและหญิงมีการลงทะเบียนวิชาใดแตกต่างกันอย่างไร?
4. มีนักศึกษากี่คนที่ลงทะเบียนทั้งวิชาภาษาไทยและภาษาอังกฤษ?