"""Binary search tree tests."""

from algorithms.data_structures.binary_search_tree import BinarySearchTree


class TestBinarySearchTree:
    """Binary search tree test suite."""

    def test_binary_search_tree_init(self) -> None:
        """Test binary search tree."""
        binary_search_tree = BinarySearchTree[int]()
        assert binary_search_tree.root is None

    def test_binary_search_tree_insert(self) -> None:
        """Test binary search tree insert."""
        binary_search_tree = BinarySearchTree[int]()
        binary_search_tree.insert(2)
        binary_search_tree.insert(1)
        binary_search_tree.insert(3)
        assert binary_search_tree.depth() == 1

    def test_binary_search_tree_str(self) -> None:
        """Test binary search tree string representation."""
        binary_search_tree = BinarySearchTree[int]()
        binary_search_tree.insert(4)
        binary_search_tree.insert(1)
        binary_search_tree.insert(3)
        binary_search_tree.insert(8)
        binary_search_tree.insert(5)
        assert str(binary_search_tree) == "2 -> 1 -> 3 -> None"
