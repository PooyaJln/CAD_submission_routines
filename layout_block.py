import tkinter as tk
from tkinter import ttk

# Creating main window

main_window = tk.Tk()
main_window.title("Bored by CAD")
main_window.resizable(width=1, height=1)

# saving the space for the menus' placemebt
menu_list = ttk.Label(main_window, text="menus").grid(row=1, column=1)

# creating some empty space
tabs_placement = ttk.Label(main_window, text="").grid(row=2, column=1)

# creating a column for the list of DWG files
label_dwg_list = ttk.Label(main_window, text="Drawing list")
label_dwg_list.grid(row=3, column=1)
dwg_list_table = tk.Listbox(main_window, height=10, width=10)
dwg_list_table.grid(row=4, column=1, columnspan=1)

tabs_parent = ttk.Notebook(main_window)
tabs_parent.grid(row=3, column=2)
# the first tab
tab1 = ttk.Frame(tabs_parent)
tabs_parent.add(tab1, text="Block attribute updater")

tab2 = ttk.Frame(tabs_parent)
tabs_parent.add(tab2, text="Plot to PDF")


# WIDGETS FOR TAB ONE
get_block_list_button = ttk.Button(tab1, text="Get the blocks in the drawings")
get_block_list_button.grid(row=1, column=1)
tab1_text1 = ttk.Label(tab1, text="Block list")
tab1_text1.grid(row=2, column=1)
block_list_table = tk.Listbox(tab1, height=10, width=10)
block_list_table.grid(row=3, column=1, columnspan=2)
# block_table = ttk.listbox(tab1, height=6, width=35)
# block_table.grid
tab1_text2 = ttk.Label(tab1, text="Block data")
tab1_text2.grid(row=4, column=1)
block_data_table = tk.Listbox(tab1, height=10, width=10)
block_data_table.grid(row=5, column=1, columnspan=2)
# WIDGETS FOR TAB TWO
# tab2_text1 = Label(tab2, text="Zoom")
# tab2_text1.grid(row=6, column=5)
#
# tab2_text2 = Label(tab2, text="Plot Style")
# tab2_text2.grid(row=6, column=8)

main_window.mainloop()
