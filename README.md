# ♟️ Chess Game AI - Hướng dẫn sử dụng & Phân tích mã nguồn

## 1. Tổng quan cấu trúc thư mục

```
src/
├── ai_engine.py        # Trí tuệ nhân tạo (AI)
├── chess_engine.py     # Logic, trạng thái, luật chơi
├── chess_gui.py        # Giao diện đồ họa (Pygame)
├── chess_UX_UI.py      # Giao diện khởi động (Tkinter)
├── chesssetup.py       # File khởi động nhanh
├── enums.py            # Định nghĩa hằng số
├── Piece.py            # Định nghĩa các quân cờ
├── requirements.txt    # Thư viện cần thiết
└── images/             # Thư mục ảnh quân cờ
```

---

## 2. Sơ đồ kiến trúc & luồng hoạt động

![Sơ đồ kiến trúc chương trình](images/so%20do.jpg)

- **chess_UX_UI.py**: Khởi động, chọn chế độ chơi, màu quân, độ khó.
- **chesssetup.py**: Chạy vào giao diện chính.
- **chess_gui.py**: Vẽ bàn cờ, quân cờ, sidebar, lịch sử nước đi, popup kết thúc.
- **ai_engine.py**: AI tính toán nước đi tốt nhất bằng Minimax & Alpha-Beta.
- **chess_engine.py**: Quản lý trạng thái bàn cờ, kiểm tra luật, thực hiện nước đi.
- **Piece.py**: Định nghĩa các quân cờ và logic di chuyển.
- **enums.py**: Định nghĩa hằng số cho người chơi/quân cờ.

---

## 3. Giải thích từng file & các hàm chính (đánh dấu dòng)

### 3.1. `enums.py`
- **Mục đích:** Định nghĩa các hằng số cho người chơi/quân cờ.
- **Class:** `Player` (dòng 1)

### 3.2. `Piece.py`
- **Mục đích:** Định nghĩa các class quân cờ (Xe, Mã, Tượng, Hậu, Vua, Tốt).
- **Class:** `Piece` (dòng 9)
- **Các class con:** `Rook` (dòng 80), `Knight` (dòng 179), `Bishop` (dòng 222), `Pawn` (dòng 306), `Queen` (dòng 377), `King` (dòng 446)
- **Các hàm tiêu biểu:**  
  - `__init__` (dòng 15, 85, 227, 382)
  - `get_row_number` (dòng 30)
  - `get_col_number` (dòng 34)
  - `get_name` (dòng 38)
  - `get_player` (dòng 42)
  - `get_valid_peaceful_moves(game_state)`
  - `get_valid_piece_takes(game_state)`
  - `get_valid_piece_moves(game_state)`

### 3.3. `chess_engine.py`
- **Mục đích:** Quản lý toàn bộ logic, trạng thái, luật chơi cờ vua.
- **Class:** `game_state` (dòng 28)
- **Class:** `chess_move` (dòng 939)
- **Các hàm tiêu biểu:**  
  - `__init__` (dòng 34, 940)
  - `get_piece` (dòng 139)
  - `is_valid_piece` (dòng 153)
  - `get_valid_moves` (dòng 160)
  - `move_piece` (dòng 365)
  - `undo_move` (dòng 546)
  - `checkmate_stalemate_checker` (dòng 261)
  - `get_moving_piece` (dòng 980)
  - `get_captured_piece` (dòng 983)

### 3.4. `ai_engine.py`
- **Mục đích:** Cung cấp trí tuệ nhân tạo cho game cờ vua.
- **Class:** `chess_ai` (dòng 9)
- **Các hàm tiêu biểu:**  
  - `minimax_white` (dòng 16)
  - `minimax_black` (dòng 108)
  - `evaluate_board` (dòng 192)
  - `get_piece_value` (dòng 209)

### 3.5. `chess_gui.py`
- **Mục đích:** Xây dựng giao diện đồ họa (Pygame), xử lý sự kiện, vẽ bàn cờ, quân cờ, popup, sidebar, lịch sử nước đi, popup kết thúc.
- **Các hàm chính:**  
  - `load_images` (dòng 34)
  - `draw_game_state` (dòng 46)
  - `draw_squares` (dòng 102)
  - `draw_pieces` (dòng 115)
  - `highlight_square` (dòng 129)
  - `main` (dòng 158)
  - `draw_status_bar` (dòng 515)
  - `draw_text` (dòng 545)
  - `draw_game_time` (dòng 572)
  - `draw_controls` (dòng 590)
  - `draw_sidebar` (dòng 607)
  - `draw_end_game_buttons` (dòng 672)
  - `draw_labels` (dòng 701)
  - `draw_move_history` (dòng 719)
  - `draw_endgame_popup` (dòng 785)

### 3.6. `chess_UX_UI.py`
- **Mục đích:** Giao diện khởi động (Tkinter), chọn chế độ chơi, màu quân, độ khó.
- **Class:** `ChessInterface` (dòng 6)
- **Các hàm tiêu biểu:**  
  - `__init__` (dòng 7)
  - `load_background_image` (dòng 35)
  - `create_choice_buttons` (dòng 54)
  - `on_resize` (dòng 101)
  - `perform_resize` (dòng 110)
  - `button_clicked_solo` (dòng 176)
  - `button_clicked_AI` (dòng 188)
  - `show_color_selection_screen` (dòng 192)
  - `select_color_and_show_difficulty` (dòng 264)
  - `show_difficulty_selection_screen` (dòng 269)
  - `select_difficulty_and_start` (dòng 342)
  - `show_confirm_popup` (dòng 354)
  - `start_ai_game` (dòng 389)
  - `back_to_main_menu` (dòng 403)
  - `button_clicked_exit` (dòng 423)
  - `run` (dòng 428)

### 3.7. `chesssetup.py`
- **Mục đích:** File khởi động nhanh, chỉ cần chạy file này để vào giao diện chính.
- **Nội dung:** 
  ```python
  from chess_UX_UI import ChessInterface

  if __name__ == "__main__":
      app = ChessInterface()
      app.run()
  ```

### 3.8. `requirements.txt`
- **Mục đích:** Liệt kê thư viện cần thiết (chỉ cần `pygame`).

---

## 4. Luồng hoạt động tổng thể

1. **Khởi động:** Chạy `chesssetup.py` → Giao diện menu (Tkinter) → Chọn chế độ chơi.
2. **Vào game:** Giao diện Pygame hiện ra, vẽ bàn cờ, quân cờ, sidebar, timer, lịch sử nước đi.
3. **Chơi game:** Người chơi hoặc AI thực hiện nước đi, cập nhật trạng thái, kiểm tra luật, vẽ lại giao diện.
4. **Kết thúc:** Khi chiếu hết, hòa, đầu hàng... hiện popup chuyên nghiệp, chọn "Trở lại" hoặc "Thoát".

---

## 5. Hướng dẫn bảo trì/nâng cấp

- **Muốn thêm luật mới:** Sửa trong `chess_engine.py` (class `game_state`)
- **Muốn thay đổi giao diện:** Sửa trong `chess_gui.py` (các hàm vẽ, biến cấu hình)
- **Muốn nâng cấp AI:** Sửa trong `ai_engine.py` (class `chess_ai`)
- **Muốn thêm chế độ chơi:** Sửa trong `chess_UX_UI.py` (class `ChessInterface`)
- **Muốn thêm hình ảnh:** Thêm vào thư mục `images/` và cập nhật `load_images()`

---

## 6. Giải thích chi tiết thuật toán Minimax & Alpha-Beta Pruning

### 6.1. Minimax là gì?

- **Minimax** là thuật toán giúp AI chọn nước đi tốt nhất bằng cách giả lập mọi khả năng tiếp theo, giả định đối thủ cũng chơi tối ưu.
- **Ý tưởng:**  
  - AI (max) chọn nước đi để điểm số bàn cờ là lớn nhất.
  - Đối thủ (min) chọn nước đi để điểm số bàn cờ là nhỏ nhất.
- **Ví dụ thực tế:**  
  - Giống như chơi cờ caro, bạn luôn chọn nước đi khiến đối thủ khó thắng nhất.

### 6.2. Alpha-Beta Pruning là gì?

- **Alpha-Beta Pruning** là kỹ thuật tối ưu cho Minimax, giúp bỏ qua những nhánh không cần thiết, tăng tốc độ tính toán.
- **Alpha:** Giá trị lớn nhất mà max (AI) chắc chắn đạt được.
- **Beta:** Giá trị nhỏ nhất mà min (đối thủ) chắc chắn đạt được.
- **Nếu tại một nhánh, beta ≤ alpha, thì không cần xét tiếp nhánh đó.**

### 6.3. Cách hoạt động trên bàn cờ

- **Hàm chính:**  
  - `minimax_white` (dòng 16, [ai_engine.py](src/ai_engine.py))
  - `minimax_black` (dòng 108, [ai_engine.py](src/ai_engine.py))
- **Quy trình:**  
  1. AI duyệt tất cả nước đi hợp lệ (hàm `get_all_legal_moves` ở [chess_engine.py](src/chess_engine.py)).
  2. Với mỗi nước đi, AI giả lập bàn cờ mới, gọi đệ quy minimax cho đối thủ.
  3. Đánh giá bàn cờ bằng hàm `evaluate_board`.
  4. Sử dụng alpha-beta để cắt nhánh không cần thiết.
  5. Trả về nước đi tốt nhất ở độ sâu gốc.

**Ví dụ đơn giản:**  
- Nếu AI là trắng, có thể ăn hậu đen hoặc đi nước phòng thủ. Minimax sẽ tính điểm cho từng trường hợp, chọn nước ăn hậu nếu điểm số cao nhất.

### 6.4. Chế độ dễ/khó hoạt động thế nào?

- **Chế độ dễ:** Độ sâu tìm kiếm nhỏ (ví dụ: depth = 1 hoặc 2). AI chỉ nhìn trước 1-2 nước, thường chọn nước đơn giản.
- **Chế độ khó:** Độ sâu tìm kiếm lớn (ví dụ: depth = 3 hoặc 4). AI nhìn xa hơn, tính toán nhiều nhánh, chọn nước tối ưu hơn.

**Ví dụ thực tế:**  
- **Dễ:** AI chỉ ăn quân nếu có thể, không phòng thủ, dễ bị chiếu hết.
- **Khó:** AI vừa ăn quân, vừa phòng thủ, tránh bị chiếu hết, có thể "bẫy" người chơi.

---

## 7. Chú thích từng dòng, từng class, từng hàm (ví dụ)

**Ví dụ chú thích class và hàm trong `Piece.py`:**
```python
class Piece:
    """Lớp cơ sở cho tất cả quân cờ, chứa các thuộc tính và phương thức chung."""
    def __init__(self, name, row_number, col_number, player):
        """Khởi tạo quân cờ với tên, vị trí, người sở hữu."""
        self._name = name
        self.row_number = row_number
        self.col_number = col_number
        self._player = player
    ...
```

---

## 8. Hướng dẫn sử dụng

### Cài đặt
```bash
pip install pygame
```

### Chạy game
```bash
python chesssetup.py
```
Hoặc chạy trực tiếp `chess_UX_UI.py` để vào menu chọn chế độ.

---

## 9. Liên hệ & đóng góp

- Nếu có ý tưởng nâng cấp, vui lòng tạo Pull Request hoặc Issue trên GitHub.
- Tác giả: [Tên nhóm/Thành viên]

---


