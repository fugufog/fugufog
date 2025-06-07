import threading  # 导入线程模块
import tkinter as tk

from tkinter import ttk, messagebox
from shutdown_logic import schedule_shutdown, cancel_shutdown

class ShutdownAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("定时关机软件")
        self.root.geometry("400x250")  # 调整窗口大小
        self.root.configure(bg="#f0f0f0")  # 设置背景颜色

        # 设置主题（使用ttk的现代主题）
        self.style = ttk.Style()
        self.style.theme_use("clam")  # 可选主题：clam, alt, default, classic

        # 添加图标（需要准备一个ico文件）
        try:
            self.root.iconbitmap("icon.ico")  # 图标文件路径
        except:
            pass  # 如果图标文件不存在，忽略

        # 添加标题
        self.title_label = ttk.Label(root, text="定时关机软件", font=("Arial", 16, "bold"), background="#f0f0f0")
        self.title_label.pack(pady=10)

        # 添加输入框和标签
        self.input_frame = ttk.Frame(root)
        self.input_frame.pack(pady=10)

        self.label = ttk.Label(self.input_frame, text="请输入定时关机的分钟数：", font=("Arial", 12))
        self.label.grid(row=0, column=0, padx=5, pady=5)

        self.entry = ttk.Entry(self.input_frame, font=("Arial", 12), width=10)
        self.entry.grid(row=0, column=1, padx=5, pady=5)

        # 添加按钮
        self.button_frame = ttk.Frame(root)
        self.button_frame.pack(pady=20)

        self.shutdown_button = ttk.Button(self.button_frame, text="定时关机", style="TButton", command=self.on_shutdown)
        self.shutdown_button.grid(row=0, column=0, padx=10)

        self.cancel_button = ttk.Button(self.button_frame, text="取消关机", style="TButton", command=self.on_cancel)
        self.cancel_button.grid(row=0, column=1, padx=10)

        # 自定义按钮样式
        self.style.configure("TButton", font=("Arial", 12), padding=10, background="#4CAF50", foreground="white")
        self.style.map("TButton", background=[("active", "#45a049")])

    def on_shutdown(self):
        """
        定时关机按钮点击事件
        """
        try:
            minutes = int(self.entry.get())
            if minutes <= 0:
                messagebox.showerror("错误", "请输入一个大于0的数字！")
                return

            # 使用子线程执行定时关机逻辑
            shutdown_thread = threading.Thread(target=self.run_shutdown, args=(minutes,))
            shutdown_thread.start()

            messagebox.showinfo("成功", f"系统将在 {minutes} 分钟后关闭。")
            self.root.destroy()  # 关闭窗口
        except ValueError as e:
            messagebox.showerror("错误", str(e))

    def run_shutdown(self, minutes):
        """
        在子线程中执行定时关机逻辑
        """
        import time
        from shutdown_logic import schedule_shutdown
        time.sleep(minutes * 60)  # 等待指定时间
        schedule_shutdown(minutes)

    def on_cancel(self):
        """
        取消关机按钮点击事件
        """
        from shutdown_logic import cancel_shutdown
        cancel_shutdown()
        messagebox.showinfo("成功", "定时关机已取消！")