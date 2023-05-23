import tkinter as tk

# 주 프로그램부
root_win = tk.Tk()                  # 기본 윈도우 객체 반환
root_win.title('나의 첫 윈도우')    # 제목표시줄에 윈도우 제목 표시
root_win.geometry('500x200-0+50')   # 윈도우의 크기 및 위치 설정
root_win.resizable(width=False, height=False)

# 화면 구성 및 이벤트 처리
# ...

root_win.mainloop()   # 윈도우에서 다양한 이벤트 처리 시작을 지시
