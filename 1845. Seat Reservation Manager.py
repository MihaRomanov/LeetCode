# https://leetcode.com/problems/seat-reservation-manager/description/


class SeatManager:
    def __init__(self, n: int):
        self.q = [i for i in range(1, n + 1)]

    def reserve(self) -> int:
        return heappop(self.q)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.q, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)

############

# 1845. Seat Reservation Manager
# https://leetcode.com/problems/seat-reservation-manager/

class SeatManager:

    def __init__(self, n: int):
        self.heap = [i for i in range(1, n + 1)]

    def reserve(self) -> int:
        return heapq.heappop(self.heap)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)
# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)