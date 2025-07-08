# 📚 HƯỚNG DẪN SỬ DỤNG & PHÂN TÍCH MÃ NGUỒN CHESS GAME AI

## 1. Tổng quan cấu trúc thư mục

```
src/
├── ai_engine.py
├── chess_engine.py
├── chess_gui.py
├── chess_UX_UI.py
├── chesssetup.py
├── enums.py
├── Piece.py
├── requirements.txt
└── images/ (thư mục ảnh quân cờ)
```

---

## Sơ đồ kiến trúc & luồng hoạt động giữa các file

<p align="center">
  <img src="images/so do.jpg" alt="Sơ đồ kiến trúc chương trình" width="600"/>
</p>

---

## 2. Giải thích từng file (có kèm vị trí dòng code)

### 2.1. `enums.py`
- **Mục đích:** Định nghĩa các hằng số cho người chơi và quân cờ.
- **Class:** `Player` (dòng 1)
  - `PLAYER_1 = 'white'`: Người chơi 1 (quân trắng)
  - `PLAYER_2 = 'black'`: Người chơi 2 (quân đen)
  - `EMPTY = -9`: Ô trống trên bàn cờ
  - `PIECES`: Danh sách tên các quân cờ (trắng/đen)

---

### 2.2. `Piece.py`
- **Mục đích:** Định nghĩa các class quân cờ (Xe, Mã, Tượng, Hậu, Vua, Tốt).
- **Class:** `Piece` (dòng 9)
- **Class:** `Rook(Piece)` (dòng 80)
- **Class:** `Knight(Piece)` (dòng 179)
- **Class:** `Bishop(Piece)` (dòng 222)
- **Class:** `Pawn(Piece)` (dòng 306)
- **Class:** `Queen(Piece)` (dòng 377)
- **Class:** `King(Piece)` (dòng 446)
  - Mỗi class cài đặt logic di chuyển, ăn quân riêng biệt (ví dụ: `Rook.traverse`, `Knight.get_valid_piece_takes`, ...)
  - Các hàm quan trọng:
    - `get_valid_peaceful_moves(game_state)`: trả về các ô có thể di chuyển không ăn quân
    - `get_valid_piece_takes(game_state)`: trả về các ô có thể ăn quân
    - `get_valid_piece_moves(game_state)`: trả về tất cả nước đi hợp lệ
  - **Các hàm tiêu biểu:**
    - `__init__` (dòng 15, 85, 227, 382)
    - `get_row_number` (dòng 30)
    - `get_col_number` (dòng 34)
    - `get_name` (dòng 38)
    - `get_player` (dòng 42)
    - ...

---

### 2.3. `chess_engine.py`
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
    - ...

---

### 2.4. `ai_engine.py`
- **Mục đích:** Cung cấp trí tuệ nhân tạo cho game cờ vua.
- **Class:** `chess_ai` (dòng 9)
  - **Các hàm tiêu biểu:**
    - `minimax_white` (dòng 16)
    - `minimax_black` (dòng 108)
    - `evaluate_board` (dòng 192)
    - `get_piece_value` (dòng 209)

---

### 2.5. `chess_gui.py`
- **Mục đích:** Xây dựng giao diện đồ họa (Pygame), xử lý sự kiện, vẽ bàn cờ, quân cờ, popup, sidebar, lịch sử nước đi, popup kết thúc, ...
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

---

### 2.6. `chess_UX_UI.py`
- **Mục đích:** Giao diện khởi động (Tkinter), chọn chế độ chơi, chọn màu quân, chọn độ khó, điều hướng vào game chính.
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

---

### 2.7. `chesssetup.py`
- **Mục đích:** File khởi động nhanh, chỉ cần chạy file này để vào giao diện chính.
- **Nội dung:** 
  ```python
  from chess_UX_UI import ChessInterface

  if __name__ == "__main__":
      app = ChessInterface()
      app.run()
  ```

---

### 2.8. `requirements.txt`
- **Mục đích:** Liệt kê thư viện cần thiết (chỉ cần `pygame`).

---

## 3. Hướng dẫn sử dụng

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

## 6. Chú thích từng dòng, từng class, từng hàm (ví dụ)

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


