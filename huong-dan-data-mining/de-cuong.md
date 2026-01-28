# Đề Cương Ôn Tập Data Mining Chi Tiết

Tài liệu này tổng hợp lý thuyết cốt lõi và hướng dẫn giải chi tiết các dạng bài tập, bao gồm các trường hợp đặc biệt và ví dụ cụ thể.

---

## 📚 Tài Liệu Tham Khảo

Mỗi chương có 2 file chính:
- **`huong-dan-chuong-XX.md`**: Lý thuyết chi tiết, ví dụ và bài tập có lời giải
- **`tong-hop-cong-thuc.md`**: Tổng hợp công thức nhanh với ví dụ minh họa

---

## 📘 Chương 02: Tiền Xử Lý Dữ Liệu (Data Preprocessing)

### 📖 File tham khảo:
- [Hướng dẫn chi tiết](chuong-02/huong-dan-chuong-02.md)
- [Tổng hợp công thức](chuong-02/tong-hop-cong-thuc.md)

### 1. Thống Kê Mô Tả (Descriptive Statistics)
Cho tập dữ liệu $X = \{x_1, x_2, ..., x_n\}$ đã được sắp xếp tăng dần.

*   **Mean (Trung bình):**
    $$\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$$

*   **Median (Trung vị):** Giá trị nằm giữa tập dữ liệu.
    *   **Trường hợp $n$ lẻ:** Median là phần tử ở vị trí thứ $(n+1)/2$.
        $$Median = x_{(n+1)/2}$$
    *   **Trường hợp $n$ chẵn:** Median là trung bình cộng của 2 phần tử ở giữa (vị trí $n/2$ và $n/2 + 1$).
        $$Median = \frac{x_{n/2} + x_{n/2 + 1}}{2}$$

*   **Mode (Yếu vị):** Giá trị xuất hiện nhiều lần nhất trong tập dữ liệu.
    *   Nếu có nhiều giá trị cùng tần suất cao nhất $\rightarrow$ Tập dữ liệu đa yếu vị (Multimodal).

*   **Quartiles (Tứ phân vị):** Chia dữ liệu thành 4 phần bằng nhau.
    *   **Q2 (Median):** Tính như trên.
    *   **Q1 (Tứ phân vị thứ nhất):** Median của nửa đầu dữ liệu (các giá trị nhỏ hơn Q2).
    *   **Q3 (Tứ phân vị thứ ba):** Median của nửa sau dữ liệu (các giá trị lớn hơn Q2).
    *   *Lưu ý:* Khi tính Q1, Q3, nếu $n$ lẻ, thường không bao gồm Q2 vào nửa đầu/nửa sau.

*   **Standard Deviation (Độ lệch chuẩn):**
    $$\sigma = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n}}$$

### 2. Trực Quan Hóa & Outliers (Boxplot)
*   **IQR (Interquartile Range):** Khoảng trải giữa.
    $$IQR = Q3 - Q1$$
*   **Xác định Outliers (Ngoại lệ):**
    *   **Biên dưới (Lower Fence):** $LF = Q1 - 1.5 \times IQR$
    *   **Biên trên (Upper Fence):** $UF = Q3 + 1.5 \times IQR$
    *   Bất kỳ giá trị nào $< LF$ hoặc $> UF$ đều là Outlier.

### 3. Làm Mịn Dữ Liệu (Data Smoothing) - Binning
**Phương pháp Bin Means (Trung bình Bin):**
1.  **Sắp xếp** dữ liệu tăng dần.
2.  **Phân chia (Partition):** Chia dữ liệu vào các bin (thùng).
    *   *Equal-depth (frequency):* Mỗi bin có số lượng phần tử bằng nhau. (Thường dùng).
    *   *Equal-width:* Khoảng giá trị mỗi bin bằng nhau.
3.  **Làm mịn:** Thay thế TẤT CẢ giá trị trong mỗi bin bằng giá trị TRUNG BÌNH của bin đó.

### 4. Chuẩn Hóa Dữ Liệu (Normalization)

*   **Min-Max Normalization:** Đưa giá trị $v$ về khoảng $[new\_min, new\_max]$ (thường là $[0, 1]$).
    $$v' = \frac{v - min_{old}}{max_{old} - min_{old}} \times (new\_max - new\_min) + new\_min$$
    *   *Ví dụ:* $v=35, min=13, max=70$, đưa về $[0, 1]$.
        $$v' = \frac{35 - 13}{70 - 13} \times (1 - 0) + 0 = \frac{22}{57} \approx 0.386$$

*   **Z-Score Normalization:** Dùng khi không biết rõ min/max hoặc có outliers.
    $$v' = \frac{v - \mu}{\sigma}$$
    *   $\mu$: Trung bình.
    *   $\sigma$: Độ lệch chuẩn.
    *   *Biến thể (Dùng Mean Absolute Deviation - MAD):* $v' = \frac{v - \mu}{MAD}$ với $MAD = \frac{1}{n}\sum |x_i - \bar{x}|$.

*   **Decimal Scaling:** Di chuyển dấu phẩy động.
    $$v' = \frac{v}{10^j}$$
    *   $j$ là số nguyên nhỏ nhất sao cho giá trị tuyệt đối lớn nhất của tập dữ liệu sau khi chia nhỏ hơn 1 ($|v'| < 1$).
    *   *Ví dụ:* Tập dữ liệu có giá trị lớn nhất là 980 $\rightarrow$ Chia cho 1000 ($j=3$) $\rightarrow 0.98$.

---

## 📙 Chương 03: Luật Kết Hợp (Association Rules)

### 📖 File tham khảo:
- [Hướng dẫn chi tiết](chuong-03/huong-dan-chuong-03.md)
- [Tổng hợp công thức](chuong-03/tong-hop-cong-thuc.md)

### 1. Các Độ Đo Cơ Bản

*   **Support (Độ hỗ trợ):**
    $$Support(X) = \frac{count(X)}{total\_transactions}$$
    $$Support(X \rightarrow Y) = Support(X \cup Y)$$

*   **Confidence (Độ tin cậy):**
    $$Confidence(X \rightarrow Y) = \frac{Support(X \cup Y)}{Support(X)}$$

*   **Lift (Độ nâng):**
    $$Lift(X \rightarrow Y) = \frac{Confidence(X \rightarrow Y)}{Support(Y)}$$
    *   Lift > 1: Tương quan dương
    *   Lift = 1: Độc lập
    *   Lift < 1: Tương quan âm

### 2. Thuật Toán Apriori (Chi tiết Join & Prune)
Tìm tập phổ biến với $min\_sup$.
*   **Bước Join ($L_{k-1} \bowtie L_{k-1}$):**
    *   Kết hợp hai tập mục trong $L_{k-1}$ nếu chúng giống nhau ở $k-2$ phần tử đầu tiên.
    *   *Ví dụ:* $L_2 = \{ \{A, B\}, \{A, C\}, \{A, E\}, \{B, C\} \}$
        *   Join $\{A, B\}$ và $\{A, C\} \rightarrow \{A, B, C\}$ (Candidate $C_3$).
        *   Join $\{A, B\}$ và $\{A, E\} \rightarrow \{A, B, E\}$.
*   **Bước Prune (Cắt tỉa):**
    *   Với mỗi candidate $c \in C_k$, kiểm tra TẤT CẢ tập con kích thước $k-1$ của nó.
    *   Nếu có bất kỳ tập con nào **không thuộc** $L_{k-1}$, loại bỏ $c$.
    *   *Ví dụ:* Xét $C_3 = \{A, B, C\}$. Các tập con là $\{A, B\}, \{A, C\}, \{B, C\}$. Nếu $\{B, C\}$ không có trong $L_2$, thì loại bỏ $\{A, B, C\}$.

### 3. Thuật Toán FP-Growth (Cấu trúc Cây)
*   **Header Table:** Bảng chứa các item phổ biến (đã sắp xếp giảm dần theo support) và con trỏ đến node đầu tiên của item đó trong cây.
*   **Node-Links:** Các liên kết nối các node cùng tên (cùng item) trên cây để duyệt nhanh khi tính support.
*   **Conditional Pattern Base:** Tập hợp các "con đường" từ gốc đến item đang xét (không bao gồm item đó).
*   **Conditional FP-Tree:** Cây con được xây dựng từ Conditional Pattern Base. Nếu cây này chỉ có 1 đường dẫn đơn, ta tổ hợp các node trên đường dẫn để ra tập phổ biến.

---

## 📗 Chương 04: Phân Loại (Classification)

### 📖 File tham khảo:
- [Hướng dẫn chi tiết](chuong-04/huong-dan-chuong-04.md)
- [Tổng hợp công thức](chuong-04/tong-hop-cong-thuc.md)

### 1. Naive Bayes & Laplace Smoothing
*   **Định lý Bayes:**
    $$P(C|X) = \frac{P(X|C) \times P(C)}{P(X)}$$

*   **Naive Bayes (giả định độc lập):**
    $$P(C|X_1, X_2, ..., X_n) \propto P(C) \times \prod_{i=1}^{n} P(X_i|C)$$

*   **Vấn đề:** Nếu một giá trị thuộc tính chưa từng xuất hiện trong lớp $C$ trong tập huấn luyện, $P(x_i | C) = 0$, dẫn đến xác suất hậu nghiệm bằng 0.

*   **Khắc phục (Laplace Correction):**
    $$P(x_i | C) = \frac{Count(x_i, C) + 1}{Count(C) + |V|}$$
    *   $|V|$: Số lượng giá trị phân biệt của thuộc tính $x$ (Vocabulary size).
    *   *Ví dụ:* Thuộc tính "Màu sắc" có $\{Đỏ, Xanh, Vàng\} \rightarrow |V|=3$. Nếu lớp "Yes" có 5 mẫu, trong đó không có mẫu nào màu Đỏ:
        $$P(\text{Đỏ} | \text{Yes}) = \frac{0 + 1}{5 + 3} = \frac{1}{8}$$

### 2. Decision Tree - Entropy & Gain
Cho tập $S$ có $p$ mẫu Positive (+) và $n$ mẫu Negative (-). Tổng số mẫu $N = p + n$.
*   **Entropy của tập $S$:** Độ đo sự không chắc chắn.
    $$Entropy(S) = - \frac{p}{N} \log_2 \left(\frac{p}{N}\right) - \frac{n}{N} \log_2 \left(\frac{n}{N}\right)$$
    *   *Lưu ý:* Nếu $p=0$ hoặc $n=0$, Entropy = 0 (Hoàn toàn thuần nhất). Nếu $p=n$, Entropy = 1 (Hỗn loạn nhất).
*   **Entropy sau khi chia theo thuộc tính A:**
    $$Entropy_A(S) = \sum_{v \in Values(A)} \frac{|S_v|}{|S|} \times Entropy(S_v)$$
*   **Information Gain:** Mức độ giảm Entropy.
    $$Gain(S, A) = Entropy(S) - Entropy_A(S)$$
*   **Gain Ratio (C4.5):**
    $$GainRatio(S, A) = \frac{Gain(S, A)}{SplitInfo(S, A)}$$
*   **Gini Index (CART):**
    $$Gini(S) = 1 - \sum p_i^2$$

### 3. Đánh Giá Mô Hình (Confusion Matrix)
Trong bài toán phát hiện bệnh (Bệnh = Positive, Không bệnh = Negative):
*   **Accuracy (Độ chính xác tổng thể):**
    $$Accuracy = \frac{TP + TN}{TP + TN + FP + FN}$$
*   **Precision (Độ chính xác của dự báo dương):** Trong các ca máy đoán là Bệnh, bao nhiêu ca thực sự Bệnh?
    $$Precision = \frac{TP}{TP + FP}$$
*   **Recall / Sensitivity (Độ nhạy):** Trong các ca thực sự Bệnh, máy phát hiện được bao nhiêu?
    $$Recall = \frac{TP}{TP + FN}$$
*   **F1-Score:** Cân bằng giữa Precision và Recall.
    $$F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}$$

---

## 📕 Chương 05: Phân Cụm (Clustering)

### 📖 File tham khảo:
- [Hướng dẫn chi tiết](chuong-05/huong-dan-chuong-05.md)
- [Tổng hợp công thức](chuong-05/tong-hop-cong-thuc.md)

### 1. Khoảng Cách (Distance Metrics)
Cho 2 điểm $A(x_1, y_1)$ và $B(x_2, y_2)$:
*   **Euclidean:** $d = \sqrt{(x_1-x_2)^2 + (y_1-y_2)^2}$
*   **Manhattan:** $d = |x_1-x_2| + |y_1-y_2|$
*   **Minkowski:** $d = (\sum|x_i - y_i|^p)^{1/p}$
*   **Cosine Similarity:** $sim = \frac{A \cdot B}{||A|| \times ||B||}$

### 2. K-Means (Cập nhật trọng tâm)
*   **Bước Assignment:** Gán điểm $X_i$ vào cụm $k$ nếu $d(X_i, C_k)$ là nhỏ nhất.
*   **Bước Update Centroid:** Tính lại tọa độ tâm cụm $C_k$ mới bằng trung bình cộng tọa độ các điểm thuộc cụm đó.
    $$C_k^{new} = \left( \frac{\sum x}{m}, \frac{\sum y}{m} \right)$$
    *   $m$: Số lượng điểm trong cụm $k$.

### 3. Hierarchical Clustering (Cập nhật ma trận khoảng cách)
Khi gộp 2 cụm $U$ và $V$ thành cụm mới $(UV)$, khoảng cách từ $(UV)$ đến cụm $W$ bất kỳ được tính lại:
*   **Single Linkage (Min):** $d((UV), W) = \min \{ d(U, W), d(V, W) \}$
*   **Complete Linkage (Max):** $d((UV), W) = \max \{ d(U, W), d(V, W) \}$
*   **Average Linkage:** Trung bình khoảng cách các điểm.

### 4. DBSCAN (Mật độ)
*   **Core Point (Điểm lõi):** Có ít nhất $MinPts$ điểm trong bán kính $\epsilon$.
*   **Border Point (Điểm biên):** Nằm trong bán kính $\epsilon$ của Core Point nhưng không đủ $MinPts$.
*   **Noise Point (Điểm nhiễu):** Không phải Core cũng không phải Border.

### 5. Đánh Giá Clustering
*   **Silhouette Score:**
    $$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$$
    *   $a(i)$: Khoảng cách trung bình trong cùng cluster
    *   $b(i)$: Khoảng cách trung bình nhỏ nhất đến cluster khác
*   **WCSS (Within-Cluster Sum of Squares):**
    $$WCSS = \sum_k \sum_{x \in C_k} d(x, centroid_k)^2$$

---

## 📌 Lưu Ý Quan Trọng

### Khi Làm Bài Tập:
1. **Đọc kỹ đề bài** - Xác định rõ yêu cầu
2. **Xác định phương pháp** - Chọn thuật toán/công thức phù hợp
3. **Tính toán cẩn thận** - Kiểm tra từng bước
4. **Trình bày rõ ràng** - Ghi rõ công thức và kết quả trung gian

### Các Lỗi Thường Gặp:
- **Chương 2:** Quên sắp xếp dữ liệu trước khi tính quartiles
- **Chương 3:** Không kiểm tra đủ tất cả subsets khi prune
- **Chương 4:** Quên áp dụng Laplace smoothing khi có xác suất = 0
- **Chương 5:** Tính sai khoảng cách hoặc không cập nhật centroid đúng

---

## 🎯 Checklist Ôn Tập

### Chương 02:
- [ ] Tính được Mean, Median, Mode, Quartiles, Std
- [ ] Xác định outliers bằng Boxplot
- [ ] Áp dụng 3 phương pháp chuẩn hóa (Min-Max, Z-Score, Decimal Scaling)
- [ ] Làm mịn dữ liệu bằng Binning

### Chương 03:
- [ ] Tính Support, Confidence, Lift
- [ ] Chạy thuật toán Apriori (Join & Prune)
- [ ] Xây dựng FP-Tree
- [ ] Sinh luật kết hợp từ frequent itemsets

### Chương 04:
- [ ] Áp dụng Naive Bayes với Laplace Smoothing
- [ ] Tính Entropy, Information Gain, Gain Ratio
- [ ] Xây dựng Decision Tree
- [ ] Tính Accuracy, Precision, Recall, F1-Score

### Chương 05:
- [ ] Tính các khoảng cách (Euclidean, Manhattan, Cosine)
- [ ] Chạy thuật toán K-Means
- [ ] Xây dựng Hierarchical Clustering (Dendrogram)
- [ ] Áp dụng DBSCAN
- [ ] Đánh giá clustering (Silhouette, WCSS)
