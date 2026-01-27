# Hướng Dẫn Data Mining - Khai Phá Dữ Liệu

## 📚 Giới Thiệu

Đây là bộ tài liệu hướng dẫn chi tiết về Data Mining (Khai phá dữ liệu), bao gồm các chương về:
- Tiền xử lý dữ liệu
- Luật kết hợp
- Phân loại
- Phân cụm

Mỗi chương được tổ chức với:
- ✅ Lý thuyết và công thức toán học
- ✅ Giải thích chi tiết các thuật toán
- ✅ Ví dụ minh họa từng bước
- ✅ Bài tập thực hành có lời giải

## 📂 Cấu Trúc Thư Mục

```
huong-dan-data-mining/
├── README.md (file này)
├── chuong-02/
│   ├── huong-dan-chuong-02.md
│   └── images/
│       ├── Screenshot_20260126_233511.png
│       ├── Screenshot_20260126_233522.png
│       └── Screenshot_20260126_233528.png
├── chuong-03/
│   ├── huong-dan-chuong-03.md
│   └── images/
│       ├── Screenshot_20260126_233622.png
│       └── Screenshot_20260126_233633.png
├── chuong-04/
│   ├── huong-dan-chuong-04.md
│   └── images/
│       ├── Screenshot_20260126_233702.png
│       ├── Screenshot_20260126_233711.png
│       ├── Screenshot_20260126_233715.png
│       └── Screenshot_20260126_233724.png
└── chuong-05/
    ├── huong-dan-chuong-05.md
    └── images/
        └── Screenshot_20260126_233711.png
```

## 📖 Nội Dung Các Chương

### [Chương 02: Tiền Xử Lý Dữ Liệu](chuong-02/huong-dan-chuong-02.md)

**Nội dung chính:**
- Các phương pháp chuẩn hóa (Normalization)
  - Min-Max Normalization
  - Z-Score Normalization
  - Decimal Scaling
- Biểu đồ trực quan
  - Boxplot (phát hiện outliers)
  - Scatter Plot
- Làm mịn dữ liệu (Smoothing)
  - Smoothing by Bin Means
  - Smoothing by Bin Boundaries
- Phân tích và xác định Outliers

**Công thức quan trọng:**
```
Min-Max: v' = (v - min) / (max - min) × (new_max - new_min) + new_min
Z-Score: v' = (v - μ) / σ
Decimal Scaling: v' = v / 10^j
```

---

### [Chương 03: Luật Kết Hợp - Association Rules](chuong-03/huong-dan-chuong-03.md)

**Nội dung chính:**
- Các khái niệm cơ bản
  - Support, Confidence, Lift
- Thuật toán Apriori
  - Nguyên lý Apriori
  - Các bước chi tiết
  - Sinh luật kết hợp
- Thuật toán FP-Growth
  - FP-Tree structure
  - Mining process
- Thuật toán ECLAT
  - Vertical data format

**Công thức quan trọng:**
```
Support(X) = count(X) / total_transactions
Confidence(X → Y) = Support(X ∪ Y) / Support(X)
Lift(X → Y) = Confidence(X → Y) / Support(Y)
```

---

### [Chương 04: Phân Loại - Classification](chuong-04/huong-dan-chuong-04.md)

**Nội dung chính:**
- Naive Bayes Classifier
  - Định lý Bayes
  - Naive Bayes Assumption
  - Laplace Smoothing
- Decision Trees
  - ID3 (Information Gain)
  - C4.5 (Gain Ratio)
  - CART (Gini Index)
- Model Evaluation
  - Confusion Matrix
  - Accuracy, Precision, Recall
  - F1-Score
- K-Nearest Neighbors (KNN)

**Công thức quan trọng:**
```
Bayes: P(C|X) = [P(X|C) × P(C)] / P(X)
Entropy: Entropy(S) = -Σ pᵢ × log₂(pᵢ)
Accuracy: (TP + TN) / (TP + TN + FP + FN)
Precision: TP / (TP + FP)
Recall: TP / (TP + FN)
```

---

### [Chương 05: Phân Cụm - Clustering](chuong-05/huong-dan-chuong-05.md)

**Nội dung chính:**
- Độ đo khoảng cách
  - Euclidean Distance
  - Manhattan Distance
  - Cosine Similarity
  - Jaccard Similarity
- Thuật toán K-Means
  - Nguyên lý và các bước
  - Ví dụ chi tiết
- Hierarchical Clustering
  - Agglomerative vs Divisive
  - Linkage Methods
- DBSCAN
  - Density-based clustering
- Đánh giá Clustering
  - Silhouette Score
  - Within-Cluster Sum of Squares (WCSS)

**Công thức quan trọng:**
```
Euclidean: d(x, y) = √[Σ(xᵢ - yᵢ)²]
Manhattan: d(x, y) = Σ|xᵢ - yᵢ|
Cosine: similarity = (A · B) / (||A|| × ||B||)
```

## 🎯 Cách Sử Dụng

1. **Học lý thuyết:** Đọc phần giải thích và công thức trong mỗi chương
2. **Xem ví dụ:** Theo dõi các ví dụ được giải chi tiết từng bước
3. **Làm bài tập:** Thực hành với các bài tập có lời giải
4. **Tham khảo hình ảnh:** Xem các screenshot bài tập gốc trong thư mục `images/`

## 💡 Tips Học Tập

- **Nắm vững công thức:** Ghi nhớ và hiểu ý nghĩa từng công thức
- **Làm theo ví dụ:** Tự tay tính toán theo các bước trong ví dụ
- **So sánh thuật toán:** Hiểu rõ ưu/nhược điểm và khi nào dùng thuật toán nào
- **Thực hành nhiều:** Làm đi làm lại các bài tập cho đến khi thuần thục

## 📊 Bảng So Sánh Nhanh

### Thuật Toán Association Rules

| Thuật toán | Số lần scan | Sinh candidates | Bộ nhớ | Phù hợp |
|------------|-------------|-----------------|--------|---------|
| Apriori | Nhiều (k+1) | Có | Ít | DB nhỏ, sparse |
| FP-Growth | 2 lần | Không | Nhiều | DB lớn, dense |
| ECLAT | Ít | Không | Trung bình | Sparse data |

### Thuật Toán Classification

| Thuật toán | Training time | Prediction time | Ưu điểm chính |
|------------|---------------|-----------------|---------------|
| Naive Bayes | Nhanh | Nhanh | Đơn giản, hiệu quả |
| Decision Tree | Trung bình | Nhanh | Dễ hiểu, visual |
| KNN | Không có | Chậm | Không cần training |

### Thuật Toán Clustering

| Thuật toán | Complexity | Cần chỉ định K | Phát hiện noise |
|------------|------------|----------------|-----------------|
| K-Means | O(nkt) | Có | Không |
| Hierarchical | O(n²logn) | Không | Không |
| DBSCAN | O(n logn) | Không | Có |

## 📝 Ghi Chú

- Các công thức được viết bằng markdown, dễ đọc trên GitHub hoặc editor hỗ trợ markdown
- Mỗi ví dụ đều có lời giải chi tiết từng bước
- Hình ảnh gốc của bài tập được lưu trong thư mục `images/` để tham khảo

## 🔗 Tài Liệu Tham Khảo

- Giáo trình Data Mining - Trần Quốc Việt (NLU/CNTT)
- Các screenshot bài tập trong thư mục `images/`

## ⚖️ License

Tài liệu này được tạo ra cho mục đích học tập và ôn thi.

---

**Chúc bạn học tốt! 📚✨**

*Cập nhật lần cuối: 26/01/2026*
