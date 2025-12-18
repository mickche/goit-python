import time

arrows = ["→", "↘", "↓", "↙", "←", "↖", "↑", "↗"]


def start_clock():
    i = 0
    while True:
        current_time = time.strftime("%H:%M")

        arrow = arrows[i % len(arrows)]

        print(f"\rЧас: {current_time} {arrow}", end="", flush=True)

        i += 1
        time.sleep(0.2)


if __name__ == "__main__":
    start_clock()