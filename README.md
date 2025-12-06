import subprocess
from tqdm import tqdm

def parse_size(val):
    val = val.strip().lower().replace(",", "")
    unit = ""
    for u in ["k", "m", "g", "t"]:
        if val.endswith(u):
            unit = u
            val = val[:-1]
            break
    number = float(val)
    if unit == "k":
        return number * 1024
    elif unit == "m":
        return number * 1024**2
    elif unit == "g":
        return number * 1024**3
    elif unit == "t":
        return number * 1024**4
    else:
        return number

src = r"D:\Test1"
dest = r"D:\Test2"

cmd = ["robocopy", src, dest, "/E"]

with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True) as proc:
    pbar = tqdm(total=100, desc="Copying", unit="%")

    for line in proc.stdout:
        stripped = line.lstrip()
        if stripped.startswith("Bytes"):
            parts = stripped.split()
            # ["Bytes", ":", "54.65", "m", "30.20", "m", ...]
            
            total_val = parts[2] + parts[3]
            copied_val = parts[4] + parts[5]

            total_bytes = parse_size(total_val)
            copied_bytes = parse_size(copied_val)

            percent = (copied_bytes / total_bytes) * 100
            if percent > 100:
                percent = 100

            pbar.n = percent
            pbar.refresh()

    pbar.close()
