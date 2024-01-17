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
        ll.insert(2)
        assert ll.search(2) == 2

    def test_linked_list_search_not_found(self) -> None:
        """Test linked list search for a non-existing value."""
        ll = LinkedList[int]()
        ll.insert(2)
        assert ll.search(3) is None

    def test_linked_list_insert(self) -> None:
        """Test linked list insert."""
        ll = LinkedList[int]()
        ll.insert(2)
        assert ll.search(2) == 2

    def test_linked_list_delete(self) -> None:
        """Test linked list delete."""
        ll = LinkedList[int]()
        ll.insert(2)
        ll.insert(3)
        ll.delete(2)
        assert ll.search(2) is None

    def test_linked_list_delete_not_found(self) -> None:
        """Test linked list delete for a non-existing value."""
        ll = LinkedList[int]()
        ll.insert(2)
        ll.insert(3)
        ll.delete(4)
        assert ll.search(4) is None

    def test_linked_list_delete_first(self) -> None:
        """Test linked list delete for the first value."""
        ll = LinkedList[int]()
        ll.delete(1)
        assert ll.search(1) is None

