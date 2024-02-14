"""A Binary Search Tree data structure."""

from abc import abstractmethod
from dataclasses import dataclass
from typing import Generic, Optional, Protocol, TypeVar


class Comparable(Protocol):
    """Protocol for annotating comparable types."""

    @abstractmethod
    def __lt__(self: "T", other: "T") -> bool:
        """Less than comparison."""


T = TypeVar("T", bound=Comparable)


@dataclass
class Node(Generic[T]):
    """Node of a binary search tree."""

    value: T
    parent: Optional["Node[T]"] = None
    left: Optional["Node[T]"] = None
    right: Optional["Node[T]"] = None


class BinarySearchTree(Generic[T]):
    """Binary Search Tree data structure."""

    def __init__(self) -> None:
        """Initialize the binary search tree."""
        self.root: Optional[Node[T]] = None

    def insert(self, value: T) -> None:
        """
        Insert a value into the binary search tree.

        :param value: Value to insert.
        :type value: T

        :Example:
            >>> from algorithms.data_structures.binary_search_tree import BinarySearchTree
            >>> binary_search_tree = BinarySearchTree()
            >>> binary_search_tree.insert(1)
            >>> binary_search_tree.insert(2)
            >>> binary_search_tree.insert(3)
            >>> binary_search_tree.insert(4)
            >>> binary_search_tree
        """
        if self.root is None:
            self.root = Node(value)
            return

        current: Optional[Node[T]] = self.root
        while current is not None:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    current.left.parent = current
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    current.right.parent = current
                    break
                current = current.right

    def depth(self) -> int:
        """
        Return the depth of the binary search tree.

        :return: Depth of the binary search tree.
        :rtype: int
        """
        if self.root is None:
            return 0

        queue = [self.root]
        depth = 0
        while True:
            if len(queue) == 0:
                break

            for _ in range(len(queue)):
                current = queue.pop(0)
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
            depth += 1

        return depth

    def traversal_level_order(self) -> list[tuple[T, int]]:
        """
        Return the level order traversal of the binary search tree.

        :return: Level order traversal of the binary search tree.
        :rtype: list[T]
        """
        if self.root is None:
            return []

        queue = [self.root]

        result = []

        depth = 0

        while len(queue) > 0:
            for _ in range(len(queue)):
                current = queue.pop(0)
                result.append((current.value, depth))
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
            depth += 1

        return result

    def to_list(self) -> list[Optional[T]]:
        """
        Return the list representation of the binary search tree.

        :return: List representation of the binary search tree.
        :rtype: list[T]
        """
        if self.root is None:
            return []

        result: list[Optional[T]] = [None for _ in range(2 ** self.depth() - 1)]

        queue = [(self.root, 0)]

        while len(queue) > 0:
            for _ in range(len(queue)):
                tmp = queue.pop(0)
                current = tmp[0]
                index = tmp[1]
                result[index] = current.value
                if current.left is not None:
                    queue.append((current.left, index * 2 + 1))
                if current.right is not None:
                    queue.append((current.right, index * 2 + 2))

        return result

    def __str__(self) -> str:
        """
        Return a string representation of the binary search tree.

        :return: String representation of the binary search tree.
        :rtype: str
        """
        if self.root is None:
            return ""

        result: list[str] = []

        list_view = self.to_list()

        depth = self.depth()
        width = 2 ** (depth - 2) * 6 - 1

        t_width = width

        current_idx = 0
        for i in range(depth):
            tmp = [" " for _ in range(width)]
            for j in range(2**i):
                if list_view[current_idx] is not None:
                    tmp[(t_width // 2) + j * (t_width + 1)] = str(
                        list_view[current_idx]
                    )
                current_idx += 1
            result.append("".join(tmp))
            t_width = t_width // 2
        return "\n".join(result)
