from tkinter import *
import serial.tools.list_ports
import serial


def connect_menu_init():
    global root, connect_btn, refresh_btn, high_btn, low_btn
    ## MAI WINDOW##
    root = Tk()
    root.title("Serial comunication")
    root.geometry("550x300")
    root.config(bg="")
    ##LABELS##
    port_label = Label(root, text = "Available Port:")
    port_label.grid(column = 1, row = 2, pady = 20, padx=10)

    port_bd = Label(root, text="Baude Rate:")
    port_bd.grid(column=1, row=3, pady=20, padx=10)
    ##BUTTONS##
    refresh_btn = Button(root, text = "Refresh", height = 2, width = 10, command=update_coms)
    refresh_btn.grid(column=3, row=2)

    high_btn = Button(root, text = "Write Data", height= 2, width= 15, command = write_data("some data"), state = 'disable')
    high_btn.grid(column=2, row=4)

    low_btn = Button(root, text = "Write Other Data", height= 2, width= 15, command = write_data("some data"), state = 'disable')
    low_btn.grid(column=3, row=4)

    port_label = Label(root, text="Stare:")
    port_label.grid(column=1, row=4, pady=20, padx=10)

    connect_btn = Button(root, text = "Connect", height = 2, width = 10, state = 'disable' , command=connexion)
    connect_btn.grid(column=3, row=3)
    baud_select()
    update_coms()

def connect_check(args):
    if "-" in clicked_com.get() or "-" in clicked_bd.get():
        connect_btn["state"] = "disable"
    else:
        connect_btn["state"] = "active"

def baud_select():
    global clicked_bd, drop_bd
    clicked_bd = StringVar()
    bds = ["-",
           "9600"]
    clicked_bd.set(bds[0])
    drop_bd = OptionMenu(root, clicked_bd, *bds, command= connect_check)
    drop_bd.config(width= 20)
    drop_bd.grid(column=2, row=3, padx=50)

def update_coms():
    global clicked_com, drop_COM, port_final
    ports = serial.tools.list_ports.comports()
    coms = [com[1] for com in ports]
    coms.insert(0, "-")
    print(coms)
    port_final = ['-']
    for i in range(0, len(coms)):
        if 'Arduino' in coms[i]:
            port_com = coms[i]
            port_final.append(port_com[20:24])

    try:
        drop_COM.destroy()
    except:
        pass

    clicked_com = StringVar()
    clicked_com.set(coms[0])
    drop_COM = OptionMenu(root, clicked_com, *port_final, command= connect_check)
    drop_COM.config(width=20)
    drop_COM.grid(column=2, row=2, padx=50)
    connect_check(0)


def connexion():
    global ser, serialData, port, baud, high_btn, low_btn
    if connect_btn["text"] in "Disconnect":
        serialData = False
        connect_btn["text"] = "Connect"
        refresh_btn["state"] = "active"
        drop_bd["state"]= "active"
        drop_COM["state"]= "active"
        high_btn["state"]="disable"
        low_btn["state"] = "disable"

    else:
        serialData = True
        connect_btn["text"] = "Disconnect"
        refresh_btn["state"] = "disable"
        drop_bd["state"] = "disable"
        drop_COM["state"] = "disable"
        high_btn["state"] = "active"
        low_btn["state"] = "active"
        port = clicked_com.get()
        baud = clicked_bd.get()

        try:
            ser = serial.Serial(port, baud, timeout=0)
        except:
            pass

def write_data(data):
    try:
        ser.write(data)
    except:
        pass

connect_menu_init()

root.mainloop()


