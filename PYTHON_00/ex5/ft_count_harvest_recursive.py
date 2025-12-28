def ft_count(n):
    if n:
        ft_count(n - 1)
        print(f"Day {n}")


def ft_count_harvest_recursive():
    x = input("Days until harvest: ")
    ft_count(int(x))
    print("Harvest time!")
