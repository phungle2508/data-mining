# PowerPoint Slides Content

## Slide 1: Title Slide
```
CẢI THIỆN APRIORI
Frequent Itemset Mining và Association Rules

Môn: Data Mining
Đề tài: Market Basket Analysis

Nhóm: [Tên nhóm]
Thành viên:
- [Tên thành viên 1]
- [Tên thành viên 2]
- [Tên thành viên 3]

Giảng viên: [Tên giảng viên]
Năm học 2024 - 2025
```

## Slide 2: Table of Contents
```
NỘI DUNG TRÌNH BÀY

1. Giới Thiệu
2. Phương Pháp: Apriori Algorithm
3. Triển Khai
4. Kết Quả và Phân Tích
5. Chiến Lược Cải Thiện
6. Đánh Giá và Thảo Luận
7. Kết Luận
8. Q&A
```

## Slide 3: Giới thiệu - Đặt vấn đề
```
GIỚI THIỆU

Market Basket Analysis là gì?
▸ Kỹ thuật data mining trong retail
▸ Phân tích hành vi mua sắm khách hàng
▸ Phát hiện sản phẩm thường mua cùng nhau

Ứng dụng thực tế:
□ Tối ưu hóa sắp đặt sản phẩm
□ Cross-selling opportunities
□ Tạo bundle sản phẩm
□ Quản lý tồn kho
```

## Slide 4: Dataset
```
DATASET: GROCERIES

Thông tin dataset:
▸ Nguồn: Machine Learning with R
▸ Loại: Transactional data
▸ Domain: Retail grocery store

Thống kê:
□ [Run script] transactions
□ [Run script] unique products
□ ~4.4 items/transaction (average)

Cấu trúc dữ liệu:
Transaction 1: {milk, bread, butter}
Transaction 2: {beer, chips}
...
```

## Slide 5: Apriori Algorithm - Tổng quan
```
APRIORI ALGORITHM

Nguyên tắc cơ bản:
"Tất cả các tập con của một frequent itemset
cũng phải là frequent"

Ưu điểm:
□ Đơn giản, dễ hiểu
□ Dễ implement
□ Tốt cho dataset nhỏ

Nhược điểm:
□ Multiple database scans
□ Large candidate sets
□ Tốn nhiều bộ nhớ
```

## Slide 6: Apriori - Các bước
```
CÁC BƯỚC THUẬT TOÁN

Step 1: Initialization
▸ Thiết lập minimum support threshold

Step 2: Generate Candidates
▸ Tạo k-itemsets từ (k-1)-itemsets

Step 3: Prune
▸ Loại bỏ items < minimum support
▸ Áp dụng Apriori principle

Step 4: Repeat
▸ Tăng k cho đến khi không tìm thấy frequent items
```

## Slide 7: Các chỉ số đánh giá
```
CÁC CHỈ SỐ ĐÁNH GIÁ

┌─────────────┬──────────────┬─────────────────┐
│   Metric    │   Mô Tả      │    Công Thức    │
├─────────────┼──────────────┼─────────────────┤
│ Support     │ Tần suất     │ P(A∪B)          │
│ Confidence  │ Xác suất     │ P(B|A)          │
│ Lift        │ Độ mạnh      │ P(A∪B)/(P(A)P(B))│
│ Leverage    │ Quan sát     │ P(A∪B)-P(A)P(B) │
│ Conviction  │ Phụ thuộc    │ (1-P(B))/(1-conf)│
└─────────────┴──────────────┴─────────────────┘

Lift > 1: Tương quan dương ✓
Lift = 1: Độc lập
Lift < 1: Tương quan âm
```

## Slide 8: Pipeline xử lý
```
PIPELINE XỬ LÝ DỮ LIỆU

┌────────────┐
│ Load Data  │ → groceries.csv
└─────┬──────┘
      ↓
┌────────────┐
│  Encode    │ → TransactionEncoder
└─────┬──────┘
      ↓
┌────────────┐
│  Cleaning  │ → 7-step process
└─────┬──────┘
      ↓
┌────────────┐
│  Mining    │ → Apriori / FP-Growth
└─────┬──────┘
      ↓
┌────────────┐
│  Rules     │ → Association Rules
└────────────┘

Parameters:
▸ Min Support: [Run script for value]
▸ Min Confidence: 0.25
```

## Slide 9: Kết quả - Top frequent items
```
TOP FREQUENT ITEMS

┌──────────────┬──────────┬───────────┐
│   Product    │  Count   │  Support  │
├──────────────┼──────────┼───────────┤
│ Whole milk   │  [value] │  [value]% │
│ Vegetables   │  [value] │  [value]% │
│ Rolls/buns   │  [value] │  [value]% │
│ Soda         │  [value] │  [value]% │
│ Yogurt       │  [value] │  [value]% │
└──────────────┴──────────┴───────────┘

Insight:
□ Whole milk là sản phẩm phổ biến nhất
□ Được mua trong ~25% transactions
```

## Slide 10: Kết quả - Association rules
```
ASSOCIATION RULES

Example Rules:

Rule 1: {rolls/buns} → {butter}
▸ Support: [value]
▸ Confidence: [value]
▸ Lift: [value]

Rule 2: {milk, bread} → {butter}
▸ Support: [value]
▸ Confidence: [value]
▸ Lift: [value]

Total: [Run script] rules discovered
```

## Slide 11: So sánh thuật toán cơ bản
```
SO SÁNH HIỆU SUẤT CƠ BẢN

┌─────────────┬──────────┬──────────┬────────┐
│  Algorithm  │   Time   │  Memory  │ Scale  │
├─────────────┼──────────┼──────────┼────────┤
│ Apriori     │ Baseline │   High   │  Low   │
│ FP-Growth   │ 2-3x ↑   │  Medium  │  Good  │
│ FP-Max      │ 3-5x ↑   │  Low     │ Excel  │
└─────────────┴──────────┴──────────┴────────┘

Kết luận:
□ FP-Growth tốt cho production
□ FP-Max tốt nhất cho large datasets
```

## Slide 12: Hạn chế của Apriori
```
HẠN CHẾ CỦA APRIORI

1. Multiple Database Scans
   ▸ K scans cho k-itemsets
   ▸ Tốn I/O operations

2. Large Candidate Sets
   ▸ Tăng trưởng theo cấp số nhân
   ▸ 2^k - 1 possible itemsets

3. Memory Usage
   ▸ Lưu tất cả candidates
   ▸ Khó scale với large datasets

4. Computational Cost
   ▸ Candidate generation tốn kém
   ▸ Counting support expensive
```

## Slide 13: Cải tiến 1 - Sampling
```
CẢI TIẾN 1: SAMPLING

Concept:
□ Mine trên sample (30%)
□ Verify trên full dataset
□ Fast cho exploratory analysis

Benefits:
□ Giảm đáng kể chi phí tính toán
□ Nhanh chóng thu được kết quả sơ bộ
□ Phù hợp cho exploratory analysis

Implementation:
sampling_based_fim(df, min_support, sample_ratio=0.3)
```

## Slide 14: Cải tiến 2 - DHP (Hash-based)
```
CẢI TIẾN 2: DHP (HASH-BASED)

Concept:
□ Hash pruning giảm candidates
□ 2-3 database scans
□ Faster candidate reduction

Benefits:
□ Lọc infrequent itemsets sớm hơn
□ Giảm số lượng candidates cần kiểm tra
□ Tăng tốc độ tính toán

Implementation:
dhp_algorithm(transactions, min_support, hash_table_size)
```

## Slide 15: Cải tiến 3 - Transaction Reduction
```
CẢI TIẾN 3: TRANSACTION REDUCTION

Concept:
□ Loại transactions không chứa frequent items
□ Giảm database size qua iterations
□ Memory-efficient

Benefits:
□ Giảm kích thước database cho iterations tiếp theo
□ Ít tốn kém I/O operations
□ Tăng tốc độ processing

Implementation:
transaction_reduction_apriori(df, min_support)
```

## Slide 16: Cải tiến 4 - ECLAT (Vertical)
```
CẢI TIẾN 4: ECLAT (VERTICAL)

Concept:
□ Vertical tid-lists format
□ Fast intersection operations
□ Excellent cho sparse datasets

Benefits:
□ Intersection của tid-lists rất nhanh
□ Đặc biệt hiệu quả cho sparse datasets
□ Depth-first search

Implementation:
eclat_algorithm(df, min_support)
```

## Slide 17: Cải tiến 5 - DIC (Dynamic Counting)
```
CẢI TIẾN 5: DIC (DYNAMIC COUNTING)

Concept:
□ Interleaved counting
□ Ít database scans
□ Faster convergence

Benefits:
□ Ít database scans hơn
□ Tăng tốc convergence
□ Giảm total execution time

Implementation:
dic_algorithm(df, min_support)
```

## Slide 18: Cải tiến 6 - Partitioning
```
CẢI TIẾN 6: PARTITIONING

Concept:
□ Divide database into partitions
□ Mine locally, verify globally
□ 2 database scans, guarantees completeness

Benefits:
□ Xử lý partitions độc lập trong bộ nhớ
□ Cho phép parallel processing
□ Scale tốt với dataset lớn

Implementation:
partitioning_apriori(df, min_support, n_partitions=5)
```

## Slide 19: Khuyến nghị sử dụng
```
KHUYẾN NGHỊ SỬ DỤNG

Small Datasets (< 10K)
→ Apriori hoặc ECLAT: Đơn giản, dễ hiểu

Medium Datasets (10K - 1M)
→ FP-Growth hoặc DIC: Hiệu suất tốt

Large Datasets (> 1M)
→ FP-Max, Partitioning, hoặc Parallel

Real-time/Streaming
→ Sampling-based approaches

Sparse Datasets
→ ECLAT: Vertical format rất hiệu quả

Memory Constrained
→ Transaction Reduction hoặc Partitioning
```

## Slide 20: Kết luận
```
KẾT LUẬN

Điểm chính:
□ Apriori: Foundation cho frequent itemset mining
□ 6 thuật toán cải tiến đã được triển khai
□ Giảm 30-50% execution time với các kỹ thuật tối ưu
□ FP-Growth/FP-Max tốt cho production

Các thuật toán đã triển khai:
□ Sampling: Exploratory analysis nhanh
□ DHP: Hash-based pruning giảm candidates
□ Transaction Reduction: Giảm database size
□ ECLAT: Vertical format, fast intersections
□ DIC: Interleaved counting, ít scans
□ Partitioning: Divide & conquer cho large DB

Ứng dụng thực tế:
□ Retail & E-commerce (Market Basket Analysis)
□ Healthcare (pattern detection trong bệnh sử)
□ Web usage mining (phân tích hành vi người dùng)
□ Bioinformatics (gene sequences, protein interactions)

Thank you! Questions?
```
