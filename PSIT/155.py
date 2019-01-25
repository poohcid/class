"""BusStop I"""

def main():
    """BusStop I"""
    limit = int(input())
    busstop = int(input())
    total, bus = 0, []
    for i in range(busstop):
        bus1 = list(map(int, input().split()))
        stop = bus1.pop(0)
        if i > 0:
            total += bus.count(stop)
            bus = list(filter(lambda x: x != stop, bus))
        bus += bus1
        bus = [j for j in bus if busstop >= j >= stop]
        if len(bus) > limit:
            del bus[limit::]
        print(bus)
    print(total)

main()
