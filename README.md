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
  - `back_to_main_menu()` (dòng 403)
  - `button_clicked_exit()` (dòng 423)
  - `run()` (dòng 428)

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

## 4. Giải thích chi tiết thuật toán AI: Minimax & Alpha-Beta Pruning

### 4.0. Khái niệm về Minimax và Alpha-Beta Pruning

#### Minimax là gì?

Minimax là một thuật toán ra quyết định trong các trò chơi đối kháng như cờ vua, cờ caro, cờ tướng... Thuật toán này giúp AI giả lập tất cả các nước đi có thể xảy ra, giả định rằng cả AI và đối thủ đều chơi tối ưu.  
- **AI (Max)** luôn cố gắng chọn nước đi để điểm số bàn cờ là lớn nhất cho mình.
- **Đối thủ (Min)** luôn cố gắng chọn nước đi để điểm số bàn cờ là nhỏ nhất cho AI.

#### Alpha-Beta Pruning là gì?

Alpha-Beta Pruning là kỹ thuật tối ưu hóa cho Minimax, giúp loại bỏ các nhánh không cần thiết trong cây tìm kiếm, từ đó tăng tốc độ tính toán.  
- **Alpha** là giá trị lớn nhất mà AI (Max) chắc chắn đạt được.
- **Beta** là giá trị nhỏ nhất mà đối thủ (Min) chắc chắn đạt được.
- Nếu tại một nhánh, beta ≤ alpha, thuật toán sẽ dừng duyệt nhánh đó vì không thể có kết quả tốt hơn.

---

### 4.1. Tổng quan hoạt động

Khi đến lượt AI, thuật toán sẽ duyệt qua tất cả các nước đi hợp lệ, giả lập từng trạng thái bàn cờ mới, đánh giá điểm số, và chọn nước đi tối ưu nhất dựa trên việc giả định đối thủ cũng sẽ chơi tối ưu.

---

### 4.2. Biểu đồ luồng hoạt động thuật toán Minimax

```
Lượt AI (Max)
│
├─ Nước đi 1
│   ├─ Đối thủ (Min) nước đi 1.1
│   │   ├─ AI (Max) nước đi 1.1.1
│   │   └─ AI (Max) nước đi 1.1.2
│   └─ Đối thủ (Min) nước đi 1.2
│       ├─ AI (Max) nước đi 1.2.1
│       └─ AI (Max) nước đi 1.2.2
│
├─ Nước đi 2
│   ├─ Đối thủ (Min) nước đi 2.1
│   │   ├─ AI (Max) nước đi 2.1.1
│   │   └─ AI (Max) nước đi 2.1.2
│   └─ Đối thủ (Min) nước đi 2.2
│       ├─ AI (Max) nước đi 2.2.1
│       └─ AI (Max) nước đi 2.2.2
│
...
```

- **Max:** AI chọn điểm số lớn nhất.
- **Min:** Đối thủ chọn điểm số nhỏ nhất.
- Độ sâu của cây là số lượt nhìn trước (depth).

---

### 4.3. Biểu đồ cắt nhánh Alpha-Beta

```
           AI (Max)
          /        \
        5           ?
      /   \       /   \
     3     5     2     4
    / \   / \   / \   / \
    3  3  5  5  2  2  4  4

Nếu nhánh bên trái đã có điểm số 5 (alpha), khi duyệt nhánh bên phải, nếu điểm số nhỏ hơn 5 (beta <= alpha), thuật toán sẽ bỏ qua các nhánh còn lại.
```

---

### 4.4. Quy trình áp dụng vào bàn cờ

1. **Lấy trạng thái bàn cờ hiện tại.**
2. **Duyệt tất cả nước đi hợp lệ của AI.**
3. **Với mỗi nước đi:**
   - Giả lập trạng thái mới.
   - Gọi đệ quy minimax cho đối thủ.
   - Đánh giá điểm số bàn cờ bằng hàm `evaluate_board`.
   - Sử dụng alpha-beta để cắt nhánh không cần thiết.
4. **Chọn nước đi có điểm số tối ưu nhất.**

---

### 4.5. Ví dụ minh họa trực quan với icon quân cờ

#### Ví dụ: AI là trắng, có 2 quân tốt ♙, đen có 1 quân tốt ♟

**Bàn cờ ban đầu:**

```
+---+---+---+
| ♙ |   | ♙ |
+---+---+---+
|   | ♟ |   |
+---+---+---+
```

**Bước 1 (AI - Max):**
- AI có thể:
  - Di chuyển ♙ bên trái lên (Nước đi A)
  - Di chuyển ♙ bên phải sang phải (Nước đi B)

```
        [Bàn cờ ban đầu]
             |
      +------+------+
      |             |
[Nước đi A]   [Nước đi B]
  ♙ tiến lên   ♙ sang phải
      |             |
      v             v
+---+---+---+   +---+---+---+
|   |   | ♙ |   | ♙ |   |   |
+---+---+---+   +---+---+---+
| ♙ | ♟ |   |   |   | ♟ | ♙ |
+---+---+---+   +---+---+---+
```

**Bước 2 (Đen - Min):**
- Đen đáp trả bằng cách di chuyển ♟ hoặc ăn quân trắng nếu có thể.

---

### 4.6. Sơ đồ cây cho các chế độ AI

#### Chế độ dễ (depth = 1):

```
[AI] ♙ ♙ vs ♟
  |
  +--Nước đi A--> [Đánh giá điểm số]
  +--Nước đi B--> [Đánh giá điểm số]
=> Chọn nước đi có điểm số cao nhất ở lượt đầu tiên.
```

#### Chế độ trung bình (depth = 2):

```
[AI] ♙ ♙ vs ♟
  |
  +--Nước đi A--> [Đen đáp trả] --Đánh giá điểm số-->
  +--Nước đi B--> [Đen đáp trả] --Đánh giá điểm số-->
=> Xem xét cả nước đi của đối thủ, chọn nước đi tối ưu hơn.
```

#### Chế độ khó (depth = 3+):

```
[AI] ♙ ♙ vs ♟
  |
  +--Nước đi A--> [Đen đáp trả] --> [AI tiếp tục] --Đánh giá điểm số-->
  +--Nước đi B--> [Đen đáp trả] --> [AI tiếp tục] --Đánh giá điểm số-->
=> Xem xét nhiều lượt, có thể tạo bẫy hoặc phòng thủ sâu hơn.
```

---

### 4.7. Alpha-Beta Pruning minh họa

```
[AI] ♙ ♙ vs ♟
  |
  +--Nước đi 1 (alpha = 3)
  |     |
  |     +--Đen đáp trả (beta = 2)  <-- bị cắt nhánh vì beta < alpha
  |
  +--Nước đi 2 (alpha = 3)
        |
        +--Đen đáp trả (beta = 4)
```

---

### 4.8. Ví dụ chi tiết về thuật toán Minimax & Alpha-Beta Pruning trong AI cờ vua

#### Ví dụ 1: AI chọn nước đi tốt nhất (Minimax cơ bản)

Giả sử bàn cờ chỉ còn 2 quân tốt trắng và 1 quân tốt đen, AI là trắng. Trắng có 2 lựa chọn:
- **Nước đi A:** Tiến tốt lên, có thể ăn tốt đen ở lượt sau.
- **Nước đi B:** Di chuyển tốt sang ngang, không tạo ra lợi thế.

Thuật toán Minimax sẽ:
1. Duyệt cả 2 nước đi.
2. Giả lập trạng thái bàn cờ sau mỗi nước đi.
3. Đánh giá điểm số (ví dụ: ăn được tốt đen thì +1 điểm).
4. Chọn nước đi có điểm số cao nhất.

**Mã minh họa:**
```python
ai = chess_ai()
best_move = ai.minimax_white(gs, depth=2, alpha=-float('inf'), beta=float('inf'), maximizing_player=True, player_color=Player.PLAYER_1)
gs.move_piece(*best_move)
```

---

#### Ví dụ 2: Alpha-Beta Pruning giúp tăng tốc

Giả sử AI đã tìm được một nhánh có điểm số là +3 (alpha). Khi duyệt các nhánh khác, nếu điểm số của đối thủ (beta) nhỏ hơn +3, thuật toán sẽ bỏ qua các nhánh đó vì đối thủ sẽ không chọn.

**Biểu đồ minh họa:**
```
AI (Max)
│
├─ Nước đi 1 (alpha = 3)
│   └─ Đối thủ (Min) nước đi 1.1 (beta = 2)  ← bị cắt nhánh vì beta < alpha
│
├─ Nước đi 2 (alpha = 3)
│   └─ Đối thủ (Min) nước đi 2.1 (beta = 4)
```

---

#### Ví dụ 3: Điều chỉnh độ khó AI

- **Chế độ dễ:** AI chỉ nhìn trước 1 nước đi (depth = 1), thường chỉ ăn quân nếu có thể, không phòng thủ.
- **Chế độ khó:** AI nhìn trước 3-4 nước đi (depth = 3 hoặc 4), vừa ăn quân vừa phòng thủ, tránh bị chiếu hết.

**Mã minh họa:**
```python
# AI dễ
best_move = ai.minimax_white(gs, depth=1, alpha=-float('inf'), beta=float('inf'), maximizing_player=True, player_color=Player.PLAYER_1)

# AI khó
best_move = ai.minimax_white(gs, depth=4, alpha=-float('inf'), beta=float('inf'), maximizing_player=True, player_color=Player.PLAYER_1)
```

---

#### Ví dụ 4: AI phòng thủ trước nước chiếu hết

Giả sử đối thủ chuẩn bị chiếu hết, AI sẽ dùng Minimax để tìm nước đi ngăn chặn chiếu hết thay vì chỉ ăn quân.

**Mã minh họa:**
```python
# Trạng thái bàn cờ: Đen chuẩn bị chiếu hết trắng
best_move = ai.minimax_white(gs, depth=3, alpha=-float('inf'), beta=float('inf'), maximizing_player=True, player_color=Player.PLAYER_1)
# AI sẽ chọn nước đi giúp vua trắng thoát khỏi chiếu hết
gs.move_piece(*best_move)
```

---

#### Ví dụ 5: AI tạo bẫy cho đối thủ

Ở chế độ khó, AI có thể "nhử" đối thủ ăn quân để sau đó chiếu hết hoặc lấy lợi thế.

**Mã minh họa:**
```python
# Trạng thái bàn cờ: AI có thể hy sinh quân nhỏ để dụ đối thủ vào thế chiếu hết
best_move = ai.minimax_white(gs, depth=4, alpha=-float('inf'), beta=float('inf'), maximizing_player=True, player_color=Player.PLAYER_1)
gs.move_piece(*best_move)
```

---

**Lưu ý:**  
- Các ví dụ trên đều sử dụng hàm `minimax_white` hoặc `minimax_black` trong `ai_engine.py`.
- Để kiểm tra kết quả, hãy in ra trạng thái bàn cờ sau khi AI thực hiện nước đi.
- Có thể thay đổi độ sâu (`depth`) để kiểm tra sự khác biệt giữa các chế độ AI.

---

### 4.9. Giải thích chi tiết về game_state và cách xác định vị trí quân cờ

#### 1. Khởi tạo game_state

- **game_state** là class trung tâm quản lý toàn bộ trạng thái bàn cờ, các quân cờ, lượt chơi, lịch sử nước đi, kiểm tra luật cờ...
- Khi bạn tạo một đối tượng game_state, bàn cờ sẽ được khởi tạo với các quân cờ ở vị trí ban đầu theo luật cờ vua.

**Ví dụ khởi tạo:**
```python
from chess_engine import game_state

gs = game_state()  # Tạo bàn cờ mới, quân cờ được đặt đúng vị trí xuất phát
```

#### 2. Hàm get_piece(row, col) dùng để làm gì?

- Hàm này trả về đối tượng quân cờ nằm ở vị trí hàng `row`, cột `col` trên bàn cờ.
- Nếu vị trí đó không có quân cờ, hàm sẽ trả về None hoặc một giá trị đặc biệt (tùy cách cài đặt).

**Cách sử dụng:**
```python
piece = gs.get_piece(6, 0)  # Lấy quân cờ ở hàng 6, cột 0 (thường là tốt trắng ở vị trí xuất phát)
if piece is not None:
    print(piece.get_name())  # In ra tên quân cờ, ví dụ 'Pawn'
    print(piece.get_player())  # In ra người sở hữu quân cờ (Player.PLAYER_1 hoặc Player.PLAYER_2)
```

#### 3. Làm sao để rà vị trí quân cờ trên bàn?

- Bạn có thể duyệt qua toàn bộ bàn cờ bằng vòng lặp, kiểm tra từng ô bằng `get_piece(row, col)` để xác định quân cờ nào đang ở đâu.

**Ví dụ rà toàn bộ bàn cờ:**
```python
for row in range(8):
    for col in range(8):
        piece = gs.get_piece(row, col)
        if piece is not None:
            print(f"Quân {piece.get_name()} của {piece.get_player()} ở vị trí ({row}, {col})")
```

#### 4. Ứng dụng trong AI

- Khi AI cần đánh giá bàn cờ, nó sẽ sử dụng các hàm như `get_piece(row, col)` để xác định vị trí, loại quân, và tính toán điểm số cho từng trạng thái.
- Các hàm như `get_valid_moves(player)` sẽ dựa vào vị trí quân cờ để trả về danh sách nước đi hợp lệ cho từng người chơi.

---

**Tóm lại:**  
- game_state giúp quản lý toàn bộ bàn cờ và quân cờ.
- get_piece(row, col) là công cụ để truy xuất vị trí và thông tin quân cờ trên bàn.
- Bạn có thể duyệt bàn cờ, kiểm tra vị trí, loại quân, và sử dụng thông tin này cho AI hoặc giao diện.

---

### 4.10. Mô tả cách Minimax và Alpha-Beta hoạt động trên bàn cờ

1. **Xác định vị trí quân cờ:**  
   - AI sử dụng trạng thái bàn cờ (game_state) để biết vị trí từng quân cờ, loại quân, màu quân.
   - Các hàm như `get_piece(row, col)` giúp truy xuất quân cờ tại vị trí cụ thể.

2. **Đánh giá nước đi:**  
   - AI duyệt tất cả nước đi hợp lệ bằng hàm `get_valid_moves(player)`.
   - Với mỗi nước đi, AI giả lập trạng thái bàn cờ mới bằng `move_piece`.
   - Đánh giá bàn cờ bằng hàm `evaluate_board(game_state)`, dựa trên giá trị quân cờ (hậu, xe, mã, tốt...) và vị trí chiến lược.

3. **Quy trình Minimax:**  
   - Ở mỗi lượt, AI sẽ thử tất cả nước đi, giả lập phản ứng của đối thủ, tiếp tục cho đến độ sâu nhất định (depth).
   - Ở mỗi trạng thái, AI tính điểm số bàn cờ và chọn nước đi tối ưu nhất.

4. **Quy trình Alpha-Beta:**  
   - Khi duyệt cây nước đi, nếu điểm số của một nhánh không thể tốt hơn nhánh đã duyệt, thuật toán sẽ bỏ qua nhánh đó để tiết kiệm thời gian.

---

**Ví dụ đánh giá nước đi:**
- Nếu AI có thể ăn quân hậu ♛ của đối thủ, điểm số sẽ tăng mạnh.
- Nếu AI di chuyển quân tốt ♙ lên gần phong cấp, điểm số cũng tăng.
- Nếu AI bị chiếu hết, điểm số sẽ rất thấp.

---

**Tóm lại:**  
Minimax giúp AI "nhìn trước" nhiều lượt, đánh giá từng trạng thái bàn cờ, chọn nước đi tối ưu. Alpha-Beta Pruning giúp quá trình này nhanh hơn bằng cách loại bỏ các nhánh không cần thiết.  
AI xác định vị trí quân cờ và đánh giá nước đi dựa vào trạng thái bàn cờ, giá trị quân, và các hàm kiểm tra luật trong game_state.


