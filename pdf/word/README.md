# Word Document Folder

## Contents
- `word_content.md` - Full content for Word document report

## Formatting Requirements (from slide_01_yeu_cau_bao_cao.md)
- **Khổ giấy**: A4
- **Font chữ**: Times New Roman
- **Cỡ chữ**: 13
- **Lề**:
  - Top: 0.7"
  - Bottom: 0.7"
  - Left: 0.7"
  - Right: 0.7"
  - Header/Footer: 0.4"
- **Giãn cách dòng**: 1.2

## Structure
1. Mục lục (Table of Contents)
2. Chương 1: Giới thiệu (Introduction)
3. Chương 2: Cơ sở lý thuyết và công nghệ sử dụng (Theoretical Basis and Technology)
4. Chương 3: Hiện thực và kết quả (Implementation and Results)
5. Chương 4: Đánh giá kết quả (Result Evaluation)
6. Chương 5: Kết luận (Conclusion)
7. Tài liệu tham khảo (References)

## To Generate Word Document
You can use pandoc to convert markdown to Word:
```bash
pandoc word_content.md -o report.docx --reference-doc=template.docx
```

Or open the markdown file in a text editor and copy content to Word with proper formatting.
