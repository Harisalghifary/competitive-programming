def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
    # count dict
    # insert to min heap (negative)

    # while true
    # append key with val times, push it again?
    freq = Counter(s)
    heap = [(-ord(ch), count) for ch, count in freq.items()]
    heapq.heapify(heap)
    res = []
    while heap:
        curr = heappop(heap)
        ch, count = curr
        chara = chr(abs(ch))
        used = min(repeatLimit, count)
        res.append(chara*used)
        count -= used
        
        # how to handle remain count
        if count > 0:
            if not heap: break

            nextChar, nextCount = heappop(heap)
            res.append(chr(abs(nextChar)))
            nextCount-=1
            if nextCount > 0:
                heappush(heap, (nextChar, nextCount))
            heappush(heap, (ch, count))


    return "".join(res)