# Read input
n = int(input())
for _ in range(n):
    phrase = input().strip()
    if phrase.startswith("Simon says"):
        print(phrase[11:-1])
    
    
# print(simonSays)