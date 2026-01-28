# Tổng Hợp Công Thức - Chương 05: Phân Cụm (Clustering)

## I. Độ Đo Khoảng Cách (Distance Metrics)

### 1. Euclidean Distance

**Công thức:**
```
d(x, y) = √[Σ(xᵢ - yᵢ)²]
```

**Ví dụ:** A=(2,10), B=(5,4)
```
d(A, B) = √[(2-5)² + (10-4)²]
        = √[9 + 36]
        = √45
        = 6.71
```

### 2. Manhattan Distance

**Công thức:**
```
d(x, y) = Σ|xᵢ - yᵢ|
```

**Ví dụ:** A=(2,10), B=(5,4)
```
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

**Ví dụ với p=3:** A=(2,10), B=(5,4)
```
d(A, B) = (|2-5|³ + |10-4|³)^(1/3)
        = (3³ + 6³)^(1/3)
        = (27 + 216)^(1/3)
        = 243^(1/3)
        = 6.24
```

### 4. Cosine Similarity

**Công thức:**
```
similarity = cos(θ) = (A · B) / (||A|| × ||B||)
                    = Σ(Aᵢ × Bᵢ) / (√Σ(Aᵢ²) × √Σ(Bᵢ²))
```

**Cosine Distance:**
```
distance = 1 - similarity
```

**Ví dụ:** A=(1,2,3), B=(2,3,4)
```
A · B = 1×2 + 2×3 + 3×4 = 2 + 6 + 12 = 20
||A|| = √(1² + 2² + 3²) = √14 = 3.74
||B|| = √(2² + 3² + 4²) = √29 = 5.39

similarity = 20 / (3.74 × 5.39) = 20 / 20.16 = 0.992
distance = 1 - 0.992 = 0.008
```

### 5. Jaccard Similarity

**Công thức (cho tập hợp):**
```
Jaccard(A, B) = |A ∩ B| / |A ∪ B|
```

**Ví dụ:** A={1,2,3,4}, B={3,4,5,6}
```
A ∩ B = {3, 4} → |A ∩ B| = 2
A ∪ B = {1, 2, 3, 4, 5, 6} → |A ∪ B| = 6

Jaccard(A, B) = 2/6 = 0.333
```

---

## II. K-Means Clustering

### 1. Algorithm

**Input:**
- K: Số lượng cụm
- Dataset: Tập dữ liệu cần phân cụm

**Các bước:**
```
1. Khởi tạo: Chọn K centroids ngẫu nhiên

2. Repeat:
   a) Assignment step: Gán mỗi điểm vào cụm có centroid gần nhất
   b) Update step: Cập nhật centroid = trung bình các điểm trong cụm

3. Until: Centroids không thay đổi hoặc đạt số iteration tối đa
```

### 2. Assignment Step

**Công thức:**
```
For each point x:
  cluster(x) = argmin d(x, centroid_k)
               k
```

**Ví dụ:** Điểm A=(2,5), C1=(2,10), C2=(5,8)
```
d(A, C1) = √[(2-2)² + (5-10)²] = √25 = 5
d(A, C2) = √[(2-5)² + (5-8)²] = √18 = 4.24

→ A thuộc Cluster 2 (vì 4.24 < 5)
```

### 3. Update Step

**Công thức:**
```
For each cluster k:
  centroid_k = mean(points in cluster k)
             = (Σ xᵢ / n, Σ yᵢ / n)
```

**Ví dụ:** Cluster có {A2, A3, A4} = {(2,5), (8,4), (5,8)}
```
centroid = ((2+8+5)/3, (5+4+8)/3)
         = (15/3, 17/3)
         = (5, 5.67)
```

### 4. Ví Dụ Đầy Đủ

**Dataset:** A1=(2,10), A2=(2,5), A3=(8,4), A4=(5,8), K=2

**Iteration 1:**
```
Khởi tạo: C1=(2,10), C2=(5,8)

Assignment:
A1: d(A1,C1)=0, d(A1,C2)=3.6 → Cluster 1
A2: d(A2,C1)=5, d(A2,C2)=4.24 → Cluster 2
A3: d(A3,C1)=8.49, d(A3,C2)=5 → Cluster 2
A4: d(A4,C1)=3.6, d(A4,C2)=0 → Cluster 2

Cluster 1: {A1}
Cluster 2: {A2, A3, A4}

Update:
C1 = (2, 10)
C2 = ((2+8+5)/3, (5+4+8)/3) = (5, 5.67)
```

**Iteration 2:**
```
(Lặp lại với C1=(2,10), C2=(5,5.67) cho đến hội tụ)
```

---

## III. Hierarchical Clustering

### 1. Linkage Methods

**Single Linkage (Nearest Neighbor):**
```
d(C1, C2) = min{d(x, y) | x ∈ C1, y ∈ C2}
```

**Ví dụ:** C1={A,B}, C2={C,D}
```
d(C1, C2) = min{d(A,C), d(A,D), d(B,C), d(B,D)}
```

**Complete Linkage (Farthest Neighbor):**
```
d(C1, C2) = max{d(x, y) | x ∈ C1, y ∈ C2}
```

**Average Linkage:**
```
d(C1, C2) = avg{d(x, y) | x ∈ C1, y ∈ C2}
          = Σ Σ d(x, y) / (|C1| × |C2|)
```

**Centroid Linkage:**
```
d(C1, C2) = d(centroid(C1), centroid(C2))
```

### 2. Agglomerative (Bottom-up)

**Các bước:**
```
1. Mỗi điểm là 1 cluster
2. Repeat:
   - Merge 2 clusters gần nhất
3. Until: Chỉ còn 1 cluster
```

**Ví dụ:** 4 điểm A, B, C, D

**Ma trận khoảng cách:**
```
     A    B    C    D
A    0   2.0  5.0  8.0
B   2.0   0   4.0  7.0
C   5.0  4.0   0   3.0
D   8.0  7.0  3.0   0
```

**Iteration 1:**
```
Min distance = 2.0 (A-B)
Merge: {A, B}
Clusters: {A,B}, {C}, {D}
```

**Iteration 2 (Single Linkage):**
```
d({A,B}, C) = min(d(A,C), d(B,C)) = min(5.0, 4.0) = 4.0
d({A,B}, D) = min(d(A,D), d(B,D)) = min(8.0, 7.0) = 7.0
d(C, D) = 3.0

Min distance = 3.0 (C-D)
Merge: {C, D}
Clusters: {A,B}, {C,D}
```

---

## IV. DBSCAN

### 1. Parameters

- **ε (epsilon)**: Bán kính vùng lân cận
- **MinPts**: Số điểm tối thiểu trong vùng lân cận

### 2. Loại Điểm

**Core point:**
```
Điểm p là core point nếu:
|N_ε(p)| ≥ MinPts

Trong đó N_ε(p) = {q | d(p,q) ≤ ε}
```

**Border point:**
- Trong vùng ε của core point
- Nhưng không phải core point

**Noise point:**
- Không thuộc 2 loại trên

### 3. Ví Dụ

**Dataset:** 5 điểm, ε=3, MinPts=2

**Tính số neighbors:**
```
A: neighbors trong ε=3 → {B, C} → |N|=2 ≥ MinPts → Core
B: neighbors → {A} → |N|=1 < MinPts → Border (trong vùng của A)
C: neighbors → {A} → |N|=1 < MinPts → Border (trong vùng của A)
D: neighbors → {} → |N|=0 < MinPts → Noise
E: neighbors → {} → |N|=0 < MinPts → Noise
```

**Kết quả:**
```
Cluster 1: {A, B, C}
Noise: {D, E}
```

---

## V. Đánh Giá Clustering

### 1. Silhouette Score

**Cho mỗi điểm i:**
```
a(i) = khoảng cách trung bình đến các điểm trong cùng cluster
b(i) = khoảng cách trung bình nhỏ nhất đến các điểm ở cluster khác

s(i) = (b(i) - a(i)) / max(a(i), b(i))
```

**Silhouette Score tổng thể:**
```
S = mean(s(i)) cho tất cả điểm
```

**Giá trị:**
- s(i) gần 1: Điểm được phân cụm tốt
- s(i) gần 0: Điểm nằm giữa 2 clusters
- s(i) < 0: Điểm có thể bị phân sai cluster

**Ví dụ:** Điểm A trong Cluster 1
```
a(A) = mean(d(A, B), d(A, C)) = (2 + 3)/2 = 2.5
b(A) = mean(d(A, D), d(A, E)) = (8 + 9)/2 = 8.5

s(A) = (8.5 - 2.5) / max(2.5, 8.5)
     = 6 / 8.5
     = 0.706
```

### 2. Within-Cluster Sum of Squares (WCSS)

**Công thức:**
```
WCSS = Σ Σ d(x, centroid_k)²
       k x∈Ck
```

**Ví dụ:** 2 clusters
```
Cluster 1: {A, B}, centroid C1
Cluster 2: {C, D}, centroid C2

WCSS = [d(A,C1)² + d(B,C1)²] + [d(C,C2)² + d(D,C2)²]
```

**Elbow Method:**
- Vẽ đồ thị WCSS theo K
- Chọn K tại "khuỷu tay" (điểm cong)

### 3. Davies-Bouldin Index

**Công thức:**
```
DB = (1/K) × Σ max[(avg_dist(Ci) + avg_dist(Cj)) / d(Ci, Cj)]
            i  j≠i
```

**Giá trị:** Càng thấp càng tốt

---

## VI. Bảng Tra Công Thức Nhanh

| Độ đo | Công thức | Ghi chú |
|-------|-----------|---------|
| Euclidean | `√[Σ(xᵢ-yᵢ)²]` | Khoảng cách thẳng |
| Manhattan | `Σ\|xᵢ-yᵢ\|` | Khoảng cách khối |
| Minkowski | `(Σ\|xᵢ-yᵢ\|ᵖ)^(1/p)` | Tổng quát |
| Cosine | `(A·B)/(\\|A\\|×\\|B\\|)` | Độ tương tự góc |
| Jaccard | `\|A∩B\|/\|A∪B\|` | Cho tập hợp |
| Centroid | `Σxᵢ/n` | Trung tâm cụm |
| Single Link | `min{d(x,y)}` | Nearest neighbor |
| Complete Link | `max{d(x,y)}` | Farthest neighbor |
| Average Link | `avg{d(x,y)}` | Trung bình |
| Silhouette | `(b-a)/max(a,b)` | Đánh giá clustering |
| WCSS | `ΣΣd(x,c)²` | Tổng bình phương |

---

## VII. So Sánh Thuật Toán

| Thuật toán | Ưu điểm | Nhược điểm | Complexity | Khi nào dùng |
|------------|---------|------------|------------|--------------|
| K-Means | Nhanh, đơn giản | Cần K, nhạy outliers | O(nkt) | Biết trước K, clusters tròn |
| Hierarchical | Không cần K, dendrogram | Chậm | O(n²logn) | Cần phân cấp, dữ liệu nhỏ |
| DBSCAN | Phát hiện noise, không cần K | Nhạy ε, MinPts | O(n logn) | Clusters phức tạp, có noise |
| PAM | Robust với outliers | Chậm hơn K-Means | O(k(n-k)²) | Cần medoids thực tế |

---

## VIII. Ví Dụ Tổng Hợp

### Ví dụ K-Means đầy đủ

**Dataset:** A=(2,10), B=(2,5), C=(8,4), D=(5,8), K=2

**Iteration 1:**
```
Init: C1=(2,10), C2=(5,8)

Distances:
A: d(A,C1)=0, d(A,C2)=3.6 → Cluster 1
B: d(B,C1)=5, d(B,C2)=4.24 → Cluster 2
C: d(C,C1)=8.49, d(C,C2)=5 → Cluster 2
D: d(D,C1)=3.6, d(D,C2)=0 → Cluster 2

Clusters:
Cluster 1: {A}
Cluster 2: {B, C, D}

Update:
C1 = (2, 10)
C2 = ((2+8+5)/3, (5+4+8)/3) = (5, 5.67)
```

**Iteration 2:**
```
Distances với C1=(2,10), C2=(5,5.67):
A: d(A,C1)=0, d(A,C2)=5.09 → Cluster 1
B: d(B,C1)=5, d(B,C2)=3.07 → Cluster 2
C: d(C,C1)=8.49, d(C,C2)=3.14 → Cluster 2
D: d(D,C1)=3.6, d(D,C2)=2.36 → Cluster 2

Clusters không đổi → Hội tụ
```

**Kết quả cuối cùng:**
```
Cluster 1: {A}
Cluster 2: {B, C, D}
```
