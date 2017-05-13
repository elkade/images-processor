from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from tkinter import filedialog
import numpy as np
import PIL.Image
import PIL.ImageTk
import matplotlib
from skimage.exposure import adjust_gamma

from tabs import *

matplotlib.use('TkAgg')


def destroy(e):
    sys.exit()


root = Tk()
root.wm_title("Łukasz Dragan - Podstawy przetwarzania obrazow")

image_frame = Frame(root)
image_frame.pack(padx=5, pady=10, anchor=NW, side=LEFT)

tab_frame = Frame(root)
tab_frame.pack(padx=5, pady=10, anchor=NW, side=LEFT)

image = PIL.Image.open("lenna.png")
X = np.asarray(image)
photo = PIL.ImageTk.PhotoImage(image)
original_image = Label(image_frame, image=photo)
original_image.image = photo
original_image.pack()


def callback():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    img = PIL.Image.open(file_path)
    pht = PIL.ImageTk.PhotoImage(img)
    original_image.config(image=pht)
    original_image.image = pht


b = Button(image_frame, text="Load image...", command=callback)
b.pack()

bar = TabBar(tab_frame, "Kontrast")

tab1 = Tab(tab_frame, "Kontrast")
# Label(tab1, text="tab1 text", bg="white", fg="red").pack(side=TOP, expand=YES, fill=BOTH)

w = Scale(master=tab1, orient=HORIZONTAL, from_=0, to=100, command=lambda x: print(x))
w.pack()

tab2 = Tab(tab_frame, "Jasność")
Label(tab2, text="Gamma").pack(side=TOP, fill=BOTH, expand=YES)


def gamma(x):
    global X
    global original_image
    l = np.log(int(x)/100)*-1
    print(l)
    I = adjust_gamma(X, gamma=l, gain=1)
    image = PIL.Image.fromarray(np.uint8(I))
    photo = PIL.ImageTk.PhotoImage(image)
    original_image.config(image=photo)
    original_image.image = photo


w = Scale(master=tab2, orient=HORIZONTAL, from_=1, to=100, command=gamma)
w.pack()

tab3 = Tab(tab_frame, "Histogram")
Label(tab3, bg='white', text="Tab3 text").pack(
    side=LEFT, expand=YES, fill=BOTH)

f = Figure(figsize=(5, 4), dpi=100)
a = f.add_subplot(111)
t = arange(0.0, 3.0, 0.01)
s = sin(2 * pi * t)
a.plot(t, s)
a.set_title('Tk embedding')
a.set_xlabel('X axis label')
a.set_ylabel('Y label')

canvas = FigureCanvasTkAgg(f, master=tab3)

canvas.show()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

# button = Button(master=image_frame, text='Quit', command=sys.exit)
# button.pack(side=BOTTOM)

bar.add(tab1)
bar.add(tab2)
bar.add(tab3)
# bar.config(bd=2, relief=RIDGE)			# add some border
bar.show()

mainloop()
