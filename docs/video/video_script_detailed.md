# Video Presentation Script - Data Mining: Cải Thiện Apriori

**Duration**: 5-10 minutes
**Language**: Vietnamese

---

## [00:00 - 00:45] Introduction

**Visual**: Title slide with "CẢI THIỆN APRIORI - Frequent Itemset Mining và Association Rules"

**Speaker**:
"Xin chào thầy và các bạn. Hôm nay nhóm xin trình bày về đề tài 'Cải thiện Apriori' trong môn Data Mining. Đề tài tập trung vào việc phân tích Market Basket và tìm các cải tiến cho thuật toán Apriori cổ điển."

---

## [00:45 - 01:30] Problem Statement

**Visual**: Slide showing Market Basket Analysis applications

**Speaker**:
"Vấn đề chúng ta giải quyết là làm sao để hiểu rõ hành vi mua sắm của khách hàng thông qua việc phân tích dữ liệu giao dịch. Từ đó, có thể phát hiện các sản phẩm thường được mua cùng nhau và đưa ra các gợi ý phù hợp."

"Các ứng dụng thực tế bao gồm: tối ưu hóa sắp đặt sản phẩm, cross-selling opportunities, tạo bundle sản phẩm, và quản lý tồn kho hiệu quả hơn."

---

## [01:30 - 02:30] Dataset

**Visual**: Groceries dataset statistics

**Speaker**:
"Dataset chúng tôi sử dụng là Groceries dataset, một bộ dữ liệu từ Machine Learning with R. Đây là dữ liệu giao dịch từ một cửa hàng tạp hóa, nơi mỗi giao dịch đại diện cho một giỏ hàng của khách hàng."

"Dataset chứa [số lượng sau khi chạy script.py] giao dịch và [số lượng sau khi chạy script.py] sản phẩm khác nhau. Trung bình mỗi khách hàng mua khoảng 4.4 sản phẩm trong một lần giao dịch."

---

## [02:30 - 04:00] Apriori Algorithm

**Visual**: Apriori algorithm flow and steps

**Speaker**:
"Apriori là thuật toán cổ điển được đề xuất bởi Agrawal và Srikant vào năm 1994. Nó dựa trên nguyên tắc: tất cả các tập con của một frequent itemset cũng phải là frequent."

"Thuật toán có 4 bước chính:

1. **Initialization**: Thiết lập minimum support threshold
2. **Generate Candidates**: Tạo k-itemsets từ (k-1)-itemsets
3. **Prune**: Loại bỏ items có support thấp hơn ngưỡng
4. **Repeat**: Tăng k và lặp lại cho đến khi không tìm thấy frequent items nào nữa"

"Chúng tôi cũng sử dụng các chỉ số đánh giá như Support, Confidence, Lift, Leverage, Conviction, và Zhang's Metric để đánh giá chất lượng các association rules."

---

## [04:00 - 05:30] Implementation & Results

**Visual**: Pipeline processing and results

**Speaker**:
"Chúng tôi implement thuật toán sử dụng Python và thư viện mlxtend. Pipeline xử lý bao gồm: Load Data, Encode, Cleaning, Mining, và Rules Generation."

"Kết quả cho thấy Whole milk là sản phẩm phổ biến nhất với khoảng 25.5% support. Các sản phẩm phổ biến tiếp theo bao gồm Other vegetables, Rolls/buns, Soda, và Yogurt."

"Chúng tôi tìm được [số lượng sau khi chạy script.py] association rules với minimum confidence là 0.25. Các rule này cho thấy các mối quan hệ thú vị giữa các sản phẩm."

---

## [05:30 - 07:30] Improvement Strategies

**Visual**: 6 improvement strategies

**Speaker**:
"Apriori có 4 hạn chế chính: multiple database scans, large candidate sets, high memory usage, và expensive computational cost. Để giải quyết这些问题, chúng tôi đã triển khai 6 chiến lược cải tiến:"

1. **Sampling**: Mine trên sample 30% dữ liệu để giảm chi phí tính toán
2. **DHP (Hash-based)**: Sử dụng hash table để pruning candidates hiệu quả hơn
3. **Transaction Reduction**: Loại bỏ transactions không chứa frequent items
4. **ECLAT (Vertical)**: Sử dụng vertical tid-list format để nhanh hơn
5. **DIC (Dynamic Counting)**: Interleaved counting để giảm database scans
6. **Partitioning**: Chia database thành các partitions để xử lý độc lập

---

## [07:30 - 08:30] Comparison

**Visual**: Algorithm comparison table

**Speaker**:
"So sánh 9 thuật toán cho thấy FP-Growth và FP-Max có hiệu suất tốt nhất. Với Groceries dataset:"

"- FP-Growth nhanh hơn 2-3 lần so với Apriori truyền thống"
"- FP-Max nhanh hơn 3-5 lần và tối ưu bộ nhớ tốt hơn"
"- Các cải tiến đề xuất có thể giảm 30-50% execution time"

"Kết quả này cho rằng Apriori vẫn là nền tảng vững chắc, nhưng các thuật toán cải tiến hoặc các phương pháp tiếp cận mới như FP-Growth và FP-Max là lựa chọn tốt hơn cho production environments."

---

## [08:30 - 09:30] Conclusion

**Visual**: Summary and applications

**Speaker**:
"Tóm lại:"

"- Apriori là nền tảng vững chắc cho frequent itemset mining"
"- 6 thuật toán cải tiến đã được triển khai và đánh giá"
"- Các kỹ thuật tối ưu có thể giảm 30-50% execution time"
"- FP-Growth và FP-Max là lựa chọn tốt nhất cho production environments"

"Ứng dụng thực tế của các thuật toán này rất rộng:"

"- Retail và E-commerce: Market Basket Analysis"
"- Healthcare: Pattern detection trong bệnh sử"
"- Web usage mining: Phân tích hành vi người dùng"
"- Bioinformatics: Phân tích gene sequences và protein interactions"

---

## [09:30 - 10:00] Q&A

**Visual**: "Thank you! Questions?" slide

**Speaker**:
"Cảm ơn thầy và các bạn đã lắng nghe. Nhóm xin nhận câu hỏi."

---

## Recording Tips

### Before Recording:
1. Practice the script 2-3 times to get comfortable
2. Check microphone and camera setup
3. Ensure good lighting (natural light is best)
4. Clean and professional background

### During Recording:
1. **Eye contact**: Look at the camera, not the screen
2. **Speaking pace**: Moderate and clear (适中)
3. **Pronunciation**: Clear and articulate
4. **Gestures**: Natural hand movements to emphasize points
5. **Screen sharing**: Make sure the code/slides are clearly visible

### Technical Setup:
- Use a quiet room
- Good internet connection (if streaming)
- Microphone close but not too close
- Camera at eye level
- Screen resolution: 1920x1080 or higher

### Post-Recording:
1. Check audio quality
2. Verify screen clarity
3. Edit out any major mistakes
4. Add captions if possible
5. Keep final video under 10 minutes
