from time import perf_counter

hs = {
    "Atlanta": ["Xavier", "Yolanda", "Zeus"],
    "Boston": ["Yolanda", "Xavier", "Zeus"],
    "Chicago": ["Xavier", "Yolanda", "Zeus"]
}

sh = {
    "Xavier": ["Boston", "Atlanta", "Chicago"],
    "Yolanda": ["Atlanta", "Boston", "Chicago"],
    "Zeus": ["Atlanta", "Boston", "Chicago"]
}

ahs = {
    "Atlanta": "Xavier",
    "Boston": "Zeus",
    "Chicago": "Yolanda"
}

ash = {
    "Xavier": "Atlanta",
    "Yolanda": "Chicago",
    "Zeus": "Boston"
}

raspr = "Стабильное распределение"

t1 = perf_counter()

for hosp, students in hs.items():
    flag = False
    for s in students:
        if ahs[hosp] == s and flag is False:
            print(f"{hosp}: {s} — устойчивая пара")
            break

        if (
            sh[s].index(hosp) < sh[s].index(ash[s])
            and hs[hosp].index(s) < hs[hosp].index(ahs[hosp])
        ):
            flag = True
            raspr = "Нестабильное распределение"
            print(f"{hosp}: {s} — неустойчивая пара")

t2 = perf_counter()

print(f"Затраченное время: {t2 - t1}")
print(raspr)