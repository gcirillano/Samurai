import os, io, re
SRC = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.dirname(SRC)
OUT = os.path.join(OUT_DIR, 'index.html')
parts = sorted(f for f in os.listdir(SRC) if re.match(r'^\d\d-.*\.html$', f))
os.makedirs(OUT_DIR, exist_ok=True)
with io.open(OUT, 'w', encoding='utf-8', newline='\n') as out:
    for p in parts:
        with io.open(os.path.join(SRC, p), 'r', encoding='utf-8') as f:
            out.write(f.read())
            out.write('\n')
size = os.path.getsize(OUT)
lines = sum(1 for _ in io.open(OUT, encoding='utf-8'))
print('OK', OUT, size, 'bytes', lines, 'lines', parts)
