import matplotlib.pyplot as plt
def fifo(pages, frames):
    memory = []
    page_faults = 0

    for page in pages:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            page_faults += 1

    return page_faults


pages = [7, 0, 1, 2, 0, 3, 0, 4]
frames = 3

print("FIFO Page Faults:", fifo(pages, frames))

def lru(pages, frames):
    memory = []
    page_faults = 0

    for page in pages:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            page_faults += 1
        else:
            memory.remove(page)
            memory.append(page)

    return page_faults
print("LRU Page Faults:", lru(pages, frames))

def optimal(pages, frames):
    memory = []
    page_faults = 0

    for i in range(len(pages)):
        if pages[i] not in memory:
            if len(memory) < frames:
                memory.append(pages[i])
            else:
                future = pages[i+1:]
                replace_index = -1
                farthest = -1

                for j in range(len(memory)):
                    if memory[j] not in future:
                        replace_index = j
                        break
                    else:
                        idx = future.index(memory[j])
                        if idx > farthest:
                            farthest = idx
                            replace_index = j

                memory[replace_index] = pages[i]
            page_faults += 1

    return page_faults

import tkinter as tk

def run_simulation():
    pages = list(map(int, entry_pages.get().split(",")))
    frames = int(entry_frames.get())

    result_fifo.config(text="FIFO: " + str(fifo(pages, frames)))
    result_lru.config(text="LRU: " + str(lru(pages, frames)))
    result_opt.config(text="Optimal: " + str(optimal(pages, frames)))


root = tk.Tk()
root.title("VM Optimizer")

tk.Label(root, text="Pages (comma separated)").pack()
entry_pages = tk.Entry(root)
entry_pages.pack()

tk.Label(root, text="Frames").pack()
entry_frames = tk.Entry(root)
entry_frames.pack()

tk.Button(root, text="Run", command=run_simulation).pack()

result_fifo = tk.Label(root, text="")
result_fifo.pack()

result_lru = tk.Label(root, text="")
result_lru.pack()

result_opt = tk.Label(root, text="")
result_opt.pack()

root.mainloop()

import tkinter as tk

def run_simulation():
    try:
        pages = list(map(int, entry_pages.get().split(",")))
        frames = int(entry_frames.get())

        result_fifo.config(text="FIFO: " + str(fifo(pages, frames)))
        result_lru.config(text="LRU: " + str(lru(pages, frames)))
        result_opt.config(text="Optimal: " + str(optimal(pages, frames)))
    except:
        result_fifo.config(text="Invalid Input ❌")


root = tk.Tk()
root.title("Virtual Memory Optimizer")
root.geometry("400x400")
root.configure(bg="#1e1e2f")

title = tk.Label(root, text="VM Optimizer", font=("Arial", 18, "bold"), bg="#1e1e2f", fg="white")
title.pack(pady=10)

tk.Label(root, text="Pages (e.g. 7,0,1,2)", bg="#1e1e2f", fg="white").pack()
entry_pages = tk.Entry(root, width=30)
entry_pages.pack(pady=5)

tk.Label(root, text="Frames", bg="#1e1e2f", fg="white").pack()
entry_frames = tk.Entry(root, width=10)
entry_frames.pack(pady=5)

tk.Button(root, text="Run Simulation", command=run_simulation, bg="#4CAF50", fg="white").pack(pady=15)

result_fifo = tk.Label(root, text="", bg="#1e1e2f", fg="white", font=("Arial", 12))
result_fifo.pack()

result_lru = tk.Label(root, text="", bg="#1e1e2f", fg="white", font=("Arial", 12))
result_lru.pack()

result_opt = tk.Label(root, text="", bg="#1e1e2f", fg="white", font=("Arial", 12))
result_opt.pack()

root.mainloop()

def run_simulation():
    try:
        pages = list(map(int, entry_pages.get().split(",")))
        frames = int(entry_frames.get())

        fifo_faults = fifo(pages, frames)
        lru_faults = lru(pages, frames)
        opt_faults = optimal(pages, frames)

        result_fifo.config(text="FIFO: " + str(fifo_faults))
        result_lru.config(text="LRU: " + str(lru_faults))
        result_opt.config(text="Optimal: " + str(opt_faults))

        # 📊 Graph
        algorithms = ["FIFO", "LRU", "Optimal"]
        faults = [fifo_faults, lru_faults, opt_faults]

        plt.bar(algorithms, faults)
        plt.title("Page Fault Comparison")
        plt.xlabel("Algorithms")
        plt.ylabel("Page Faults")
        plt.show()

    except:
        result_fifo.config(text="Invalid Input ❌")