import sys, pymupdf
d = pymupdf.open(sys.argv[1]); out = sys.argv[2]; pages = [int(x) for x in sys.argv[3].split(",")] if len(sys.argv)>3 else range(len(d))
print("pages:", len(d))
for i in pages:
    d[i].get_pixmap(dpi=int(sys.argv[4]) if len(sys.argv)>4 else 70).save(f"{out}-{i+1}.png")
