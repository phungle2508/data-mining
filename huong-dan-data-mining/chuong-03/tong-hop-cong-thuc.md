# Tổng Hợp Công Thức - Chương 03: Luật Kết Hợp

## I. Các Độ Đo Cơ Bản

### 1. Support (Độ hỗ trợ)
```
Support(X) = count(X) / total_transactions

Support(X → Y) = Support(X ∪ Y)
```

**Ví dụ:** Với 10 giao dịch, 6 giao dịch chứa A
```
Support(A) = 6/10 = 0.6
```

### 2. Confidence (Độ tin cậy)
```
Confidence(X → Y) = Support(X ∪ Y) / Support(X)
```

**Ví dụ:** Support(A) = 0.6, Support(A,C) = 0.6
```
Confidence(A → C) = 0.6 / 0.6 = 1.0
```

### 3. Lift (Độ nâng)
```
Lift(X → Y) = Confidence(X → Y) / Support(Y)
            = Support(X ∪ Y) / (Support(X) × Support(Y))
```

**Giải thích:**
- Lift > 1: X và Y có tương quan dương (xuất hiện cùng nhau)
- Lift = 1: X và Y độc lập
- Lift < 1: X và Y có tương quan âm

**Ví dụ:** Support(A,C) = 0.6, Support(A) = 0.6, Support(C) = 0.8
```
Lift(A → C) = 0.6 / (0.6 × 0.8) = 0.6 / 0.48 = 1.25
```

### 4. Conviction
```
Conviction(X → Y) = (1 - Support(Y)) / (1 - Confidence(X → Y))
```

**Ví dụ:** Confidence(A → C) = 1.0, Support(C) = 0.8
```
Conviction(A → C) = (1 - 0.8) / (1 - 1.0) = 0.2 / 0 = ∞
```

### 5. Leverage
```
Leverage(X → Y) = Support(X ∪ Y) - Support(X) × Support(Y)
```

**Ví dụ:**
```
Leverage(A → C) = 0.6 - (0.6 × 0.8) = 0.6 - 0.48 = 0.12
```

---

## II. Thuật Toán Apriori

### Nguyên Lý Apriori
```
Nếu một itemset là frequent (phổ biến),
thì tất cả các subset của nó cũng phải frequent.

Ngược lại: Nếu một itemset không frequent,
thì tất cả superset của nó cũng không frequent.
```

### Các Bước

**Bước 1: Tìm L₁ (frequent 1-itemsets)**
```
- Scan database, đếm support của từng item
- L₁ = {items có support ≥ min_sup}
```

**Bước 2: Sinh Candidates Cₖ**
```
Join step: Kết hợp (k-1)-itemsets từ Lₖ₋₁
Prune step: Loại bỏ candidates có subset không frequent
```

**Bước 3: Tính Support và Lọc**
```
- Scan database, tính support cho candidates
- Lₖ = {c ∈ Cₖ | support(c) ≥ min_sup}
```

**Bước 4: Lặp lại cho đến khi không còn frequent itemsets mới**

### Ví Dụ

**Dataset:** 10 giao dịch, min_sup = 0.3 (≥ 3 giao dịch)

**Iteration 1:**
```
Item | Count | Frequent?
-----|-------|----------
A    | 6     | ✓
B    | 4     | ✓
C    | 8     | ✓
D    | 6     | ✓
E    | 4     | ✓

L₁ = {{A}, {B}, {C}, {D}, {E}}
```

**Iteration 2:**
```
Join L₁ with L₁ → C₂ = {{A,B}, {A,C}, {A,D}, ...}

Scan và đếm:
{A,C}: 6 ✓
{A,D}: 4 ✓
{B,C}: 3 ✓
{C,D}: 5 ✓
{C,E}: 3 ✓
{D,E}: 3 ✓

L₂ = {{A,C}, {A,D}, {B,C}, {C,D}, {C,E}, {D,E}}
```

---

## III. Thuật Toán FP-Growth

### Các Bước

**Bước 1: Tạo Header Table**
```
1. Scan database lần 1, đếm support
2. Loại bỏ items có support < min_sup
3. Sắp xếp theo support giảm dần
```

**Bước 2: Xây dựng FP-Tree**
```
1. Scan database lần 2
2. Với mỗi transaction:
   - Sắp xếp items theo thứ tự header table
   - Chèn vào FP-Tree
   - Cập nhật node-links
```

**Bước 3: Mining FP-Tree**
```
Với mỗi item (từ dưới lên):
1. Tạo conditional pattern base
2. Tạo conditional FP-tree
3. Đệ quy tìm frequent itemsets
```

### Ví Dụ

**Header Table:**
```
Item | Count
-----|------
X    | 9
Y    | 8
Z    | 7
T    | 5
```

**FP-Tree:**
```
       root
      /    \
    X:8   Y:1
    |      |
   Y:7    Z:1
  / \      |
Z:5  T:2  T:1
|
T:1
```

---

## IV. Thuật Toán ECLAT

### Nguyên Lý

Sử dụng vertical data format (TID list) thay vì horizontal

**Horizontal format:**
```
TID | Items
----|-------
1   | A, C
2   | A, B, C
```

**Vertical format:**
```
Item | TID list
-----|----------
A    | {1, 2}
B    | {2}
C    | {1, 2}
```

### Tính Support bằng Intersection

```
Support({A, C}) = |TID(A) ∩ TID(C)| / total_transactions
                = |{1, 2} ∩ {1, 2}| / 2
                = 2 / 2 = 1.0
```

---

## V. Sinh Luật Kết Hợp

### Từ Frequent Itemset

**Với mỗi frequent itemset X:**
```
1. Sinh tất cả non-empty subsets s của X
2. Với mỗi subset s:
   - Tạo luật: s → (X - s)
   - Tính confidence = support(X) / support(s)
   - Nếu confidence ≥ min_conf → chấp nhận luật
```

**Ví dụ:** Từ {A, C, D} với support = 0.3
```
Subsets:
{A} → {C,D}: conf = 0.3 / 0.6 = 0.5
{C} → {A,D}: conf = 0.3 / 0.8 = 0.375
{D} → {A,C}: conf = 0.3 / 0.6 = 0.5
{A,C} → {D}: conf = 0.3 / 0.6 = 0.5
{A,D} → {C}: conf = 0.3 / 0.4 = 0.75 ✓
{C,D} → {A}: conf = 0.3 / 0.5 = 0.6 ✓

Với min_conf = 0.6:
Luật được chấp nhận:
- {A,D} → {C} (conf = 0.75)
- {C,D} → {A} (conf = 0.6)
```

---

## VI. Bảng Tra Công Thức Nhanh

| Độ đo | Công thức | Ý nghĩa |
|-------|-----------|---------|
| Support(X) | `count(X) / total` | Tần suất xuất hiện của X |
| Support(X→Y) | `Support(X∪Y)` | Tần suất xuất hiện cùng nhau |
| Confidence(X→Y) | `Support(X∪Y) / Support(X)` | Xác suất Y khi có X |
| Lift(X→Y) | `Confidence(X→Y) / Support(Y)` | Mức độ tương quan |
| Conviction(X→Y) | `(1-Support(Y)) / (1-Confidence(X→Y))` | Độ phụ thuộc |
| Leverage(X→Y) | `Support(X∪Y) - Support(X)×Support(Y)` | Độ lệch so với độc lập |

---

## VII. So Sánh Thuật Toán

| Tiêu chí | Apriori | FP-Growth | ECLAT |
|----------|---------|-----------|-------|
| Số lần scan DB | Nhiều (k+1) | 2 lần | 1 lần |
| Sinh candidates | Có | Không | Không |
| Bộ nhớ | Ít | Nhiều (FP-Tree) | Trung bình |
| Tốc độ | Chậm | Nhanh | Trung bình |
| Phù hợp | DB nhỏ, sparse | DB lớn, dense | DB sparse |
