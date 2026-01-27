# Chương 05: Phân Cụm - Clustering

## I. Tổng Quan
Phân cụm (Clustering) là kỹ thuật unsupervised learning, nhóm các đối tượng tương tự vào cùng một cụm (cluster) mà không cần nhãn trước.

**Ứng dụng:**
- Phân khúc khách hàng
- Phân tích hình ảnh
- Phát hiện anomaly
- Tổ chức tài liệu

**Khác biệt với Classification:**
- Classification: Có nhãn (supervised)
- Clustering: Không có nhãn (unsupervised)

## II. Độ Đo Khoảng Cách (Distance Metrics)

### 1. Euclidean Distance (Khoảng cách Euclid)

**Công thức:**
```
d(x, y) = √[Σ(xᵢ - yᵢ)²]
```

**Ví dụ:**
```
A = (2, 10), B = (5, 4)
d(A, B) = √[(2-5)² + (10-4)²]
        = √[9 + 36]
        = √45
        = 6.71
```

### 2. Manhattan Distance (Khoảng cách Manhattan)

**Công thức:**
```
d(x, y) = Σ|xᵢ - yᵢ|
```

**Ví dụ:**
```
A = (2, 10), B = (5, 4)
d(A, B) = |2-5| + |10-4|
        = 3 + 6
        = 9
```

### 3. Minkowski Distance

**Công thức:**
```
d(x, y) = (Σ|xᵢ - yᵢ|ᵖ)^(1/p)
```

**Trong đó:**
- p = 1: Manhattan Distance
- p = 2: Euclidean Distance
- p = ∞: Chebyshev Distance

**Ví dụ với p = 3:**
```
A = (2, 10), B = (5, 4)
d(A, B) = (|2-5|³ + |10-4|³)^(1/3)
        = (3³ + 6³)^(1/3)
        = (27 + 216)^(1/3)
        = 243^(1/3)
        = 6.24
```

### 4. Cosine Similarity (Độ tương tự Cosine)

**Công thức:**
```
similarity = cos(θ) = (A · B) / (||A|| × ||B||)
                    = Σ(Aᵢ × Bᵢ) / (√Σ(Aᵢ²) × √Σ(Bᵢ²))
```

**Cosine Distance:**
```
distance = 1 - similarity
```

**Ví dụ:**
```
A = (1, 2, 3), B = (2, 3, 4)

A · B = 1×2 + 2×3 + 3×4 = 2 + 6 + 12 = 20
||A|| = √(1² + 2² + 3²) = √14 = 3.74
||B|| = √(2² + 3² + 4²) = √29 = 5.39

similarity = 20 / (3.74 × 5.39) = 20 / 20.16 = 0.992
distance = 1 - 0.992 = 0.008
```

### 5. Jaccard Similarity (Cho tập hợp)

**Công thức:**
```
Jaccard(A, B) = |A ∩ B| / |A ∪ B|
```

**Ví dụ:**
```
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A ∩ B = {3, 4} → |A ∩ B| = 2
A ∪ B = {1, 2, 3, 4, 5, 6} → |A ∪ B| = 6

Jaccard(A, B) = 2/6 = 0.333
```

## III. Thuật Toán K-Means

### 1. Nguyên Lý

Chia dữ liệu thành K cụm, mỗi điểm thuộc cụm có centroid (trung tâm) gần nhất.

### 2. Các Bước

**Input:**
- K: Số lượng cụm
- Dataset: Tập dữ liệu cần phân cụm

**Algorithm:**
```
1. Khởi tạo: Chọn K centroids ngẫu nhiên
2. Repeat:
   a) Assignment step: Gán mỗi điểm vào cụm có centroid gần nhất
   b) Update step: Cập nhật centroid = trung bình các điểm trong cụm
3. Until: Centroids không thay đổi hoặc đạt số iteration tối đa
```

**Assignment Step:**
```
For each point x:
  cluster(x) = argmin d(x, centroid_k)
               k
```

**Update Step:**
```
For each cluster k:
  centroid_k = mean(points in cluster k)
             = Σ(points) / count(points)
```

### 3. Ví Dụ Chi Tiết

**Bài 2: Cho dữ liệu phân nhiều vế hình phân nhóm như sau:**

**Training Example:**
```
| Example | running nose | coughing | reddened skin | fever |
|---------|--------------|----------|---------------|-------|
| d1      | +            | +        | +             | -     |
| d2      | +            | +        | +             | +     |
| d3      | +            | -        | -             | +     |
| d4      | -            | +        | +             | -     |
| d5      | -            | -        | -             | -     |
| d6      | -            | +        | +             | +     |
```

**Câu a)** Xem như các trường tính (ngoại trừ Training Example) là thuộc tính nhị phận trực tiếp sai với đối tượng

**Chuyển đổi sang dạng vector:**
```
d1 = (1, 1, 1, 0)
d2 = (1, 1, 1, 1)
d3 = (1, 0, 0, 1)
d4 = (0, 1, 1, 0)
d5 = (0, 0, 0, 0)
d6 = (0, 1, 1, 1)
```

**Câu b)** Xem như các trường tính là khoảng cách Euclidean

**Tính khoảng cách giữa các điểm:**
```
d(d1, d2) = √[(1-1)² + (1-1)² + (1-1)² + (0-1)²] = √1 = 1
d(d1, d3) = √[(1-1)² + (1-0)² + (1-0)² + (0-1)²] = √3 = 1.73
d(d1, d4) = √[(1-0)² + (1-1)² + (1-1)² + (0-0)²] = √1 = 1
...
```

### 4. Ví Dụ K-Means với K=2

**Cho tập điểm 8 điểm đầu:** A1=(2,10), A2+(2,5), A3=(8,4), A4=(5,8), A5=(7,5), A6=(6,4), A7=(1,2), A8=(4,9)

**Iteration 1:**

**Khởi tạo centroids:**
```
C1 = A1 = (2, 10)
C2 = A4 = (5, 8)
```

**Assignment Step (tính khoảng cách):**
```
A1: d(A1,C1) = 0, d(A1,C2) = √[(2-5)²+(10-8)²] = √13 = 3.6
    → Cluster 1

A2: d(A2,C1) = √[(2-2)²+(5-10)²] = 5
    d(A2,C2) = √[(2-5)²+(5-8)²] = √18 = 4.24
    → Cluster 2

A3: d(A3,C1) = √[(8-2)²+(4-10)²] = √72 = 8.49
    d(A3,C2) = √[(8-5)²+(4-8)²] = √25 = 5
    → Cluster 2

A4: d(A4,C1) = √13 = 3.6, d(A4,C2) = 0
    → Cluster 2

A5: d(A5,C1) = √[(7-2)²+(5-10)²] = √50 = 7.07
    d(A5,C2) = √[(7-5)²+(5-8)²] = √13 = 3.6
    → Cluster 2

A6: d(A6,C1) = √[(6-2)²+(4-10)²] = √52 = 7.21
    d(A6,C2) = √[(6-5)²+(4-8)²] = √17 = 4.12
    → Cluster 2

A7: d(A7,C1) = √[(1-2)²+(2-10)²] = √65 = 8.06
    d(A7,C2) = √[(1-5)²+(2-8)²] = √52 = 7.21
    → Cluster 2

A8: d(A8,C1) = √[(4-2)²+(9-10)²] = √5 = 2.24
    d(A8,C2) = √[(4-5)²+(9-8)²] = √2 = 1.41
    → Cluster 2
```

**Kết quả:**
```
Cluster 1: {A1} = {(2,10)}
Cluster 2: {A2, A3, A4, A5, A6, A7, A8}
```

**Update Step:**
```
C1 = (2, 10) (không đổi vì chỉ có 1 điểm)

C2 = mean({A2, A3, A4, A5, A6, A7, A8})
   = ((2+8+5+7+6+1+4)/7, (5+4+8+5+4+2+9)/7)
   = (33/7, 37/7)
   = (4.71, 5.29)
```

**Iteration 2:**

**Assignment Step với C1=(2,10), C2=(4.71, 5.29):**
```
(Tính lại khoảng cách cho tất cả các điểm)
...
```

**Lặp lại cho đến khi hội tụ**

### 5. Bài 3: Sử dụng thuật toán k-means với khoảng cách Euclidean để phản cụm 7 điểm

**Đề bài:** A=(-2,5), B=(8,4), C=(-1,2), D=(-2,10), E=(7,5), F=(6,4), G=(0,0)

**Câu a)** Sử dụng thuật toán k-means (PAM) với khoảng cách Euclidean để phân cụm 7 điểm:
A=(-2,5), B=(8,4), C=(-1,2), D=(-2,10), E=(7,5), F=(6,4), G=(0,0) vào 2 cụm (mỗi lần lặp cân cú lần và mối điểm có tổng cùm chắc với mới điểm mà nó thuộc về, cụm mà mỗi điểm trở thành cù)

**Lời giải:**

**PAM (Partition Around Medoids) khác với K-Means:**
- K-Means: Centroid là điểm trung bình (có thể không thuộc dataset)
- PAM: Medoid là điểm thực tế trong dataset

**Iteration 1:**
```
Chọn 2 medoids ban đầu: A=(-2,5), B=(8,4)

Tính khoảng cách:
C: d(C,A) = √[(-1+2)²+(2-5)²] = √[1+9] = √10 = 3.16
   d(C,B) = √[(-1-8)²+(2-4)²] = √[81+4] = √85 = 9.22
   → Cluster A

D: d(D,A) = √[(-2+2)²+(10-5)²] = √25 = 5
   d(D,B) = √[(-2-8)²+(10-4)²] = √[100+36] = √136 = 11.66
   → Cluster A

E: d(E,A) = √[(7+2)²+(5-5)²] = √81 = 9
   d(E,B) = √[(7-8)²+(5-4)²] = √[1+1] = √2 = 1.41
   → Cluster B

F: d(F,A) = √[(6+2)²+(4-5)²] = √[64+1] = √65 = 8.06
   d(F,B) = √[(6-8)²+(4-4)²] = √4 = 2
   → Cluster B

G: d(G,A) = √[(-2-0)²+(5-0)²] = √[4+25] = √29 = 5.39
   d(G,B) = √[(8-0)²+(4-0)²] = √[64+16] = √80 = 8.94
   → Cluster A

Cluster A: {A, C, D, G}
Cluster B: {B, E, F}
```

**Update medoids:**
```
Tính tổng khoảng cách từ mỗi điểm đến các điểm khác trong cùng cluster
Chọn điểm có tổng khoảng cách nhỏ nhất làm medoid mới
```

### 6. Bài 4: Phân cụm gần cận

**Đề bài:** Tạo cây phân cấp (phân cụm gần phân cụm) sử dụng phương pháp Nearest Neighbor để ở khoảng cách Euclidean trên tập điểm:

A1=(2,10), A2=(2,5), A3=(8,4), A4=(5,8), A5=(7,5), A6=(6,4), A7=(1,2), A8=(4,9)

**Lời giải:**

**Hierarchical Clustering - Single Linkage (Nearest Neighbor):**

**Bước 1: Tính ma trận khoảng cách:**
```
      A1    A2    A3    A4    A5    A6    A7    A8
A1    0    5.0   8.5   3.6   7.1   7.2   8.1   2.2
A2    5.0   0    6.7   4.2   5.8   5.7   3.2   3.6
A3    8.5  6.7    0    5.0   1.4   2.0   7.3   6.4
A4    3.6  4.2   5.0    0    3.6   4.1   6.4   1.4
A5    7.1  5.8   1.4   3.6    0    1.4   6.7   4.5
A6    7.2  5.7   2.0   4.1   1.4    0    6.4   5.0
A7    8.1  3.2   7.3   6.4   6.7   6.4    0    5.8
A8    2.2  3.6   6.4   1.4   4.5   5.0   5.8    0
```

**Bước 2: Tìm cặp gần nhất:**
```
Min distance = 1.4 (nhiều cặp: A3-A5, A5-A6, A4-A8)
Chọn A3-A5 (hoặc bất kỳ)

Merge: {A3, A5}
```

**Bước 3: Cập nhật ma trận (Single Linkage - khoảng cách min):**
```
d({A3,A5}, A1) = min(d(A3,A1), d(A5,A1)) = min(8.5, 7.1) = 7.1
...
```

**Tiếp tục cho đến khi tất cả điểm thuộc 1 cluster**

**Dendrogram (cây phân cấp):**
```
Cắt ở độ cao phù hợp để có số clusters mong muốn
```

## IV. Hierarchical Clustering (Phân Cụm Phân Cấp)

### 1. Agglomerative (Bottom-up)

**Các bước:**
```
1. Mỗi điểm là 1 cluster
2. Repeat:
   - Merge 2 clusters gần nhất
3. Until: Chỉ còn 1 cluster
```

### 2. Divisive (Top-down)

**Các bước:**
```
1. Tất cả điểm trong 1 cluster
2. Repeat:
   - Tach cluster xa nhất thành 2
3. Until: Mỗi điểm là 1 cluster
```

### 3. Linkage Methods (Độ đo khoảng cách giữa clusters)

**Single Linkage (Nearest Neighbor):**
```
d(C1, C2) = min{d(x, y) | x ∈ C1, y ∈ C2}
```

**Complete Linkage (Farthest Neighbor):**
```
d(C1, C2) = max{d(x, y) | x ∈ C1, y ∈ C2}
```

**Average Linkage:**
```
d(C1, C2) = avg{d(x, y) | x ∈ C1, y ∈ C2}
```

**Centroid Linkage:**
```
d(C1, C2) = d(centroid(C1), centroid(C2))
```

## V. DBSCAN (Density-Based Spatial Clustering)

### 1. Khái Niệm

**Parameters:**
- **ε (epsilon)**: Bán kính vùng lân cận
- **MinPts**: Số điểm tối thiểu trong vùng lân cận

**Loại điểm:**
- **Core point**: Có ≥ MinPts điểm trong vùng ε
- **Border point**: Trong vùng ε của core point nhưng không phải core
- **Noise point**: Không thuộc 2 loại trên

### 2. Algorithm

```
1. For each unvisited point p:
   a) Mark p as visited
   b) Find neighbors N trong vùng ε
   c) If |N| < MinPts:
      - Mark p as noise (tạm thời)
   d) Else:
      - Create new cluster C
      - Expand cluster (DFS/BFS từ p)
```

### 3. Ưu điểm DBSCAN

- Không cần chỉ định số clusters trước
- Phát hiện clusters có hình dạng bất kỳ
- Phát hiện noise/outliers

## VI. Đánh Giá Clustering

### 1. Silhouette Score

**Cho mỗi điểm i:**
```
a(i) = khoảng cách trung bình đến các điểm trong cùng cluster
b(i) = khoảng cách trung bình nhỏ nhất đến các điểm ở cluster khác

s(i) = (b(i) - a(i)) / max(a(i), b(i))
```

**Silhouette Score:**
```
S = mean(s(i)) cho tất cả điểm
```

**Giá trị:**
- s(i) gần 1: Điểm được phân cụm tốt
- s(i) gần 0: Điểm nằm giữa 2 clusters
- s(i) < 0: Điểm có thể bị phân sai cluster

### 2. Within-Cluster Sum of Squares (WCSS)

**Công thức:**
```
WCSS = Σ Σ d(x, centroid_k)²
       k x∈Ck
```

**Dùng Elbow Method:**
- Vẽ đồ thị WCSS theo K
- Chọn K tại "khuỷu tay" (điểm cong)

### 3. Davies-Bouldin Index

**Công thức:**
```
DB = (1/K) × Σ max[( avg_dist(Ci) + avg_dist(Cj) ) / d(Ci, Cj)]
            i  j≠i
```

**Giá trị:** Càng thấp càng tốt

## VII. Tổng Kết

### So Sánh Các Thuật Toán

| Thuật toán | Ưu điểm | Nhược điểm | Complexity |
|------------|---------|------------|------------|
| K-Means | Nhanh, đơn giản | Cần chỉ định K, nhạy với outliers | O(nkt) |
| Hierarchical | Không cần K, visualization tốt | Chậm | O(n²logn) |
| DBSCAN | Phát hiện noise, không cần K | Nhạy với ε và MinPts | O(n logn) |

### Khi nào dùng thuật toán nào?

| Trường hợp | Thuật toán |
|------------|------------|
| Biết trước số clusters | K-Means |
| Cần dendrogram | Hierarchical |
| Clusters hình dạng phức tạp | DBSCAN |
| Dữ liệu có nhiều noise | DBSCAN |
| Dữ liệu lớn | K-Means (hoặc Mini-Batch K-Means) |

## VIII. Tài Liệu Tham Khảo

![Hình ảnh bài tập](images/Screenshot_20260126_233711.png)
