import tkinter as tk
from PIL import Image, ImageTk
import sys
import importlib
import os

class ChessInterface:
    def __init__(self):
        # Tạo cửa sổ chính
        self.root = tk.Tk()
        self.root.title("Cờ Vua")
        # Đặt kích thước ban đầu, nhưng cửa sổ có thể thay đổi kích thước
        self.root.geometry("1000x800")
        self.root.minsize(600, 480) # Đặt kích thước tối thiểu

        # Khởi tạo các biến lưu trữ widget và ảnh
        self.original_background_image = None
        self.background_photo = None
        self.button_solo = None
        self.button_play_with_AI = None
        self.button_exit = None
        self._resize_job = None

        # Tạo Canvas để vẽ giao diện, nó sẽ lấp đầy cửa sổ
        self.canvas = tk.Canvas(self.root, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Tải và hiển thị các thành phần UI
        self.load_background_image()
        self.create_choice_buttons()

        # Gán sự kiện thay đổi kích thước cho canvas
        self.canvas.bind("<Configure>", self.on_resize)

    def load_background_image(self):
        """Tải ảnh nền từ file và lưu ảnh gốc."""
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            image_path = os.path.join(current_dir, "images", "BG.png")
            
            self.original_background_image = Image.open(image_path)
            # Tạo một item ảnh trên canvas với tag "background" để cập nhật sau
            self.canvas.create_image(0, 0, anchor="nw", tags="background")

        except FileNotFoundError:
            print(f"Không tìm thấy file ảnh nền tại: {image_path}")
            self.original_background_image = None
            self.canvas.configure(bg="white")
        except Exception as e:
            print(f"Lỗi khi tải ảnh nền: {e}")
            self.original_background_image = None
            self.canvas.configure(bg="white")

    def create_choice_buttons(self):
        """Tạo tiêu đề và các nút bấm ban đầu."""
        # Widget cha là canvas
        parent_widget = self.canvas

        # --- Vẽ Tiêu đề "Chơi Cờ Vua" - sẽ được định vị lại trong on_resize ---
        parent_widget.create_text(0, 0, text="Chơi Cờ Vua",
                                  font=("Gill Sans Nova Ultra Bold", 40, "bold"),
                                  fill="black", anchor="center", tags="title")

        # --- Nút Chơi Đôi ---
        self.button_solo = tk.Button(self.root,
                                text="Chơi Đôi",
                                command=self.button_clicked_solo,
                                activebackground="#3399ff", activeforeground="white",
                                anchor="center", bd=3, bg="#00FF00", cursor="hand2",
                                disabledforeground="gray", fg="black", font=("Arial", 12, "bold"),
                                height=2, highlightbackground="black", highlightcolor="green",
                                highlightthickness=2, justify="center", overrelief="raised",
                                padx=10, pady=5, width=15, wraplength=100)
        parent_widget.create_window(0, 0, window=self.button_solo, anchor="center", tags="solo_button")

        # --- Nút Chơi với AI ---
        self.button_play_with_AI = tk.Button(self.root,
                                        text="Chơi với AI",
                                        command=self.button_clicked_AI,
                                        activebackground="#3399ff", activeforeground="white",
                                        anchor="center", bd=3, bg="#00FF00", cursor="hand2",
                                        disabledforeground="gray", fg="black", font=("Arial", 12, "bold"),
                                        height=2, highlightbackground="black", highlightcolor="green",
                                        highlightthickness=2, justify="center", overrelief="raised",
                                        padx=10, pady=5, width=15, wraplength=100)
        parent_widget.create_window(0, 0, window=self.button_play_with_AI, anchor="center", tags="ai_button")

        # --- Nút Thoát ---
        self.button_exit = tk.Button(self.root,
                                text="Thoát",
                                command=self.button_clicked_exit,
                                activebackground="#59080A", activeforeground="white",
                                anchor="center", bd=3, bg="#E33539", cursor="hand2",
                                disabledforeground="gray", fg="black", font=("Arial", 12, "bold"),
                                height=2, highlightbackground="black", highlightcolor="green",
                                highlightthickness=2, justify="center", overrelief="raised",
                                padx=10, pady=5, width=15, wraplength=100)
        parent_widget.create_window(0, 0, window=self.button_exit, anchor="center", tags="exit_button")

    def on_resize(self, event):
        """
        Xử lý sự kiện thay đổi kích thước cửa sổ.
        Sử dụng debounce để tránh gọi lại hàm quá nhiều lần khi người dùng kéo thả.
        """
        if self._resize_job:
            self.root.after_cancel(self._resize_job)
        self._resize_job = self.root.after(50, self.perform_resize)

    def perform_resize(self):
        """Thực hiện việc thay đổi kích thước và vị trí các widget."""
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        if width < 10 or height < 10: # Bỏ qua nếu cửa sổ quá nhỏ
            return

        # 1. Cập nhật ảnh nền
        if self.original_background_image:
            # Thay đổi kích thước ảnh để vừa với canvas
            resized_image = self.original_background_image.resize((width, height), Image.LANCZOS)
            self.background_photo = ImageTk.PhotoImage(resized_image)
            self.canvas.itemconfig("background", image=self.background_photo)
            self.canvas.coords("background", 0, 0)

        # 2. Cập nhật Tiêu đề (Vị trí và Kích thước Font)
        # Kích thước font chữ co dãn theo chiều cao cửa sổ, có giới hạn min/max
        title_font_size = max(20, min(int(height / 15), 60))
        self.canvas.itemconfig("title", font=("Gill Sans Nova Ultra Bold", title_font_size, "bold"))
        self.canvas.coords("title", width / 2, height * 0.4)

        # 3. Cập nhật các nút (Vị trí và Kích thước Font)
        button_font_size = max(8, min(int(height / 40), 16))
        button_y = height * 0.60  # Vị trí Y của các nút
        button_spacing = width / 5.5 # Khoảng cách giữa các nút

        button_font = ("Arial", button_font_size, "bold")
        self.button_solo.config(font=button_font)
        self.button_play_with_AI.config(font=button_font)
        self.button_exit.config(font=button_font)
        
        center_x = width / 2
        self.canvas.coords("solo_button", center_x - button_spacing, button_y)
        self.canvas.coords("ai_button", center_x, button_y)
        self.canvas.coords("exit_button", center_x + button_spacing, button_y)

    def button_clicked_solo(self):
        # Chuyển đến chế độ chơi solo (2 người chơi)
        self.root.destroy()
        try:
            # Import và chạy chess_gui với chế độ 'solo'
            import chess_gui
            chess_gui.main(game_mode='solo')
        except ImportError:
            print("Không tìm thấy file chess_gui.py")
        except Exception as e:
            print(f"Lỗi khi khởi động game: {e}")

    def button_clicked_AI(self):
        # Chuyển đến màn hình chọn màu quân cờ
        self.show_color_selection_screen()

    def show_color_selection_screen(self):
        """Hiển thị màn hình chọn màu quân cờ cho chế độ chơi với AI."""
        # Xóa tất cả các widget hiện tại
        self.canvas.delete("all")
        
        # Tải lại ảnh nền
        if self.original_background_image:
            width = self.canvas.winfo_width()
            height = self.canvas.winfo_height()
            if width > 10 and height > 10:
                resized_image = self.original_background_image.resize((width, height), Image.LANCZOS)
                self.background_photo = ImageTk.PhotoImage(resized_image)
                self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw", tags="background")
        
        # Tạo tiêu đề "Chọn Màu Quân Cờ"
        title_font_size = max(20, min(int(self.canvas.winfo_height() / 15), 60))
        self.canvas.create_text(self.canvas.winfo_width() / 2, self.canvas.winfo_height() * 0.3, 
                               text="Chọn Màu Quân Cờ", 
                               font=("Gill Sans Nova Ultra Bold", title_font_size, "bold"),
                               fill="black", anchor="center", tags="color_title")
        
        # Tạo nút "White" (Trắng)
        button_font_size = max(8, min(int(self.canvas.winfo_height() / 40), 16))
        button_font = ("Arial", button_font_size, "bold")
        
        self.button_white = tk.Button(self.root,
                                     text="White",
                                     command=self.select_white,
                                     activebackground="#3399ff", activeforeground="white",
                                     anchor="center", bd=3, bg="#FFFFFF", cursor="hand2",
                                     disabledforeground="gray", fg="black", font=button_font,
                                     height=2, highlightbackground="black", highlightcolor="green",
                                     highlightthickness=2, justify="center", overrelief="raised",
                                     padx=10, pady=5, width=15, wraplength=100)
        
        # Tạo nút "Black" (Đen)
        self.button_black = tk.Button(self.root,
                                     text="Black",
                                     command=self.select_black,
                                     activebackground="#3399ff", activeforeground="white",
                                     anchor="center", bd=3, bg="#000000", cursor="hand2",
                                     disabledforeground="gray", fg="white", font=button_font,
                                     height=2, highlightbackground="black", highlightcolor="green",
                                     highlightthickness=2, justify="center", overrelief="raised",
                                     padx=10, pady=5, width=15, wraplength=100)
        
        # Đặt vị trí các nút
        center_x = self.canvas.winfo_width() / 2
        button_y = self.canvas.winfo_height() * 0.6
        button_spacing = self.canvas.winfo_width() / 6
        
        self.canvas.create_window(center_x - button_spacing, button_y, 
                                 window=self.button_white, anchor="center", tags="white_button")
        self.canvas.create_window(center_x + button_spacing, button_y, 
                                 window=self.button_black, anchor="center", tags="black_button")
        
        # Tạo nút "Quay Lại"
        self.button_back = tk.Button(self.root,
                                    text="Quay Lại",
                                    command=self.back_to_main_menu,
                                    activebackground="#59080A", activeforeground="white",
                                    anchor="center", bd=3, bg="#E33539", cursor="hand2",
                                    disabledforeground="gray", fg="black", font=button_font,
                                    height=2, highlightbackground="black", highlightcolor="green",
                                    highlightthickness=2, justify="center", overrelief="raised",
                                    padx=10, pady=5, width=15, wraplength=100)
        
        self.canvas.create_window(center_x, button_y + 80, 
                                 window=self.button_back, anchor="center", tags="back_button")

    def select_white(self):
        """Xử lý khi người chơi chọn màu trắng."""
        print("Người chơi đã chọn màu trắng")
        # Ở đây bạn có thể thêm logic để khởi động game với AI, người chơi đi trước
        self.start_ai_game("white")

    def select_black(self):
        """Xử lý khi người chơi chọn màu đen."""
        print("Người chơi đã chọn màu đen")
        # Ở đây bạn có thể thêm logic để khởi động game với AI, AI đi trước
        self.start_ai_game("black")

    def start_ai_game(self, player_color):
        """Khởi động game với AI."""
        self.root.destroy()
        try:
            # Import và chạy chess_gui với tham số chế độ chơi và màu quân cờ
            import chess_gui
            chess_gui.main(game_mode='ai', player_color=player_color)
        except ImportError:
            print("Không tìm thấy file chess_gui.py")
        except Exception as e:
            print(f"Lỗi khi khởi động game: {e}")

    def back_to_main_menu(self):
        """Quay lại màn hình chính."""
        # Xóa tất cả các widget hiện tại
        self.canvas.delete("all")
        
        # Tải lại ảnh nền
        if self.original_background_image:
            width = self.canvas.winfo_width()
            height = self.canvas.winfo_height()
            if width > 10 and height > 10:
                resized_image = self.original_background_image.resize((width, height), Image.LANCZOS)
                self.background_photo = ImageTk.PhotoImage(resized_image)
                self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw", tags="background")
        
        # Tạo lại các nút ban đầu
        self.create_choice_buttons()
        
        # Cập nhật vị trí các nút
        self.perform_resize()

    def button_clicked_exit(self):
        # Đóng cửa sổ và thoát chương trình
        self.root.destroy()
        sys.exit()

    def run(self):
        # Chạy ứng dụng
        self.root.mainloop()

if __name__ == "__main__":
    app = ChessInterface()
    app.run()