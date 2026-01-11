# Video Presentation Folder

## Contents
- `video_script.md` - Script for video presentation (5-10 minutes)

## Video Script Timeline

### [00:00 - 00:45] Introduction
"Xin chào thầy/các bạn. Hôm nay nhóm xin trình bày về đề tài
'Cải thiện Apriori' trong môn Data Mining. Đề tài tập trung vào
việc phân tích Market Basket và tìm các cải tiến cho thuật toán
Apriori cổ điển."

### [00:45 - 01:30] Problem Statement
"Vấn đề chúng ta giải quyết là làm sao để hiểu rõ hành vi mua sắm
của khách hàng thông qua việc phân tích dữ liệu giao dịch. Từ đó,
có thể phát hiện các sản phẩm thường được mua cùng nhau và đưa ra
các gợi ý phù hợp."

### [01:30 - 02:30] Dataset
"Dataset chúng tôi sử dụng là Groceries dataset với [số lượng sau khi chạy]
giao dịch và [số lượng sau khi chạy] sản phẩm khác nhau. Mỗi giao dịch
đại diện cho một giỏ hàng của khách hàng."

### [02:30 - 04:00] Apriori Algorithm
"Apriori là thuật toán cổ điển dựa trên nguyên tắc: tất cả các tập
con của một frequent itemset cũng phải là frequent. Thuật toán có
4 bước chính: Initialization, Generate Candidates, Prune, và Repeat."

### [04:00 - 05:30] Implementation & Results
"Chúng tôi implement thuật toán sử dụng thư viện mlxtend và phát
hiện Whole milk là sản phẩm phổ biến nhất với ~25.5% support.
Tìm được [số lượng sau khi chạy] association rules với minimum confidence 0.25."

### [05:30 - 07:30] Improvement Strategies
"Apriori có 4 hạn chế chính: multiple database scans, large candidate
sets, high memory usage, và expensive computational cost. Chúng tôi
đã triển khai 6 chiến lược cải tiến: Sampling, DHP, Transaction Reduction,
ECLAT, DIC, và Partitioning."

### [07:30 - 08:30] Comparison
"So sánh 9 thuật toán cho thấy FP-Growth và FP-Max có hiệu suất tốt nhất.
Với Groceries dataset, các cải tiến có thể giảm 30-50% execution time."

### [08:30 - 09:30] Conclusion
"Tóm lại, Apriori là nền tảng vững chắc nhưng các cải tiến có thể
giảm đáng kể execution time. FP-Growth và FP-Max là lựa chọn tốt nhất
cho production environments."

### [09:30 - 10:00] Q&A
"Cảm ơn thầy/các bạn đã lắng nghe. Nhóm xin nhận câu hỏi."

## Video Requirements
- **Duration**: 5-10 minutes
- **Show presenter**: Yes (hiện hình người báo cáo)
- **Audio quality**: Clear and audible
- **Screen sharing**: Clear and visible

## Tips for Recording
1. Practice before recording
2. Speaking pace:适中 (moderate pace)
3. Eye contact với camera
4. Clear pronunciation
5. Professional setting
6. Good lighting
7. Quiet environment
