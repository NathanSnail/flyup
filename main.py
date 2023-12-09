import itertools
import math

# order bugs:
# fly up, fly down, phasing, pipe bomb trigger

# muls = [
#     0.75,  # ep
#     1.1,  # slimeball
#     0.5,  # giga nuke
#     2, # slither / chaotic
#     0.33, # phasing
#     0.3, # heavy
#     7.5, # light
#     2.5, # speed
#     0.32, # accel
#     1.68, # decel
#     0.4 # shield
# ]

remap = {
    0.75: "ep",
    1.1: "slimeball",
    0.5: "giga nuke",
    2: "slither",
    0.33: "phasing",
    0.3: "heavy",
    7.5: "light",
    2.5: "speed",
    0.32: "accel",
    1.68: "decel",
    0.4: "shield"
}

bad = ["slimeball", "giga nuke"]
badm = []
for e in bad:
    for k, v in remap.items():
        if v == e:
            badm.append(k)

muls = [k for k, v in remap.items()]

muls.sort()

fly = 1.2
err = (2**29+50000)/(2**29) - 1
# err = 0.005
# err = 10 ** -7 * 0.5
flyl = math.log(fly)
x = 1
target = float(input("target:")) / 7.92
res = []
be = []

while x < 16:
    print(f"starting {x}")
    # print(res)
    for result in itertools.combinations_with_replacement(muls, x):
        v = 1
        # print(result)
        # small -> big
        for elem in result:
            v *= elem
            v = min(v, 20)
        fc = math.log(target / v) / flyl
        # print(v,fc)
        f1 = math.floor(fc)
        v1 = v * fly ** f1
        # print(result,abs(target / v1 - 1))
        if abs(target / v1 - 1) < err:
            res.append([result, f1, v1])
            # print(res)
            # err = abs(target / v1 - 1)
            # print(f"{result} {f1} has val {v1:.4f})")
        f1 = math.ceil(fc)
        v1 = v * fly ** f1
        if abs(target / v1 - 1) < err:
            res.append([result, f1, v1])
            # print(res)
            # err = abs(target / v1 - 1)
            # print(f"{result} {f1} has err {v1:.4f})")
    print(f"done {x}, found {len(res)} total")
    x += 1

for elem in res:
    score = len(elem[0]) + len(set(elem[0])) * 4
    for badi in badm:
        if badi in elem[0]:
            score += 1
    be.append((score, elem))

be.sort(key=lambda x: x[0])
# be.sort(key = lambda x: abs(x[1][2] / target - 1))
be.reverse()
for el in be:
    b = ""
    for x in set(el[1][0]):
        if x in remap.keys():
            b += f"{remap[x]} * {el[1][0].count(x)}, "
    b += f"{el[1][1]} * fly up has "
    err_n = (el[1][2] / target - 1) * 100
    err_s = ("+" if err_n >= 0 else "") + f"{err_n:.5f}"
    b += f"{err_s}% error "
    b += f"and metric {el[0]:.0f}"
    print(b)
# print(be)
