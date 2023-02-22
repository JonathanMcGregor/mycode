challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]
e= challenge[2][1]
g= challenge[2][0]
n= challenge[3]
print(f"My {e}! The {g} do {n}!")

trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
e= challenge[2][1]
g= challenge[2][0]
n= challenge[3]
print(f"My {e}! The {g} do {n}!")

nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana", 15, "d": "nothing"}]
e= challenge[2][1]
g= challenge[2][0]
n= challenge[3]
print(f"My {e}! The {g} do {n}!")
