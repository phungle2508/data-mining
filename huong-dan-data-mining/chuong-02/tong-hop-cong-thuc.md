# Tổng Hợp Công Thức - Chương 02: Tiền Xử Lý Dữ Liệu

## BÀI 1: Chuẩn Hóa Dữ Liệu Tuổi

### 1. Các Công Thức Thống Kê Cơ Bản

#### Mean (Giá trị trung bình)
```
μ = Σv / n
```

**Ví dụ:** Dữ liệu: 23, 27, 39, 41, 50
```
μ = (23 + 27 + 39 + 41 + 50) / 5 = 180 / 5 = 36
```

#### Median (Trung vị)
```
Median = value[(n+1)/2]  (n lẻ)
Median = (value[n/2] + value[n/2 + 1]) / 2  (n chẵn)
```

**Ví dụ:** Dữ liệu: 23, 27, 39, 41, 50 (n=5, lẻ)
```
Median = value[(5+1)/2] = value[3] = 39
```

#### Mode (Yếu vị)
Giá trị xuất hiện nhiều lần nhất trong tập dữ liệu.

**Ví dụ:** Dữ liệu: 23, 23, 27, 27, 39, 41
```
Mode = 23 và 27 (cả hai xuất hiện 2 lần)
```

#### Standard Deviation (Độ lệch chuẩn)
```
σ = √[Σ(v - μ)² / n]
```

**Ví dụ:** Dữ liệu: 10, 12, 14, 16, 18 (μ = 14)
```
σ = √[((10-14)² + (12-14)² + (14-14)² + (16-14)² + (18-14)²) / 5]
σ = √[(16 + 4 + 0 + 4 + 16) / 5]
σ = √[40 / 5] = √8 ≈ 2.83
```

#### Variance (Phương sai)
```
σ² = Σ(v - μ)² / n
```

**Ví dụ:** Từ ví dụ trên
```
σ² = 40 / 5 = 8
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

**Ví dụ:** Dữ liệu: 23, 23, 27, 27, 39, 41, 47, 49, 50 (n=9)
```
Q2 = value[(9+1)/2] = value[5] = 39
Q1 = value[(9+1)/4] = value[2.5] = (23 + 27) / 2 = 25
Q3 = value[3(9+1)/4] = value[7.5] = (47 + 49) / 2 = 48
```

#### IQR (Interquartile Range)
```
IQR = Q3 - Q1
```

**Ví dụ:** Từ ví dụ trên
```
IQR = 48 - 25 = 23
```

#### Fences (Giới hạn phát hiện outliers)
```
Lower fence = Q1 - 1.5 × IQR

Upper fence = Q3 + 1.5 × IQR
```

**Ví dụ:** Từ ví dụ trên
```
Lower fence = 25 - 1.5 × 23 = 25 - 34.5 = -9.5
Upper fence = 48 + 1.5 × 23 = 48 + 34.5 = 82.5
```

#### Xác định Outliers
```
Outlier nếu:
  - value < Lower fence
  - HOẶC value > Upper fence
```

**Ví dụ:** Kiểm tra giá trị 100
```
100 > 82.5 → 100 là outlier
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

**Ví dụ:** Bin: [13, 15, 16, 16, 19]
```
Mean = (13 + 15 + 16 + 16 + 19) / 5 = 79 / 5 = 15.8
Kết quả: [15.8, 15.8, 15.8, 15.8, 15.8]
```

### 2. Smoothing by Bin Boundaries (Làm mịn theo biên)
```
Với mỗi giá trị v trong bin:
  Nếu v - min ≤ max - v:
    v' = min của bin
  Ngược lại:
    v' = max của bin
```

**Ví dụ:** Bin: [13, 15, 16, 16, 19] (min=13, max=19)
```
13: 13-13=0 ≤ 19-13=6 → 13
15: 15-13=2 ≤ 19-15=4 → 13
16: 16-13=3 ≤ 19-16=3 → 13 hoặc 19 (bằng nhau)
16: 16-13=3 ≤ 19-16=3 → 19
19: 19-13=6 > 19-19=0 → 19
Kết quả: [13, 13, 13, 19, 19] hoặc [13, 13, 19, 19, 19]
```

---

## BÀI 3: Phân Vị Giá Trị Của Các Phương Pháp Chuẩn Hóa

### 1. Min-Max Normalization
```
v' = (v - min(A)) / (max(A) - min(A)) × (new_max - new_min) + new_min
```

**Trong đó:**
- `v`: Giá trị gốc
- `v'`: Giá trị sau chuẩn hóa
- `min(A)`: Giá trị nhỏ nhất của thuộc tính A
- `max(A)`: Giá trị lớn nhất của thuộc tính A
- `new_min`, `new_max`: Khoảng giá trị mới (thường là [0, 1])

**Đặc điểm:**
- Chuyển đổi về khoảng [new_min, new_max]
- Nhạy cảm với outliers

**Ví dụ:** Chuẩn hóa 35 trong khoảng [23, 50] về [0, 1]
```
v' = (35 - 23) / (50 - 23) × (1 - 0) + 0
v' = 12 / 27 ≈ 0.44
```

### 2. Z-Score Normalization
```
v' = (v - μ) / σ
```

**Trong đó:**
- `μ`: Giá trị trung bình
- `σ`: Độ lệch chuẩn

**Đặc điểm:**
- Kết quả có mean = 0, std = 1
- Phù hợp với phân phối chuẩn

**Ví dụ:** Dữ liệu: 200, 300, 400, 600, 1000 (μ=500, σ≈282.84)
```
v' của 200 = (200 - 500) / 282.84 ≈ -1.06
v' của 1000 = (1000 - 500) / 282.84 ≈ 1.77
```

### 3. Z-Score với MAD (Mean Absolute Deviation)
```
v' = (v - μ) / MAD

MAD = Σ|v - μ| / n
```

**Đặc điểm:**
- Ít nhạy cảm với outliers hơn z-score thông thường
- Robust hơn với dữ liệu có nhiễu

**Ví dụ:** Dữ liệu: 200, 300, 400, 600, 1000 (μ=500)
```
MAD = (|200-500| + |300-500| + |400-500| + |600-500| + |1000-500|) / 5
MAD = (300 + 200 + 100 + 100 + 500) / 5 = 240

v' của 200 = (200 - 500) / 240 = -1.25
v' của 1000 = (1000 - 500) / 240 ≈ 2.08
```

### 4. Decimal Scaling Normalization
```
v' = v / 10^j
```

**Trong đó:**
- `j`: Số nguyên nhỏ nhất sao cho max(|v'|) < 1

**Đặc điểm:**
- Đơn giản, nhanh chóng
- Phụ thuộc vào giá trị lớn nhất

**Ví dụ:** Dữ liệu: 5, 10, 50, 215 (max=215)
```
j = 3 (vì 10³ = 1000 > 215)
v' = v / 1000

5 → 0.005
10 → 0.010
50 → 0.050
215 → 0.215
```

---

## BÀI 4: Áp Dụng Các Phương Pháp Chuẩn Hóa

**Dataset mẫu:** 200, 300, 400, 600, 1000

### 1. Min-Max Normalization về [0, 1]
```
min = 200, max = 1000

200 → (200-200)/800 = 0
300 → (300-200)/800 = 0.125
400 → (400-200)/800 = 0.25
600 → (600-200)/800 = 0.5
1000 → (1000-200)/800 = 1
```

### 2. Z-Score Normalization
```
μ = (200+300+400+600+1000)/5 = 500
σ = √[(90000+40000+10000+10000+250000)/5] ≈ 282.84

200 → (200-500)/282.84 ≈ -1.06
300 → (300-500)/282.84 ≈ -0.71
400 → (400-500)/282.84 ≈ -0.35
600 → (600-500)/282.84 ≈ 0.35
1000 → (1000-500)/282.84 ≈ 1.77
```

### 3. Z-Score với MAD
```
μ = 500
MAD = (300+200+100+100+500)/5 = 240

200 → (200-500)/240 = -1.25
300 → (300-500)/240 ≈ -0.83
400 → (400-500)/240 ≈ -0.42
600 → (600-500)/240 ≈ 0.42
1000 → (1000-500)/240 ≈ 2.08
```

### 4. Decimal Scaling
```
max = 1000 → j = 4 (vì 10⁴ = 10000 > 1000)

200 → 200/10000 = 0.02
300 → 300/10000 = 0.03
400 → 400/10000 = 0.04
600 → 600/10000 = 0.06
1000 → 1000/10000 = 0.1
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

**Ví dụ:** Dữ liệu: 5, 10, 11, 13, 15, 35, 50, 55, 72, 92, 204, 215 (n=12, 4 bins)
```
Mỗi bin có 12/4 = 3 phần tử

Bin 1: [5, 10, 11]
Bin 2: [13, 15, 35]
Bin 3: [50, 55, 72]
Bin 4: [92, 204, 215]
```

### 2. Equal-Width Partitioning
```
Độ rộng mỗi bin = (max - min) / số lượng bins
```

**Ví dụ:** Dữ liệu: 5, 10, 11, 13, 15, 35, 50, 55, 72, 92, 204, 215 (4 bins)
```
Độ rộng = (215 - 5) / 4 = 52.5

Bin 1: [5, 57.5) → {5, 10, 11, 13, 15, 35, 50, 55}
Bin 2: [57.5, 110) → {72, 92}
Bin 3: [110, 162.5) → {}
Bin 4: [162.5, 215] → {204, 215}
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
| Mode (Yếu vị) | Giá trị xuất hiện nhiều nhất | Bài 1, 11 |
| Std (Độ lệch chuẩn) | `σ = √[Σ(v-μ)²/n]` | Bài 1 |
| Variance (Phương sai) | `σ² = Σ(v-μ)²/n` | Bài 1 |
| MAD (Độ lệch tuyệt đối TB) | `MAD = Σ\|v-μ\|/n` | Bài 3, 4 |
| Q1 (25%) | `value[(n+1)/4]` | Bài 1, 8-11 |
| Q2 (50%) | `value[(n+1)/2]` | Bài 1, 8-11 |
| Q3 (75%) | `value[3(n+1)/4]` | Bài 1, 8-11 |
| IQR | `Q3 - Q1` | Bài 1, 8-11 |
| Lower Fence | `Q1 - 1.5×IQR` | Bài 1, 8-11 |
| Upper Fence | `Q3 + 1.5×IQR` | Bài 1, 8-11 |
| Min-Max | `v' = (v-min)/(max-min)×(new_max-new_min)+new_min` | Bài 3, 4, 5 |
| Z-Score | `v' = (v-μ)/σ` | Bài 3, 4, 5, 6 |
| Z-Score với MAD | `v' = (v-μ)/MAD` | Bài 3, 4 |
| Decimal Scaling | `v' = v/10^j` | Bài 3, 4, 5 |
| Pearson | `r = Σ[(x-μx)(y-μy)]/√[Σ(x-μx)²×Σ(y-μy)²]` | Bài 6 |
| Bin Means | `Mean = Σvi/k` | Bài 2 |
| Bin Boundaries | `v' = min hoặc max gần nhất` | Bài 2 |
| Equal-width | `(max-min)/n_bins` | Bài 7 |
| Equal-depth | `n/n_bins` | Bài 7 |

