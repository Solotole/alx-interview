#!/usr/bin/python3
""" Determining if boxes are unlockable """
from collections import deque


def breadth_first_search(boxes):
    """ function to employ the Breadth first search """
    visited = set()

    queue = deque([0])
    visited.add(0)

    while queue:
        current_box = queue.popleft()
        for key in boxes[current_box]:
            if key not in visited and key < len(boxes):
                visited.add(key)
                queue.append(key)

    return visited


def canUnlockAll(boxes):
    """ function dealing with unlockable boxs determination
        Args:
            boxes (list): list of lists representing lockboxes
        Return:
            return True if all are unlockable and False otherwise
        Requirements:
                    - employing Breadth first search while using the keys
                        in a box as a course to the next box
                    - keeping track of all visisted boxes by using set
                    - return True if all are unlockable and False otherwise
    """
    if not boxes:
        return False

    visited_boxes = breadth_first_search(boxes)

    return len(visited_boxes) == len(boxes)
