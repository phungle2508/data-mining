# Tổng Hợp Công Thức - Chương 02: Tiền Xử Lý Dữ Liệu

## BÀI 1: Chuẩn Hóa Dữ Liệu Tuổi

### 1. Các Công Thức Thống Kê Cơ Bản

#### Mean (Giá trị trung bình)
```
μ = Σv / n
```

#### Median (Trung vị)
```
Median = value[(n+1)/2]  (n lẻ)
Median = (value[n/2] + value[n/2 + 1]) / 2  (n chẵn)
```

#### Mode (Yếu vị)
Giá trị xuất hiện nhiều lần nhất trong tập dữ liệu.

#### Standard Deviation (Độ lệch chuẩn)
```
σ = √[Σ(v - μ)² / n]
```

#### Variance (Phương sai)
```
σ² = Σ(v - μ)² / n
```

---

### 2. Các Công Thức Boxplot

#### Quartiles (Tứ phân vị)
```
Q2 (Median) = value[(n+1)/2]

Q1 (25%) = value[(n+1)/4]
         = (value[k] + value[k+1]) / 2  (nếu vị trí không nguyên)

Q3 (75%) = value[3(n+1)/4]
         = (value[k] + value[k+1]) / 2  (nếu vị trí không nguyên)
```

#### IQR (Interquartile Range)
```
IQR = Q3 - Q1
```

#### Fences (Giới hạn phát hiện outliers)
```
Lower fence = Q1 - 1.5 × IQR

Upper fence = Q3 + 1.5 × IQR
```

#### Xác định Outliers
```
Outlier nếu:
  - value < Lower fence
  - HOẶC value > Upper fence
```

---

## BÀI 2: Làm Mịn Dữ Liệu (Smoothing)

### 1. Smoothing by Bin Means (Làm mịn theo trung bình)
```
Mean của bin = Σ(vi) / k

Với mỗi giá trị trong bin:
  v'i = Mean của bin
```

**Trong đó:**
- `k`: Số phần tử trong bin
- `vi`: Giá trị thứ i trong bin

### 2. Smoothing by Bin Boundaries (Làm mịn theo biên)
```
Với mỗi giá trị v trong bin:
  Nếu v - min ≤ max - v:
    v' = min của bin
  Ngược lại:
    v' = max của bin
```

---

## BÀI 3: Chuẩn Hóa Min-Max

### Công thức Min-Max Normalization
```
v' = (v - min(A)) / (max(A) - min(A)) × (new_max - new_min) + new_min
```

**Trong đó:**
- `v`: Giá trị gốc
- `v'`: Giá trị sau chuẩn hóa
- `min(A)`: Giá trị nhỏ nhất của thuộc tính A
- `max(A)`: Giá trị lớn nhất của thuộc tính A
- `new_min`, `new_max`: Khoảng giá trị mới (thường là [0, 1])

---

## BÀI 4: Chuẩn Hóa Z-Score

### Công thức Z-Score Normalization
```
v' = (v - μ) / σ
```

**Trong đó:**
- `μ` (mu): Giá trị trung bình (mean)
- `σ` (sigma): Độ lệch chuẩn (standard deviation)

### Các công thức phụ trợ
```
μ = Σv / n

σ = √[Σ(v - μ)² / n]

σ² = Σ(v - μ)² / n  (Variance)
```

---

## BÀI 5: Các Phương Pháp Chuẩn Hóa

### 1. Min-Max Normalization (Xem Bài 3)

### 2. Z-Score Normalization (Xem Bài 4)

### 3. Decimal Scaling Normalization
```
v' = v / 10^j
```

**Trong đó:**
- `j`: Số nguyên nhỏ nhất sao cho max(|v'|) < 1

---

## BÀI 6: Hệ Số Tương Quan Pearson

### Công thức đầy đủ:
```
r = Σ[(x - μx)(y - μy)] / √[Σ(x - μx)² × Σ(y - μy)²]
```

### Công thức với dữ liệu đã chuẩn hóa z-score:
```
r = Σ(zx × zy) / n

Trong đó:
  zx = (x - μx) / σx
  zy = (y - μy) / σy
```

---

## BÀI 7: Phân Chia Dữ Liệu Thành Bins (Partitioning)

### 1. Equal-Frequency/Equal-Depth Partitioning
```
Số phần tử mỗi bin = n / số lượng bins
```

### 2. Equal-Width Partitioning
```
Độ rộng mỗi bin = (max - min) / số lượng bins
```

### 3. Clustering
Nhóm các giá trị gần nhau vào cùng một cluster (không có công thức cố định).

---

## BÀI 8-11: Xác Định Và Xử Lý Outliers

### Quy trình xác định Outliers
```
Bước 1: Sắp xếp dữ liệu tăng dần

Bước 2: Tính Q1, Q2, Q3
  - Q2 = value[(n+1)/2]
  - Q1 = value[(n+1)/4]
  - Q3 = value[3(n+1)/4]

Bước 3: Tính IQR
  - IQR = Q3 - Q1

Bước 4: Tính fences
  - Lower fence = Q1 - 1.5 × IQR
  - Upper fence = Q3 + 1.5 × IQR

Bước 5: Xác định outliers
  - Giá trị < Lower fence → Outlier
  - Giá trị > Upper fence → Outlier

Bước 6: Xử lý outliers
  - Loại bỏ outliers
  - Hoặc thay thế bằng giá trị biên (fence)
  - Hoặc sử dụng các phương pháp khác tùy bài toán
```

---

## PHỤ LỤC: Bảng Tra Công Thức Nhanh

| Mục đích | Công thức | Bài tham khảo |
|----------|-----------|--------------|
| Mean (Trung bình) | `μ = Σv/n` | Bài 1 |
| Median (Trung vị) | `value[(n+1)/2]` | Bài 1 |
| Mode (Yếu vị) | Giá trị xuất hiện nhiều nhất | Bài 1 |
| Std (Độ lệch chuẩn) | `σ = √[Σ(v-μ)²/n]` | Bài 1 |
| Variance (Phương sai) | `σ² = Σ(v-μ)²/n` | Bài 1 |
| Q1 (25%) | `value[(n+1)/4]` | Bài 1 |
| Q2 (50%) | `value[(n+1)/2]` | Bài 1 |
| Q3 (75%) | `value[3(n+1)/4]` | Bài 1 |
| IQR | `Q3 - Q1` | Bài 1 |
| Lower Fence | `Q1 - 1.5×IQR` | Bài 1 |
| Upper Fence | `Q3 + 1.5×IQR` | Bài 1 |
| Min-Max | `v' = (v-min)/(max-min)×(new_max-new_min)+new_min` | Bài 3, 5 |
| Z-Score | `v' = (v-μ)/σ` | Bài 4, 5, 6 |
| Decimal Scaling | `v' = v/10^j` | Bài 5 |
| Pearson | `r = Σ[(x-μx)(y-μy)]/√[Σ(x-μx)²×Σ(y-μy)²]` | Bài 6 |
| Bin Means | `Mean = Σvi/k` | Bài 2 |
| Bin Boundaries | `v' = min hoặc max gần nhất` | Bài 2 |
| Equal-width | `(max-min)/n_bins` | Bài 7 |
| Equal-depth | `n/n_bins` | Bài 7 |
