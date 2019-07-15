import subprocess
import sys
import time
import datetime
import logging
import yaml
from pathlib import Path


logging.basicConfig(format="%(asctime)s %(message)s", level=logging.DEBUG)


def read_box_file(filename: str):
    with open(filename, "r") as f:
        docs = yaml.safe_load(f)
    return docs


def play(sound_name: str):
    sound_dir = "/System/Library/Sounds/"
    filename = sound_dir + sound_name + ".aiff"
    logging.info("Playing %s", filename)
    subprocess.call(["/usr/bin/afplay", filename])


def say(text: str):
    logging.info("Saying %s", text)
    subprocess.call(["/usr/bin/say", text])


def sleep(duration):
    logging.info("Sleeping for %5.2f minutes.", duration)
    duration_seconds = duration * 60
    elapsed_seconds = 0
    while elapsed_seconds < duration_seconds:
        seconds_left = int(duration_seconds - elapsed_seconds)
        print(f"\r{(seconds_left // 60):02}:{(seconds_left % 60):02}  left", end="")
        time.sleep(1)
        elapsed_seconds += 1
    print("")


def run(boxes, box):
    if isinstance(box, str):
        run(boxes, boxes[box])

    if isinstance(box, list):
        for b in box:
            run(boxes, b)

    if isinstance(box, dict):
        if "play" in box:
            play(box["play"])
        if "say" in box:
            say(box["say"])

        duration = box.get("duration", 1)
        sleep(duration)


def log_box(start_time, name):
    with open("timebox_log.csv", "at") as f:
        f.write(f"{start_time.isoformat()},{name}\n")


def main():
    if len(sys.argv) == 1:
        print("Usage: python timebox <box_name> <box_name>")
        return

    filename = "timebox.yaml"
    box_file = Path(filename)
    if not box_file.is_file():
        print(f"Could not find {filename}.")
        return

    boxes = read_box_file(filename)

    for box_name in sys.argv[1:]:
        if box_name in boxes:
            now = datetime.datetime.now()
            run(boxes, boxes[box_name])
            log_box(now, box_name)
        else:
            logging.error("The box %s does not exist in %s.", box_name, filename)


if __name__ == "__main__":
    main()
