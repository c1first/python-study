This Python package, called animals, contains five Python modules: cat, cow,
dog, horse, and sheep. There is also a special file with the rather unusual name
`__init__.py`. This file is called a package initialization file; the presence of this
file tells the Python system that this directory contains a package. The package
initialization file can also be used to initialize the package (hence the name) and can
also be used to make importing the package easier.

Just like we used the module name when calling a function within a module, we
use the package name when referring to a module within a package. For example,
consider the following code:

```
import animals.cow
animals.cow.speak()
```

In this example, the speak() function is defined within the cow.py module, which
itself is part of the animals package.

Packages are a great way of organizing more complicated Python programs. You
can use them to group related modules together, and you can even define packages
inside packages (called nested packages) to keep your program super-organized.

