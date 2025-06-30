import chess_engine
import pygame as py
import os
import time
import datetime
import sys

import ai_engine
from enums import Player

"""Các biến cấu hình cho giao diện"""
STATUS_BAR_HEIGHT = 50  # Chiều cao thanh trạng thái
WIDTH = HEIGHT = 565    # Chiều rộng và chiều cao của bàn cờ
BOARD_WIDTH = 565       # Chiều rộng bàn cờ
BOARD_HEIGHT = 565      # Chiều cao bàn cờ
SIDEBAR_WIDTH = 200     # Chiều rộng cột bên phải
TOTAL_WIDTH = BOARD_WIDTH + SIDEBAR_WIDTH  # Tổng chiều rộng cửa sổ
DIMENSION = 8          # Kích thước bàn cờ (8x8)
SQ_SIZE = HEIGHT // DIMENSION  # Kích thước mỗi ô trên bàn cờ
MAX_FPS = 60          # FPS cho các hiệu ứng animation
IMAGES = {}           # Dictionary chứa hình ảnh các quân cờ
colors = [(240, 217, 181), (181, 136, 99)]  # Màu gỗ sáng và tối cho bàn cờ

# TODO: AI cho quân đen đã được hoàn thiện. Cần phát triển tương tự cho các chế độ khác

def load_images():
    """
    Tải hình ảnh cho tất cả các quân cờ
    Hình ảnh được scale để vừa với kích thước ô
    """
    # Lấy đường dẫn của thư mục chứa file chess_gui.py
    current_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(current_dir, "images")
    
    for p in Player.PIECES:
        image_path = os.path.join(images_dir, p + ".png")
        IMAGES[p] = py.transform.scale(py.image.load(image_path), (SQ_SIZE, SQ_SIZE))

def draw_game_state(screen, game_state, valid_moves, square_selected):
    """
    Vẽ toàn bộ bàn cờ với các quân cờ
    
    Args:
        screen: Màn hình pygame
        game_state: Trạng thái hiện tại của trò chơi cờ vua
        valid_moves: Danh sách các nước đi hợp lệ
        square_selected: Ô được chọn hiện tại
    """
    draw_squares(screen)  # Vẽ các ô bàn cờ
    highlight_square(screen, game_state, valid_moves, square_selected)  # Đánh dấu ô được chọn và nước đi hợp lệ
    draw_pieces(screen, game_state)  # Vẽ các quân cờ

def draw_squares(screen):
    """
    Vẽ bàn cờ với các ô xen kẽ hai màu
    """
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r + c) % 2]  # Xen kẽ màu sáng và tối
            rect = py.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE)
            py.draw.rect(screen, color, rect)
            py.draw.rect(screen, (100, 100, 100), rect, 1)  # Vẽ viền màu xám đậm, dày 1 px


# Code cũ đã được comment - sử dụng phiên bản mới với viền
# def draw_squares(screen):
#     ''' Draw the chess board with the alternating two colors
#     :param screen:          -- the pygame screen
#     '''
#     for r in range(DIMENSION):
#         for c in range(DIMENSION):
#             color = colors[(r + c) % 2]
#             py.draw.rect(screen, color, py.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def draw_pieces(screen, game_state):
    """
    Vẽ các quân cờ lên bàn cờ
    
    Args:
        screen: Màn hình pygame
        game_state: Trạng thái hiện tại của trò chơi cờ vua
    """
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = game_state.get_piece(r, c)
            if piece is not None and piece != Player.EMPTY:
                # Vẽ quân cờ tại vị trí tương ứng
                screen.blit(IMAGES[piece.get_player() + "_" + piece.get_name()],
                            py.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def highlight_square(screen, game_state, valid_moves, square_selected):
    """
    Đánh dấu ô được chọn và các nước đi hợp lệ
    
    Args:
        screen: Màn hình pygame
        game_state: Trạng thái hiện tại của trò chơi
        valid_moves: Danh sách các nước đi hợp lệ
        square_selected: Ô được chọn hiện tại
    """
    if square_selected != () and game_state.is_valid_piece(square_selected[0], square_selected[1]):
        row, col = square_selected
        # Kiểm tra xem quân cờ được chọn có thuộc về người chơi hiện tại không
        if (game_state.whose_turn() and game_state.get_piece(row, col).is_player(Player.PLAYER_1)) or \
           (not game_state.whose_turn() and game_state.get_piece(row, col).is_player(Player.PLAYER_2)):
            
            # Đánh dấu ô được chọn bằng màu xanh dương
            s = py.Surface((SQ_SIZE, SQ_SIZE))
            s.set_alpha(150)  # Tăng độ trong suốt để rõ hơn
            s.fill(py.Color(0, 0, 255))  # Màu xanh dương cho ô được chọn
            screen.blit(s, (col * SQ_SIZE, row * SQ_SIZE))

            # Đánh dấu các ô có thể di chuyển bằng màu xanh lá
            s.fill(py.Color(0, 255, 0, 100))  # Màu xanh lá nhạt cho các ô có thể đi
            for move in valid_moves:
                screen.blit(s, (move[1] * SQ_SIZE, move[0] * SQ_SIZE))

# Code cũ đã được comment - sử dụng phiên bản mới với màu sắc tốt hơn
# def highlight_square(screen, game_state, valid_moves, square_selected):
#     if square_selected != () and game_state.is_valid_piece(square_selected[0], square_selected[1]):
#         row = square_selected[0]
#         col = square_selected[1]
#         if (game_state.whose_turn() and game_state.get_piece(row, col).is_player(Player.PLAYER_1)) or \
#                 (not game_state.whose_turn() and game_state.get_piece(row, col).is_player(Player.PLAYER_2)):
#             # hightlight selected square
#             s = py.Surface((SQ_SIZE, SQ_SIZE))
#             s.set_alpha(100)
#             s.fill(py.Color("blue"))
#             screen.blit(s, (col * SQ_SIZE, row * SQ_SIZE))
#             # highlight move squares
#             s.fill(py.Color("green"))
#             for move in valid_moves:
#                 screen.blit(s, (move[1] * SQ_SIZE, move[0] * SQ_SIZE))


def main(game_mode, player_color=None):
    """
    Hàm chính của trò chơi
    Xử lý logic chính và vòng lặp game

    Args:
        game_mode (str): Chế độ chơi ('ai' hoặc 'solo').
        player_color (str, optional): Màu của người chơi ('white' hoặc 'black'). Mặc định là None.
    """
    # Thiết lập chế độ chơi dựa trên đầu vào từ UI
    number_of_players = 1 if game_mode == 'ai' else 2
    human_player = ''
    if number_of_players == 1:
        # 'w' cho trắng, 'b' cho đen
        human_player = 'w' if player_color == 'white' else 'b'

    # Khởi tạo pygame
    py.init()
    screen = py.display.set_mode((TOTAL_WIDTH, BOARD_HEIGHT))
    clock = py.time.Clock()
    game_state = chess_engine.game_state()
    load_images()  # Tải hình ảnh quân cờ

    # Các biến trạng thái game
    running = True
    square_selected = ()  # Theo dõi ô được chọn cuối cùng
    player_clicks = []    # Theo dõi các lần click của người chơi (hai tuple)
    valid_moves = []      # Danh sách các nước đi hợp lệ
    game_over = False     # Trạng thái kết thúc game
    
    # Biến theo dõi thời gian chơi
    game_start_time = datetime.datetime.now()
    game_end_time = None
    surrendered = False   # Trạng thái đầu hàng
    
    # Biến điều khiển luồng sau khi game kết thúc
    restart_ui = False
    
    # Biến lưu trữ vùng chữ nhật của các nút khi game kết thúc
    tro_lai_rect, thoat_rect = None, None

    # Khởi tạo AI nếu cần
    ai = None
    if number_of_players == 1:
        ai = ai_engine.chess_ai()
        game_state = chess_engine.game_state()

    # Nếu người chơi chọn quân đen và chơi với AI, AI đi trước
    if number_of_players == 1 and human_player == 'b':
        ai_move = ai.minimax_black(game_state, 3, -100000, 100000, True, Player.PLAYER_1)
        game_state.move_piece(ai_move[0], ai_move[1], True)

    # Vòng lặp chính của game
    while running:
        for e in py.event.get():
            if e.type == py.QUIT:
                running = False
            elif e.type == py.MOUSEBUTTONDOWN:
                location = py.mouse.get_pos()
                
                if game_over:
                    # Xử lý click cho các nút khi game kết thúc
                    if tro_lai_rect and tro_lai_rect.collidepoint(location):
                        running = False
                        restart_ui = True
                    elif thoat_rect and thoat_rect.collidepoint(location):
                        running = False
                        restart_ui = False # Thoát hoàn toàn
                        
                elif not game_over:
                    # Kiểm tra xem click có nằm trong vùng bàn cờ không
                    if location[0] < BOARD_WIDTH:
                        col = location[0] // SQ_SIZE   # Chuyển đổi thành tọa độ cột
                        row = location[1] // SQ_SIZE   # Chuyển đổi thành tọa độ hàng
                        
                        # Xử lý click chuột
                        if square_selected == (row, col):
                            # Nếu click vào ô đã chọn, bỏ chọn
                            square_selected = ()
                            player_clicks = []
                        else:
                            # Chọn ô mới
                            square_selected = (row, col)
                            player_clicks.append(square_selected)
                        
                        # Khi đã chọn đủ 2 ô (ô nguồn và ô đích)
                        if len(player_clicks) == 2:
                            # Kiểm tra xem nước đi có hợp lệ không
                            if (player_clicks[1][0], player_clicks[1][1]) not in valid_moves:
                                # Nước đi không hợp lệ, reset
                                square_selected = ()
                                player_clicks = []
                                valid_moves = []
                            else:
                                # Thực hiện nước đi
                                game_state.move_piece((player_clicks[0][0], player_clicks[0][1]),
                                                      (player_clicks[1][0], player_clicks[1][1]), False)
                                square_selected = ()
                                player_clicks = []
                                valid_moves = []

                                # Cập nhật màn hình ngay lập tức để hiển thị nước đi của người chơi
                                draw_game_state(screen, game_state, valid_moves, square_selected)
                                py.display.flip()

                                # AI thực hiện nước đi của mình nếu là chế độ chơi với máy
                                if number_of_players == 1:
                                    # Hiển thị thông báo AI đang suy nghĩ
                                    font = py.font.SysFont("Arial", 30, True, False)
                                    thinking_text = font.render("AI is thinking...", True, py.Color("black"))
                                    text_rect = thinking_text.get_rect(center=(BOARD_WIDTH // 2, BOARD_HEIGHT // 2))
                                    
                                    # Vẽ overlay mờ và thông báo
                                    overlay = py.Surface((BOARD_WIDTH, BOARD_HEIGHT))
                                    overlay.set_alpha(128)
                                    overlay.fill((255, 255, 255))
                                    screen.blit(overlay, (0, 0))
                                    screen.blit(thinking_text, text_rect)
                                    py.display.flip()
                                    
                                    # Đợi 2 giây để AI "suy nghĩ"
                                    time.sleep(2)
                                    
                                    if human_player == 'w':
                                        ai_move = ai.minimax_white(game_state, 3, -100000, 100000, True, Player.PLAYER_2)
                                        game_state.move_piece(ai_move[0], ai_move[1], True)
                                    elif human_player == 'b':
                                        ai_move = ai.minimax_black(game_state, 3, -100000, 100000, True, Player.PLAYER_1)
                                        game_state.move_piece(ai_move[0], ai_move[1], True)
                        else:
                            # Lấy danh sách các nước đi hợp lệ cho quân cờ được chọn
                            valid_moves = game_state.get_valid_moves((row, col))
                            if valid_moves is None:
                                valid_moves = []
                    else:
                        # Kiểm tra click vào nút đầu hàng
                        button_rect = py.Rect(BOARD_WIDTH + 30, 150, SIDEBAR_WIDTH - 60, 50)
                        if button_rect.collidepoint(location) and not surrendered and not game_over:
                            surrendered = True
                            game_over = True
            elif e.type == py.KEYDOWN:
                if e.key == py.K_r:  # Phím R để reset game
                    game_over = False
                    game_state = chess_engine.game_state()
                    valid_moves = []
                    square_selected = ()
                    player_clicks = []
                    valid_moves = []
                    surrendered = False
                    game_start_time = datetime.datetime.now()
                    game_end_time = None
                elif e.key == py.K_u:  # Phím U để undo nước đi
                    game_state.undo_move()
                    print(len(game_state.move_log))
                elif e.key == py.K_s:  # Phím S để đầu hàng
                    if not game_over:
                        surrendered = True
                        game_over = True

        # Vẽ trạng thái game
        draw_game_state(screen, game_state, valid_moves, square_selected)
        
        # Vẽ cột bên phải với bảng thời gian và nút đầu hàng
        draw_sidebar(screen, game_start_time, surrendered, game_over, game_end_time)

        # Kiểm tra trạng thái kết thúc game và vẽ màn hình kết thúc
        was_game_running = not game_over
        
        if surrendered:
            game_over = True
            draw_text(screen, "Ban da thua AI!", color=py.Color("white"), background_alpha=128)
        else:
            endgame = game_state.checkmate_stalemate_checker()
            if endgame == 0:  # Quân đen thắng
                game_over = True
                draw_text(screen, "Quân đen thắng.")
            elif endgame == 1:  # Quân trắng thắng
                game_over = True
                draw_text(screen, "Quân trắng thắng.")
            elif endgame == 2:  # Hòa (stalemate)
                game_over = True
                draw_text(screen, "Hòa (Stalemate).")

        # Nếu game vừa mới kết thúc, ghi lại thời gian
        if game_over and was_game_running:
            game_end_time = datetime.datetime.now()
        
        # Nếu game đã kết thúc, vẽ các nút lựa chọn
        if game_over:
            tro_lai_rect, thoat_rect = draw_end_game_buttons(screen)
            
        clock.tick(MAX_FPS)  # Giới hạn FPS
        py.display.flip()    # Cập nhật màn hình
    
    # Sau khi vòng lặp kết thúc, thoát pygame
    py.quit()

    # Nếu người dùng chọn trở lại, khởi chạy lại giao diện chính
    if restart_ui:
        import chess_UX_UI
        app = chess_UX_UI.ChessInterface()
        app.run()

def draw_status_bar(screen, game_state):
    """
    Vẽ thanh trạng thái hiển thị thông tin về lượt chơi và trạng thái chiếu
    
    Args:
        screen: Màn hình pygame
        game_state: Trạng thái hiện tại của trò chơi
    """
    font = py.font.SysFont("Arial", 24, True, False)
    text = ""
    
    # Hiển thị thông tin về trạng thái chiếu hoặc lượt chơi
    if game_state.is_in_check():
        if game_state.whose_turn():
            text = "White is in Check"
        else:
            text = "Black is in Check"
    else:
        if game_state.whose_turn():
            text = "White's Turn"
        else:
            text = "Black's Turn"
    
    # Vẽ thanh trạng thái
    text_obj = font.render(text, True, py.Color("black"))
    rect = py.Rect(0, WIDTH, WIDTH, STATUS_BAR_HEIGHT)
    py.draw.rect(screen, (200, 200, 200), rect)  # Nền xám nhạt
    screen.blit(text_obj, (10, WIDTH + (STATUS_BAR_HEIGHT - text_obj.get_height()) // 2))

    # Code cũ đã được comment - sử dụng logic mới hiệu quả hơn
    # elif human_player is 'w':
    #     ai = ai_engine.chess_ai()
    #     game_state = chess_engine.game_state()
    #     valid_moves = []
    #     while running:
    #         for e in py.event.get():
    #             if e.type == py.QUIT:
    #                 running = False
    #             elif e.type == py.MOUSEBUTTONDOWN:
    #                 if not game_over:
    #                     location = py.mouse.get_pos()
    #                     col = location[0] // SQ_SIZE
    #                     row = location[1] // SQ_SIZE
    #                     if square_selected == (row, col):
    #                         square_selected = ()
    #                         player_clicks = []
    #                     else:
    #                         square_selected = (row, col)
    #                         player_clicks.append(square_selected)
    #                     if len(player_clicks) == 2:
    #                         if (player_clicks[1][0], player_clicks[1][1]) not in valid_moves:
    #                             square_selected = ()
    #                             player_clicks = []
    #                             valid_moves = []
    #                         else:
    #                             game_state.move_piece((player_clicks[0][0], player_clicks[0][1]),
    #                                                   (player_clicks[1][0], player_clicks[1][1]), False)
    #                             square_selected = ()
    #                             player_clicks = []
    #                             valid_moves = []
    #
    #                             ai_move = ai.minimax(game_state, 3, -100000, 100000, True, Player.PLAYER_2)
    #                             game_state.move_piece(ai_move[0], ai_move[1], True)
    #                     else:
    #                         valid_moves = game_state.get_valid_moves((row, col))
    #                         if valid_moves is None:
    #                             valid_moves = []
    #             elif e.type == py.KEYDOWN:
    #                 if e.key == py.K_r:
    #                     game_over = False
    #                     game_state = chess_engine.game_state()
    #                     valid_moves = []
    #                     square_selected = ()
    #                     player_clicks = []
    #                     valid_moves = []
    #                 elif e.key == py.K_u:
    #                     game_state.undo_move()
    #                     print(len(game_state.move_log))
    #         draw_game_state(screen, game_state, valid_moves, square_selected)
    #
    #         endgame = game_state.checkmate_stalemate_checker()
    #         if endgame == 0:
    #             game_over = True
    #             draw_text(screen, "Black wins.")
    #         elif endgame == 1:
    #             game_over = True
    #             draw_text(screen, "White wins.")
    #         elif endgame == 2:
    #             game_over = True
    #             draw_text(screen, "Stalemate.")
    #
    #         clock.tick(MAX_FPS)
    #         py.display.flip()
    #
    # elif human_player is 'b':
    #     pass


def draw_text(screen, text, color=py.Color("black"), background_alpha=None):
    """
    Vẽ văn bản lên màn hình, có thể có nền mờ.
    
    Args:
        screen: Màn hình pygame
        text: Văn bản cần hiển thị
        color: Màu sắc của văn bản
        background_alpha (int, optional): Độ trong suốt của lớp phủ nền (0-255).
    """
    # Vẽ lớp phủ mờ nếu được yêu cầu
    if background_alpha is not None:
        overlay = py.Surface((BOARD_WIDTH, BOARD_HEIGHT))
        overlay.set_alpha(background_alpha)
        overlay.fill((0, 0, 0))  # Lớp phủ màu đen
        screen.blit(overlay, (0, 0))
        
    font = py.font.SysFont("Arial", 40, True, False)
    text_object = font.render(text, True, color)
    text_location = text_object.get_rect(center=(BOARD_WIDTH // 2, BOARD_HEIGHT // 2))
    screen.blit(text_object, text_location)

def draw_game_time(screen, start_time):
    """
    Hiển thị thời gian đã chơi ở góc trên bên phải màn hình
    
    Args:
        screen: Màn hình pygame
        start_time: Thời điểm bắt đầu game
    """
    current_time = datetime.datetime.now()
    elapsed_time = current_time - start_time
    minutes = int(elapsed_time.total_seconds() // 60)
    seconds = int(elapsed_time.total_seconds() % 60)
    
    time_text = f"Thời gian: {minutes:02d}:{seconds:02d}"
    font = py.font.SysFont("Arial", 16, True, False)
    text_object = font.render(time_text, True, py.Color("black"))
    screen.blit(text_object, (WIDTH - text_object.get_width() - 10, 10))

def draw_controls(screen):
    """
    Hiển thị hướng dẫn phím tắt ở góc dưới bên trái màn hình
    """
    controls_text = [
        "R: Reset game",
        "U: Undo move", 
        "S: Surrender"
    ]
    
    font = py.font.SysFont("Arial", 12, True, False)
    y_position = HEIGHT - 60
    
    for i, text in enumerate(controls_text):
        text_object = font.render(text, True, py.Color("black"))
        screen.blit(text_object, (10, y_position + i * 15))

def draw_sidebar(screen, start_time, surrendered, game_over, game_end_time):
    """
    Vẽ cột bên phải với bảng thời gian và nút đầu hàng
    
    Args:
        screen: Màn hình pygame
        start_time: Thời điểm bắt đầu game
        surrendered: Trạng thái đầu hàng
        game_over: Trạng thái kết thúc game
        game_end_time: Thời điểm kết thúc game
    """
    # Vẽ nền cột bên phải
    sidebar_rect = py.Rect(BOARD_WIDTH, 0, SIDEBAR_WIDTH, BOARD_HEIGHT)
    py.draw.rect(screen, (240, 240, 240), sidebar_rect)  # Màu xám nhạt
    py.draw.rect(screen, (100, 100, 100), sidebar_rect, 2)  # Viền
    
    # Vẽ tiêu đề "Bảng Thời Gian"
    title_font = py.font.SysFont("Arial", 22, True, False)
    title_text = title_font.render("TIMER", True, py.Color("black"))
    title_rect = title_text.get_rect(center=(BOARD_WIDTH + SIDEBAR_WIDTH // 2, 30))
    screen.blit(title_text, title_rect)
    
    # Tính và hiển thị thời gian
    end_time = game_end_time if game_end_time else datetime.datetime.now()
    elapsed_time = end_time - start_time
    minutes = int(elapsed_time.total_seconds() // 60)
    seconds = int(elapsed_time.total_seconds() % 60)
    
    time_font = py.font.SysFont("Arial", 30, True, False)
    time_text = f"{minutes:02d}:{seconds:02d}"
    time_surface = time_font.render(time_text, True, py.Color("black"))
    time_rect = time_surface.get_rect(center=(BOARD_WIDTH + SIDEBAR_WIDTH // 2, 80))
    
    # Vẽ khung thời gian
    time_box_rect = py.Rect(BOARD_WIDTH + 20, 60, SIDEBAR_WIDTH - 40, 40)
    py.draw.rect(screen, (255, 255, 255), time_box_rect)  # Nền trắng
    py.draw.rect(screen, (0, 0, 0), time_box_rect, 2)  # Viền đen
    screen.blit(time_surface, time_rect)
    
    # Vẽ nút đầu hàng
    surrender_font = py.font.SysFont("Arial", 20, True, False)
    if surrendered or game_over:
        # Nút bị vô hiệu hóa
        button_color = (150, 150, 150)
        text_color = (100, 100, 100)
        button_text = "Dau Hang"
    else:
        # Nút hoạt động
        button_color = (220, 50, 50)
        text_color = (255, 255, 255)
        button_text = "Dau Hang"
    
    # Vẽ nút đầu hàng
    button_rect = py.Rect(BOARD_WIDTH + 30, 150, SIDEBAR_WIDTH - 60, 50)
    py.draw.rect(screen, button_color, button_rect)
    py.draw.rect(screen, (0, 0, 0), button_rect, 2)
    
    surrender_surface = surrender_font.render(button_text, True, text_color)
    surrender_text_rect = surrender_surface.get_rect(center=button_rect.center)
    screen.blit(surrender_surface, surrender_text_rect)
    
    # Vẽ hướng dẫn phím tắt
    controls_font = py.font.SysFont("Arial", 16, True, False)
    controls_text = [
        "Keys:   ",
        "R:   Reset",
        "U:   Undo"
    ]
    
    y_start = 250
    for i, text in enumerate(controls_text):
        text_surface = controls_font.render(text, True, py.Color("black"))
        screen.blit(text_surface, (BOARD_WIDTH + 20, y_start + i * 20))

def draw_end_game_buttons(screen):
    """
    Vẽ các nút "Trở lại" và "Thoát" khi game kết thúc.
    """
    button_font = py.font.SysFont("Arial", 20, True, False)
    button_y = BOARD_HEIGHT // 2 + 80
    button_width = 150
    button_height = 50
    spacing = 30
    center_x = BOARD_WIDTH // 2

    # Nút Trở Lại
    tro_lai_rect = py.Rect(center_x - button_width - spacing // 2, button_y, button_width, button_height)
    py.draw.rect(screen, (0, 150, 50), tro_lai_rect, border_radius=8)
    py.draw.rect(screen, (255, 255, 255), tro_lai_rect, 2, border_radius=8)
    tro_lai_text = button_font.render("Tro Lai", True, py.Color("white"))
    tro_lai_text_rect = tro_lai_text.get_rect(center=tro_lai_rect.center)
    screen.blit(tro_lai_text, tro_lai_text_rect)

    # Nút Thoát
    thoat_rect = py.Rect(center_x + spacing // 2, button_y, button_width, button_height)
    py.draw.rect(screen, (200, 50, 50), thoat_rect, border_radius=8)
    py.draw.rect(screen, (255, 255, 255), thoat_rect, 2, border_radius=8)
    thoat_text = button_font.render("Thoat", True, py.Color("white"))
    thoat_text_rect = thoat_text.get_rect(center=thoat_rect.center)
    screen.blit(thoat_text, thoat_text_rect)

    return tro_lai_rect, thoat_rect

if __name__ == "__main__":
    # Giao diện chính của game được chạy từ chess_UX_UI.py
    # Bạn có thể bỏ comment ở các dòng dưới để test nhanh các chế độ
    # main('solo')
    # main('ai', 'white')
    pass
