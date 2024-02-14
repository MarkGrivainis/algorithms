"""Test linked list."""
from algorithms.data_structures.linked_list import LinkedList


class TestLinkedList:
    """Test linked list."""

    def test_linked_list_initialization(self) -> None:
        """Test linked list initialization."""
        ll = LinkedList[int]()
        assert str(ll) == "None"

    def test_linked_list_search_found(self) -> None:
        """Test linked list search for an existing value."""
        ll = LinkedList[int]()
        ll.insert(1)
        assert ll.search(1) == 1

    def test_linked_list_search_not_found(self) -> None:
        """Test linked list search for a non-existing value."""
        ll = LinkedList[int]()
        ll.insert(1)
        assert ll.search(2) is None

    def test_linked_list_insert(self) -> None:
        """Test linked list insert."""
        ll = LinkedList[int]()
        ll.insert(1)
        assert str(ll) == "1 -> None"
        assert ll.search(1) == 1

    def test_linked_list_delete(self) -> None:
        """Test linked list delete."""
        ll = LinkedList[int]()
        ll.insert(1)
        ll.insert(2)
        ll.insert(3)
        ll.delete(2)
        assert str(ll) == "3 -> 1 -> None"
        assert ll.search(2) is None

    def test_linked_list_delete_not_found(self) -> None:
        """Test linked list delete for a non-existing value."""
        ll = LinkedList[int]()
        ll.insert(1)
        ll.insert(2)
        ll.delete(3)
        assert ll.search(3) is None
        assert str(ll) == "2 -> 1 -> None"

    def test_linked_list_delete_empty(self) -> None:
        """Test linked list delete for an empty list."""
        ll = LinkedList[int]()
        ll.delete(1)
        assert ll.search(1) is None
        assert str(ll) == "None"

    def test_linked_list_delete_first(self) -> None:
        """Test linked list delete for the first value."""
        ll = LinkedList[int]()
        ll.insert(1)
        ll.delete(1)
        assert ll.search(1) is None
        assert str(ll) == "None"

    def test_linked_list_delete_last(self) -> None:
        """Test linked list delete for the last value."""
        ll = LinkedList[int]()
        ll.insert(1)
        ll.insert(2)
        ll.delete(2)
        assert ll.search(2) is None
        assert str(ll) == "1 -> None"

    def test_linked_list_len(self) -> None:
        """Test linked list length."""
        ll = LinkedList[int]()
        assert len(ll) == 0
        ll.insert(1)
        assert len(ll) == 1
        ll.insert(2)
        assert len(ll) == 2

    def test_linked_list_iteration(self) -> None:
        """Test linked list iteration."""
        ll = LinkedList[int]()
        ll.insert(1)
        ll.insert(2)
        ll.insert(3)
        assert list(ll) == [3, 2, 1]
        assert ll.search(2) == 2
