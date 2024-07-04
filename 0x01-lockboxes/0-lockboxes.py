#!/usr/bin/python3
"""A method that determines if all boxes can be opened"""


def canUnlockAll(boxes=[]):
    """Function returns True if all boxes can be opened
    else return False
    """
    if not boxes:
        return False

    keys = set([0])
    for box_id, box in enumerate(boxes):
        for key in box:
            if key < len(boxes) and key != box_id:
                keys.add(key)

    if len(keys) != len(boxes):
        return False

    return True


if __name__ == '__main__':
    boxes = [
                [1, 3],
                [2],
                [3, 0],
                [1, 2, 3],
            ]
    print(unlockBoxes(boxes))

    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(unlockBoxes(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(unlockBoxes(boxes))
