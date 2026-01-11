# Word Document Template Guide

## Document Formatting Requirements

According to `slide_01_yeu_cau_bao_cao.md`:
- **Khổ giấy**: A4
- **Font chữ**: Times New Roman
- **Cỡ chữ**: 13pt
- **Lề**:
  - Top: 0.7"
  - Bottom: 0.7"
  - Left: 0.7"
  - Right: 0.7"
  - Header/Footer: 0.4"
- **Giãn cách dòng**: 1.2

## Document Structure (5 Chapters)

### Trang bìa (Cover Page)
```
ĐẠI HỌC [TÊN TRƯỜNG]

KHOA CÔNG NGHỆ THÔNG TIN

---

BÁO CÁO MÔN: DATA MINING

ĐỀ TÀI:
# CẢI THIỆN APRIORI
Frequent Itemset Mining và Association Rules

---

Sinh viên thực hiện:
[Tên sinh viên 1] - MSSV: [...]
[Tên sinh viên 2] - MSSV: [...]

Giảng viên hướng dẫn:
[Tên giảng viên]

---

Năm học 2024 - 2025
```

### Table of Contents
1. Giới Thiệu
2. Cơ Sở Lý Thuyết Và Công Nghệ Sử Dụng
3. Hiện Thực Và Kết Quả
4. Đánh Giá Kết Quả
5. Kết Luận
6. Tài Liệu Tham Khảo

---

## Chapter Content Summary

### Chapter 1: Giới Thiệu
- 1.1 Đặt vấn đề
- 1.2 Dataset: Groceries

### Chapter 2: Cơ Sở Lý Thuyết Và Công Nghệ Sử Dụng
- 2.1 Tổng quan về Apriori Algorithm
- 2.2 Các bước thuật toán
- 2.3 Các chỉ số đánh giá
- 2.4 Pipeline xử lý dữ liệu
- 2.5 Lựa chọn tham số
- 2.6 Công nghệ sử dụng

### Chapter 3: Hiện Thực Và Kết Quả
- 3.1 Pipeline xử lý dữ liệu
- 3.2 Data cleaning process
- 3.3 Frequent itemset mining
- 3.4 Thống kê dataset
- 3.5 Top frequent items
- 3.6 Association rules được phát hiện
- 3.7 So sánh hiệu suất

### Chapter 4: Đánh Giá Kết Quả
- 4.1 Các chỉ số hiệu suất
- 4.2 Đánh giá chất lượng rule
- 4.3 Khuyến nghị sử dụng

### Chapter 5: Kết Luận
- 5.1 Kết quả đạt được
- 5.2 Hạn chế của Apriori
- 5.3 Các chiến lược cải tiến đã triển khai
- 5.4 Ứng dụng thực tế

---

## How to Create the Word Document

### Method 1: Using Pandoc (Recommended)
```bash
pandoc word_content.md -o report.docx \
  --reference-doc=template.docx \
  --toc \
  --toc-depth=3
```

### Method 2: Manual Copy to Microsoft Word
1. Open Microsoft Word
2. Set page layout:
   - Size: A4
   - Margins: 0.7" all sides
   - Font: Times New Roman, 13pt
   - Line spacing: 1.2
3. Copy content from `word_content.md`
4. Paste with formatting
5. Add page numbers
6. Generate Table of Contents automatically

### Method 3: Using Google Docs
1. Go to docs.google.com
2. Create new document
3. File > Page setup:
   - Paper size: A4
   - Margins: 0.7" all sides
4. Copy content from `word_content.md`
5. Format with:
   - Font: Times New Roman
   - Size: 13pt
   - Line spacing: 1.2
6. Insert > Table of Contents

---

## Required Elements Checklist

- [ ] Cover page with all required information
- [ ] Table of Contents (with page numbers)
- [ ] Chapter 1: Giới thiệu
- [ ] Chapter 2: Cơ sở lý thuyết và công nghệ sử dụng
- [ ] Chapter 3: Hiện thực và kết quả
- [ ] Chapter 4: Đánh giá kết quả
- [ ] Chapter 5: Kết luận
- [ ] References/Tài liệu tham khảo
- [ ] Code snippets (if applicable)
- [ ] Tables and figures with captions
- [ ] Proper headers and footers
- [ ] Page numbers

---

## Tips for Professional Formatting

1. **Headers**: Use Word's built-in Heading styles (Heading 1, Heading 2, etc.)
2. **Code**: Use monospace font (Consolas or Courier New)
3. **Tables**: Add borders and consistent formatting
4. **Figures**: Add captions below each figure
5. **References**: Use consistent citation style
6. **Page breaks**: Insert before each major chapter
7. **Spelling**: Run spell-check (Vietnamese)
8. **Headers/Footers**: Include document title and page numbers

---

## Notes

- The `word_content.md` file contains all the content formatted in Markdown
- You can convert Markdown to Word using pandoc or manually copy/paste
- Make sure to fill in the placeholder values like [Run script for value] after running your Python scripts
- Include any relevant screenshots or diagrams to enhance understanding
