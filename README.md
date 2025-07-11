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

### 3.9. Giải thích chi tiết cách sử dụng các hàm tiêu biểu

### enums.py
- **Player (dòng 1):**  
  Định nghĩa các giá trị hằng số cho người chơi (PLAYER_1, PLAYER_2, EMPTY) và tên quân cờ.  
  **Sử dụng:**  
  ```python
  from enums import Player
  if piece.get_player() == Player.PLAYER_1:
      # xử lý cho quân trắng
  ```

---

### Piece.py
- **Piece (dòng 9):**  
  Lớp cha cho tất cả quân cờ, chứa các thuộc tính và phương thức chung.
  - `__init__` (dòng 15): Khởi tạo quân cờ với tên, vị trí, người sở hữu.
  - `get_row_number` (dòng 30): Trả về số hàng hiện tại của quân cờ.
  - `get_col_number` (dòng 34): Trả về số cột hiện tại của quân cờ.
  - `get_name` (dòng 38): Trả về tên quân cờ.
  - `get_player` (dòng 42): Trả về người sở hữu quân cờ.
  - `get_valid_peaceful_moves(game_state)`: Trả về danh sách các ô có thể di chuyển mà không ăn quân.
  - `get_valid_piece_takes(game_state)`: Trả về danh sách các ô có thể ăn quân.
  - `get_valid_piece_moves(game_state)`: Trả về tất cả nước đi hợp lệ (kết hợp peaceful và takes).

  **Ví dụ sử dụng:**
  ```python
  piece = Piece("p", 6, 0, Player.PLAYER_1)
  moves = piece.get_valid_piece_moves(game_state)
  ```

- **Các class con:**  
  - `Rook`, `Knight`, `Bishop`, `Pawn`, `Queen`, `King`:  
    Mỗi class đều override các hàm di chuyển phù hợp với luật cờ vua cho từng loại quân.

---

### chess_engine.py
- **game_state (dòng 28):**  
  Quản lý trạng thái bàn cờ, các quân cờ, lượt chơi, kiểm tra luật.
  - `__init__` (dòng 34): Khởi tạo trạng thái bàn cờ.
  - `get_piece(row, col)` (dòng 139): Trả về quân cờ tại vị trí (row, col).
  - `is_valid_piece(row, col)` (dòng 153): Kiểm tra xem vị trí có quân cờ hợp lệ không.
  - `get_valid_moves(player)` (dòng 160): Trả về danh sách nước đi hợp lệ cho người chơi.
  - `move_piece(from_row, from_col, to_row, to_col)` (dòng 365): Thực hiện nước đi.
  - `undo_move()`: Hoàn tác nước đi trước.
  - `checkmate_stalemate_checker()` (dòng 261): Kiểm tra trạng thái chiếu hết/hòa.

  **Ví dụ sử dụng:**
  ```python
  gs = game_state()
  valid_moves = gs.get_valid_moves(Player.PLAYER_1)
  gs.move_piece(6, 0, 4, 0)
  ```

---

### ai_engine.py
- **chess_ai (dòng 9):**  
  Lớp AI sử dụng thuật toán minimax và alpha-beta pruning.
  - `minimax_white(game_state, depth, alpha, beta, maximizing_player, player_color, root_depth=None)` (dòng 16):  
    Tìm nước đi tốt nhất cho quân trắng.  
    **Tham số:**  
    - `game_state`: Trạng thái bàn cờ hiện tại  
    - `depth`: Độ sâu tìm kiếm  
    - `alpha`, `beta`: Giá trị cắt nhánh  
    - `maximizing_player`: Đang là lượt AI hay đối thủ  
    - `player_color`: Màu quân AI  
    - `root_depth`: Độ sâu gốc (dùng để trả về nước đi thay vì điểm số)
  - `minimax_black(...)` (dòng 108): Tương tự cho quân đen.
  - `evaluate_board(game_state)` (dòng 192): Đánh giá điểm số bàn cờ hiện tại.
  - `get_piece_value(piece)` (dòng 209): Trả về giá trị điểm số của quân cờ.

  **Ví dụ sử dụng:**
  ```python
  ai = chess_ai()
  best_move = ai.minimax_white(gs, depth=3, alpha=-float('inf'), beta=float('inf'), maximizing_player=True, player_color=Player.PLAYER_1)
  ```

---

### chess_gui.py
- **load_images() (dòng 34):**  
  Tải hình ảnh cho các quân cờ từ thư mục images.
- **draw_game_state(screen, game_state, valid_moves, square_selected, ...) (dòng 46):**  
  Vẽ bàn cờ, quân cờ, highlight nước đi, lịch sử, v.v.
- **draw_squares(screen, board_flipped=False) (dòng 102):**  
  Vẽ các ô bàn cờ.
- **draw_pieces(screen, game_state, board_flipped=False) (dòng 115):**  
  Vẽ các quân cờ lên bàn cờ.
- **highlight_square(screen, game_state, valid_moves, square_selected, board_flipped=False) (dòng 129):**  
  Highlight ô được chọn và các nước đi hợp lệ.
- **main(game_mode, player_color=None, difficulty=None) (dòng 158):**  
  Hàm khởi động giao diện Pygame, xử lý sự kiện chính.
- **draw_sidebar(screen, ...) (dòng 607):**  
  Vẽ cột bên phải: thời gian, nút đầu hàng, độ khó, v.v.

  **Ví dụ sử dụng:**
  ```python
  draw_game_state(screen, gs, valid_moves, square_selected)
  ```

---

### chess_UX_UI.py
- **ChessInterface (dòng 6):**  
  Lớp giao diện khởi động (Tkinter).
  - `__init__` (dòng 7): Khởi tạo giao diện.
  - `load_background_image()` (dòng 35): Tải hình nền.
  - `create_choice_buttons()` (dòng 54): Tạo các nút chọn chế độ chơi.
  - `on_resize()` (dòng 101): Xử lý khi cửa sổ thay đổi kích thước.
  - `button_clicked_solo()` (dòng 176): Xử lý khi chọn chơi solo.
  - `button_clicked_AI()` (dòng 188): Xử lý khi chọn chơi với AI.
  - `show_color_selection_screen()` (dòng 192): Hiển thị màn hình chọn màu quân.
  - `select_color_and_show_difficulty()` (dòng 264): Chọn màu quân và hiển thị chọn độ khó.
  - `show_difficulty_selection_screen()` (dòng 269): Hiển thị màn hình chọn độ khó.
  - `select_difficulty_and_start()` (dòng 342): Chọn độ khó và bắt đầu game.
  - `show_confirm_popup()` (dòng 354): Hiển thị popup xác nhận.
  - `start_ai_game()` (dòng 389): Bắt đầu game với AI.
  - `back_to_main_menu()` (dòng 403): Quay lại menu chính.
  - `button_clicked_exit()` (dòng 423): Xử lý khi nhấn nút thoát.
  - `run()` (dòng 428): Chạy giao diện Tkinter.

  **Ví dụ sử dụng:**
  ```python
  app = ChessInterface()
  app.run()
  ```

---

### chesssetup.py
- **Khởi động nhanh:**  
  Chỉ cần chạy file này để vào giao diện chính.
  ```python
  from chess_UX_UI import ChessInterface

  if __name__ == "__main__":
      app = ChessInterface()
      app.run()
  ```

---

### requirements.txt
- **Cài đặt thư viện:**  
  Chạy lệnh sau để cài đặt các thư viện cần thiết:
  ```bash
  pip install -r requirements.txt
  ```

---

**Lưu ý:**  
- Khi sử dụng các hàm, luôn truyền đúng kiểu dữ liệu và trạng thái hiện tại của game.
- Có thể tham khảo thêm docstring trong từng file để hiểu chi tiết hơn về từng hàm.


