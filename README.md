import subprocess
import re
from tqdm import tqdm

src = r"D:\Test1"
dest = r"D:\Test2"

bytes_line_pattern = re.compile(r"Bytes:\s+([\d\.]+\s*\w?)\s+([\d\.]+\s*\w?)")

def parse_size(s):
    s = s.strip().lower()
    if s.endswith("g"):
        return float(s[:-1]) * 1024**3
    elif s.endswith("m"):
        return float(s[:-1]) * 1024**2
    elif s.endswith("k"):
        return float(s[:-1]) * 1024
    else:
        return float(s)

cmd = ["robocopy", src, dest, "/E"]

with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True) as proc:
    pbar = tqdm(total=100, desc="Copying", unit="%")

    for line in proc.stdout:
        match = bytes_line_pattern.search(line)
        if match:
            total_str = match.group(1)
            copied_str = match.group(2)

            total_bytes = parse_size(total_str)
            copied_bytes = parse_size(copied_str)

            percent = (copied_bytes / total_bytes) * 100
            pbar.n = percent
            pbar.refresh()

    pbar.close()
