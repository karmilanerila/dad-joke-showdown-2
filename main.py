import os

JOKE = "I asked the clock for a second opinion, but it just kept ticking -- I guess it didn't have the time for me."


def main():
    joke = JOKE.strip()
    if not joke or len(joke) > 200:
        raise ValueError("entry must be 1 to 200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(joke)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
