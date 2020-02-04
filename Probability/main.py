import enum, random

class Kid(enum.Enum):
    BOY = 0
    GIRL = 1

def random_kid():
    return random.choice([Kid.BOY, Kid.GIRL])

both_girls = 0
either_girl = 0
older_girl = 0

random.seed(0)

for _ in range(10000):
    younger = random_kid()
    older = random_kid()

    if older == Kid.GIRL:
        older_girl += 1
    if younger == Kid.GIRL and older == Kid.GIRL:
        both_girls += 1
    if younger == Kid.GIRL or older == Kid.GIRL:
        either_girl += 1

print("P(both | older) : ", both_girls / older_girl)
print("P(both | either) : ", both_girls / either_girl)

