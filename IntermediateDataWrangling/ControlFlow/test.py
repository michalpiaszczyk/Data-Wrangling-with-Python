import timeit
time_taken = timeit.timeit('[x for x in [0, 1] * 1000000 if x]', number=1)

print(f"Czas wykonania: {time_taken} sekund")