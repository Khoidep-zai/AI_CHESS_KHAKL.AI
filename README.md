# ♟️ Chess Game AI

---

## 📑 Mục lục
- [1. Tổng quan cấu trúc thư mục](#1-tổng-quan-cấu-trúc-thư-mục)
- [2. Sơ đồ kiến trúc & luồng hoạt động](#2-sơ-đồ-kiến-trúc--luồng-hoạt-động)
- [3. Giải thích từng file & các hàm chính](#3-giải-thích-từng-file--các-hàm-chính)
  - [3.1. src/ - Mã nguồn chính](#31-src---mã-nguồn-chính)
  - [3.2. face_pixel/ - Demo vẽ khuôn mặt pixel](#32-face_pixel---demo-vẽ-khuôn-mặt-pixel)
  - [3.3. images/ - Ảnh quân cờ & giao diện](#33-images---ảnh-quân-cờ--giao-diện)
- [4. Hướng dẫn cài đặt & chạy](#4-hướng-dẫn-cài-đặt--chạy)
- [5. Giải thích chi tiết thuật toán AI](#5-giải-thích-chi-tiết-thuật-toán-ai)

---

## 1. Tổng quan cấu trúc thư mục

```text
python-chess-master/
├── src/                # Mã nguồn chính game cờ vua
│   ├── ai_engine.py
│   ├── chess_engine.py
│   ├── chess_gui.py
│   ├── chess_UX_UI.py
│   ├── chesssetup.py
│   ├── enums.py
│   ├── Piece.py
│   └── requirements.txt
├── face_pixel/         # Demo vẽ khuôn mặt pixel bằng pygame
│   ├── faces.py
│   ├── mẫu/
│   │   ├── baby.py
│   │   ├── adult.py
│   │   └── old.py
│   └── requirements.txt
├── images/             # Ảnh quân cờ, ảnh nền, sơ đồ kiến trúc
│   ├── BG.png ...
│   └── so do.jpg
└── README.md           # Tài liệu hướng dẫn & phân tích mã nguồn
```

---

## 2. Sơ đồ kiến trúc & luồng hoạt động

![Sơ đồ kiến trúc chương trình](images/so%20do.jpg)

- **src/**: Toàn bộ logic, AI, giao diện, engine cờ vua.
- **face_pixel/**: Demo vẽ mặt pixel (baby, adult, old) bằng pygame, không liên quan trực tiếp đến game cờ vua.
- **images/**: Ảnh quân cờ, ảnh nền, sơ đồ kiến trúc.

---

## 3. Giải thích từng file & các hàm chính

### 3.1. src/ - Mã nguồn chính
- **ai_engine.py**: Trí tuệ nhân tạo (AI) - thuật toán minimax, alpha-beta.
- **chess_engine.py**: Logic, trạng thái, luật chơi, quản lý bàn cờ.
- **chess_gui.py**: Giao diện đồ họa (Pygame), vẽ bàn cờ, lịch sử nước đi, popup.
- **chess_UX_UI.py**: Giao diện khởi động (Tkinter), chọn chế độ, màu quân, độ khó.
- **Piece.py**: Định nghĩa các quân cờ và logic di chuyển.
- **enums.py**: Hằng số cho người chơi/quân cờ.
- **chesssetup.py**: File khởi động nhanh.
- **requirements.txt**: Thư viện cần thiết (chỉ cần `pygame`).

### 3.2. face_pixel/ - Demo vẽ khuôn mặt pixel
- **faces.py**: Hàm vẽ mặt pixel (em bé, người lớn, người già) bằng pygame.
- **mẫu/**: Các file demo chạy độc lập, mỗi file vẽ một loại mặt, mắt di chuyển theo chuột.
  - `baby.py`, `adult.py`, `old.py`: Chạy trực tiếp bằng python để xem hiệu ứng.
- **requirements.txt**: Nếu chỉ chạy demo vẽ mặt, chỉ cần `pygame`. Nếu dùng AI nhận diện khuôn mặt, cần cài thêm `transformers`, `torch` (hiện tại không bắt buộc).

**Cách chạy demo:**
```bash
python face_pixel/mẫu/baby.py
python face_pixel/mẫu/adult.py
python face_pixel/mẫu/old.py
```

### 3.3. images/ - Ảnh quân cờ & giao diện
- Chứa ảnh PNG cho từng quân cờ, ảnh nền, sơ đồ kiến trúc.
- Sử dụng cho giao diện Pygame và minh họa README.

---

## 4. Hướng dẫn cài đặt & chạy

### 4.1. Cài đặt thư viện
- **Cờ vua:**
  ```bash
  pip install -r src/requirements.txt
  ```
- **Face Pixel (nếu cần):**
  ```bash
  pip install pygame
  # Nếu dùng AI nhận diện khuôn mặt:
  pip install -r face_pixel/requirements.txt
  ```

### 4.2. Chạy game cờ vua
```bash
python src/chesssetup.py
```

### 4.3. Chạy demo vẽ mặt pixel
```bash
python face_pixel/mẫu/baby.py
python face_pixel/mẫu/adult.py
python face_pixel/mẫu/old.py
```

---

## 5. Giải thích chi tiết thuật toán AI

- **AI sử dụng thuật toán minimax và alpha-beta pruning** để tìm nước đi tốt nhất.
- Có thể điều chỉnh độ khó bằng cách thay đổi độ sâu tìm kiếm (depth).
- Xem chi tiết giải thích, ví dụ, sơ đồ cây trong phần dưới của README (đã trình bày rất rõ).

---

## 6. Giao diện & trải nghiệm người dùng
- Giao diện khởi động chuyên nghiệp với Tkinter: chọn chế độ, màu quân, độ khó.
- Giao diện chơi chính bằng Pygame: bàn cờ đẹp, sidebar, lịch sử nước đi, popup kết thúc.
- Lịch sử nước đi hiển thị rõ ràng, có cả thời gian, ăn quân, phong cấp tốt.
- Demo vẽ mặt pixel sinh động, dễ mở rộng cho các bài tập đồ họa hoặc AI nhận diện khuôn mặt.

---

## 7. Đóng góp & phát triển
- Mã nguồn rõ ràng, chú thích chi tiết, dễ mở rộng.
- Có thể tích hợp thêm AI nhận diện khuôn mặt, các chế độ chơi mới, hoặc cải tiến giao diện.
- Mọi đóng góp, phản hồi xin gửi về nhóm phát triển!

---

> **Bản quyền & phát triển:**
> - Nhóm KHAKL.AI - Đồ án AI 2025
> - Liên hệ: ...

---

## 8. Phân tích giải thuật Minimax & Alpha-Beta Pruning

### 8.1. Minimax là gì?
- **Minimax** là giải thuật ra quyết định trong các trò chơi đối kháng (như cờ vua, caro, cờ tướng...).
- Ý tưởng: AI giả lập tất cả các nước đi có thể xảy ra, giả định cả AI và đối thủ đều chơi tối ưu.
    - **AI (Max)** luôn chọn nước đi để điểm số bàn cờ là lớn nhất cho mình.
    - **Đối thủ (Min)** luôn chọn nước đi để điểm số bàn cờ là nhỏ nhất cho AI.

### 8.2. Alpha-Beta Pruning là gì?
- **Alpha-Beta Pruning** là kỹ thuật tối ưu hóa cho Minimax, giúp loại bỏ các nhánh không cần thiết trong cây tìm kiếm, tăng tốc độ tính toán.
    - **Alpha**: Giá trị lớn nhất mà AI (Max) chắc chắn đạt được.
    - **Beta**: Giá trị nhỏ nhất mà đối thủ (Min) chắc chắn đạt được.
    - Nếu tại một nhánh, beta ≤ alpha, thuật toán sẽ dừng duyệt nhánh đó vì không thể có kết quả tốt hơn.

![Sơ đồ tổng quát Minimax](images/minimax_tree.jpg)

**Giải thích:**
- Node đầu tiên (AI - Max, màu xanh lá hoặc có ký hiệu 🟢) là lượt của máy tính.
- Các nhánh từ AI là các nước đi có thể chọn.
- Mỗi nước đi của AI sẽ dẫn đến lượt của đối thủ (Min).
- Đối thủ cũng có nhiều lựa chọn, mỗi lựa chọn lại dẫn đến các trạng thái bàn cờ khác nhau (các node lá).
- Các node lá là điểm số đánh giá bàn cờ (ví dụ: 3, 5, 2, 4, ...).
- AI sẽ chọn nước đi sao cho điểm số tệ nhất mà mình nhận được là lớn nhất (chiến lược tối ưu hóa).
- Node/nước đi được đánh dấu ⭐ là nước đi tốt nhất mà AI sẽ chọn.

### 8.3. Ví dụ minh họa đơn giản

![Sơ đồ ví dụ minh họa Minimax](images/minimax_example.jpg)

**Giải thích:**
- AI có 2 lựa chọn: Nước đi A và Nước đi B.
- Mỗi nước đi của AI, đối thủ lại có 2 cách đáp trả.
- Mỗi đáp trả dẫn đến một điểm số (ví dụ: +2, 0, -1, 1).
- AI sẽ chọn nước đi A vì điểm số tệ nhất của A (0) vẫn tốt hơn điểm số tệ nhất của B (-1).
- Node ⭐ là điểm số tệ nhất mà AI sẽ nhận được nếu chọn nước đi đó (chiến lược "chọn tốt nhất trong các trường hợp xấu nhất").

### 8.4. Alpha-Beta Pruning là gì?
- **Alpha-Beta Pruning** là kỹ thuật tối ưu hóa cho Minimax, giúp loại bỏ các nhánh không cần thiết trong cây tìm kiếm, tăng tốc độ tính toán.
    - **Alpha**: Giá trị lớn nhất mà AI (Max) chắc chắn đạt được.
    - **Beta**: Giá trị nhỏ nhất mà đối thủ (Min) chắc chắn đạt được.
    - Nếu tại một nhánh, beta ≤ alpha, thuật toán sẽ dừng duyệt nhánh đó vì không thể có kết quả tốt hơn.

### 8.5. Sơ đồ Alpha-Beta Pruning

![Sơ đồ Alpha-Beta Pruning](images/alphabeta_pruning.jpg)

**Giải thích:**
- Các nhánh bị đánh dấu 🚫 hoặc màu đỏ là nhánh bị "cắt tỉa" (pruned), tức là không cần duyệt tiếp vì chắc chắn không thể tốt hơn các nhánh đã duyệt.
- Điều này giúp AI tiết kiệm rất nhiều thời gian khi tính toán nước đi.
- Node AI (Max) vẫn là điểm xuất phát, các node Min là lượt của đối thủ.
- Khi AI phát hiện một nhánh không thể tốt hơn nhánh đã có, nó sẽ bỏ qua các nhánh còn lại (ví dụ: các node có ký hiệu 🚫).

### 8.6. Mã giả thuật toán Minimax (có Alpha-Beta)

```python
def minimax(node, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or node is terminal:
        return evaluate(node)
    if maximizingPlayer:
        maxEval = -inf
        for child in node.children:
            eval = minimax(child, depth-1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Cắt tỉa
        return maxEval
    else:
        minEval = +inf
        for child in node.children:
            eval = minimax(child, depth-1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Cắt tỉa
        return minEval
```

### 8.7. Ứng dụng thực tế trong game cờ vua
- AI sẽ duyệt tất cả nước đi hợp lệ, giả lập trạng thái bàn cờ mới, đánh giá điểm số, và chọn nước đi tối ưu nhất dựa trên việc giả định đối thủ cũng sẽ chơi tối ưu.
- Độ sâu (depth) càng lớn, AI càng mạnh nhưng càng tốn thời gian.

---


