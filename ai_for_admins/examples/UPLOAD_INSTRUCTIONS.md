# การอัปโหลดตัวอย่างข้อมูลไปยัง Google Sheets

เอกสารนี้อธิบายวิธีอัปโหลดตัวอย่างข้อมูลที่สร้างขึ้นสำหรับการอบรมไปยัง Google Sheets โดยใช้สคริปต์ Python

## ขั้นตอนการเตรียมความพร้อม

### 1. ติดตั้ง Dependencies

1. ติดตั้ง Python 3.7 ขึ้นไป (หากยังไม่มี)
2. ติดตั้ง dependencies ที่จำเป็น:
   ```
   pip install -r requirements.txt
   ```
   
### 2. เปิดใช้งาน Google Sheets API และ Google Drive API

1. เข้าไปที่ [Google Cloud Console](https://console.cloud.google.com/)
2. เลือกโปรเจกต์ที่เกี่ยวข้องกับ credentials.json (โปรเจกต์ "aunqa-452819")
3. ไปที่ "APIs & Services" > "Library"
4. ค้นหาและเปิดใช้งาน APIs ต่อไปนี้:
   - Google Sheets API
   - Google Drive API
5. รอสักครู่ให้การเปิดใช้งานเสร็จสมบูรณ์

## การใช้งานสคริปต์

สคริปต์ `upload_to_sheets.py` จะอัปโหลดไฟล์ CSV ทั้งหมดในโฟลเดอร์ `sheets/` ไปยัง Google Sheets โดยอัตโนมัติ:

1. เรียกใช้สคริปต์:
   ```
   python upload_to_sheets.py
   ```

2. หากนี่เป็นครั้งแรกที่ใช้งาน:
   - เว็บเบราว์เซอร์จะเปิดขึ้นเพื่อให้คุณลงชื่อเข้าใช้บัญชี Google
   - อนุญาตสิทธิ์ที่จำเป็นสำหรับแอปพลิเคชัน (อาจมีคำเตือนเกี่ยวกับการพัฒนาแอป ให้คลิกดำเนินการต่อได้)

3. สคริปต์จะสร้าง Google Sheets สองไฟล์:
   - "Student Registration Data - AI for Admins Workshop"
   - "Faculty Projects Data - AI for Admins Workshop"

4. แต่ละไฟล์จะมีสองชีทย่อย:
   - "Untidy Data" - ข้อมูลที่ไม่เป็นระเบียบ
   - "Tidy Data" - ข้อมูลที่เป็น Tidy Data แล้ว

5. ไฟล์จะถูกตั้งค่าให้สามารถเข้าถึงได้โดยใช้ลิงก์สำหรับทุกคนที่มีลิงก์ (Anyone with the link can view)

6. ลิงก์ Google Sheets จะถูกบันทึกไว้ในไฟล์ `sheets/spreadsheet_links.md`

## หมายเหตุ

- ต้องมีไฟล์ `credentials.json` ที่ถูกต้อง (มีอยู่แล้วในโปรเจกต์นี้)
- สคริปต์นี้จะสร้างไฟล์ `token.json` ในไดเรกทอรีหลักเพื่อเก็บ token การเข้าถึง Google API
- หากมีปัญหาเกี่ยวกับการอนุญาต ให้ลบไฟล์ `token.json` แล้วรันสคริปต์ใหม่