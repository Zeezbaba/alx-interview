#!/usr/bin/python3
"""Function to unlock all given number of boxes"""


def canUnlockAll(boxes):
    # lenght of boxes
    n = len(boxes)

    # created set to keep track of opened boxes
    openedBoxes = set()

    # stack for boxes to explore
    stackbox = [0]

    openedBoxes.add(0)

    while stackbox:
        currentBox = stackbox.pop()
        for key in boxes[currentBox]:
            if key not in openedBoxes and key < n:
                # Opened boxes
                openedBoxes.add(key)
                stackbox.append(key)

    return len(openedBoxes) == n
