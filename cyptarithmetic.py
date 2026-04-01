import itertools

letters = 'SENDMORY'
digits = range(10)

for perm in itertools.permutations(digits, len(letters)):
    s,e,n,d,m,o,r,y = perm

   
    if s == 0 or m == 0:
        continue

    send = 1000*s + 100*e + 10*n + d
    more = 1000*m + 100*o + 10*r + e
    money = 10000*m + 1000*o + 100*n + 10*e + y

    if send + more == money:
        print("\nSolution Found:\n")
        print(f"S={s}, E={e}, N={n}, D={d}, M={m}, O={o}, R={r}, Y={y}")
        print(f"{send} + {more} = {money}")
        break