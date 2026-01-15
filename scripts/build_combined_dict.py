import sys
import time 

print(f"dictionary=main:sk,locale=sk,description=Slovencina,date={int(time.time())},version=1")

for line in sys.stdin:
    word, freq = line.strip().split()
    print(f" word={word},f={freq},flags=,originalFreq={freq}")