#==========about===========

names = "Tiles磁贴"
versions = "1.1.0"

#==========import==========

from tkinter import *
from tkinter import colorchooser,messagebox,filedialog,ttk,font
from PIL import Image,ImageTk
from os import path

#===========read autosave===========

tou = 1
bcolor = "#0078d7"
fcolor = "#000000"
chang = 200
read = ""
if path.exists("autosave_text.txt"):
    with open("autosave_text.txt","r",encoding="utf-8") as read_autosave:
        read = read_autosave.read()

if path.exists("autosave_length.txt"):
    with open("autosave_length.txt","r",encoding="utf-8") as read_autosave_length:
        chang = int(read_autosave_length.read())

if path.exists("autosave_color.txt"):
    with open("autosave_color.txt","r",encoding="utf-8") as read_autosave_color:
        lines = read_autosave_color.readlines()
        bcolor = lines[0].strip("\n")
        fcolor = lines[1]

if path.exists("autosave_transparent.txt"):
    with open("autosave_transparent.txt","r",encoding="utf-8") as read_autosave_transparent:
        tou = float(read_autosave_transparent.read())

#===========main===========

root = Tk()
root.overrideredirect(1)
root.configure(bg=bcolor)
root.attributes('-alpha',tou)
root.wm_attributes('-topmost',1)
window = 1
x = 0
x1 = 0
y = 0
y1 = 0
new_x = 0
new_x1 = 0
new_y = 0
new_y1 = 0
mode = 1
he = None
se = None
st = None
lll = None
e = None
font_check = None
help_num = 0
close_window = False
root.geometry(f"{chang}x{chang}")
def on_drag_start(event):
    global x, y
    x = event.x
    y = event.y
def on_drag(event):
    global new_x,new_y
    deltax = event.x - x
    deltay = event.y - y
    new_x = root.winfo_x() + deltax
    new_y = root.winfo_y() + deltay
    root.geometry(f"{chang}x{chang}+{new_x}+{new_y}")
def on_drag_stop(event):
    global x, y
    x = 0
    y = 0
def on_drag_start1(event):
    global x1, y1
    x1 = event.x
    y1 = event.y
def on_drag1(event):
    global new_x1,new_y1
    deltax = event.x - x1
    deltay = event.y - y1
    new_x1 = he.winfo_x() + deltax
    new_y1 = he.winfo_y() + deltay
    he.geometry(f"+{new_x1}+{new_y1}")
def on_drag_stop1(event):
    global x1, y1
    x1 = 0
    y1 = 0
def help_key(event):
    global he,lll,help_num
    help_num += 1
    if help_num == 2:
        messagebox.showwarning(title="注意",message="帮助窗口开太多了，先关闭一个窗口吧。")
        help_num -= 1
        return 0
    he = Tk()
    he.wm_attributes('-topmost',1)
    he.attributes('-alpha',tou)
    into = '''按键帮助：\n右键：打开设置\n按键：退出\n鼠标滚轮：调整窗口大小'''
    he.configure(bg=bcolor)
    he.overrideredirect(1)
    he.attributes('-alpha', 1)
    he.wm_attributes('-topmost', 1)
    lll = Label(he,text=into,font=("微软雅黑",15),bg=bcolor,fg=fcolor)
    lll.pack()
    he.bind("<Key>", lambda event:he.destroy())
    he.bind("<ButtonPress-1>", on_drag_start1)
    he.bind("<B1-Motion>", on_drag1)
    he.bind("<ButtonRelease-1>", on_drag_stop1)
    he.mainloop()
def help_exit(event):
    global help_num
    he.destroy()
    help_num -= 1
def func(mess):
    mess.after(1500, lambda: mess.destroy())
menus = None
image = None
icon = None
a = 1
def ge(button,text,font):
    global a
    if a == 1:
        a = 0
        button.config(text="启用文本")
        ll.pack_forget()
    else:
        try:
            int(font.get())
        except Exception as e:
            messagebox.showerror("错误！", "错误！字体大小应为数字！\n%s" % e)
            return 0
        a = 1
        button.config(text="禁用文本")
        ll.delete("1.0",END)
        ll.insert(END,text.get("1.0",END))
        ll.config(font=("微软雅黑",int(font.get())))
        ll.pack()
def turn_font(a):
    ll.config(font=("微软雅黑", int(a)))
def windows_setting():
    global st,e
    st = Tk()
    st.wm_attributes('-topmost',1)
    st.title("窗口")
    st.wm_attributes("-toolwindow", 2)
    Label(st,text="窗口大小：").grid(row=0,column=0)
    e = Scale(st,from_=1,to=800,orient=HORIZONTAL,command=save,length=500)
    e.set(chang)
    e.grid(row=0,column=1)
    Button(st,text="默认",command=lambda:repair(e)).grid(row=0,column=2)
    Label(st,text="颜色：").grid(row=1,column=0)
    Button(st,text="窗口",command=che).grid(row=1,column=1)
    Button(st, text="文字", command=chee).grid(row=1, column=2)
    Label(st,text="透明度（1最小，10最大）：").grid(row=2,column=0)
    s = Scale(st,from_=1,to=10,orient=HORIZONTAL,command=test)
    s.set(tou*10)
    s.grid(row=2,column=1)
    Button(st,text="退出",command=exit).grid(row=3,column=0)
    Button(st, text="关于",command=about).grid(row=3, column=2)
    st.mainloop()
def repair(e):
    global chang
    e.set(200)
    chang = 200
    root.geometry("200x200")
def exit():
    root.destroy()
    try:
        he.destroy()
    except:
        pass
    try:
        se.destroy()
    except:
        pass
    try:
        st.destroy()
    except:
        pass
    try:
        font_check.destroy()
    except:
        pass
def test(a):
    global tou
    tou = int(a)/10
    root.attributes('-alpha',int(a)/10)
    try:
        he.attributes('-alpha',int(a)/10)
    except:
        pass
def save(e):
    global chang
    chang = int(e)
    root.geometry(f"{chang}x{chang}")
def che():
    global bcolor
    c = colorchooser.askcolor()
    bcolor = str(c[1]) if not c[1] == None and not c[1] == "" else bcolor
    root.configure(bg=bcolor)
    ll.config(bg=bcolor)
    b.config(bg=bcolor)
    try:
        he.configure(bg=bcolor)
        lll.config(bg=bcolor)
    except:
        pass
def chee():
    global fcolor
    c = colorchooser.askcolor()
    fcolor = str(c[1]) if not c[1] == None and not c[1] == "" else fcolor
    ll.config(fg=fcolor)
    b.config(fg=fcolor)
    try:
        lll.config(fg=fcolor)
    except:
        pass
im = Image.open("Frame 97.png")
im = im.resize((100,100))
imm = ImageTk.PhotoImage(im)
def about(name=names,version=versions):
    stt = Toplevel()
    stt.wm_attributes('-topmost',1)
    stt.title("关于")
    stt.wm_attributes("-toolwindow", 2)
    Label(stt,image=imm).pack()
    Label(stt,text="\n    %s v%s    \n    张泊桥 编程    \n" % (name,version),font=("微软雅黑",20)).pack()
    stt.mainloop()
def help():
    h = Toplevel(root)
    h.title("设置")
    h.wm_attributes('-topmost',1)
    h.wm_attributes("-toolwindow", 2)
    Button(h,text="关于程序",command=about).pack()
    Button(h, text="窗口设置",command=windows_setting).pack()
    Button(h, text="按键帮助", command=lambda:help_key(None)).pack()
    Button(h, text="退出程序",command=exit).pack()
def save_file():
    location = filedialog.asksaveasfilename(defaultextension="txt",filetypes=[("txt文件",".txt")])
    if location == "" or location == None:
        return 0
    into = ll.get("1.0",END)
    with open(location,"w",encoding="utf-8") as f:
        f.write(into)
        f.close()
def open_file():
    location = filedialog.askopenfilename(filetypes=[("txt文件",".txt")])
    if location == "" or location == None:
        return 0
    with open(location,"r",encoding="utf-8") as f:
        ll.delete("1.0",END)
        ll.insert(END,"".join(f.readlines()))
def auto_save():
    with open("autosave_text.txt","w",encoding="utf-8") as autosave_text:
        autosave_text.write(ll.get("1.0",END))
    with open("autosave_length.txt","w",encoding="utf-8") as autosave_length:
        autosave_length.write(str(chang))
    with open("autosave_color.txt","w",encoding="utf-8") as autosave_color:
        autosave_color.write(bcolor)
        autosave_color.write("\n")
        autosave_color.write(fcolor)
    with open("autosave_transparent.txt","w",encoding="utf-8") as autosave_transparent:
        autosave_transparent.write(str(tou))
    root.after(1000,auto_save)
def check_font():
    global font_check
    now_font = check_fontfile_exists()
    now_font_new = now_font if isinstance(now_font,tuple) else eval(now_font)
    font_check = Tk()
    font_check.attributes('-topmost', 'true')
    font_check.wm_attributes("-toolwindow", 2)
    var = StringVar()
    var.set("Arial")
    font_check.title("更改字体")
    val = [i for i in font.families() if i[0] != "@"]
    com = ttk.Combobox(font_check,textvariable=var,value=tuple(val),width=50)
    com.set(now_font_new[0])
    com.pack()
    Label(font_check,text="字体大小：")
    scale = Scale(font_check,from_=1,to=150,orient=HORIZONTAL,length=400)
    scale.set(now_font_new[1])
    scale.pack()
    Label(font_check,text="粗体选项：").pack()
    bold = ttk.Combobox(font_check,value=("不粗体","粗体"))
    if len(now_font_new) == 2:
        bold.set("不粗体")
    else:
        bold.set("粗体")
    bold.pack()
    Button(font_check,text="保存",command=lambda:save_font(com,scale,bold),width=50).pack()
def check_fontfile_exists(auto_create:bool=True,default_font:tuple=("微软雅黑",15)):
    if path.exists("tiles_font.txt"):
        return read_font_from_file()
    else:
        if auto_create:
            save_font_to_file(default_font)
            return default_font
        else:
            return default_font
def save_font(fontf,biger,bold):
    save_font_to_file((fontf.get(),int(biger.get()),"bold") if bold.get() == "粗体" else (fontf.get(),int(biger.get())))
    fon = eval(read_font_from_file())
    ll.config(font=fon)
def save_font_to_file(font):
    with open("tiles_font.txt","w",encoding="utf-8") as save:
        save.write(str(font))
def read_font_from_file():
    with open("tiles_font.txt","r",encoding="utf-8") as font_read:
        readed = font_read.read()
    return readed
b = Label(root,text=": : :",bg=bcolor,fg=fcolor,cursor="fleur")
b.pack(fill=X)
menu = Menu(root,tearoff=False)
menu1 = Menu(menu,tearoff=False)
menu.add_cascade(label="设置",menu=menu1)
menu1.add_command(label="窗口",command=windows_setting)
menu1.add_command(label="字体",command=check_font)
menu1.add_separator()
menu1.add_command(label="退出",command=exit)
menu1.add_command(label="关于",command=about)
menu1.add_separator()
menu1.add_command(label="保存为文件",command=save_file)
menu1.add_command(label="打开文件",command=open_file)
root.config(menu=menu)
now_font = check_fontfile_exists()
now_font_new = now_font if isinstance(now_font,tuple) else eval(now_font)
ll = Text(root,bg=bcolor,font=now_font_new,fg=fcolor)
ll.pack()
b.bind("<ButtonPress-1>", on_drag_start)
b.bind("<B1-Motion>", on_drag)
b.bind("<ButtonRelease-1>", on_drag_stop)
root.after(1000,auto_save)
ll.insert(END,read)
root.mainloop()