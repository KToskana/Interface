# mpu9250 açı ve ivme i2c kullanılıyor
# bmp280 basınç-> ikincil kurtarma sistemini aktif ediyor  i2c kullanılıyor
# neo7m gps uart kullanılıyor
# 3 lora var sx12oo olarak
#gpsbaud 4800

import random
import tkinter as Tk
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import runpy

ivmex_dosya = open("ivme_x.txt","w+")
ivmey_dosya = open("ivme_y.txt","w+")
ivmez_dosya = open("ivme_z.txt","w+")
gyrox_dosya = open("gyro_x.txt","w+")

cond=False

# GUI
root = Tk.Tk()
root.title('Statera Interface')
root.configure(background= '#4c6b8b')
label = Tk.Label(root, text="Statera Roket Takımı", font=("Consolas", 20, "bold"),bg='#4c6b8b', fg='white').grid(column=1, row=0)

fig = plt.figure(figsize=(20, 3),  dpi=90)


# fig.set_figheight(6)
# fig.set_figwidth(6)

plt.style.use('fivethirtyeight')
# values for first graph
x_vals = []
y_vals = []
# values for second graph
y_vals2 = []
# values for third graph
y_vals3 = []

index = count()

y1,y2,y3,y4=0,0,0,0


#file_globals = runpy.run_path("data.py")

def animate(i):
    global cond
    if (cond==True):

        # Generate values
        y1 = int(ivmex_dosya.readline())
        y2 = int(ivmey_dosya.readline())
        y3 = int(ivmez_dosya.readline())
        y4 = int(gyrox_dosya.readline())

       # write_file.write(x_vals)
       # write_file.write(y_vals)

        ind = next(index)
        x_vals.append(ind)
        y_vals.append(y1)
        y_vals2.append(y2)
        y_vals3.append(y3)
        Tk.Label(root, text=str(y1),borderwidth=2,padx=30, relief="raised",  font=("Tahoma", 12, "bold")).place(x=380,y=370)
            #grid(row=2, column=0,padx=0)
        Tk.Label(root, text=str(y2),borderwidth=2,padx=30, relief="raised", font=("Tahoma", 12, "bold")).place(x=880,y=370)
        Tk.Label(root, text=str(y3),borderwidth=2,padx=30, relief="raised", font=("Tahoma", 12, "bold")).place(x=1380,y=370)


        Tk.Label(root, text="GPS", font=("Tahoma", 12, "bold"), bg='#4c6b8b', fg='black').place(x=910,y=460)
        Tk.Label(root, text=str(y4), borderwidth=2, pady=150,padx=300, relief="sunken", font=("Tahoma", 12, "bold")).grid(row=10,column=1,padx=0,pady=150)


        # Get all axes of figure
        ax1, ax2, ax3 = fig.get_axes()
        # Clear current data
        ax1.cla()
        ax2.cla()
        ax3.cla()
        # Plot new data
        ax1.plot(x_vals, y_vals, color="black")
        ax2.plot(x_vals, y_vals2)
        ax3.plot(x_vals, y_vals3, color="red")

        ax1.set_title("Velocity - Time", size=12)
        ax2.set_title("Pressure - Time", size=12)
        ax3.set_title("Height - Time", size=12)
        ax1.patch.set_facecolor('#4c6b8b')
        ax2.patch.set_facecolor('#4c6b8b')
        ax3.patch.set_facecolor('#4c6b8b')


def plot_start():
    global cond
    cond=True

def plot_stop():
    global cond
    cond = False

fig.patch.set_facecolor('#4c6b8b')
#fig.patch.set_linewidth('1')
#fig.patch.set_edgecolor('black')


# graph 1
canvas = FigureCanvasTkAgg(fig, master=root)

canvas.get_tk_widget().grid(column=0, row=1, columnspan=3)


# Create 3 subplots in row 1 and column 1 to 3 #7293b5

fig.subplots(1, 3)

# plt.subplot(351)
# plt.subplot(353)
# plt.subplot(355)

ani = FuncAnimation(fig, animate, interval=1000, blit=False)


logo= Tk.PhotoImage(file='logo.png')
Tk.Label(root, bg='#4c6b8b',image=logo).grid(column=0, row=0)
start=Tk.Button(root, text="Start",font=("Tahoma", 12),command=lambda:plot_start())
start.place(x=50, y=50)
stop=Tk.Button(root, text="Stop",font=("Tahoma", 12),command=lambda:plot_stop())
stop.place(x=50, y=100)
Tk.mainloop()