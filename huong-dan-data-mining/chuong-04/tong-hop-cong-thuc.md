# Tổng Hợp Công Thức - Chương 04: Phân Loại (Classification)

## I. Naive Bayes Classifier

### 1. Định Lý Bayes

**Công thức cơ bản:**
```
P(C|X) = [P(X|C) × P(C)] / P(X)
```

**Trong đó:**
- `P(C|X)`: Posterior probability - Xác suất lớp C khi đã biết X
- `P(X|C)`: Likelihood - Xác suất xuất hiện X khi thuộc lớp C
- `P(C)`: Prior probability - Xác suất ban đầu của lớp C
- `P(X)`: Evidence - Xác suất xuất hiện X

**Ví dụ:**
```
P(Spam|"free") = P("free"|Spam) × P(Spam) / P("free")
```

### 2. Naive Bayes với nhiều thuộc tính

**Công thức:**
```
P(C|X₁,X₂,...,Xₙ) = P(C) × ∏ P(Xᵢ|C) / P(X)
                   = P(C) × P(X₁|C) × P(X₂|C) × ... × P(Xₙ|C) / P(X)
```

**Quyết định phân loại:**
```
Class = argmax P(C|X) = argmax P(C) × ∏ P(Xᵢ|C)
         C                C
```

**Ví dụ:** Phân loại email với 2 từ "free" và "money"
```
P(Spam|free,money) ∝ P(Spam) × P(free|Spam) × P(money|Spam)
P(Ham|free,money) ∝ P(Ham) × P(free|Ham) × P(money|Ham)

Chọn class có xác suất cao hơn
```

### 3. Categorical Naive Bayes

**Tính xác suất:**
```
P(Xᵢ = v | C) = count(Xᵢ = v và C) / count(C)
```

**Ví dụ:** Với class "Nam", thuộc tính "Năng lượng"
```
P(Năng lượng = Phong | Nam) = (Số người Nam có Năng lượng Phong) / (Tổng số Nam)
                              = 3/3 = 1.0
```

### 4. Gaussian Naive Bayes

**Công thức (cho dữ liệu liên tục):**
```
P(Xᵢ = x | C) = 1/(√(2π)σc) × exp(-(x - μc)²/(2σc²))
```

**Trong đó:**
- `μc`: Mean của Xᵢ trong class C
- `σc`: Standard deviation của Xᵢ trong class C

**Ví dụ:** Với chiều cao trong class "Nam"
```
μ_nam = 175 cm, σ_nam = 10 cm
P(Chiều cao = 180 | Nam) = 1/(√(2π)×10) × exp(-(180-175)²/(2×10²))
```

### 5. Laplace Smoothing

**Vấn đề:** Nếu P(Xᵢ|C) = 0, toàn bộ tích bị = 0

**Giải pháp:**
```
P(Xᵢ = v | C) = [count(Xᵢ = v và C) + 1] / [count(C) + |V|]
```

**Trong đó:**
- `|V|`: Số lượng giá trị khác nhau của Xᵢ

**Ví dụ:** Với 2 giá trị {male, female}
```
P(male | low) = (2 + 1) / (4 + 2) = 3/6 = 0.5
P(female | low) = (2 + 1) / (4 + 2) = 3/6 = 0.5
```

---

## II. Decision Trees (Cây Quyết Định)

### 1. Entropy (Độ hỗn loạn)

**Công thức:**
```
Entropy(S) = -Σ pᵢ × log₂(pᵢ)
```

**Trong đó:**
- `pᵢ`: Tỷ lệ của class i trong tập S

**Ví dụ:** Tập S có 9 positive, 5 negative
```
p₊ = 9/14 = 0.643
p₋ = 5/14 = 0.357

Entropy(S) = -(0.643 × log₂(0.643) + 0.357 × log₂(0.357))
           = -(0.643 × (-0.638) + 0.357 × (-1.486))
           = -(-0.410 - 0.531)
           = 0.941
```

### 2. Information Gain (ID3)

**Công thức:**
```
Gain(S, A) = Entropy(S) - Σ [|Sᵥ|/|S|] × Entropy(Sᵥ)
```

**Trong đó:**
- `A`: Thuộc tính
- `Sᵥ`: Tập con của S có giá trị v cho thuộc tính A

**Chọn thuộc tính:** Thuộc tính có Gain cao nhất

**Ví dụ:** Thuộc tính "Outlook" với 3 giá trị {Sunny, Overcast, Rain}
```
Entropy(S) = 0.941

S_sunny: 2 positive, 3 negative
Entropy(S_sunny) = -(2/5 × log₂(2/5) + 3/5 × log₂(3/5)) = 0.971

S_overcast: 4 positive, 0 negative
Entropy(S_overcast) = 0

S_rain: 3 positive, 2 negative
Entropy(S_rain) = 0.971

Gain(S, Outlook) = 0.941 - (5/14 × 0.971 + 4/14 × 0 + 5/14 × 0.971)
                 = 0.941 - 0.693
                 = 0.248
```

### 3. Gain Ratio (C4.5)

**Split Information:**
```
SplitInfo(S, A) = -Σ [|Sᵥ|/|S|] × log₂(|Sᵥ|/|S|)
```

**Gain Ratio:**
```
GainRatio(S, A) = Gain(S, A) / SplitInfo(S, A)
```

**Ưu điểm:** Tránh bias với thuộc tính có nhiều giá trị

**Ví dụ:**
```
SplitInfo(S, Outlook) = -(5/14 × log₂(5/14) + 4/14 × log₂(4/14) + 5/14 × log₂(5/14))
                      = 1.577

GainRatio(S, Outlook) = 0.248 / 1.577 = 0.157
```

### 4. Gini Index (CART)

**Công thức:**
```
Gini(S) = 1 - Σ pᵢ²
```

**Gini Gain:**
```
GiniGain(S, A) = Gini(S) - Σ [|Sᵥ|/|S|] × Gini(Sᵥ)
```

**Chọn thuộc tính:** Thuộc tính có Gini Gain cao nhất (hoặc Gini thấp nhất)

**Ví dụ:** Tập S có 9 positive, 5 negative
```
Gini(S) = 1 - (9/14)² - (5/14)²
        = 1 - 0.413 - 0.128
        = 0.459
```

---

## III. Model Evaluation (Đánh Giá Mô Hình)

### 1. Confusion Matrix

**Cấu trúc:**
```
                    Predicted
                | Positive | Negative |
----------------|----------|----------|
Actual Positive |    TP    |    FN    |
Actual Negative |    FP    |    TN    |
```

**Trong đó:**
- **TP (True Positive)**: Dự đoán đúng Positive
- **TN (True Negative)**: Dự đoán đúng Negative
- **FP (False Positive)**: Dự đoán sai Positive (Type I Error)
- **FN (False Negative)**: Dự đoán sai Negative (Type II Error)

### 2. Accuracy (Độ chính xác)

**Công thức:**
```
Accuracy = (TP + TN) / (TP + TN + FP + FN)
```

**Ví dụ:** TP=10, TN=4, FP=6, FN=1
```
Accuracy = (10 + 4) / (10 + 4 + 6 + 1) = 14/21 = 0.667 = 66.7%
```

### 3. Precision (Độ chính xác dương)

**Công thức:**
```
Precision = TP / (TP + FP)
```

**Ý nghĩa:** Trong số những cái dự đoán là Positive, bao nhiêu % đúng?

**Ví dụ:**
```
Precision = 10 / (10 + 6) = 10/16 = 0.625 = 62.5%
```

### 4. Recall / Sensitivity (Độ nhạy)

**Công thức:**
```
Recall = TP / (TP + FN)
```

**Ý nghĩa:** Trong số những cái thực tế là Positive, bao nhiêu % được phát hiện?

**Ví dụ:**
```
Recall = 10 / (10 + 1) = 10/11 = 0.909 = 90.9%
```

### 5. Specificity (Độ đặc hiệu)

**Công thức:**
```
Specificity = TN / (TN + FP)
```

**Ví dụ:**
```
Specificity = 4 / (4 + 6) = 4/10 = 0.4 = 40%
```

### 6. F1-Score

**Công thức:**
```
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```

**Ví dụ:** Precision=0.625, Recall=0.909
```
F1 = 2 × (0.625 × 0.909) / (0.625 + 0.909)
   = 2 × 0.568 / 1.534
   = 0.740 = 74%
```

---

## IV. K-Nearest Neighbors (KNN)

### 1. Distance Metrics

**Euclidean Distance:**
```
d(x, y) = √[Σ(xᵢ - yᵢ)²]
```

**Ví dụ:** x=(1,2), y=(4,6)
```
d(x, y) = √[(1-4)² + (2-6)²] = √[9 + 16] = √25 = 5
```

**Manhattan Distance:**
```
d(x, y) = Σ|xᵢ - yᵢ|
```

**Ví dụ:**
```
d(x, y) = |1-4| + |2-6| = 3 + 4 = 7
```

**Minkowski Distance:**
```
d(x, y) = (Σ|xᵢ - yᵢ|ᵖ)^(1/p)
```
- p = 1: Manhattan
- p = 2: Euclidean

### 2. KNN Algorithm

**Các bước:**
```
1. Tính khoảng cách từ điểm cần dự đoán đến tất cả điểm training
2. Chọn k điểm gần nhất
3. Voting: Class xuất hiện nhiều nhất trong k điểm
```

**Chọn K:**
- K nhỏ: Nhạy cảm với nhiễu
- K lớn: Mượt hơn nhưng mất thông tin local
- K tốt: Thường là √n (n = số điểm training)

---

## V. Bảng Tra Công Thức Nhanh

| Mục đích | Công thức | Ghi chú |
|----------|-----------|---------|
| Bayes | `P(C\|X) = P(X\|C)×P(C)/P(X)` | Định lý Bayes cơ bản |
| Naive Bayes | `P(C\|X) ∝ P(C)×∏P(Xᵢ\|C)` | Giả định độc lập |
| Laplace | `[count+1]/[total+\|V\|]` | Tránh xác suất 0 |
| Entropy | `-Σpᵢ×log₂(pᵢ)` | Độ hỗn loạn |
| Info Gain | `Entropy(S) - Σ[p×Entropy(Sᵥ)]` | ID3 |
| Gain Ratio | `Gain/SplitInfo` | C4.5 |
| Gini | `1 - Σpᵢ²` | CART |
| Accuracy | `(TP+TN)/(TP+TN+FP+FN)` | Độ chính xác tổng thể |
| Precision | `TP/(TP+FP)` | Độ chính xác dương |
| Recall | `TP/(TP+FN)` | Độ nhạy |
| F1-Score | `2×Precision×Recall/(P+R)` | Trung bình điều hòa |
| Euclidean | `√[Σ(xᵢ-yᵢ)²]` | Khoảng cách thẳng |
| Manhattan | `Σ\|xᵢ-yᵢ\|` | Khoảng cách khối |

---

## VI. So Sánh Thuật Toán

| Thuật toán | Ưu điểm | Nhược điểm | Khi nào dùng |
|------------|---------|------------|--------------|
| Naive Bayes | Nhanh, đơn giản, ít data | Giả định độc lập | Text classification, categorical data |
| Decision Tree | Dễ hiểu, không cần chuẩn hóa | Dễ overfitting | Dữ liệu có rule rõ ràng |
| KNN | Đơn giản, không training | Chậm khi predict, nhạy K | Dữ liệu nhỏ, pattern local |

---

## VII. Ví Dụ Tổng Hợp

### Ví dụ Naive Bayes

**Training Data:**
```
| gender | area  | risk |
|--------|-------|------|
| male   | urban | low  |
| female | rural | low  |
| male   | urban | high |
```

**Prior:**
```
P(low) = 2/3 = 0.667
P(high) = 1/3 = 0.333
```

**Likelihood (với Laplace):**
```
P(male | low) = (1+1)/(2+2) = 2/4 = 0.5
P(urban | low) = (1+1)/(2+2) = 2/4 = 0.5
```

**Predict:** gender=male, area=urban
```
P(low | male, urban) ∝ 0.667 × 0.5 × 0.5 = 0.167
P(high | male, urban) ∝ 0.333 × 0.5 × 0.5 = 0.083

→ Kết luận: low (0.167 > 0.083)
```
