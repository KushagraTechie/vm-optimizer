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