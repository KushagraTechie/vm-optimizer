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