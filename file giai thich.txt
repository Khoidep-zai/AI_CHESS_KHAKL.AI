=====================================================
Giải thích chi tiết từng file trong dự án Chess Game
=====================================================
1. enums.py - File định nghĩa hằng số
    Mục đích: Định nghĩa các hằng số cơ bản cho trò chơi
    Nội dung chính:
    Player.PLAYER_1 = 'white': Định nghĩa người chơi 1 (quân trắng)
    Player.PLAYER_2 = 'black': Định nghĩa người chơi 2 (quân đen)
    Player.EMPTY = -9: Định nghĩa ô trống trên bàn cờ
    Player.PIECES: Danh sách tất cả các loại quân cờ (r: xe, n: mã, b: tượng, q: hậu, k: vua, p: tốt)

2. Piece.py - File định nghĩa các quân cờ
    Mục đích: Chứa các lớp định nghĩa từng loại quân cờ và luật di chuyển
    Các lớp chính:
    Piece: Lớp cơ sở cho tất cả quân cờ
    Rook: Xe - di chuyển theo hàng ngang và dọc
    Knight: Mã - di chuyển theo hình chữ L
    Bishop: Tượng - di chuyển theo đường chéo
    Queen: Hậu - kết hợp khả năng của Xe và Tượng
    King: Vua - di chuyển 1 ô theo mọi hướng
    Pawn: Tốt - di chuyển tiến và ăn chéo
    Chức năng: Mỗi lớp có các phương thức để tính toán nước đi hợp lệ

3. chess_engine.py - File động cơ trò chơi chính
    Mục đích: Quản lý logic trò chơi, trạng thái bàn cờ và luật chơi
    Các thành phần chính:
    game_state: Lớp quản lý trạng thái trò chơi
    Khởi tạo bàn cờ 8x8 với vị trí ban đầu
    Quản lý lượt chơi (trắng/đen)
    Kiểm tra chiếu, chiếu hết, hòa
    Xử lý nhập thành, bắt tốt qua đường
    Lưu trữ lịch sử nước đi
    chess_move: Lớp đại diện cho một nước đi
    Chức năng: Xử lý tất cả logic game, kiểm tra tính hợp lệ của nước đi

4. chess_gui.py - File giao diện đồ họa chính
    Mục đích: Tạo giao diện người dùng bằng Pygame
    Các thành phần chính:
    load_images(): Tải hình ảnh các quân cờ
    draw_game_state(): Vẽ bàn cờ và quân cờ
    draw_squares(): Vẽ các ô bàn cờ xen kẽ
    highlight_square(): Đánh dấu ô được chọn và nước đi hợp lệ
    main(): Hàm chính xử lý vòng lặp game
    Chức năng: Xử lý tương tác chuột, hiển thị trạng thái game, điều khiển luồng chơi

5. ai_engine.py - File động cơ AI
    Mục đích: Cung cấp trí tuệ nhân tạo cho trò chơi
    Thuật toán sử dụng:
    Minimax: Thuật toán tìm kiếm nước đi tốt nhất
    Alpha-Beta Pruning: Tối ưu hóa tìm kiếm minimax
    Các phương thức chính:
    minimax_white(): AI cho quân trắng
    minimax_black(): AI cho quân đen
    evaluate_board(): Đánh giá trạng thái bàn cờ
    Chức năng: Tính toán nước đi tốt nhất cho AI dựa trên đánh giá bàn cờ

6. chess_UX_UI.py - File giao diện khởi động
    Mục đích: Tạo màn hình menu chính và chọn chế độ chơi
    Công nghệ: Sử dụng Tkinter thay vì Pygame
    Các chức năng:
    Hiển thị menu chính với 3 lựa chọn: Chơi Đôi, Chơi với AI, Thoát
    Màn hình chọn màu quân cờ khi chơi với AI
    Giao diện responsive (thay đổi kích thước theo cửa sổ)
    Chức năng: Điều hướng người dùng vào các chế độ chơi khác nhau

7. requirements.txt - File yêu cầu thư viện
    Mục đích: Liệt kê các thư viện cần thiết
    Nội dung: pygame~=2.0.0.dev8 - thư viện đồ họa chính

8. Thư mục images/
    Mục đích: Chứa hình ảnh các quân cờ và giao diện
    Nội dung: File PNG cho từng loại quân cờ (trắng/đen) và ảnh nền

9. Thư mục __pycache__
    Mục đích:
        Thư mục __pycache__ được Python tạo ra tự động để lưu trữ các file bytecode đã biên dịch (file .pyc).
    Cách hoạt động:
    1. Quá trình biên dịch:
    Khi bạn chạy file .py lần đầu, Python sẽ:
        Đọc mã nguồn từ file .py
        Biên dịch thành bytecode (mã máy)
        Lưu bytecode vào file .pyc trong thư mục __pycache__
    2. Lần chạy tiếp theo:
    Python sẽ kiểm tra xem file .pyc có tồn tại không
    Nếu có và file .py không bị thay đổi → Python sẽ chạy trực tiếp từ .pyc
    Điều này giúp tăng tốc độ khởi động chương trình
    Ví dụ cụ thể:
        __pycache__/
        ├── chess_engine.cpython-39.pyc    # Bytecode của chess_engine.py
        ├── chess_gui.cpython-39.pyc       # Bytecode của chess_gui.py
        ├── ai_engine.cpython-39.pyc       # Bytecode của ai_engine.py
        ├── Piece.cpython-39.pyc           # Bytecode của Piece.py
        └── enums.cpython-39.pyc           # Bytecode của enums.py
    Lợi ích:
        ⚡ Tăng tốc: Khởi động chương trình nhanh hơn
        💾 Tiết kiệm: Không phải biên dịch lại mã nguồn
        🔄 Tự động: Python quản lý hoàn toàn

============================
GIẢI THÍCH HOẠT ĐỘNG PROJECT CỜ VUA AI
============================

1. QUY TRÌNH HOẠT ĐỘNG TỔNG THỂ
-------------------------------
1. Người dùng chạy chương trình (thường là file giao diện như chess_UX_UI.py hoặc chess_gui.py).
2. Giao diện được tạo ra, hiển thị bàn cờ, các quân cờ.
3. Trạng thái game (bàn cờ, quân cờ, lượt chơi, lịch sử nước đi, ...) được khởi tạo thông qua lớp game_state trong chess_engine.py.
4. Người chơi hoặc AI thực hiện nước đi:
   - Người chơi chọn quân và nước đi trên giao diện.
   - Nếu có AI, AI sẽ tính toán nước đi dựa trên trạng thái hiện tại.
5. Kiểm tra nước đi hợp lệ, xử lý các luật đặc biệt (nhập thành, phong cấp, en passant, chiếu, chiếu hết, hòa...).
6. Cập nhật bàn cờ, lịch sử nước đi, trạng thái game.
7. Giao diện được cập nhật để phản ánh trạng thái mới của bàn cờ.
8. Lặp lại cho đến khi kết thúc game (chiếu hết, hòa hoặc người chơi dừng lại).

2. VAI TRÒ VÀ LIÊN KẾT CỦA TỪNG FILE
------------------------------------
- chess_engine.py: Quản lý toàn bộ trạng thái và luật chơi cờ vua (bàn cờ, quân cờ, nước đi hợp lệ, lịch sử, kiểm tra chiếu, chiếu hết, hòa, nhập thành, phong cấp, en passant...). Được sử dụng bởi các file giao diện và AI để truy xuất, cập nhật trạng thái game.

- Piece.py: Định nghĩa các lớp quân cờ (Xe, Mã, Tượng, Hậu, Vua, Tốt) và các phương thức liên quan (di chuyển, kiểm tra nước đi hợp lệ, ...). Được chess_engine.py import để khởi tạo và thao tác với các quân cờ trên bàn cờ.

- enums.py: Định nghĩa các hằng số, enum cho người chơi (Player 1, Player 2, EMPTY), giúp code dễ đọc và quản lý trạng thái. Được import vào các file khác để xác định quân cờ thuộc về ai, ô trống, v.v.

- ai_engine.py: Chứa thuật toán AI để máy tính tự động chọn nước đi (ví dụ: minimax, alpha-beta pruning, ...). Sử dụng trạng thái bàn cờ từ chess_engine.py để phân tích và chọn nước đi, sau đó trả về nước đi cho giao diện hoặc engine thực hiện.

- chess_gui.py: Xây dựng giao diện đồ họa (GUI) cho game cờ vua, hiển thị bàn cờ, quân cờ, nhận sự kiện từ người dùng (chuột, bàn phím). Giao tiếp với chess_engine.py để lấy trạng thái bàn cờ, thực hiện nước đi, cập nhật giao diện sau mỗi nước đi.

- chess_UX_UI.py: Có thể là giao diện người dùng đơn giản hơn (UX/UI), hoặc giao diện dòng lệnh, hoặc các chức năng phụ trợ cho GUI. Tương tác với chess_engine.py để điều khiển game, có thể gọi AI từ ai_engine.py nếu chơi với máy.

- images/: Chứa hình ảnh các quân cờ, bàn cờ, background phục vụ cho giao diện đồ họa. Được chess_gui.py hoặc chess_UX_UI.py sử dụng để hiển thị hình ảnh lên giao diện.

3. SƠ ĐỒ LUỒNG HOẠT ĐỘNG GIỮA CÁC FILE 
dạng ảnh:
image.png
----------------------------------------------------------
+---------------------+         +-----------------------+
|  chess_gui.py       |         |  chess_UX_UI.py       |
|  (Giao diện)        |         |  (Giao diện dòng lệnh)|
+----------+----------+         +----------+------------+
           |                               |
           |                               |
           +-----------+   +---------------+
                       |   |
                       v   v
                  +--------------------+
                  |  chess_engine.py   |
                  | (Quản lý trạng thái|
                  |  & luật chơi)      |
                  +----+-----+----+----+
                       |     |    |
         +-------------+     |    +-------------+
         |                   |                  |
         v                   v                  v
   +-----------+      +-----------+      +-------------+
   | Piece.py  |      | enums.py  |      | ai_engine.py|
   | (Lớp quân |      | (Enum,    |      | (AI chọn    |
   |  cờ)      |      |  hằng số) |      |  nước đi)   |
   +-----------+      +-----------+      +-------------+
         |                   |                  |
         +-------------------+------------------+
                             |
                             v
                      +-------------+
                      |  images/    |
                      | (Hình ảnh)  |
                      +-------------+



4. TÓM TẮT THỨ TỰ HOẠT ĐỘNG
---------------------------
1. Giao diện (GUI/UX) khởi tạo game
2. Khởi tạo trạng thái bàn cờ (chess_engine.py)
3. Tạo các quân cờ (Piece.py), enum (enums.py)
4. Người chơi hoặc AI thực hiện nước đi (ai_engine.py)
5. Kiểm tra, cập nhật trạng thái, lịch sử (chess_engine.py)
6. Cập nhật giao diện, hình ảnh (images/)
7. Tiếp tục lặp lại cho đến khi kết thúc game.

=============================================
GIẢI THÍCH THUẬT TOÁN MINIMAX TRONG AI CỜ VUA
==============================================

1. Minimax là gì?
Minimax là thuật toán tìm kiếm được dùng trong các trò chơi đối kháng (như cờ vua) để chọn nước đi tối ưu.
AI sẽ giả lập tất cả các nước đi có thể, giả định đối thủ cũng sẽ chơi tốt nhất, và chọn nước đi giúp mình có lợi nhất (hoặc đối thủ bị bất lợi nhất).
Alpha-beta pruning là kỹ thuật cắt tỉa các nhánh không cần thiết, giúp tăng tốc độ tính toán.

2. Cách hoạt động trong code của bạn
a. Hai hàm chính:
    minimax_white: Dùng khi AI điều khiển quân trắng.
    minimax_black: Dùng khi AI điều khiển quân đen.
b. Tham số đầu vào:
    game_state: Trạng thái bàn cờ hiện tại.
    depth: Độ sâu tìm kiếm (số lượt đi AI sẽ nhìn trước).
    alpha, beta: Giá trị dùng cho alpha-beta pruning.
    maximizing_player: Đang ở lượt tối đa hóa (AI) hay tối thiểu hóa (đối thủ).
    player_color: Màu quân đang xét.
c. Luồng thuật toán:
    Kiểm tra trạng thái kết thúc game:
        Nếu đã chiếu hết, thua, hòa thì trả về điểm số rất lớn/nhỏ hoặc điểm hòa.
    Điều kiện dừng:
        Nếu đạt độ sâu tối đa hoặc game kết thúc, trả về điểm đánh giá bàn cờ (evaluate_board).
    Tìm kiếm đệ quy:
        Nếu là lượt maximizing (AI):
    Duyệt tất cả nước đi hợp lệ.
    Thực hiện nước đi đó trên bàn cờ.

    Gọi đệ quy minimax với depth-1, chuyển sang lượt minimizing (đối thủ).
    Hoàn tác nước đi.
    Lưu lại giá trị lớn nhất (max).
    Cập nhật alpha, nếu beta <= alpha thì cắt nhánh (pruning).
    Nếu là lượt minimizing (đối thủ):
        Tương tự, nhưng lưu giá trị nhỏ nhất (min), cập nhật beta.
    Trả về kết quả:
        Ở độ sâu gốc (thường là depth=3), trả về nước đi tốt nhất.
        Ở các độ sâu khác, trả về điểm số tốt nhất.

**Ví dụ minh họa đơn giản:**
- AI nhìn trước 2 lượt (depth=2):
  - AI thử đi nước A, giả lập đối thủ đi các nước đáp trả A1, A2, A3...
  - AI thử đi nước B, giả lập đối thủ đi các nước đáp trả B1, B2, B3...
  - Đánh giá điểm số cuối mỗi nhánh, chọn nước đi (A hoặc B) có điểm số tốt nhất cho mình.


3. Giải thích từng bước  dễ hiểu
    AI sẽ thử tất cả các nước đi có thể của mình.
    Với mỗi nước đi, AI sẽ giả lập cho đối thủ đi tiếp, và lại tiếp tục giả lập cho mình đi, lặp lại đến khi đạt độ sâu nhất định hoặc game kết thúc.
    Ở mỗi trạng thái, AI sẽ đánh giá bàn cờ (tính điểm dựa trên số lượng, giá trị quân cờ, vị trí...).
    AI sẽ chọn nước đi giúp mình có điểm số cao nhất (nếu là maximizing) hoặc thấp nhất (nếu là minimizing).
    Nhờ alpha-beta pruning, nếu phát hiện một nhánh không thể tốt hơn nhánh đã có, AI sẽ bỏ qua nhánh đó để tiết kiệm thời gian.

4. Đánh giá bàn cờ (evaluate_board)
- Hàm này sẽ tính tổng điểm các quân cờ trên bàn, có thể cộng thêm điểm cho vị trí tốt, trừ điểm cho bị chiếu, v.v.
- Kết quả này dùng để so sánh các trạng thái bàn cờ trong minimax.

6. Tóm tắt
    * Minimax giúp AI chọn nước đi tốt nhất bằng cách giả lập nhiều lượt đi tới trước.
    * Alpha-beta pruning giúp tăng tốc bằng cách loại bỏ các nhánh không cần thiết.
    * Độ sâu càng lớn, AI càng mạnh nhưng càng chậm.

