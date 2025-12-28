def ft_count_harvest_iterative():
    remain_days = input("Days until harvest: ")
    for i in range(1, int(remain_days) + 1):
        print(f"Day {i}")
    print("Harvest time!")
