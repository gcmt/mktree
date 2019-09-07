import os
import unittest
import importlib.machinery

module_path = os.path.join(os.path.dirname(__file__), "mktree")
mktree = importlib.machinery.SourceFileLoader("mktree", module_path).load_module()


class TestDirTree(unittest.TestCase):
    def test_tree_parsing(self):

        load = mktree.DirTree.load

        def eq(a, b):
            self.assertEqual(set(a), set(b))

        eq(load(["a/b"]), ["a/b"])
        eq(load(["a/b,c"]), ["a/b", "a/c"])
        eq(load(["a/b,c.d"]), ["a/b", "a/c", "d"])
        eq(load(["a/b/c,d..e/f"]), ["a/b/c", "a/b/d", "e/f"])
        eq(load(["a/b/c,d..e/f.g.h"]), ["a/b/c", "a/b/d", "e/f", "g", "h"])

        eq(load(["a", "b"]), ["a", "b"])
        eq(load(["a/b", "c,d"]), ["a/b", "c", "d"])
        eq(load(["a/b,c", "d/e,f.g"]), ["a/b", "a/c", "d/e", "d/f", "g"])

        eq(load(["a//b,c"]), ["a/b", "a/c"])
        eq(load(["a/b,,c"]), ["a/b", "a/c"])
        eq(load(["a/b,c.."]), ["a/b", "a/c"])
        eq(load(["a/,."]), ["a"])
        eq(load(["/,.a"]), ["a"])

        eq(load([r"foo\,bar"]), ["foo,bar"])
        eq(load([r"foo\\,bar"]), ["foo\\", "bar"])
        eq(load([r"foo\bar,baz"]), [r"foobar", "baz"])
        eq(load([r"foo\\bar,baz"]), [r"foo\bar", "baz"])
        eq(load([r"foo\\\bar,baz"]), [r"foo\bar", "baz"])
        eq(load([r"foo\\\\bar,baz"]), [r"foo\\bar", "baz"])


if __name__ == "__main__":
    unittest.main()
