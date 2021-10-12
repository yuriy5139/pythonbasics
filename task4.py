f_src = 'task4_src.txt'
f_dst = 'task4_dst.txt'

# на всякий случай будем уметь создавать программно
story = "One — 1\nTwo — 2\nThree — 3\nFour — 4"
with open(f_src, 'w', encoding='utf8') as f:
    print(story, file=f)

subst = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

try:
    with open(f_src, 'r', encoding='utf8') as src:
        with open(f_dst, 'w', encoding='utf16') as dst:
            for ln in src:
                print(f"{subst[ln.split(' — ')[0]]} — {ln.split(' — ')[1]}", file=dst)
except Exception as e:
    print("что-то снова пошло не так:", e)
