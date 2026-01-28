# Chương 02: Tiền Xử Lý Dữ Liệu (Data Preprocessing)

## I. Tổng Quan
Tiền xử lý dữ liệu là bước quan trọng trong Data Mining, giúp làm sạch và chuẩn hóa dữ liệu trước khi phân tích.

## II. Các Phương Pháp Chuẩn Hóa (Normalization)

### 1. Min-Max Normalization (Chuẩn hóa Min-Max)

**Công thức:**
```
v' = (v - min(A)) / (max(A) - min(A)) × (new_max - new_min) + new_min
```

**Trong đó:**
- `v`: Giá trị gốc
- `v'`: Giá trị sau chuẩn hóa
- `min(A)`: Giá trị nhỏ nhất của thuộc tính A
- `max(A)`: Giá trị lớn nhất của thuộc tính A
- `new_min`, `new_max`: Khoảng giá trị mới (thường là [0, 1])

**Ví dụ:** Chuẩn hóa age=35 sang khoảng [0, 1]
```
Giả sử: min(age) = 23, max(age) = 50
v' = (35 - 23) / (50 - 23) × (1 - 0) + 0
v' = 12 / 27 ≈ 0.44
```

### 2. Z-Score Normalization (Chuẩn hóa Z-Score)

**Công thức:**
```
v' = (v - μ) / σ
```

**Trong đó:**
- `μ` (mu): Giá trị trung bình (mean)
- `σ` (sigma): Độ lệch chuẩn (standard deviation)

**Cách tính:**
1. Tính mean: `μ = Σv / n`
2. Tính standard deviation: `σ = √[Σ(v - μ)² / n]`
3. Áp dụng công thức

**Đặc điểm:**
- Kết quả có mean = 0, std = 1
- Phù hợp khi dữ liệu tuân theo phân phối chuẩn
- Giữ được outliers

### 3. Decimal Scaling (Chuẩn hóa theo thập phân)

**Công thức:**
```
v' = v / 10^j
```

**Trong đó:**
- `j`: Số nguyên nhỏ nhất sao cho max(|v'|) < 1

**Ví dụ:**
```
Dữ liệu: 5, 10, 11, 13, 15, 35, 50, 55, 72, 92, 204, 215
max = 215 → cần chia cho 10^3 = 1000
v' = v / 1000
Kết quả: 0.005, 0.010, 0.011, ..., 0.204, 0.215
```

## III. Biểu Đồ Trực Quan (Visualization)

### 1. Boxplot (Biểu đồ hộp)

**Mục đích:** Phát hiện outliers

**Các thành phần:**
- **Q1 (Quartile 1)**: Tứ phân vị thứ nhất (25%)
- **Q2 (Median)**: Trung vị (50%)
- **Q3 (Quartile 3)**: Tứ phân vị thứ ba (75%)
- **IQR**: Interquartile Range = Q3 - Q1
- **Lower fence**: Q1 - 1.5 × IQR
- **Upper fence**: Q3 + 1.5 × IQR
- **Outliers**: Các điểm nằm ngoài fence

**Cách vẽ:**
1. Sắp xếp dữ liệu theo thứ tự tăng dần
2. Tìm Q1, Q2, Q3
3. Tính IQR
4. Xác định fence và outliers
5. Vẽ biểu đồ hộp

### 2. Scatter Plot (Biểu đồ phân tán)

**Mục đích:** Xem mối quan hệ giữa 2 biến

**Cách vẽ:**
- Trục X: Biến độc lập
- Trục Y: Biến phụ thuộc
- Mỗi điểm (x, y) là một bản ghi

## IV. Làm Mịn Dữ Liệu (Smoothing)

### 1. Smoothing by Bin Means (Làm mịn theo trung bình bin)

**Các bước:**
1. Sắp xếp dữ liệu
2. Chia thành các bin có độ sâu bằng nhau
3. Thay thế giá trị trong mỗi bin bằng giá trị trung bình của bin đó

**Ví dụ:**
```
Dữ liệu: 13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30
Chia thành 3 bins (mỗi bin 5 phần tử):

Bin 1: [13, 15, 16, 16, 19]
Mean = (13+15+16+16+19)/5 = 15.8
→ Bin 1 sau: [15.8, 15.8, 15.8, 15.8, 15.8]

Bin 2: [20, 20, 21, 22, 22]
Mean = 21
→ Bin 2 sau: [21, 21, 21, 21, 21]

Bin 3: [25, 25, 25, 25, 30]
Mean = 26
→ Bin 3 sau: [26, 26, 26, 26, 26]
```

### 2. Smoothing by Bin Boundaries (Làm mịn theo biên)

**Các bước:**
1. Sắp xếp dữ liệu
2. Chia thành các bin
3. Thay thế giá trị bằng giá trị gần nhất (min hoặc max của bin)

**Ví dụ:**
```
Bin 1: [13, 15, 16, 16, 19]
Min = 13, Max = 19
→ Bin 1 sau: [13, 13, 19, 19, 19]
```

## V. Phân Tích Và Xác Định Outliers

### Phương pháp Equal-Width Partitioning

**Công thức:**
```
Độ rộng mỗi bin = (max - min) / số lượng bins
```

### Phương pháp Equal-Depth Partitioning

**Cách thực hiện:**
- Mỗi bin chứa số lượng phần tử bằng nhau
- Số phần tử mỗi bin = tổng số phần tử / số bins

### Equal-Frequency Partitioning

Tương tự Equal-Depth, đảm bảo tần suất xuất hiện trong mỗi bin tương đương nhau.

### Clustering

Nhóm các giá trị gần nhau vào cùng một cluster.

## VI. Bài Tập Thực Hành

### Bài 1: Chuẩn hóa dữ liệu tuổi

**Đề bài:** Cho bảng dữ liệu age và %fat:

| age | 23 | 23 | 27 | 27 | 39 | 41 | 47 | 49 | 50 |
|-----|----|----|----|----|----|----|----|----|-----|
| %fat| 9.5| 26.5| 7.8| 17.8| 31.4| 25.9| 27.4| 27.2| 31.2|

**Câu a)** Tính giá trị trung bình, trung vị, yếu vị và độ lệch chuẩn của age và %fat

**Lời giải:**

**Cho age:**
- Dữ liệu đã sắp xếp: 23, 23, 27, 27, 39, 41, 47, 49, 50
- Mean (trung bình): μ = (23+23+27+27+39+41+47+49+50)/9 = 326/9 ≈ 36.22
- Median (trung vị): Vị trí thứ 5 = 39
- Mode (yếu vị): 23 và 27 (xuất hiện 2 lần)
- Std (độ lệch chuẩn):
  ```
  σ = √[Σ(v - μ)² / n]
  σ = √[((23-36.22)² + (23-36.22)² + ... + (50-36.22)²) / 9]
  σ ≈ 10.73
  ```

**Cho %fat:**
- Mean ≈ 22.74
- Median = 26.5
- Std ≈ 8.42

**Câu b)** Vẽ biểu đồ Boxplot cho age và %fat

**Lời giải:**

**Cho age:**

Dữ liệu đã sắp xếp: 23, 23, 27, 27, 39, 41, 47, 49, 50

**Bước 1: Tính các quartiles**

Với n = 9 giá trị:

- **Q2 (Median - Trung vị):** Vị trí thứ (n+1)/2 = (9+1)/2 = 5
  - Giá trị tại vị trí 5: **Q2 = 39**

- **Q1 (Tứ phân vị thứ nhất - 25%):** Vị trí thứ (n+1)/4 = (9+1)/4 = 2.5
  - Interpolation giữa vị trí 2 và 3:
  ```
  Q1 = (value[2] + value[3]) / 2
  Q1 = (23 + 27) / 2 = 50 / 2 = 25
  ```

- **Q3 (Tứ phân vị thứ ba - 75%):** Vị trí thứ 3(n+1)/4 = 3(9+1)/4 = 7.5
  - Interpolation giữa vị trí 7 và 8:
  ```
  Q3 = (value[7] + value[8]) / 2
  Q3 = (47 + 49) / 2 = 96 / 2 = 48
  ```

**Bước 2: Tính IQR (Interquartile Range)**

```
IQR = Q3 - Q1
IQR = 48 - 25 = 23
```

**Bước 3: Tính các giới hạn (fences)**

```
Lower fence = Q1 - 1.5 × IQR
Lower fence = 25 - 1.5 × 23
Lower fence = 25 - 34.5 = -9.5

Upper fence = Q3 + 1.5 × IQR
Upper fence = 48 + 1.5 × 23
Upper fence = 48 + 34.5 = 82.5
```

**Bước 4: Xác định outliers**

- Khoảng chấp nhận: [-9.5, 82.5]
- Kiểm tra các giá trị: 23, 23, 27, 27, 39, 41, 47, 49, 50
- Tất cả giá trị đều nằm trong khoảng [-9.5, 82.5]
- **Kết luận: Không có outliers**

**Câu c)** Vẽ biểu đồ phân tán (scatter plot) dựa trên age và %fat

**Lời giải:**
- Vẽ các điểm (age, %fat): (23, 9.5), (23, 26.5), (27, 7.8), ...
- Quan sát mối quan hệ giữa age và %fat

### Bài 2: Làm mịn dữ liệu

**Đề bài:** Cho dữ liệu age: 13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70

**Câu a)** Sử dụng trung bình khoảng (smoothing by bin means) với độ sâu khoảng là 3

**Lời giải:**
```
Bin 1: [13, 15, 16]
Mean = (13+15+16)/3 = 14.67
→ [14.67, 14.67, 14.67]

Bin 2: [16, 19, 20]
Mean = 18.33
→ [18.33, 18.33, 18.33]

... (tiếp tục cho các bins còn lại)
```

**Câu b)** Xác định và phân vị của phân vị, áp dụng để xác định các outliers trong dữ liệu

**Lời giải:**
```
n = 27
Q1 = giá trị ở vị trí (27+1)/4 = 7 → Q1 = 20
Q2 = giá trị ở vị trí (27+1)/2 = 14 → Q2 = 25
Q3 = giá trị ở vị trí 3(27+1)/4 = 21 → Q3 = 35
IQR = 35 - 20 = 15
Lower fence = 20 - 1.5×15 = -2.5
Upper fence = 35 + 1.5×15 = 57.5
Outliers: 70 (vượt quá upper fence)
```

### Bài 3: Phân vị giá trị của các phương pháp chuẩn hóa sau đây là gì?

**Câu a)** Chuẩn hóa min-max

**Lời giải:**
```
Phân vị: Chuyển đổi dữ liệu về khoảng [new_min, new_max] (thường là [0, 1])

Công thức: v' = (v - min(A)) / (max(A) - min(A)) × (new_max - new_min) + new_min

Ưu điểm:
- Giữ được khoảng giá trị mong muốn
- Dễ hiểu và triển khai

Nhược điểm:
- Nhạy cảm với outliers
- Khi có giá trị mới ngoài khoảng [min, max] cũ, cần chuẩn hóa lại
```

**Câu b)** Chuẩn hóa z-score

**Lời giải:**
```
Phân vị: Chuyển đổi dữ liệu về phân phối chuẩn với mean = 0, std = 1

Công thức: v' = (v - μ) / σ

Ưu điểm:
- Không phụ thuộc vào khoảng giá trị
- Phù hợp với dữ liệu phân phối chuẩn
- Giữ được thông tin về outliers

Nhược điểm:
- Yêu cầu dữ liệu tuân theo phân phối chuẩn
- Kết quả có thể nằm ngoài khoảng cố định
```

**Câu c)** Chuẩn hóa z-score sử dụng độ lệch tuyệt đối trung bình thay vì độ lệch chuẩn

**Lời giải:**
```
Phân vị: Sử dụng MAD (Mean Absolute Deviation) thay vì Standard Deviation

Công thức: v' = (v - μ) / MAD
Trong đó: MAD = Σ|v - μ| / n

Ưu điểm:
- Ít nhạy cảm với outliers hơn z-score thông thường
- Robust hơn với dữ liệu có nhiễu

Nhược điểm:
- Ít phổ biến hơn z-score chuẩn
- Khó diễn giải hơn
```

**Câu d)** Chuẩn hóa bằng cách chia tỷ lệ thập phân

**Lời giải:**
```
Phân vị: Chia dữ liệu cho lũy thừa của 10

Công thức: v' = v / 10^j
Trong đó: j là số nguyên nhỏ nhất sao cho max(|v'|) < 1

Ưu điểm:
- Rất đơn giản
- Nhanh chóng

Nhược điểm:
- Mất thông tin về phân phối
- Phụ thuộc vào giá trị lớn nhất
```

### Bài 4: Sử dụng các phương pháp sau để chuẩn hóa tập dữ liệu: 200, 300, 400, 600, 1000

**Câu a)** Chuẩn hóa min-max bằng cách đặt min = 0 và max = 1

**Lời giải:**
```
min = 200, max = 1000
v' = (v - 200) / (1000 - 200)

200 → (200-200)/800 = 0
300 → (300-200)/800 = 0.125
400 → (400-200)/800 = 0.25
600 → (600-200)/800 = 0.5
1000 → (1000-200)/800 = 1
```

**Câu b)** Chuẩn hóa z-score

**Lời giải:**
```
Mean μ = (200+300+400+600+1000)/5 = 500
Variance σ² = [(200-500)² + (300-500)² + (400-500)² + (600-500)² + (1000-500)²]/5
           = [90000 + 40000 + 10000 + 10000 + 250000]/5
           = 400000/5 = 80000
Std σ = √80000 ≈ 282.84

200 → (200-500)/282.84 ≈ -1.06
300 → (300-500)/282.84 ≈ -0.71
400 → (400-500)/282.84 ≈ -0.35
600 → (600-500)/282.84 ≈ 0.35
1000 → (1000-500)/282.84 ≈ 1.77
```

**Câu c)** Chuẩn hóa z-score sử dụng độ lệch tuyệt đối trung bình thay vì độ lệch chuẩn

**Lời giải:**
```
Mean μ = 500 (đã tính ở câu b)

MAD = (|200-500| + |300-500| + |400-500| + |600-500| + |1000-500|) / 5
    = (300 + 200 + 100 + 100 + 500) / 5
    = 1200 / 5 = 240

200 → (200-500)/240 = -300/240 = -1.25
300 → (300-500)/240 = -200/240 ≈ -0.83
400 → (400-500)/240 = -100/240 ≈ -0.42
600 → (600-500)/240 = 100/240 ≈ 0.42
1000 → (1000-500)/240 = 500/240 ≈ 2.08
```

**Câu d)** Chuẩn hóa bằng cách chia tỷ lệ thập phân

**Lời giải:**
```
max = 1000 → cần j = 4 (vì 10^4 = 10000 > 1000)

v' = v / 10000

200 → 200/10000 = 0.02
300 → 300/10000 = 0.03
400 → 400/10000 = 0.04
600 → 600/10000 = 0.06
1000 → 1000/10000 = 0.1
```

### Bài 5: Sử dụng dữ liệu về tuổi từ Bài 2

**Câu a)** Sử dụng chuẩn hóa min-max để chuyển đổi giá trị age=35 sang khoảng [0, 1]

**Lời giải:**
```
min = 13, max = 70
v' = (35 - 13) / (70 - 13) = 22 / 57 ≈ 0.386
```

**Câu b)** Sử dụng chuẩn hóa z-score để chuyển đổi giá trị age=35

**Lời giải:**
```
Tính mean và std của dữ liệu
μ ≈ 28.89
σ ≈ 13.52
v' = (35 - 28.89) / 13.52 ≈ 0.45
```

**Câu c)** Sử dụng chuẩn hóa bằng cách chia tỷ lệ thập phân để chuyển đổi giá trị age = 35

**Lời giải:**
```
max = 70 → cần j = 2 (vì 10^2 = 100 > 70)
v' = 35 / 100 = 0.35
```

### Bài 6: Sử dụng dữ liệu từ Bài 1

**Câu a)** Chuẩn hóa hai thuộc tính dựa trên chuẩn hóa z-score

**Lời giải:**
```
Đã tính ở Bài 1:
age: μ ≈ 36.22, σ ≈ 10.73
%fat: μ ≈ 22.74, σ ≈ 8.42

Áp dụng công thức z-score cho từng giá trị
```

**Câu b)** Tính hệ số tương quan (Pearson)

**Công thức Pearson:**
```
r = Σ[(x - μx)(y - μy)] / √[Σ(x - μx)² × Σ(y - μy)²]
```

Hoặc đơn giản hơn với dữ liệu đã chuẩn hóa z-score:
```
r = Σ(zx × zy) / n
```

### Bài 7: Phân chia dữ liệu thành bins

**Đề bài:** Cho dữ liệu: 5, 10, 11, 13, 15, 35, 50, 55, 72, 92, 204, 215

**Câu a)** Phân chia tần suất/độ sâu bằng nhau (equal-frequency/equal-depth partitioning)

**Lời giải:**
```
n = 12 điểm dữ liệu, chia thành 4 bins → mỗi bin có 3 phần tử

Bin 1: [5, 10, 11]
Bin 2: [13, 15, 35]
Bin 3: [50, 55, 72]
Bin 4: [92, 204, 215]
```

**Câu b)** Phân chia chiều rộng bằng nhau (equal-width partitioning)

**Lời giải:**
```
min = 5, max = 215
Độ rộng mỗi bin = (215 - 5) / 4 = 52.5

Bin 1: [5, 57.5) → {5, 10, 11, 13, 15, 35, 50, 55}
Bin 2: [57.5, 110) → {72, 92}
Bin 3: [110, 162.5) → {}
Bin 4: [162.5, 215] → {204, 215}
```

**Câu c)** Phân quan Clustering

**Lời giải:**
```
Nhóm các giá trị gần nhau:
Cluster 1: {5, 10, 11, 13, 15}
Cluster 2: {35, 50, 55}
Cluster 3: {72, 92}
Cluster 4: {204, 215}
```

### Bài 8: Phân vị và xác định outliers

**Đề bài:** Cho tập dữ liệu: 45, 37, 88, 60, 99, 35, 1, 50, 55, 48

**Câu a)** Hãy xác định vị trí tập dữ liệu đã cho

**Lời giải:**
```
Sắp xếp dữ liệu: 1, 35, 37, 45, 48, 50, 55, 60, 88, 99
n = 10

Q1 = vị trí (10+1)/4 = 2.75 → Interpolation giữa vị trí 2 và 3
Q1 = 35 + 0.75×(37-35) = 35 + 1.5 = 36.5

Q2 (Median) = vị trí (10+1)/2 = 5.5 → Interpolation giữa vị trí 5 và 6
Q2 = (48 + 50)/2 = 49

Q3 = vị trí 3(10+1)/4 = 8.25 → Interpolation giữa vị trí 8 và 9
Q3 = 60 + 0.25×(88-60) = 60 + 7 = 67
```

**Câu b)** Xác định các giá trị là ngoại lệ (Outliers) dựa trên vị phân vị tìm được

**Lời giải:**
```
IQR = Q3 - Q1 = 67 - 36.5 = 30.5

Lower fence = Q1 - 1.5×IQR = 36.5 - 1.5×30.5 = 36.5 - 45.75 = -9.25
Upper fence = Q3 + 1.5×IQR = 67 + 1.5×30.5 = 67 + 45.75 = 112.75

Kiểm tra các giá trị:
- Giá trị 1 < -9.25? Không (1 > -9.25)
- Giá trị 99 > 112.75? Không

Kết luận: Không có outliers trong tập dữ liệu này
```

### Bài 9: Phân vị và xác định outliers (2)

**Đề bài:** Cho tập dữ liệu: 9, 1, 8, 7, 9, 5, 8, 5, 4, 10, 15

**Câu c)** Hãy xác định vị trí tập dữ liệu đã cho

**Lời giải:**
```
Sắp xếp dữ liệu: 1, 4, 5, 5, 7, 8, 8, 9, 9, 10, 15
n = 11

Q1 = vị trí (11+1)/4 = 3 → Q1 = 5
Q2 = vị trí (11+1)/2 = 6 → Q2 = 8
Q3 = vị trí 3(11+1)/4 = 9 → Q3 = 9
```

**Câu d)** Xác định các giá trị là ngoại lệ (Outliers) dựa trên vị phân vị tìm được

**Lời giải:**
```
IQR = Q3 - Q1 = 9 - 5 = 4

Lower fence = Q1 - 1.5×IQR = 5 - 1.5×4 = 5 - 6 = -1
Upper fence = Q3 + 1.5×IQR = 9 + 1.5×4 = 9 + 6 = 15

Kiểm tra các giá trị:
- Tất cả giá trị đều nằm trong khoảng [-1, 15]

Kết luận: Không có outliers
```

### Bài 10: Phân tích dữ liệu YOBirth và Score

**Đề bài:** Cho tập dữ liệu về điểm số môn học X của sinh viên

| id | YOBirth | Score |
|----|---------|-------|
| 1  | 2004    | 8     |
| 2  | 2006    | 5     |
| 3  | 2004    | 9.5   |
| 4  | 2005    | 5.2   |
| 5  | 2007    | 9.5   |
| 6  | 2002    | 8.5   |
| 7  | 2006    | 10    |
| 8  | 2005    | 9.5   |
| 9  | 1999    | 5.6   |
| 10 | 2015    | 1.2   |
| 11 | 2004    | 6.4   |
| 12 | 2005    | 9.5   |
| 13 | 2006    | 3.4   |

**Câu a)** Hãy tìm kiếm và trên từng cột YOBirth và Score

**Lời giải:**

**Cho YOBirth:**
```
Dữ liệu sắp xếp: 1999, 2002, 2004, 2004, 2004, 2005, 2005, 2005, 2006, 2006, 2006, 2006, 2015
n = 13

Q1 = vị trí (13+1)/4 = 3.5 → Q1 = 2004
Q2 = vị trí (13+1)/2 = 7 → Q2 = 2005
Q3 = vị trí 3(13+1)/4 = 10.5 → Q3 = 2006

IQR = 2006 - 2004 = 2
Lower fence = 2004 - 1.5×2 = 2001
Upper fence = 2006 + 1.5×2 = 2009

Outliers: 1999 (< 2001), 2015 (> 2009)
```

**Cho Score:**
```
Dữ liệu sắp xếp: 1.2, 3.4, 5, 5.2, 5.6, 6.4, 8, 8.5, 9.5, 9.5, 9.5, 9.5, 10
n = 13

Q1 = vị trí 3.5 → Q1 = 5.2
Q2 = vị trí 7 → Q2 = 8
Q3 = vị trí 10.5 → Q3 = 9.5

IQR = 9.5 - 5.2 = 4.3
Lower fence = 5.2 - 1.5×4.3 = -1.25
Upper fence = 9.5 + 1.5×4.3 = 15.95

Outliers: Không có (tất cả giá trị nằm trong khoảng [-1.25, 15.95])
```

**Câu b)** Sử dụng tứ phân vị tìm được xác định giá trị ngoại lệ/Outliers trên cột YOBirth và Score

**Lời giải:**
- **YOBirth:** Có 2 outliers là 1999 và 2015
- **Score:** Không có outliers

### Bài 11: Tính toán thống kê mô tả

**Đề bài:** Cho tập dữ liệu về điểm số môn học X của sinh viên (như Bài 10)

| ID | DV  | Điểm |
|----|-----|------|
| 1  | 1   |      |
| 2  | 2NT | 8    |
| 3  | 1   | 6    |
| 4  | 2   | 9    |
| 5  | 3   | 5    |
| 6  | 2   | 7    |
| 7  | 5   | 6    |
| 8  | 2NT | 8    |
| 9  | 1   | 9    |
| 10 | 1   | 7    |
| 11 |     | 6    |
| 12 | 1   | 8    |

**Câu a)** Hãy điền giá trị thiếu trên thuộc tính KV bằng yếu vị (mode)

**Lời giải:**
```
Đếm tần suất các giá trị trong cột DV:
- 1: xuất hiện 5 lần
- 2: xuất hiện 1 lần
- 2NT: xuất hiện 2 lần
- 3: xuất hiện 1 lần
- 5: xuất hiện 1 lần

Mode (yếu vị) = 1 (xuất hiện nhiều nhất)

Điền vào các ô trống:
- ID 1: DV = 1
- ID 11: DV = 1
```

**Câu b)** Hãy điền giá trị thiếu trên thuộc tính Điểm bởi:

**+ Giá trị trung bình**
```
Các điểm hiện có: 8, 6, 9, 5, 7, 6, 8, 9, 7, 6, 8
Mean = (8+6+9+5+7+6+8+9+7+6+8) / 11 = 79 / 11 ≈ 7.18

Điền vào ID 1: Điểm = 7.18 (hoặc làm tròn = 7)
```

**+ Trung vị**
```
Sắp xếp các điểm: 5, 6, 6, 6, 7, 7, 8, 8, 8, 9, 9
n = 11
Median = vị trí (11+1)/2 = 6 → Median = 7

Điền vào ID 1: Điểm = 7
```

**+ Yếu vị**
```
Đếm tần suất:
- 5: 1 lần
- 6: 3 lần
- 7: 2 lần
- 8: 3 lần
- 9: 2 lần

Mode = 6 hoặc 8 (cả hai đều xuất hiện 3 lần)

Điền vào ID 1: Điểm = 6 hoặc 8
```

## VII. Tổng Kết

**Khi nào dùng phương pháp nào?**

| Phương pháp | Ưu điểm | Nhược điểm | Khi nào dùng |
|-------------|---------|------------|--------------|
| Min-Max | Giữ được khoảng giá trị | Nhạy cảm với outliers | Khi biết khoảng giá trị cụ thể |
| Z-Score | Không phụ thuộc khoảng giá trị | Yêu cầu phân phối chuẩn | Khi dữ liệu phân phối chuẩn |
| Decimal Scaling | Đơn giản | Mất thông tin | Khi cần chuẩn hóa nhanh |
| Bin Means | Giảm nhiễu tốt | Mất thông tin chi tiết | Khi có nhiều nhiễu |
| Bin Boundaries | Giữ được extreme values | Có thể tăng nhiễu | Khi cần giữ giá trị biên |

## VIII. Tài Liệu Tham Khảo

![Hình ảnh bài tập 1](images/Screenshot_20260126_233511.png)
![Hình ảnh bài tập 2](images/Screenshot_20260126_233522.png)
![Hình ảnh bài tập 3](images/Screenshot_20260126_233528.png)
