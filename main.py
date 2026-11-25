"""Write the one-line roast entry to /output/entry.txt."""

import os

LINE = "My agent is so autonomous; it scheduled a 2 a.m. cron whose only job is waking me to approve its autonomy."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
