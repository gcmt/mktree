mktree
======

_mktree_ is a simple tool for creating directory trees in one shot. It's
somewhat similar to what you can do with `mkdir` and brace expansion, but with
an easier syntax and better usability.

Installation
------------

Arch users can simply run the following command from the project directory:

```
makepkg -si
```

Anyone else can use `pip`:

```
pip install --user mktree
```

Usage
-----

_mktree_ allows you to create complex directory trees with a simple syntax

```
 $ mktree -P this/is,a.bunch,of/directories
 .
 ├── this
 │   ├── is
 │   └── a
 ├── bunch
 └── of
     └── directories
```

Th ``-P`` flag makes sure we are given a preview of the directory tree without
actually creating any directory. For a simpler list-like preview, use the `-p`
flag instead. A confirmation prompt is also available by using the `-i` flag.

You can find a complete list of all the available options [here](mktree.adoc).

Now let's take a look at the string we've passed as argument. Notice how the
argument string is made up of directories names separated by one of these three
special characters: `/`, `,` and `.`.

Let's start with a very basic example

```
$ mktree -P A
.
└── A
```

This will simply create a directory _A_ inside the current directory.

What if you want to create a folder _B_ inside the folder _A_?

```
$ mktree -P A/B
.
└── A
    └── B
```

That's the purpose of the `/` character: it tells _mktree_ to create the
following directories inside the previous one.

Now a little more advanced example

```
$ mktree -P A/B,C
.
└── A
    ├── B
    └── C
```

This will create the directories _B_ and _C_ inside the directory _A_.  The `,`
character tells _mktree_ to create the following directory at the same level of
the previous one.

Continuing the above example, suppose that after you type _C_ you need to
create a folder _D_ at the same level of the folder _A_. Remember that you've
used the `/` character to move one level down the directory tree and now you
want go back. That's when the `.` character comes in: it tells _mktree_ to
create the following directories one level up the directory tree

```
$ mktree -P A/B,C.D
.
└── A
│   ├── B
│   └── C
└── D
```

You can use many `.` characters in sequence to move up multiple levels, but you
won't be able to move outside the current working directory

```
$ mktree -P A/B/C,D..E/F...H
.
├─ A
│  └─ B
│     ├─ C
│     └─ D
├─ E
│  └─ F
└─ H
```

Since _mktree_ can take many tree descriptions as arguments, to avoid using `.`
multiple times in sequence to reach the root directory, you can simply start
another argument. The above example can in fact be rewritten as:

```
$ mktree -P A/B/C,D E/F H
.
├─ A
│  └─ B
│     ├─ C
│     └─ D
├─ E
│  └─ F
└─ H
```

**Note**: you can escape `.` or `,` if you'll ever need to use them as part of a directory name:

```
$ mktree -P A\\,B,C
.
├─ A,B
└─ C
```

License
-------

See [LICENSE.txt](LICENSE.txt).
