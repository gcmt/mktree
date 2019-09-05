import os
import unittest
import importlib.machinery

module_path = os.path.join(os.path.dirname(__file__), "mktree")
mktree = importlib.machinery.SourceFileLoader("mktree", module_path).load_module()


class TestDirTree(unittest.TestCase):
    def test_tree_parsing(self):

        t = mktree.DirTree.load("a/b")
        expected = ["a/b"]
        self.assertEqual(set(t), set(expected))

        t = mktree.DirTree.load("a/b,c")
        expected = ["a/b", "a/c"]
        self.assertEqual(set(t), set(expected))

        t = mktree.DirTree.load("a/b,c.d")
        expected = ["a/b", "a/c", "d"]
        self.assertEqual(set(t), set(expected))

        t = mktree.DirTree.load("a/b/c,d..e/f")
        expected = ["a/b/c", "a/b/d", "e/f"]
        self.assertEqual(set(t), set(expected))

        t = mktree.DirTree.load("a/b/c,d..e/f.g.h")
        expected = ["a/b/c", "a/b/d", "e/f", "g", "h"]
        self.assertEqual(set(t), set(expected))


if __name__ == "__main__":
    unittest.main()
