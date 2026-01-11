# PowerPoint Presentation Folder

## Contents
- `ppt_content.md` - Content for PowerPoint slides (from Part 2 of presentation_content.md)

## Slide Structure (20 slides total)

### Section 1: Introduction (Slides 1-4)
1. **Slide 1**: Title slide - "CẢI THIỆN APRIORI"
2. **Slide 2**: Table of Contents
3. **Slide 3**: Giới thiệu - Đặt vấn đề
4. **Slide 4**: Dataset: Groceries

### Section 2: Methodology (Slides 5-8)
5. **Slide 5**: Apriori Algorithm - Tổng quan
6. **Slide 6**: Các bước thuật toán
7. **Slide 7**: Các chỉ số đánh giá
8. **Slide 8**: Pipeline xử lý

### Section 3: Results (Slides 9-11)
9. **Slide 9**: Top frequent items
10. **Slide 10**: Association rules
11. **Slide 11**: So sánh hiệu suất cơ bản

### Section 4: Limitations (Slide 12)
12. **Slide 12**: Hạn chế của Apriori

### Section 5: Improvements (Slides 13-18)
13. **Slide 13**: Cải tiến 1: Sampling
14. **Slide 14**: Cải tiến 2: DHP (Hash-based)
15. **Slide 15**: Cải tiến 3: Transaction Reduction
16. **Slide 16**: Cải tiến 4: ECLAT (Vertical)
17. **Slide 17**: Cải tiến 5: DIC (Dynamic Counting)
18. **Slide 18**: Cải tiến 6: Partitioning

### Section 6: Recommendations (Slide 19)
19. **Slide 19**: Khuyến nghị sử dụng

### Section 7: Conclusion (Slide 20)
20. **Slide 20**: Kết luận

## Design Tips
- Each slide: Maximum 6 bullet points
- Font size: 24-32pt for headings, 18-24pt for content
- Use visuals (charts, diagrams) when possible
- Consistent color scheme
- Minimal animation

## To Generate PowerPoint
You can use pandoc to convert markdown to PowerPoint:
```bash
pandoc ppt_content.md -o presentation.pptx
```

Or manually create slides in PowerPoint using the content provided.
