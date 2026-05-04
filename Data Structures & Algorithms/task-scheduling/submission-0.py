from _heapq import heapify
class Solution:
    # round-robin like but we always want to schedule most frequent if we can 
    # we have buckets of size n+1, we always choose most frequent we can to put in bucket if we can't then we empty bucket and add n+1 to total
    # frequency map, start with most frequent, do we sim or just calculate inplace 
    # how do we keep track of cooldown, look n behind?
    # we have n+1 and we fill each bucket one at a time unless the task in already in that bucket then we go to the next bucket
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        freqs = list(counter.values())
        heapq.heapify_max(freqs)
        time = 0
        q = deque()
        while freqs or q:
            time+=1
            if freqs:
                count = heapq.heappop_max(freqs) - 1
                if count:
                    q.append((count, time+n))
            if q and q[0][1] == time:
                heapq.heappush_max(freqs, q.popleft()[0])
        return time

