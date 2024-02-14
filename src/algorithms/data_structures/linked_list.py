"""Implementation of a linked list."""
from dataclasses import dataclass
from typing import Generic, Iterator, Optional, TypeVar

T = TypeVar("T")


@dataclass
class Node(Generic[T]):
    """Node of a linked list containing a value and a pointer to the next node."""

    value: T
    next: Optional["Node[T]"] = None


class LinkedList(Generic[T]):
    """
    Implementation of a Linked list data structure.

    :param T: The type of the value stored in the linked list.
    :type T: TypeVar

    :param head: Head of the linked list.
    :type head: Optional[Node[T]]

    :Example:
        >>> from algorithms.data_structures.linked_list import LinkedList
        >>> linked_list = LinkedList()
        >>> linked_list.insert(1)
        >>> linked_list.insert(2)
        >>> linked_list.insert(3)
        >>> linked_list.insert(4)
        >>> linked_list.search(2)
        2
        >>> linked_list.search(5) is None
        True
    """

    def __init__(self) -> None:
        """Initialize the linked list."""
        self.head: Optional[Node[T]] = None

    def search(self, value: T) -> Optional[T]:
        """
        Search for a value in the linked list.

        :param value: Value to search for.
        :type value: T

        :return: Value if found, else None.
        :rtype: Optional[T]
        """
        current: Optional[Node[T]] = self.head
        while True:
            if current is None:
                return None
            if current.value == value:
                return current.value
            current = current.next

    def insert(self, value: T) -> None:
        """
        Insert a value at the front of the linked list.

        :param value: Value to insert.
        :type value: T

        :Example:
            >>> from algorithms.data_structures.linked_list import LinkedList
            >>> linked_list = LinkedList()
            >>> linked_list.insert(1)
            >>> linked_list.insert(2)
            >>> linked_list.insert(3)
            >>> linked_list.insert(4)
            >>> linked_list
            4 -> 3 -> 2 -> 1 -> None
        """
        self.head = Node[T](value, self.head)

    def delete(self, value: T) -> None:
        """
        Delete a value from the linked list.

        :param value: Value to delete.
        :type value: T

        :Example:
            >>> from algorithms.data_structures.linked_list import LinkedList
            >>> linked_list = LinkedList()
            >>> linked_list.insert(1)
            >>> linked_list.insert(2)
            >>> linked_list.insert(3)
            >>> linked_list.insert(4)
            >>> linked_list
            4 -> 3 -> 2 -> 1 -> None
            >>> linked_list.delete(3)
            >>> linked_list
            4 -> 2 -> 1 -> None
        """
        if self.search(value) is None:
            return

        current: Optional[Node[T]] = self.head
        if current is not None and current.value == value:
            self.head = current.next
            return

        while True:
            if current is None:
                return
            if current.next is not None and current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def __str__(self) -> str:
        """
        Return a string representation of the linked list.

        :return: String representation of the linked list.
        :rtype: str
        """
        current: Optional[Node[T]] = self.head
        result = ""
        while True:
            if current is None:
                result += "None"
                break
            result += f"{current.value}"
            result += " -> "
            current = current.next
        return result

    def __repr__(self) -> str:
        """
        Return a string representation of the linked list.

        :return: String representation of the linked list.
        :rtype: str
        """
        return str(self)

    def __len__(self) -> int:
        """
        Return the length of the linked list.

        :return: Length of the linked list.
        :rtype: int

        :Example:
            >>> from algorithms.data_structures.linked_list import LinkedList
            >>> linked_list = LinkedList()
            >>> linked_list.insert(1)
            >>> linked_list.insert(2)
            >>> linked_list.insert(3)
            >>> linked_list.insert(4)
            >>> len(linked_list)
            4
        """
        current: Optional[Node[T]] = self.head
        length = 0
        while True:
            if current is None:
                break
            length += 1
            current = current.next
        return length

    def __iter__(self) -> Iterator[T]:
        """
        Return an iterator over the linked list.

        :return: Iterator over the linked list.
        :rtype: Iterator[T]

        :Example:
            >>> from algorithms.data_structures.linked_list import LinkedList
            >>> linked_list = LinkedList()
            >>> linked_list.insert(1)
            >>> linked_list.insert(2)
            >>> linked_list.insert(3)
            >>> linked_list.insert(4)
            >>> list(linked_list)
            [4, 3, 2, 1]

        """
        current: Optional[Node[T]] = self.head
        while True:
            if current is None:
                break
            yield current.value
            current = current.next
