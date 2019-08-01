



#联系tkinter

import tkinter

import tkinter.messagebox

def main():

    flag = False


    #顶层窗口
    top = tkinter.Tk()

    #窗口大小
    top.geometry('360x360')

    #标题
    top.title('游戏')

    #创建标签对象并添加到顶层窗口
    label = tkinter.Label(top,text = 'hello,world',font = 'Arial -32',fg = 'red')
    label.pack(expand = 1)

    #创建一个装按钮的容器
    panel = tkinter.Frame(top)

    #修改标签上的文字
    def change_lable_text():
        nonlocal flag
        color,msg= ('green','hello,world')\
            if flag else ('blue','goodbye,world')
        label.config(text=msg,fg=color)

    #确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示','确定要退出么？'):
            top.quit()




    #创建按钮对象，指定添加到哪个容器 通过command参数绑定事件回调函数
    button1 = tkinter.Button(panel,text = '修改',command = change_lable_text)
    button1.pack(side = 'left')
    button2 = tkinter.Button(panel,text = '退出',command = confirm_to_quit)
    button2.pack(side = 'right')
    panel.pack(side = 'bottom')

    #开启主循环
    tkinter.mainloop()


if __name__ == '__main__':
    main()