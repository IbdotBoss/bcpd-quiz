# BCPD — Master Question Bank

> **Exam:** BeingCert Certified Python Developer · 90 questions · 120 minutes · pass 70%
> **Blueprint:** the official objectives PDF — seven domains at 20/15/15/15/15/10/10
> **Verified against:** CPython 3.12.10, NumPy 2.4.4

## How to read this bank

| Marker | Meaning |
|---|---|
| `Obj` column | The blueprint sub-objective the question tests. Coverage is measured here, not by domain totals. |
| `Src` column | Where the question came from. |
| `⚠️` | Something about this question is unsettled. Read the `Why` before trusting it. |

**Src vocabulary:** `authored` — written from the CPython documentation and executed ·
`docs` — the documentation states it directly · `mined` — a misconception observed in the wild,
re-authored from scratch and executed.

### Why you can trust the answers

Every question containing code carries a hidden `verify` block. On each build the snippet is
**executed** and the keyed answer is asserted against what CPython actually did. A question whose
answer disagrees with the interpreter fails the build. No answer here is asserted; each is shown.

That is the one thing practice sites cannot do — theirs are keyed by vote, and they disagree
with each other constantly.

---

## Domain 1 — Introduction and Setup (20%)

> 1.1 Introduction to programming language · 1.2 Setting up your programming environment ·
> 1.3 Variables, expressions, and statements · 1.4 Control structures

**Q1.** Your cousin says "Python is an interpreted language, so it is never compiled." Which statement most accurately describes what CPython actually does with a `.py` file?

- A. It translates the source directly to machine code before running anything
- B. It compiles the source to bytecode, then a virtual machine executes that bytecode
- C. It executes the source text one character at a time with no intermediate form
- D. It requires a separate compiler to be installed before any script will run

**Q2.** After you import your own module for the first time, a new folder appears next to it. What is that folder, and what is in it?

- A. `__pycache__`, holding compiled bytecode so later imports are faster
- B. `__init__`, holding the package initialisation code
- C. `__modules__`, holding a copy of the module source
- D. `__temp__`, holding files the interpreter deletes on exit

**Q3.** What is the output of this snippet, and what does it demonstrate?

```python
x = 10
print(type(x).__name__)
x = "ten"
print(type(x).__name__)
```

- A. `int` then `str` — Python is dynamically typed, so a name can be rebound to any type
- B. `int` then `int` — once a name holds an integer it is locked to that type
- C. `int` then `TypeError` — reassigning to another type raises
- D. `str` then `str` — Python infers one type for the whole program

```verify
assert _exc is None
assert _stdout == "int\nstr\n"
```

**Q4.** What is PEP 8?

- A. The official style guide for Python code — naming, indentation, line length, spacing
- B. A module in the standard library that reformats source files
- C. The specification of the Python bytecode format
- D. The proposal that introduced the `print` function

**Q5.** Which two statements about comments in Python are true? *(Choose 2)*

- A. `#` starts a comment that runs to the end of the line
- B. Python has a dedicated block-comment syntax written `/* ... */`
- C. A triple-quoted string on its own line is a string expression, not a comment
- D. Comments are stored in the compiled bytecode and readable at runtime

**Q6.** Which of these is a valid variable name in Python? *(Choose 2)*

- A. `2nd_score`
- B. `_total`
- C. `class`
- D. `total_2`

```verify
_total = 1
total_2 = 2
assert (_total, total_2) == (1, 2)
```

**Q7.** You want to confirm which Python version is installed before starting a project. Which command does that from a terminal?

- A. `python --version`
- B. `python --check`
- C. `pip version`
- D. `python -v`

**Q8.** What problem does a virtual environment (`python -m venv .venv`) solve?

- A. It gives the project its own isolated set of installed packages, so two projects can need different versions of the same library without conflict
- B. It compiles the project to a single executable file
- C. It runs the project in a sandbox with no access to the filesystem
- D. It automatically installs every package the code imports

**Q9.** Which command installs the `requests` package from PyPI?

- A. `pip install requests`
- B. `python install requests`
- C. `import requests --install`
- D. `pip get requests`

**Q10.** What is the difference between the interactive interpreter (the REPL) and running a script?

- A. In the REPL an expression's value is echoed automatically; in a script you must `print()` it
- B. The REPL cannot define functions
- C. A script cannot import modules
- D. There is no difference — the REPL runs the file line by line

**Q11.** A file `hello.py` sits in the current directory. Which command runs it?

- A. `python hello.py`
- B. `run hello.py`
- C. `python -c hello.py`
- D. `execute hello.py`

**Q12.** A beginner writes this and is surprised when it fails. What is the value and type of `age` after the first line, and what happens next?

```python
age = input("Age? ")
result = age + 1
```

- A. `age` is a `str`, so `age + 1` raises `TypeError` — `input()` always returns a string
- B. `age` is an `int`, so the code works and `result` is the age plus one
- C. `age` is a `float`, so `result` is a float
- D. `age` is a `str`, but Python converts it automatically, so `result` works

```verify
assert isinstance(_exc, EOFError)          # the harness supplies no stdin
try:
    "25" + 1
    concat_ok = True
except TypeError:
    concat_ok = False
assert concat_ok is False
```

**Q13.** What is the value of `a` and `b`?

```python
a = -7 // 2
b = -7 % 2
print(a, b)
```

- A. `-4 1`
- B. `-3 -1`
- C. `-3 1`
- D. `-4 -1`

```verify
assert _stdout == "-4 1\n"
```

**Q14.** What does this print?

```python
print(2 ** 3 ** 2)
```

- A. `512`
- B. `64`
- C. `36`
- D. `128`

```verify
assert _stdout == "512\n"
```

**Q15.** What is the final value of `n`?

```python
n = 5
n += 3
n *= 2
n -= 1
n //= 3
print(n)
```

- A. `5`
- B. `4`
- C. `15`
- D. `6`

```verify
assert _stdout == "5\n"
```

**Q16.** What does this print?

```python
x, y = 1, 2
x, y = y, x
print(x, y)
```

- A. `2 1`
- B. `1 2`
- C. `2 2`
- D. `1 1`

```verify
assert _stdout == "2 1\n"
```

**Q17.** You have the string `"12"` and want to add `3` to it numerically. Which expression gives `15`?

- A. `int("12") + 3`
- B. `"12" + 3`
- C. `str("12") + 3`
- D. `"12" + str(3)`

```verify
assert int("12") + 3 == 15
```

**Q18.** Which expression produces the string `Total: 7`?

```python
n = 7
```

- A. `f"Total: {n}"`
- B. `"Total: n"`
- C. `f"Total: n"`
- D. `"Total: " + n`

```verify
n = 7
assert f"Total: {n}" == "Total: 7"
```

**Q19.** What does this print?

```python
x = 5
print(1 < x < 10)
```

- A. `True`
- B. `False`
- C. `1`
- D. it raises a `SyntaxError`

```verify
assert _stdout == "True\n"
```

**Q20.** What is the value of `i` after this runs?

```python
i = 0
while i != 0:
    i = i - 1
else:
    i = i + 1
```

- A. `1`
- B. `0`
- C. `2`
- D. the variable becomes unavailable outside the loop

```verify
assert i == 1
```

**Q21.** What does this print?

```python
for n in range(5):
    if n == 3:
        break
else:
    print("finished")
print("done")
```

- A. `done`
- B. `finished` then `done`
- C. `done` then `finished`
- D. `finished` only

```verify
assert _stdout == "done\n"
```

**Q22.** What does `list(range(2, 10, 3))` produce?

- A. `[2, 5, 8]`
- B. `[2, 5, 8, 11]`
- C. `[3, 6, 9]`
- D. `[2, 4, 6, 8]`

```verify
assert list(range(2, 10, 3)) == [2, 5, 8]
```

**Q23.** What does this print?

```python
total = 0
for n in range(6):
    if n % 2 == 0:
        continue
    if n > 4:
        break
    total += n
print(total)
```

- A. `4`
- B. `9`
- C. `6`
- D. `1`

```verify
assert _stdout == "4\n"
```

**Q24.** What is `pass` for?

- A. It is a statement that does nothing, used where the syntax requires a statement but no action is wanted
- B. It skips the rest of the current loop iteration
- C. It exits the enclosing loop immediately
- D. It returns `None` from the enclosing function

**Q25.** What does this print?

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(i, j)
```

- A. `0 0` `1 0` `2 0`
- B. `0 0` only
- C. `0 0` `0 1` `0 2`
- D. nothing

```verify
assert _stdout == "0 0\n1 0\n2 0\n"
```

**Q26.** A grading script gives the wrong letter for a score of 95. What is wrong?

```python
score = 95
if score >= 50:
    grade = "Pass"
elif score >= 90:
    grade = "Distinction"
else:
    grade = "Fail"
print(grade)
```

- A. The first true branch wins, so `score >= 50` matches first and the Distinction branch can never be reached — order the conditions from most specific to least
- B. `elif` cannot follow a branch that assigned a variable
- C. `score >= 90` is false for 95
- D. The `else` branch always runs last regardless

```verify
assert _stdout == "Pass\n"
```

---

## Domain 2 — Data Structures (15%)

> 2.1 Lists · 2.2 Tuples · 2.3 Dictionaries · 2.4 Sets

**Q27.** What does this print?

```python
nums = [1, 2, 3]
more = nums
more.append(4)
print(nums)
```

- A. `[1, 2, 3, 4]` — both names refer to the same list object
- B. `[1, 2, 3]` — `more` is a copy
- C. `[4]`
- D. it raises a `TypeError`

```verify
assert _stdout == "[1, 2, 3, 4]\n"
```

**Q28.** You want `copy` to be an independent list so appending to it leaves `nums` unchanged. Which two do that? *(Choose 2)*

- A. `copy = nums[:]`
- B. `copy = nums`
- C. `copy = list(nums)`
- D. `copy = nums.append`

```verify
nums = [1, 2, 3]
for copy in (nums[:], list(nums)):
    copy.append(9)
assert nums == [1, 2, 3]
```

**Q29.** What does this print?

```python
letters = ["a", "b", "c", "d", "e"]
print(letters[1:4])
```

- A. `['b', 'c', 'd']`
- B. `['b', 'c', 'd', 'e']`
- C. `['a', 'b', 'c', 'd']`
- D. `['b', 'c']`

```verify
assert _stdout == "['b', 'c', 'd']\n"
```

**Q30.** What does this print?

```python
nums = [3, 1, 2]
result = nums.sort()
print(result)
```

- A. `None` — `list.sort()` sorts in place and returns `None`
- B. `[1, 2, 3]`
- C. `[3, 1, 2]`
- D. it raises an `AttributeError`

```verify
assert _stdout == "None\n"
```

**Q31.** You need the sorted values but must leave the original list untouched. Which do you use?

- A. `sorted(nums)`
- B. `nums.sort()`
- C. `nums.sorted()`
- D. `reverse(nums)`

```verify
nums = [3, 1, 2]
assert sorted(nums) == [1, 2, 3] and nums == [3, 1, 2]
```

**Q32.** What does this print?

```python
nums = [1, 2, 3, 4]
print([n * 2 for n in nums if n % 2 == 0])
```

- A. `[4, 8]`
- B. `[2, 4, 6, 8]`
- C. `[2, 6]`
- D. `[4, 8, 12, 16]`

```verify
assert _stdout == "[4, 8]\n"
```

**Q33.** Which two statements about tuples are true? *(Choose 2)*

- A. A tuple is immutable — you cannot add, remove or replace its elements
- B. A tuple can be used as a dictionary key if all its elements are hashable
- C. A tuple has an `append()` method
- D. Tuples cannot contain elements of different types

```verify
t = (1, "a")
d = {t: "ok"}
assert d[(1, "a")] == "ok"
assert not hasattr(t, "append")
```

**Q34.** What is the type of `x`?

```python
x = (5)
```

- A. `int` — parentheses alone do not make a tuple; a trailing comma does
- B. `tuple`
- C. `list`
- D. `str`

```verify
x = (5)
assert type(x) is int
```

**Q35.** What does this print?

```python
t = (1, 2, 3)
try:
    t[0] = 9
    print("changed")
except TypeError:
    print("immutable")
```

- A. `immutable`
- B. `changed`
- C. nothing
- D. it raises an unhandled `TypeError`

```verify
assert _stdout == "immutable\n"
```

**Q36.** What does this print?

```python
person = {"name": "Ada", "age": 36}
print(person.get("email", "none"))
```

- A. `none` — `get()` returns the default instead of raising when the key is missing
- B. it raises a `KeyError`
- C. `None`
- D. `email`

```verify
assert _stdout == "none\n"
```

**Q37.** What is the difference between `person["email"]` and `person.get("email")` when the key is absent?

- A. The subscript raises `KeyError`; `get()` returns `None`
- B. Both return `None`
- C. Both raise `KeyError`
- D. The subscript returns `None`; `get()` raises `KeyError`

```verify
person = {"name": "Ada"}
try:
    person["email"]
    raised = False
except KeyError:
    raised = True
assert raised and person.get("email") is None
```

**Q38.** What does this print?

```python
scores = {"a": 1, "b": 2}
scores["c"] = 3
scores["a"] = 9
print(len(scores), scores["a"])
```

- A. `3 9`
- B. `4 1`
- C. `3 1`
- D. `4 9`

```verify
assert _stdout == "3 9\n"
```

**Q39.** Which loop prints each key with its value?

```python
scores = {"a": 1, "b": 2}
```

- A. `for k, v in scores.items(): print(k, v)`
- B. `for k, v in scores: print(k, v)`
- C. `for k in scores.values(): print(k, scores[k])`
- D. `for k, v in scores.keys(): print(k, v)`

```verify
scores = {"a": 1, "b": 2}
out = [f"{k} {v}" for k, v in scores.items()]
assert out == ["a 1", "b 2"]
```

**Q40.** What does this print?

```python
nums = [1, 2, 2, 3, 3, 3]
print(len(set(nums)))
```

- A. `3`
- B. `6`
- C. `1`
- D. `2`

```verify
assert _stdout == "3\n"
```

**Q41.** What do these two sets produce?

```python
a = {1, 2, 3}
b = {3, 4}
print(a & b, a | b)
```

- A. `{3} {1, 2, 3, 4}`
- B. `{1, 2} {3}`
- C. `{3, 4} {1, 2}`
- D. it raises a `TypeError`

```verify
a = {1, 2, 3}
b = {3, 4}
assert (a & b, a | b) == ({3}, {1, 2, 3, 4})
```

**Q42.** Which two statements about sets are true? *(Choose 2)*

- A. A set stores no duplicate values
- B. A set does not support indexing such as `s[0]`
- C. A set preserves the insertion order of its elements
- D. A set can contain a list as an element

```verify
s = {1, 2}
assert not hasattr(s, "__getitem__")
try:
    {[1, 2]}
    ok = False
except TypeError:
    ok = True
assert ok
```

**Q43.** What is the type of `x`, and why does it catch people out?

```python
x = {}
```

- A. `dict` — `{}` is an empty dictionary; an empty set must be written `set()`
- B. `set`
- C. `list`
- D. `tuple`

```verify
assert type({}) is dict and type(set()) is set
```

**Q44.** A stock system must hold the ordered sequence of every scan, allow duplicates, and be edited in place. Which structure fits?

- A. A list
- B. A set
- C. A tuple
- D. A frozenset

---

## Domain 3 - Object-Oriented Programming (15%)

> 3.1 Concepts - 3.2 Creating classes - 3.3 Instance objects - 3.4 Constructors -
> 3.5 Accessing attributes - 3.6 Terminology - 3.7 Encapsulation - 3.8 Inheritance -
> 3.9 Overriding methods - 3.10 Data hiding - 3.11 Overloading/Polymorphism

**Q45.** What is the relationship between a class and an object?

- A. A class is the blueprint; an object is a concrete instance built from it
- B. An object is the blueprint; a class is one instance of it
- C. They are two names for the same thing
- D. A class can exist only inside an object

**Q46.** Which of these is *not* one of the commonly listed pillars of object-oriented programming?

- A. Compilation
- B. Encapsulation
- C. Inheritance
- D. Polymorphism

**Q47.** What does this print?

```python
class Dog:
    species = "canine"

    def __init__(self, name):
        self.name = name

a = Dog("Rex")
b = Dog("Bo")
print(a.species, b.species, a.name, b.name)
```

- A. `canine canine Rex Bo`
- B. `canine canine Bo Bo`
- C. `Rex Bo Rex Bo`
- D. it raises an `AttributeError`

```verify
assert _stdout == "canine canine Rex Bo\n"
```

**Q48.** What does this print, and why is it a classic trap?

```python
class Counter:
    total = 0

    def bump(self):
        Counter.total += 1

x, y = Counter(), Counter()
x.bump()
y.bump()
print(x.total, y.total)
```

- A. `2 2` - `total` is a class variable shared by every instance
- B. `1 1` - each instance gets its own copy
- C. `1 2`
- D. `0 0`

```verify
assert _stdout == "2 2\n"
```

**Q49.** What does this print?

```python
class Box:
    def __init__(self):
        self.items = []

p = Box()
q = Box()
p.items.append("nail")
print(len(p.items), len(q.items))
```

- A. `1 0` - each instance gets its own `items` list because it is created in `__init__`
- B. `1 1`
- C. `0 0`
- D. `2 0`

```verify
assert _stdout == "1 0\n"
```

**Q50.** What does this print?

```python
class Point:
    pass

a = Point()
b = Point()
c = a
print(a is b, a is c)
```

- A. `False True`
- B. `True True`
- C. `False False`
- D. `True False`

```verify
assert _stdout == "False True\n"
```

**Q51.** Which two statements about `__init__` are true? *(Choose 2)*

- A. It is called automatically straight after the new instance is created
- B. It is the method that allocates and returns the new object
- C. Its first parameter is the instance, conventionally named `self`
- D. A class is invalid without an explicit `__init__`

**Q52.** What happens here?

```python
class Item:
    def __init__(self):
        return 42

try:
    Item()
    print("built")
except TypeError:
    print("TypeError")
```

- A. `TypeError` - `__init__` must return `None`
- B. `built`
- C. `42`
- D. nothing is printed

```verify
assert _stdout == "TypeError\n"
```

**Q53.** What does this print?

```python
class User:
    def __init__(self, name, role="member"):
        self.name = name
        self.role = role

a = User("Ada")
b = User("Bo", "admin")
print(a.role, b.role)
```

- A. `member admin`
- B. `admin admin`
- C. `member member`
- D. it raises a `TypeError` because `User("Ada")` is missing an argument

```verify
assert _stdout == "member admin\n"
```

**Q54.** What does this print?

```python
class Car:
    def __init__(self):
        self.wheels = 4

c = Car()
print(hasattr(c, "wheels"), hasattr(c, "wings"), getattr(c, "wings", 0))
```

- A. `True False 0`
- B. `True True 0`
- C. `True False None`
- D. it raises an `AttributeError`

```verify
assert _stdout == "True False 0\n"
```

**Q55.** What does this print?

```python
class Base:
    tag = "class"

b = Base()
print(b.tag)
b.tag = "instance"
print(b.tag, Base.tag)
```

- A. `class` then `instance class`
- B. `class` then `instance instance`
- C. `class` then `class class`
- D. it raises an `AttributeError`

```verify
assert _stdout == "class\ninstance class\n"
```

**Q56.** What does an instance's `__dict__` hold?

```python
class P:
    kind = "shape"
    def __init__(self):
        self.x = 1

print(sorted(P().__dict__))
```

- A. `['x']` - only the instance attributes, not the class attributes
- B. `['kind', 'x']`
- C. `['kind']`
- D. `[]`

```verify
assert _stdout == "['x']\n"
```

**Q57.** In `car = Car("blue")`, what is `Car("blue")` called, and what is `car`?

- A. Instantiation, and `car` is an instance of `Car`
- B. Inheritance, and `car` is a subclass of `Car`
- C. Overriding, and `car` is a method
- D. Encapsulation, and `car` is an attribute

**Q58.** Why does every instance method take `self` as its first parameter?

- A. Python passes the instance explicitly as the first argument; `self` is the name that receives it
- B. `self` is a reserved keyword that Python fills in automatically
- C. It is optional and can be left out
- D. It refers to the class, not the instance

```verify
class T:
    def m(self):
        return self
t = T()
assert t.m() is t
assert T.m(t) is t
```

**Q59.** What does encapsulation mean in practice?

- A. Bundling data and the methods that operate on it into one unit, and controlling access to the internals
- B. Allowing a class to inherit from more than one parent
- C. Letting different types respond to the same method call
- D. Preventing a class from ever being subclassed

**Q60.** A colleague names an attribute `self._cache`. What does the single leading underscore mean?

- A. It is a convention meaning "internal, do not rely on this" - Python does not enforce it
- B. Python makes the attribute unreadable from outside the class
- C. It makes the attribute read-only
- D. It renames the attribute at runtime

```verify
class C:
    def __init__(self):
        self._cache = 1
assert C()._cache == 1
```

**Q61.** What does this print?

```python
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    pass

print(Dog().speak())
```

- A. `...` - `Dog` inherits `speak` from `Animal`
- B. it raises an `AttributeError`
- C. `None`
- D. `speak`

```verify
assert _stdout == "...\n"
```

**Q62.** What does this print?

```python
class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

class Bike(Vehicle):
    def __init__(self):
        super().__init__(2)
        self.pedals = True

b = Bike()
print(b.wheels, b.pedals)
```

- A. `2 True`
- B. `0 True`
- C. it raises a `TypeError` because `Bike()` takes no arguments
- D. it raises an `AttributeError` because `wheels` is never set

```verify
assert _stdout == "2 True\n"
```

**Q63.** What does this print?

```python
class A: pass
class B(A): pass

b = B()
print(isinstance(b, A), issubclass(B, A), isinstance(A(), B))
```

- A. `True True False`
- B. `False True False`
- C. `True True True`
- D. `True False False`

```verify
assert _stdout == "True True False\n"
```

**Q64.** What does this print?

```python
class A:
    def who(self):
        return "A"

class B(A):
    def who(self):
        return "B"

class C(A):
    def who(self):
        return "C"

class D(B, C):
    pass

print(D().who())
```

- A. `B`
- B. `C`
- C. `A`
- D. it raises a `TypeError` because of the ambiguous inheritance

```verify
assert _stdout == "B\n"
```

**Q65.** What does this print?

```python
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

print(Square(3).area())
```

- A. `9` - the subclass method overrides the parent's
- B. `0`
- C. `3`
- D. it raises a `TypeError`

```verify
assert _stdout == "9\n"
```

**Q66.** What does this print?

```python
class Coin:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"{self.value}p"

print(Coin(50))
```

- A. `50p` - `print()` converts its argument with `str()`, which calls `__str__`
- B. the default `<__main__.Coin object at 0x...>` representation
- C. `50`
- D. it raises a `TypeError`

```verify
assert _stdout == "50p\n"
```

**Q67.** What does this print?

```python
class Vault:
    def __init__(self):
        self.__code = 1234

v = Vault()
print(hasattr(v, "__code"), v._Vault__code)
```

- A. `False 1234` - the double underscore triggers name mangling to `_Vault__code`
- B. `True 1234`
- C. it raises an `AttributeError` on the second expression
- D. `False 0`

```verify
assert _stdout == "False 1234\n"
```

**Q68.** Which statement about "private" attributes in Python is true?

- A. There is no enforced privacy - a double underscore mangles the name, which discourages access but does not prevent it
- B. A double-underscore attribute is encrypted in memory
- C. `private` is a keyword that blocks external access
- D. Single-underscore attributes raise `AttributeError` when accessed from outside

**Q69.** What does this print, and what does it say about function overloading in Python?

```python
class Calc:
    def add(self, a, b):
        return a + b
    def add(self, a, b, c):
        return a + b + c

print(Calc().add(1, 2, 3))
```

- A. `6` - the second `def` replaces the first, so Python has no function overloading
- B. `3` - Python picks the two-argument version when given two arguments
- C. it raises a `TypeError` for a duplicate method name
- D. `1`

```verify
assert _stdout == "6\n"
```

**Q70.** What does this print, and which OOP idea does it show?

```python
class Cat:
    def speak(self):
        return "meow"

class Duck:
    def speak(self):
        return "quack"

for animal in (Cat(), Duck()):
    print(animal.speak())
```

- A. `meow` then `quack` - polymorphism through duck typing; no shared base class is needed
- B. it raises a `TypeError` because the classes are unrelated
- C. `meow` twice
- D. `quack` twice

```verify
assert _stdout == "meow\nquack\n"
```

**Q71.** Python has no function overloading. Which two are the idiomatic ways to let one method accept a varying number of arguments? *(Choose 2)*

- A. Give parameters default values
- B. Collect extras with `*args`
- C. Define the method twice with different parameter lists
- D. Annotate the method with `@overload` so Python dispatches at runtime

```verify
class C:
    def total(self, a, b=0, *args):
        return a + b + sum(args)
c = C()
assert (c.total(1), c.total(1, 2), c.total(1, 2, 3)) == (1, 3, 6)
```

---

## Domain 4 - Modules and Libraries (15%)

> 4.1 Importing a module - 4.2 Standard modules - 4.3 Creating modules -
> 4.4 Executing modules as scripts - 4.5 Working with packages -
> 4.6 Numpy arrays - 4.7 Numpy - 4.8 Array operations - 4.9 Statistical functions

**Q72.** After `import math`, which expression calls the square-root function?

- A. `math.sqrt(9)`
- B. `sqrt(9)`
- C. `math->sqrt(9)`
- D. `from math.sqrt(9)`

```verify
import math
assert math.sqrt(9) == 3.0
```

**Q73.** What is the difference between `import math` and `from math import sqrt`?

- A. The first binds the name `math` and you call `math.sqrt()`; the second binds `sqrt` directly into your namespace
- B. The first is faster because it loads less of the module
- C. The second imports the whole module twice
- D. There is no difference

```verify
import math
from math import sqrt
assert math.sqrt(4) == sqrt(4) == 2.0
```

**Q74.** What does `import numpy as np` do?

- A. It imports the module and binds it to the shorter local name `np`
- B. It imports only the part of NumPy called `np`
- C. It renames the installed package on disk
- D. It creates a copy of the module

```verify
import numpy as np
assert np.array([1]).sum() == 1
```

**Q75.** Why is `from module import *` discouraged?

- A. It pulls every public name into the current namespace, where they can silently overwrite your own names
- B. It is a syntax error outside a function
- C. It imports the module twice
- D. It prevents the module from being imported again later

**Q76.** What do these print?

```python
import math
print(math.ceil(-2.5), math.floor(-2.5))
```

- A. `-2 -3`
- B. `-3 -2`
- C. `-2 -2`
- D. `-3 -3`

```verify
assert _stdout == "-2 -3\n"
```

**Q77.** What does this print?

```python
import re
print(re.findall(r"\d+", "a1b22c333"))
```

- A. `['1', '22', '333']`
- B. `['1', '2', '2', '3', '3', '3']`
- C. `['a', 'b', 'c']`
- D. `[]`

```verify
assert _stdout == "['1', '22', '333']\n"
```

**Q78.** What does this print?

```python
from datetime import date
d = date(2026, 8, 25)
print(d.strftime("%Y-%m-%d"), d.year)
```

- A. `2026-08-25 2026`
- B. `25-08-2026 2026`
- C. `2026-8-25 2026`
- D. it raises a `ValueError`

```verify
assert _stdout == "2026-08-25 2026\n"
```

**Q79.** Which two statements about the `random` module are true? *(Choose 2)*

- A. `random.seed(42)` makes the sequence of following random numbers repeatable
- B. `random.choice(seq)` returns one element drawn from `seq`
- C. `random.randint(1, 6)` can never return 6
- D. `random.random()` returns an integer

```verify
import random
random.seed(42)
first = [random.random() for _ in range(3)]
random.seed(42)
assert first == [random.random() for _ in range(3)]
assert random.choice([7]) == 7
assert 6 in {random.randint(1, 6) for _ in range(400)}
```

**Q80.** What is `sys.path`?

- A. The list of directories the interpreter searches when importing a module
- B. The path to the currently running script
- C. The system `PATH` environment variable
- D. The folder where `pip` installs packages

```verify
import sys
assert isinstance(sys.path, list)
```

**Q81.** You save some functions in `helpers.py` and want to use them from `main.py` in the same folder. What do you write in `main.py`?

- A. `import helpers`
- B. `include helpers.py`
- C. `import helpers.py`
- D. `from helpers`

**Q82.** What is a module, in Python's own terms?

- A. A file containing Python definitions and statements, whose filename is the module name plus `.py`
- B. A compiled binary that Python loads at startup
- C. Any folder inside the project
- D. A class with only static methods

**Q83.** What does this idiom do, and why is it used?

```python
def main():
    print("running")

if __name__ == "__main__":
    main()
```

- A. `__name__` is `"__main__"` only when the file is run directly, so `main()` runs on execution but not on import
- B. It stops the file from ever being imported
- C. It renames the module to `__main__`
- D. It is required in every Python file

```verify
import __main__, math
assert __main__.__name__ == "__main__"
assert math.__name__ == "math"
```

**Q84.** What is the value of `__name__` inside `helpers.py` when `main.py` does `import helpers`?

- A. `"helpers"`
- B. `"__main__"`
- C. `"main"`
- D. `None`

**Q85.** What makes a folder a Python package in the traditional layout?

- A. It contains an `__init__.py` file
- B. It contains a `package.json` file
- C. Its name ends in `.pkg`
- D. It is listed in `sys.modules`

**Q86.** Given the package layout below, which import reaches `clean()`? *(Choose 2)*

```python
# tools/
#     __init__.py
#     text/
#         __init__.py
#         strip.py     <- defines clean()
```

- A. `from tools.text.strip import clean`
- B. `import tools.text.strip` then call `tools.text.strip.clean()`
- C. `import clean from tools.text.strip`
- D. `from tools import clean`

```verify
import os, sys, tempfile
d = tempfile.mkdtemp()
os.makedirs(os.path.join(d, "tools", "text"))
open(os.path.join(d, "tools", "__init__.py"), "w").close()
open(os.path.join(d, "tools", "text", "__init__.py"), "w").close()
with open(os.path.join(d, "tools", "text", "strip.py"), "w") as f:
    f.write("def clean(s):\n    return s.strip()\n")
sys.path.insert(0, d)
from tools.text.strip import clean
import tools.text.strip
assert clean("  x ") == "x"
assert tools.text.strip.clean(" y ") == "y"
```

**Q87.** What does this print?

```python
import numpy as np
a = np.array([1, 2, 3])
print(a)
```

- A. `[1 2 3]` - NumPy prints arrays without commas
- B. `[1, 2, 3]`
- C. `array([1, 2, 3])`
- D. `(1, 2, 3)`

```verify
assert _stdout == "[1 2 3]\n"
```

**Q88.** What does this print?

```python
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape, a.ndim, a.size)
```

- A. `(2, 3) 2 6`
- B. `(3, 2) 2 6`
- C. `(2, 3) 6 2`
- D. `(6,) 1 6`

```verify
assert _stdout == "(2, 3) 2 6\n"
```

**Q89.** What does this print?

```python
import numpy as np
print(np.arange(0, 10, 3))
```

- A. `[0 3 6 9]`
- B. `[0 3 6 9 12]`
- C. `[3 6 9]`
- D. `[0 1 2 3 4 5 6 7 8 9]`

```verify
assert _stdout == "[0 3 6 9]\n"
```

**Q90.** What does this print?

```python
import numpy as np
print(np.zeros(3), np.ones(2, dtype=int))
```

- A. `[0. 0. 0.] [1 1]`
- B. `[0 0 0] [1 1]`
- C. `[0. 0. 0.] [1. 1.]`
- D. it raises a `TypeError`

```verify
assert _stdout == "[0. 0. 0.] [1 1]\n"
```

**Q91.** What happens here, and what does it show about a NumPy array's dtype?

```python
import numpy as np
a = np.array([1, 2, 3])
a[0] = 9.7
print(a)
```

- A. `[9 2 3]` - the array holds one fixed type, so the float is truncated to fit the integer dtype
- B. `[9.7 2. 3. ]`
- C. it raises a `TypeError`
- D. `[10 2 3]`

```verify
assert _stdout == "[9 2 3]\n"
```

**Q92.** Which two statements describe how a NumPy array differs from a Python list? *(Choose 2)*

- A. Every element shares one fixed data type
- B. Arithmetic applies element by element across the whole array
- C. It can hold values of mixed types as freely as a list
- D. It grows with `append()` in place, exactly like a list

```verify
import numpy as np
a = np.array([1, 2, 3])
assert list(a * 2) == [2, 4, 6]
assert a.dtype.kind == "i"
assert not hasattr(a, "append")
```

**Q93.** What does this print?

```python
import numpy as np
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(a + b, a * 2)
```

- A. `[11 22 33] [2 4 6]`
- B. `[1 2 3 10 20 30] [2 4 6]`
- C. `[11 22 33] [1 2 3 1 2 3]`
- D. it raises a `ValueError`

```verify
assert _stdout == "[11 22 33] [2 4 6]\n"
```

**Q94.** A list and an array are given the same treatment. What does this print, and why do they differ?

```python
nums = [1, 2, 3]
import numpy as np
arr = np.array([1, 2, 3])
print(nums * 2)
print(arr * 2)
```

- A. `[1, 2, 3, 1, 2, 3]` then `[2 4 6]` - `*` repeats a list but multiplies an array element-wise
- B. `[2, 4, 6]` then `[2 4 6]`
- C. `[1, 2, 3, 1, 2, 3]` then `[1 2 3 1 2 3]`
- D. it raises a `TypeError` on the second line

```verify
assert _stdout == "[1, 2, 3, 1, 2, 3]\n[2 4 6]\n"
```

**Q95.** What does this print, and how does it differ from slicing a list?

```python
import numpy as np
a = np.array([1, 2, 3, 4])
part = a[1:3]
part[0] = 99
print(a)
```

- A. `[ 1 99  3  4]` - a NumPy slice is a view onto the original array, not a copy
- B. `[1 2 3 4]`
- C. `[99  2  3  4]`
- D. it raises a `ValueError`

```verify
assert _stdout == "[ 1 99  3  4]\n"
```

**Q96.** What does this print?

```python
import numpy as np
a = np.array([1, 2, 3, 4])
print(a[a > 2])
```

- A. `[3 4]`
- B. `[False False True True]`
- C. `[1 2]`
- D. it raises an `IndexError`

```verify
assert _stdout == "[3 4]\n"
```

**Q97.** What does this print?

```python
import numpy as np
a = np.array([2, 4, 6, 8])
print(a.mean(), a.sum(), a.max())
```

- A. `5.0 20 8`
- B. `5 20 8`
- C. `20 5.0 8`
- D. `4.0 20 8`

```verify
assert _stdout == "5.0 20 8\n"
```

**Q98.** What does this print?

```python
import numpy as np
a = np.array([[1, 2], [3, 4]])
print(a.sum(axis=0), a.sum(axis=1))
```

- A. `[4 6] [3 7]`
- B. `[3 7] [4 6]`
- C. `[10] [10]`
- D. `[1 2] [3 4]`

```verify
assert _stdout == "[4 6] [3 7]\n"
```

**Q99.** What does this print?

```python
import numpy as np
a = np.array([1, 2, 3, 4])
print(np.median(a))
```

- A. `2.5`
- B. `2`
- C. `3`
- D. `2.0`

```verify
assert _stdout == "2.5\n"
```

**Q100.** Which NumPy function returns the standard deviation of an array?

- A. `np.std(a)`
- B. `np.deviation(a)`
- C. `np.sd(a)`
- D. `np.variance(a)`

```verify
import numpy as np
assert round(float(np.std(np.array([2, 4, 4, 4, 5, 5, 7, 9]))), 3) == 2.0
```

---

## Domain 5 - Debugging and Error Handling (15%)

> 5.1 Errors and Exceptions - 5.2 Using try-except blocks - 5.3 The else block -
> 5.4 User defined exceptions - 5.5 Handling the Zero Division error exception -
> 5.6 Handling the File Not Found error exception

**Q101.** What is the difference between a syntax error and an exception?

- A. A syntax error stops the file from compiling at all; an exception is raised while otherwise valid code runs
- B. They are two names for the same thing
- C. A syntax error can be caught with `try`/`except`; an exception cannot
- D. An exception happens at compile time; a syntax error at run time

**Q102.** Which exception class sits at the top of the hierarchy, and which should you normally catch?

- A. `BaseException` is the root; catch `Exception`, which excludes `SystemExit` and `KeyboardInterrupt`
- B. `Exception` is the root; catch `BaseException` for safety
- C. `Error` is the root; catch `Error`
- D. `RuntimeError` is the root; catch `RuntimeError`

```verify
assert issubclass(Exception, BaseException)
assert not issubclass(KeyboardInterrupt, Exception)
assert issubclass(ValueError, Exception)
```

**Q103.** Which exception does each line raise?

```python
import traceback
for src in ["undefined_name", "'a' + 1", "int('abc')", "[1, 2][9]"]:
    try:
        eval(src)
    except Exception as e:
        print(type(e).__name__)
```

- A. `NameError` `TypeError` `ValueError` `IndexError`
- B. `NameError` `ValueError` `TypeError` `KeyError`
- C. `SyntaxError` `TypeError` `ValueError` `IndexError`
- D. `NameError` `TypeError` `TypeError` `IndexError`

```verify
assert _stdout == "NameError\nTypeError\nValueError\nIndexError\n"
```

**Q104.** Why does `int("abc")` raise `ValueError` rather than `TypeError`?

- A. The type is right - a string is acceptable to `int()` - but the value cannot be interpreted as a number
- B. `TypeError` is only for user-defined types
- C. It actually raises `TypeError`
- D. `ValueError` is raised whenever a conversion function is used

```verify
try:
    int("abc")
    got = None
except Exception as e:
    got = type(e).__name__
assert got == "ValueError"
try:
    int([])
    got2 = None
except Exception as e:
    got2 = type(e).__name__
assert got2 == "TypeError"
```

**Q105.** What does this print?

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("cannot divide by zero")
except Exception:
    print("something else")
```

- A. `cannot divide by zero`
- B. `something else`
- C. both lines
- D. it raises an unhandled `ZeroDivisionError`

```verify
assert _stdout == "cannot divide by zero\n"
```

**Q106.** What does this print?

```python
try:
    int("x")
except ValueError as e:
    print(type(e).__name__, len(e.args))
```

- A. `ValueError 1`
- B. `ValueError 0`
- C. `Exception 1`
- D. it raises a `SyntaxError`

```verify
assert _stdout == "ValueError 1\n"
```

**Q107.** What does this print?

```python
def f():
    try:
        return "try"
    finally:
        print("finally")

print(f())
```

- A. `finally` then `try` - the `finally` block runs even when the `try` returns
- B. `try` then `finally`
- C. `try` only
- D. `finally` only

```verify
assert _stdout == "finally\ntry\n"
```

**Q108.** Why is a bare `except:` discouraged?

- A. It catches everything including `KeyboardInterrupt` and `SystemExit`, so it can swallow a user pressing Ctrl-C
- B. It is a syntax error in Python 3
- C. It catches only `SyntaxError`
- D. It re-raises the exception automatically

**Q109.** How do you handle two exception types with one block?

- A. `except (ValueError, TypeError):`
- B. `except ValueError or TypeError:`
- C. `except ValueError, TypeError:`
- D. `except [ValueError, TypeError]:`

```verify
for bad in ["x", []]:
    try:
        int(bad)
        caught = False
    except (ValueError, TypeError):
        caught = True
    assert caught
```

**Q110.** What does this print, and what is wrong with the ordering?

```python
try:
    int("x")
except Exception:
    print("general")
except ValueError:
    print("specific")
```

- A. `general` - the first matching handler wins, so a broad class listed first makes every later, narrower one unreachable
- B. `specific`
- C. both
- D. it raises a `SyntaxError` for unreachable handlers

```verify
assert _stdout == "general\n"
```

**Q111.** What does this print?

```python
try:
    n = int("7")
except ValueError:
    print("bad input")
else:
    print("parsed", n)
finally:
    print("done")
```

- A. `parsed 7` then `done`
- B. `bad input` then `done`
- C. `parsed 7` only
- D. `done` then `parsed 7`

```verify
assert _stdout == "parsed 7\ndone\n"
```

**Q112.** What is the `else` block of a `try` statement for?

- A. Code that should run only if the `try` block raised nothing - keeping it out of `try` means its own exceptions are not caught by mistake
- B. Code that runs whether or not an exception occurred
- C. A fallback that runs when the `except` block fails
- D. An alternative spelling of `finally`

**Q113.** What does this print?

```python
try:
    raise ValueError("boom")
except ValueError:
    print("except")
else:
    print("else")
finally:
    print("finally")
```

- A. `except` then `finally`
- B. `except` then `else` then `finally`
- C. `else` then `finally`
- D. `finally` then `except`

```verify
assert _stdout == "except\nfinally\n"
```

**Q114.** How do you define your own exception type?

- A. `class InsufficientFunds(Exception): pass`
- B. `class InsufficientFunds(Error): pass`
- C. `def InsufficientFunds(): raise`
- D. `exception InsufficientFunds: pass`

```verify
class InsufficientFunds(Exception):
    pass
assert issubclass(InsufficientFunds, Exception)
```

**Q115.** What does this print?

```python
class TooCold(Exception):
    pass

try:
    raise TooCold("only 3 degrees")
except TooCold as e:
    print(type(e).__name__, e)
```

- A. `TooCold only 3 degrees`
- B. `Exception only 3 degrees`
- C. `TooCold TooCold`
- D. it raises a `TypeError` because the class has no `__init__`

```verify
assert _stdout == "TooCold only 3 degrees\n"
```

**Q116.** What does this print?

```python
class AppError(Exception):
    pass

class DatabaseError(AppError):
    pass

try:
    raise DatabaseError("timeout")
except AppError:
    print("caught by the base class")
```

- A. `caught by the base class` - an `except` clause catches the named class and every subclass of it
- B. nothing, because the classes do not match exactly
- C. it raises an unhandled `DatabaseError`
- D. `timeout`

```verify
assert _stdout == "caught by the base class\n"
```

**Q117.** Which exception does `10 / 0` raise?

- A. `ZeroDivisionError`
- B. `ValueError`
- C. `ArithmeticError`
- D. `FloatingPointError`

```verify
try:
    10 / 0
    name = None
except Exception as e:
    name = type(e).__name__
assert name == "ZeroDivisionError"
```

**Q118.** Which of these raise `ZeroDivisionError`? *(Choose 2)*

- A. `7 // 0`
- B. `7 % 0`
- C. `0 / 7`
- D. `0 ** 0`

```verify
for expr in ("7 // 0", "7 % 0"):
    try:
        eval(expr)
        raised = False
    except ZeroDivisionError:
        raised = True
    assert raised, expr
assert 0 / 7 == 0.0
assert 0 ** 0 == 1
```

**Q119.** What does `1.0 / 0` do in Python?

- A. It raises `ZeroDivisionError` - Python does not return infinity for float division by zero
- B. It returns `inf`
- C. It returns `nan`
- D. It returns `0.0`

```verify
try:
    1.0 / 0
    raised = False
except ZeroDivisionError:
    raised = True
assert raised
```

**Q120.** A report divides a total by a count that is sometimes zero. Which version handles it correctly and still reports a value?

- A. Wrap the division in `try`/`except ZeroDivisionError` and set the result to `0` in the handler
- B. Test `if count != 0.0:` after the division
- C. Catch `ValueError` around the division
- D. Use `total // count`, which never raises

```verify
def average(total, count):
    try:
        return total / count
    except ZeroDivisionError:
        return 0
assert average(10, 2) == 5.0
assert average(10, 0) == 0
```

**Q121.** Which exception does `open("nope.txt")` raise when the file does not exist?

- A. `FileNotFoundError`
- B. `IOError`
- C. `ValueError`
- D. `KeyError`

```verify
import os, tempfile
missing = os.path.join(tempfile.mkdtemp(), "nope.txt")
try:
    open(missing)
    name = None
except Exception as e:
    name = type(e).__name__
assert name == "FileNotFoundError"
```

**Q122.** Which two statements about `FileNotFoundError` are true? *(Choose 2)*

- A. It is a subclass of `OSError`
- B. `IOError` is an alias of `OSError`, so `except IOError` also catches it
- C. It is a subclass of `ValueError`
- D. It is raised when a file exists but is empty

```verify
assert issubclass(FileNotFoundError, OSError)
assert IOError is OSError
assert not issubclass(FileNotFoundError, ValueError)
```

**Q123.** What does this print when `settings.txt` does not exist?

```python
try:
    with open("settings.txt") as f:
        data = f.read()
except FileNotFoundError:
    data = "default"
print(data)
```

- A. `default`
- B. it raises an unhandled `FileNotFoundError`
- C. an empty line
- D. `settings.txt`

```verify
import os, tempfile
os.chdir(tempfile.mkdtemp())
try:
    with open("settings.txt") as f:
        data = f.read()
except FileNotFoundError:
    data = "default"
assert data == "default"
```

**Q124.** A script must keep running when a config file is missing but must stop loudly when the file exists and is unreadable. What is the right shape?

- A. Catch `FileNotFoundError` specifically and let other `OSError` subclasses propagate
- B. Use a bare `except:` so nothing can crash the script
- C. Catch `Exception` and print a message
- D. Check `os.path.exists()` and skip the `try` entirely

---

## Domain 6 - File Handling (10%)

> 6.1 Files and file paths - 6.2 Absolute and relative paths - 6.3 Reading from a file -
> 6.4 Writing to a file - 6.5 Working with Directories - 6.6 os and os.path modules

**Q125.** Why is the `with` form preferred?

```python
with open("notes.txt") as f:
    data = f.read()
```

- A. The file is closed automatically when the block ends, even if an exception is raised inside it
- B. It reads the file faster
- C. It locks the file against other programs
- D. It is the only syntax that allows reading

```verify
import os, tempfile
p = os.path.join(tempfile.mkdtemp(), "notes.txt")
open(p, "w").write("x")
try:
    with open(p) as f:
        raise RuntimeError("boom")
except RuntimeError:
    pass
assert f.closed                       # closed despite the exception
g = open(p)
g.read()
assert not g.closed                   # a bare open() leaves it open
g.close()
```

**Q126.** What is the default mode of `open(path)`, and what does it mean?

- A. `"r"` - open an existing file for reading in text mode
- B. `"w"` - open for writing, creating the file if needed
- C. `"a"` - open for appending
- D. `"rb"` - open for reading in binary mode

```verify
import os, tempfile
p = os.path.join(tempfile.mkdtemp(), "t.txt")
open(p, "w").write("x")
f = open(p)
assert f.mode == "r"
f.close()
```

**Q127.** What does `open()` return?

- A. A file object that you read from, write to and close
- B. The contents of the file as a string
- C. The path to the file
- D. A list of the file's lines

```verify
import os, tempfile
p = os.path.join(tempfile.mkdtemp(), "t.txt")
open(p, "w").write("x")
with open(p) as f:
    assert hasattr(f, "read") and hasattr(f, "close")
```

**Q128.** A script opens `"data.txt"` with no folder in front of it. Where does Python look?

- A. In the current working directory, which is not necessarily the folder the script lives in
- B. Always in the folder containing the script
- C. In the Python installation directory
- D. In every directory on `sys.path`

**Q129.** Which two are absolute paths? *(Choose 2)*

- A. `C:\data\reports\notes.txt`
- B. `/var/reports/notes.txt`
- C. `notes.txt`
- D. `../notes.txt`

```verify
import ntpath, posixpath
assert ntpath.isabs(r"C:\data\reports\notes.txt")
assert posixpath.isabs("/var/reports/notes.txt")
assert not posixpath.isabs("notes.txt")
assert not posixpath.isabs("../notes.txt")
```

**Q130.** Which function turns a relative path into an absolute one based on the current working directory?

- A. `os.path.abspath(p)`
- B. `os.path.realname(p)`
- C. `os.fullpath(p)`
- D. `os.path.absolute(p)`

```verify
import os
assert os.path.isabs(os.path.abspath("x.txt"))
assert not hasattr(os.path, "realname")
```

**Q131.** What does this print?

```python
with open("nums.txt", "w") as f:
    f.write("a\nb\nc\n")

with open("nums.txt") as f:
    print(repr(f.read()))
```

- A. `'a\nb\nc\n'` - `read()` returns the whole file as one string, newlines included
- B. `['a', 'b', 'c']`
- C. `'abc'`
- D. `'a'`

```verify
import os, tempfile
os.chdir(tempfile.mkdtemp())
assert _stdout == "'a\\nb\\nc\\n'\n"
```

**Q132.** What does this print?

```python
with open("nums.txt", "w") as f:
    f.write("a\nb\n")

with open("nums.txt") as f:
    print(f.readlines())
```

- A. `['a\n', 'b\n']` - `readlines()` keeps the newline on the end of each line
- B. `['a', 'b']`
- C. `'a\nb\n'`
- D. `['a\nb\n']`

```verify
import os, tempfile
os.chdir(tempfile.mkdtemp())
assert _stdout == "['a\\n', 'b\\n']\n"
```

**Q133.** What does this print?

```python
with open("log.txt", "w") as f:
    f.write("one\ntwo\n")

with open("log.txt") as f:
    for line in f:
        print(line.strip())
```

- A. `one` then `two`
- B. `one\ntwo\n`
- C. `['one', 'two']`
- D. nothing - a file object is not iterable

```verify
import os, tempfile
os.chdir(tempfile.mkdtemp())
assert _stdout == "one\ntwo\n"
```

**Q134.** What does this print, and why does the second read differ?

```python
with open("d.txt", "w") as f:
    f.write("hello")

with open("d.txt") as f:
    print(repr(f.read()))
    print(repr(f.read()))
```

- A. `'hello'` then `''` - the read position is now at the end of the file
- B. `'hello'` then `'hello'`
- C. `'hello'` then `None`
- D. it raises a `ValueError` on the second read

```verify
import os, tempfile
os.chdir(tempfile.mkdtemp())
assert _stdout == "'hello'\n''\n"
```

**Q135.** What does this print?

```python
with open("out.txt", "w") as f:
    f.write("first")
with open("out.txt", "w") as f:
    f.write("second")
with open("out.txt") as f:
    print(f.read())
```

- A. `second` - mode `"w"` truncates the file to empty before writing
- B. `firstsecond`
- C. `first`
- D. `first\nsecond`

```verify
import os, tempfile
os.chdir(tempfile.mkdtemp())
assert _stdout == "second\n"
```

**Q136.** Which mode adds to the end of an existing file without deleting what is already there?

- A. `"a"`
- B. `"w"`
- C. `"r+"` used alone
- D. `"x"`

```verify
import os, tempfile
os.chdir(tempfile.mkdtemp())
with open("a.txt", "w") as f:
    f.write("one")
with open("a.txt", "a") as f:
    f.write("two")
with open("a.txt") as f:
    assert f.read() == "onetwo"
```

**Q137.** What does this print?

```python
with open("w.txt", "w") as f:
    n = f.write("abc")
    f.write("def")
print(n)
with open("w.txt") as f:
    print(f.read())
```

- A. `3` then `abcdef` - `write()` returns the number of characters written and adds no newline
- B. `3` then `abc\ndef`
- C. `6` then `abcdef`
- D. `None` then `abcdef`

```verify
import os, tempfile
os.chdir(tempfile.mkdtemp())
assert _stdout == "3\nabcdef\n"
```

**Q138.** What is the difference between `os.mkdir()` and `os.makedirs()`?

- A. `mkdir` creates one directory and fails if a parent is missing; `makedirs` creates every missing parent along the way
- B. `mkdir` is for files and `makedirs` for directories
- C. `makedirs` deletes the directory if it already exists
- D. They are aliases of each other

```verify
import os, tempfile
d = tempfile.mkdtemp()
os.makedirs(os.path.join(d, "a", "b", "c"))
assert os.path.isdir(os.path.join(d, "a", "b", "c"))
try:
    os.mkdir(os.path.join(d, "x", "y"))
    raised = False
except FileNotFoundError:
    raised = True
assert raised
```

**Q139.** Which call lists the names of the entries inside a directory?

- A. `os.listdir(path)`
- B. `os.path.list(path)`
- C. `os.dir(path)`
- D. `os.readdir(path)`

```verify
import os, tempfile
d = tempfile.mkdtemp()
open(os.path.join(d, "one.txt"), "w").close()
assert os.listdir(d) == ["one.txt"]
```

**Q140.** Why use `os.path.join("data", "raw", "a.csv")` instead of `"data" + "/" + "raw" + "/" + "a.csv"`?

- A. It inserts the separator the current operating system uses, so the same code works on Windows and on Linux
- B. It checks that the file exists
- C. It is faster
- D. It converts the path to an absolute path

```verify
import os
assert os.path.join("data", "raw", "a.csv").endswith("a.csv")
assert os.sep in os.path.join("data", "raw")
```

**Q141.** What do these print for a path that is an existing file?

```python
import os, tempfile
p = os.path.join(tempfile.mkdtemp(), "f.txt")
open(p, "w").close()
print(os.path.exists(p), os.path.isfile(p), os.path.isdir(p))
```

- A. `True True False`
- B. `True False True`
- C. `True True True`
- D. `False False False`

```verify
assert _stdout == "True True False\n"
```

**Q142.** What does this print?

```python
import os
p = os.path.join("reports", "2026", "summary.csv")
print(os.path.basename(p), os.path.dirname(p) != "", os.path.splitext(p)[1])
```

- A. `summary.csv True .csv`
- B. `summary True .csv`
- C. `summary.csv True csv`
- D. `reports True .csv`

```verify
assert _stdout == "summary.csv True .csv\n"
```

---

## Domain 7 - GUI Programming (10%)

> 7.1 Introduction to GUI Programming - 7.2 Basic GUI Components -
> 7.3 Event-Driven Programming - 7.4 Layout Management - 7.5 Tkinter

**Q143.** How do you get Tkinter?

- A. It ships with the standard CPython installation - `import tkinter` works with no install step
- B. `pip install tkinter`
- C. `pip install tk`
- D. It must be downloaded from the Tcl website

```verify
import tkinter
assert tkinter.__name__ == "tkinter"
```

**Q144.** What distinguishes a GUI program from a command-line program?

- A. The user acts on visible widgets and the program responds to events, rather than reading a fixed sequence of input
- B. A GUI program cannot read or write files
- C. A GUI program runs faster
- D. A GUI program needs no main loop

**Q145.** What does `root.mainloop()` do?

- A. It starts the event loop, which waits for user actions and dispatches them to handlers - the call blocks until the window closes
- B. It draws the window once and returns immediately
- C. It repeatedly redraws the window sixty times a second
- D. It is optional decoration

**Q146.** Match the widget to its job. Which two pairings are correct? *(Choose 2)*

- A. `Label` displays text or an image the user cannot edit
- B. `Entry` accepts a single line of typed text
- C. `Button` displays scrollable multi-line text
- D. `Frame` accepts numeric input only

```verify
import tkinter as tk
for name in ("Label", "Entry", "Button", "Frame", "Text"):
    assert hasattr(tk, name)
```

**Q147.** Which call reads what the user typed into an `Entry` widget named `box`?

- A. `box.get()`
- B. `box.text`
- C. `box.value()`
- D. `box.read()`

```verify
import tkinter as tk
try:
    root = tk.Tk()
except tk.TclError:
    root = None
if root is not None:
    root.withdraw()
    box = tk.Entry(root)
    box.insert(0, "hello")
    assert box.get() == "hello"
    root.destroy()
else:
    assert hasattr(tk.Entry, "get")
```

**Q148.** Which widget holds multi-line, editable text?

- A. `Text`
- B. `Label`
- C. `Entry`
- D. `Message`

```verify
import tkinter as tk
assert hasattr(tk, "Text")
```

**Q149.** What does this pass to the button, and what is the bug?

```python
import tkinter as tk

def say_hi():
    print("hi")

root = tk.Tk()
b = tk.Button(root, command=say_hi())
```

- A. `say_hi()` calls the function immediately and passes its return value `None`; the button gets no callback. Pass `command=say_hi` with no parentheses
- B. It works correctly - the parentheses are required
- C. It raises a `TypeError` at the `Button` call
- D. The button will call `say_hi` twice

```verify
calls = []
def say_hi():
    calls.append(1)
    return None
handed_over = say_hi()          # what command=say_hi() actually passes
assert handed_over is None and len(calls) == 1
assert callable(say_hi)
```

**Q150.** Which method attaches a handler to an event such as a key press or a mouse click?

- A. `widget.bind("<Button-1>", handler)`
- B. `widget.on("click", handler)`
- C. `widget.listen("<Button-1>", handler)`
- D. `widget.attach("<Button-1>", handler)`

```verify
import tkinter as tk
assert hasattr(tk.Widget, "bind")
```

**Q151.** What does "event-driven programming" mean?

- A. The program sets up handlers and then waits; the order in which code runs is decided by what the user does
- B. The program runs its statements top to bottom and exits
- C. Every function is called on a timer
- D. Events are processed only when the program is idle

**Q152.** Which three geometry managers does Tkinter provide?

- A. `pack`, `grid` and `place`
- B. `pack`, `align` and `float`
- C. `layout`, `grid` and `anchor`
- D. `row`, `column` and `cell`

```verify
import tkinter as tk
for m in ("pack", "grid", "place"):
    assert hasattr(tk.Label, m)
```

**Q153.** What goes wrong when you call `pack()` on one widget and `grid()` on another inside the same parent container?

- A. Tkinter raises an error - a single container may be managed by only one geometry manager
- B. Both are honoured and the widgets overlap
- C. The second call is silently ignored
- D. Nothing - mixing them is the recommended approach

```verify
import tkinter as tk
try:
    root = tk.Tk()
except tk.TclError:
    root = None
if root is not None:
    root.withdraw()
    frame = tk.Frame(root)
    tk.Label(frame, text="a").pack()
    try:
        tk.Label(frame, text="b").grid(row=0, column=0)
        raised = False
    except tk.TclError:
        raised = True
    assert raised
    root.destroy()
```

**Q154.** In `widget.grid(row=1, column=2)`, what do the numbers mean?

- A. The row and column of the cell the widget occupies in its parent's grid, counted from 0
- B. The pixel offset from the top-left of the window
- C. The width and height of the widget
- D. The stacking order of the widget

**Q155.** Which two statements about `pack()` are true? *(Choose 2)*

- A. It places widgets in order against one side of the container
- B. `side` accepts values such as `"top"`, `"left"`, `"right"` and `"bottom"`
- C. It positions widgets at exact pixel coordinates
- D. It requires `row` and `column` arguments

```verify
import tkinter as tk
for side in ("top", "left", "right", "bottom"):
    assert hasattr(tk, side.upper())
```

**Q156.** What is `root = tk.Tk()`?

- A. The main application window, created once and used as the parent for the other widgets
- B. A dialog box
- C. The event loop itself
- D. A layout manager

**Q157.** A beginner creates a `Label` and calls `mainloop()`, but the window is empty. What is missing?

```python
import tkinter as tk
root = tk.Tk()
lbl = tk.Label(root, text="hello")
root.mainloop()
```

- A. The label was never handed to a geometry manager - it needs `lbl.pack()`, `lbl.grid()` or `lbl.place()`
- B. `Label` needs a `visible=True` argument
- C. `mainloop()` must be called on the label
- D. The text argument must be a variable

```verify
# noexec - the snippet ends in mainloop(), which blocks until the window closes
import tkinter as tk
try:
    root = tk.Tk()
except tk.TclError:
    root = None
if root is not None:
    root.withdraw()
    lbl = tk.Label(root, text="hello")
    assert lbl.winfo_manager() == ""      # unmanaged: nothing will draw it
    lbl.pack()
    assert lbl.winfo_manager() == "pack"
    root.destroy()
```

---

## Domain 1 — scenario and debugging

**Q158.** A function is supposed to start with an empty list every call. Why does the second call print two items?

```python
def collect(item, bucket=[]):
    bucket.append(item)
    return bucket

print(collect("a"))
print(collect("b"))
```

- A. The default `[]` is created once when the function is defined, so every call that omits `bucket` shares the same list — use `bucket=None` and build the list inside
- B. `append` returns a new list each time
- C. Python caches the return value of the first call
- D. The second call reuses the first call's argument by name

```verify
assert _stdout == "['a']\n['a', 'b']\n"
```

**Q159.** Two lists hold the same values. Why does one comparison print `True` and the other `False`?

```python
a = [1, 2]
b = [1, 2]
print(a == b, a is b)
```

- A. `==` compares the values, `is` compares identity — they are equal lists but two separate objects
- B. `is` is a faster spelling of `==` and this output is a bug
- C. `a` and `b` point at the same object, so both should be `True`
- D. Lists cannot be compared with `==`

```verify
assert _stdout == "True False\n"
```

**Q160.** A price check keeps failing even though the arithmetic looks right. What is going on?

```python
total = 0.1 + 0.2
print(total == 0.3, round(total, 2) == 0.3)
```

- A. Floats are stored in binary and `0.1 + 0.2` is very slightly more than `0.3`, so compare with rounding or a tolerance rather than `==`
- B. Python cannot add two floats
- C. `0.3` is being read as a string
- D. `round()` is broken for two decimal places

```verify
assert _stdout == "False True\n"
```

**Q161.** A loop that should print three lines prints only one. What is wrong?

```python
for n in [1, 2, 3]:
    print(n)
    break
```

- A. `break` leaves the loop on the first pass — `continue` is what skips to the next item
- B. `print` consumes the rest of the list
- C. The list needs to be wrapped in `range()`
- D. `break` is only valid inside `while`

```verify
assert _stdout == "1\n"
```

---

## Domain 2 — scenario and debugging

**Q162.** A script removes every `2` from a list, but one survives. Why?

```python
nums = [1, 2, 2, 3]
for n in nums:
    if n == 2:
        nums.remove(n)
print(nums)
```

- A. Removing from a list while iterating it shifts the remaining items back, so the loop skips one — build a new list instead
- B. `remove()` deletes only the last match
- C. The loop stops as soon as it removes anything
- D. `remove()` needs an index, not a value

```verify
assert _stdout == "[1, 2, 3]\n"
```

**Q163.** What happens here, and what is the fix?

```python
scores = {"a": 1, "b": 2}
try:
    for k in scores:
        if k == "a":
            del scores[k]
    print(scores)
except RuntimeError as e:
    print("RuntimeError")
```

- A. `RuntimeError` — a dictionary cannot change size while it is being iterated; iterate over `list(scores)` instead
- B. `{'b': 2}` — deleting during iteration is fine
- C. `KeyError`
- D. it loops forever

```verify
assert _stdout == "RuntimeError\n"
```

**Q164.** A tuple is meant to be unchangeable, so why does this work — and why does the second line still fail?

```python
t = (1, [2, 3])
t[1].append(4)
print(t)
try:
    {t}
except TypeError:
    print("unhashable")
```

- A. The tuple's own contents are fixed, but a list stored inside it can still be changed — and that mutability is why the tuple cannot be hashed
- B. Tuples are fully mutable
- C. `append` on a tuple element raises `TypeError`
- D. The tuple becomes a list after the append

```verify
assert _stdout == "(1, [2, 3, 4])\nunhashable\n"
```

**Q165.** Why does building this set fail, and what fixes it?

```python
try:
    tags = {["a", "b"], ["c"]}
except TypeError:
    tags = {("a", "b"), ("c",)}
print(len(tags))
```

- A. Set members must be hashable and a list is not — use tuples
- B. A set cannot hold more than one item of the same length
- C. Sets cannot hold sequences at all
- D. The braces make a dictionary, so it needs keys

```verify
assert _stdout == "2\n"
```

---

## Domain 3 — scenario and debugging

**Q166.** Two carts are created and one item is added, but both carts show it. What is wrong?

```python
class Cart:
    items = []
    def add(self, thing):
        self.items.append(thing)

a, b = Cart(), Cart()
a.add("apple")
print(b.items)
```

- A. `items` is a class attribute shared by every instance — create it per instance with `self.items = []` inside `__init__`
- B. `a` and `b` are the same object
- C. `append` writes to every list in the program
- D. `self.items` is a typo for `Cart.items`

```verify
assert _stdout == "['apple']\n"
```

**Q167.** A record has data but no behaviour, and is only ever read. What is the reasonable design call?

- A. A dictionary or a small data class is enough — a class earns its place when data and behaviour belong together, not for grouping values alone
- B. Always use a class; dictionaries are never appropriate
- C. Always use a dictionary; classes are only for inheritance
- D. Use a tuple, because classes cannot hold read-only data

**Q168.** Why does the second instance not see the change?

```python
class Config:
    debug = False

a, b = Config(), Config()
a.debug = True
print(a.debug, b.debug, Config.debug)
```

- A. Assigning through the instance creates a new instance attribute that shadows the class attribute for that object only
- B. `Config.debug` is copied to each instance at creation
- C. `a` and `b` are the same object
- D. it raises an `AttributeError`

```verify
assert _stdout == "True False False\n"
```

**Q169.** In the line `report.export("csv")`, name the parts in order: `report`, `export`, and `"csv"`.

- A. An instance, a method, and an argument
- B. A class, an attribute, and a parameter
- C. A module, a function, and a return value
- D. An object, a constructor, and an instance

**Q170.** A balance must never go negative, but this lets it. What is the encapsulation fix?

```python
class Account:
    def __init__(self):
        self.balance = 0

acc = Account()
acc.balance = -50
print(acc.balance)
```

- A. Keep the value internal and expose a method or `property` that validates before assigning, so the rule cannot be bypassed by writing the attribute directly
- B. Rename the attribute to `__balance`, which makes it impossible to change
- C. Declare `balance` as `private`
- D. Nothing — a negative balance is not preventable in Python

```verify
class Account:
    def __init__(self):
        self._balance = 0
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, v):
        if v < 0:
            raise ValueError("negative")
        self._balance = v
a = Account()
a.balance = 10
try:
    a.balance = -50
    blocked = False
except ValueError:
    blocked = True
assert blocked and a.balance == 10
```

**Q171.** The subclass loses the parent's setup. What is missing?

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed

try:
    print(Dog("Rex", "lab").name)
except AttributeError:
    print("AttributeError")
```

- A. `AttributeError` — the overriding `__init__` never calls `super().__init__(name)`, so `name` is never set
- B. `Rex` — the parent's `__init__` runs automatically
- C. `TypeError` — too many arguments
- D. `None`

```verify
assert _stdout == "AttributeError\n"
```

**Q172.** A subclass sets what looks like the same private attribute, but the parent's method still returns the old value. Why?

```python
class Base:
    def __init__(self):
        self.__value = 1
    def get(self):
        return self.__value

class Child(Base):
    def __init__(self):
        super().__init__()
        self.__value = 2

c = Child()
print(c.get(), c._Base__value, c._Child__value)
```

- A. `1 1 2` — the double underscore is mangled per class, so `Base` and `Child` end up with two separate attributes
- B. `2 2 2` — they are the same attribute
- C. `1 1 1`
- D. it raises an `AttributeError`

```verify
assert _stdout == "1 1 2\n"
```

**Q173.** A subclass replaces a method but should still run the parent's version first. What does that?

```python
class Logger:
    def write(self, msg):
        return "[log] " + msg

class Timestamped(Logger):
    def write(self, msg):
        return super().write("09:00 " + msg)

print(Timestamped().write("started"))
```

- A. `[log] 09:00 started` — `super().write()` calls the parent's version from inside the override
- B. `09:00 started` — the parent's version is discarded
- C. it raises a `RecursionError`
- D. `[log] started`

```verify
assert _stdout == "[log] 09:00 started\n"
```

---

## Domain 4 — scenario and debugging

**Q174.** A student saves a practice file as `random.py` in their project folder. Their other script then fails on `random.randint(1, 6)`. Why?

- A. Their own file shadows the standard library module of the same name, because the script's own directory comes first on the import path — rename the file
- B. `randint` was removed from the standard library
- C. Two modules cannot have the same name anywhere on a machine
- D. The file must be deleted from `__pycache__` first

```verify
import os, sys, tempfile
d = tempfile.mkdtemp()
with open(os.path.join(d, "random.py"), "w") as f:
    f.write("VALUE = 'mine'\n")
sys.path.insert(0, d)
for m in ("random",):
    sys.modules.pop(m, None)
import random
assert getattr(random, "VALUE", None) == "mine"      # the local file won
assert not hasattr(random, "randint")
```

**Q175.** A helper file prints a test line the moment another script imports it. What is missing?

```python
# helpers.py
def add(a, b):
    return a + b

print("self test:", add(1, 2))
```

- A. The test line needs an `if __name__ == "__main__":` guard so it runs only when the file is executed directly
- B. `print` is not allowed in an imported module
- C. The function must be defined after the print
- D. The file needs to be renamed to `__main__.py`

```verify
import os, sys, tempfile, io, contextlib
d = tempfile.mkdtemp()
with open(os.path.join(d, "helpers_demo.py"), "w") as f:
    f.write('def add(a, b):\n    return a + b\n\nif __name__ == "__main__":\n    print("self test:", add(1, 2))\n')
sys.path.insert(0, d)
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    import helpers_demo
assert buf.getvalue() == ""          # guarded: silent on import
assert helpers_demo.add(1, 2) == 3
```

**Q176.** A folder `utils/` holds `dates.py`, but `from utils.dates import today` raises `ModuleNotFoundError`. What is the most likely cause in the traditional package layout?

- A. `utils/` has no `__init__.py`, or the folder containing `utils/` is not on the import path
- B. `dates.py` must be renamed `__init__.py`
- C. Packages cannot contain modules
- D. The import must be written `import utils/dates`

```verify
import os, sys, tempfile
d = tempfile.mkdtemp()
os.makedirs(os.path.join(d, "utilsdemo"))
open(os.path.join(d, "utilsdemo", "__init__.py"), "w").close()
with open(os.path.join(d, "utilsdemo", "dates.py"), "w") as f:
    f.write("def today():\n    return 'day'\n")
sys.path.insert(0, d)
from utilsdemo.dates import today
assert today() == "day"
```

**Q177.** A beginner treats a NumPy array like a list and it does not work. Why does `append` fail?

```python
import numpy as np
a = np.array([1, 2, 3])
b = np.append(a, 4)
print(hasattr(a, "append"), a, b)
```

- A. `False [1 2 3] [1 2 3 4]` — an array has a fixed size, so there is no in-place `append`; `np.append` builds a whole new array
- B. `True [1 2 3 4] [1 2 3 4]`
- C. it raises an `AttributeError`
- D. `False [1 2 3 4] [1 2 3 4]`

```verify
assert _stdout == "False [1 2 3] [1 2 3 4]\n"
```

**Q178.** Two arrays of different lengths are added and it fails. What does the error mean?

```python
import numpy as np
try:
    print(np.array([1, 2, 3]) + np.array([10, 20]))
except ValueError:
    print("ValueError")
```

- A. `ValueError` — element-wise operations need compatible shapes, and 3 elements cannot line up with 2
- B. `[11 22 3]` — the shorter array is padded
- C. `[11 22]` — the longer array is trimmed
- D. `[1 2 3 10 20]` — they are joined

```verify
assert _stdout == "ValueError\n"
```

**Q179.** A tally of exam marks comes out wrong. What is the difference between these two lines?

```python
import numpy as np
marks = np.array([[60, 70], [80, 90]])
print(marks.mean(), marks.mean(axis=1))
```

- A. `75.0 [65. 85.]` — with no axis the mean is over every element; `axis=1` collapses the columns, giving one mean per row
- B. `75.0 [70. 80.]`
- C. `[65. 85.] 75.0`
- D. `150.0 [65. 85.]`

```verify
assert _stdout == "75.0 [65. 85.]\n"
```

**Q180.** A timestamp is needed in the format `2026-08-25`. Which is correct?

```python
from datetime import datetime
d = datetime(2026, 8, 25, 14, 30)
```

- A. `d.strftime("%Y-%m-%d")`
- B. `d.strftime("%y-%M-%D")`
- C. `d.format("YYYY-MM-DD")`
- D. `str(d.date)`

```verify
from datetime import datetime
d = datetime(2026, 8, 25, 14, 30)
assert d.strftime("%Y-%m-%d") == "2026-08-25"
```

---

## Domain 5 — scenario and debugging

**Q181.** A script silently does nothing and nobody can work out why. What is wrong with the error handling?

```python
def load(values):
    try:
        return sum(valeus)
    except:
        return None

print(load([1, 2, 3]))
```

- A. `None` — the bare `except` swallows a `NameError` caused by the typo `valeus`, hiding a bug that has nothing to do with the data
- B. `6` — Python corrects the misspelling
- C. it raises a `NameError`
- D. `0`

```verify
assert _stdout == "None\n"
```

**Q182.** What does this return, and why is it a trap?

```python
def f():
    try:
        return "try"
    finally:
        return "finally"

print(f())
```

- A. `finally` — a `return` inside `finally` replaces the one from the `try`, which silently discards the real result
- B. `try`
- C. `None`
- D. it raises a `SyntaxError`

```verify
assert _stdout == "finally\n"
```

**Q183.** A handler is meant to catch a bad number but never fires. Why?

```python
try:
    n = int("twelve")
except TypeError:
    print("caught")
except ValueError:
    print("value")
```

- A. `value` — the wrong class was tried first; a string that is not a number raises `ValueError`, not `TypeError`
- B. `caught`
- C. nothing is printed
- D. it raises an unhandled exception

```verify
assert _stdout == "value\n"
```

**Q184.** A custom exception should carry the offending value so the handler can report it. Which works?

```python
class BadTemp(Exception):
    pass

try:
    raise BadTemp(-40)
except BadTemp as e:
    print(e.args[0], str(e))
```

- A. `-40 -40` — the inherited `__init__` stores whatever it is raised with in `args`
- B. it raises a `TypeError` because the class defines no `__init__`
- C. `None None`
- D. `BadTemp -40`

```verify
assert _stdout == "-40 -40\n"
```

---

## Domain 6 — scenario and debugging

**Q185.** A script writes a report, but the file is empty when another program reads it a moment later. What is missing?

```python
f = open("report.txt", "w")
f.write("done")
print(open("report.txt").read())
f.close()
print(open("report.txt").read())
```

- A. an empty line then `done` — the text sits in a buffer until the file is closed, which is exactly what `with` guarantees
- B. `done` then `done`
- C. it raises a `ValueError`
- D. an empty line twice

```verify
assert _stdout == "\ndone\n"
```

**Q186.** A script works from its own folder and fails from anywhere else. Which fix is correct?

- A. Build the path from the script's own location, for example `os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt")`
- B. Always call `os.chdir()` to the user's home directory first
- C. Use `open("./data.txt")`, which is always relative to the script
- D. Move the file to the Python installation directory

```verify
import os
here = os.path.dirname(os.path.abspath(os.path.join(os.getcwd(), "x.py")))
assert os.path.isabs(os.path.join(here, "data.txt"))
assert not os.path.isabs("./data.txt")
```

**Q187.** A script lists a folder and then opens each file, and it fails with `FileNotFoundError` unless it is run from inside that folder. Why?

```python
import os, tempfile
d = tempfile.mkdtemp()
open(os.path.join(d, "a.txt"), "w").close()
print(os.listdir(d))
```

- A. `os.listdir()` returns bare names, not paths — rejoin each one with `os.path.join(d, name)` before opening it
- B. `os.listdir()` returns absolute paths and the script is corrupting them
- C. `os.listdir()` cannot see files created in the same script
- D. The folder must be added to `sys.path`

```verify
import os, tempfile
d = tempfile.mkdtemp()
open(os.path.join(d, "a.txt"), "w").close()
names = os.listdir(d)
assert names == ["a.txt"] and not os.path.isabs(names[0])
assert os.path.isfile(os.path.join(d, names[0]))
```

---

## Domain 7 — scenario and debugging

**Q188.** A form reads the entry box the moment the window is built and always gets an empty string. Why?

- A. The read happens before the event loop starts, so the user has not typed anything yet — read the value inside the button's callback instead
- B. `Entry.get()` only works after `destroy()`
- C. `Entry` needs `readable=True`
- D. The entry must be packed twice

```verify
import tkinter as tk
try:
    root = tk.Tk()
except tk.TclError:
    root = None
if root is not None:
    root.withdraw()
    e = tk.Entry(root)
    e.pack()
    assert e.get() == ""                 # nothing typed yet
    e.insert(0, "typed later")
    assert e.get() == "typed later"      # what the callback would see
    root.destroy()
```

**Q189.** A window is meant to show a label and a button side by side in a row, then a status bar underneath spanning both. Which manager fits without fighting?

- A. `grid`, placing the two widgets at row 0 columns 0 and 1 and the status bar at row 1 with `columnspan=2`
- B. `place`, with pixel coordinates for all three
- C. `pack` with `side="left"` for all three
- D. Mixing `grid` for the row and `pack` for the status bar in the same container

```verify
import tkinter as tk
try:
    root = tk.Tk()
except tk.TclError:
    root = None
if root is not None:
    root.withdraw()
    f = tk.Frame(root)
    tk.Label(f, text="a").grid(row=0, column=0)
    tk.Button(f, text="b").grid(row=0, column=1)
    bar = tk.Label(f, text="status")
    bar.grid(row=1, column=0, columnspan=2)
    assert bar.grid_info()["columnspan"] == 2
    root.destroy()
```

**Q190.** A button is built inside a function and the window shows it, but clicking it does nothing and no error appears. Which is the most likely cause?

- A. `command` was given the *result* of calling the handler rather than the handler itself, so the button holds `None`
- B. Buttons cannot be created inside a function
- C. `mainloop()` must be called on the button
- D. The button needs `clickable=True`

```verify
def handler():
    return "ran"
passed_by_mistake = handler()      # command=handler()
passed_correctly = handler         # command=handler
assert passed_by_mistake == "ran" and not callable(passed_by_mistake)
assert callable(passed_correctly)
```

---

<!-- ANSWERS -->

## Answers

| Q | Ans | Obj | Src | Why |
|---|---|---|---|---|
| Q1 | B | 1.1 | docs | CPython compiles source to bytecode and a virtual machine executes it. The bytecode step is real and observable — it is what lands in `__pycache__`. A is wrong because CPython emits no machine code. C describes no real interpreter. D is wrong because the compiler is inside the interpreter. |
| Q2 | A | 1.1 | docs | `__pycache__` caches the compiled bytecode as `.pyc` so a later import skips recompiling. It appears for imported modules, not for the script you run directly. `__init__.py` is a real thing but it is a file that marks a package, not this folder. |
| Q3 | A | 1.3 | authored | Python is dynamically typed: the type belongs to the object, not the name, so rebinding `x` to a string is legal. This is also why type errors surface at runtime rather than before the program starts. |
| Q4 | A | 1.1 | docs | PEP 8 is the style guide for Python code — 4-space indents, `snake_case` for functions and variables, `CapWords` for classes. It is a convention document, not code. Tools like `flake8` check against it but are not PEP 8 itself. |
| Q5 | A & C | 1.1 | authored | `#` runs to end of line and is the only comment syntax — Python has no `/* */`. A triple-quoted string on its own line is an expression that is evaluated and discarded, which is why it works as a docstring in the right position but is not a comment. Comments are discarded at compile time. |
| Q6 | B & D | 1.3 | authored | A name may contain letters, digits and underscores but may not start with a digit, so `2nd_score` is a syntax error. `class` is a reserved keyword. Leading underscores are legal and conventionally mean "internal". |
| Q7 | A | 1.2 | docs | `python --version` (or `-V`) prints the version. Lowercase `-v` is verbose mode and floods the terminal with import tracing — a genuinely confusing thing to run by accident. |
| Q8 | A | 1.2 | docs | A virtual environment gives the project its own `site-packages`, so project A can use one version of a library and project B another. It does not sandbox the filesystem and it does not install anything on its own. |
| Q9 | A | 1.2 | docs | `pip install <name>` fetches from PyPI. Inside a project prefer `python -m pip install <name>`, which guarantees the pip belonging to the Python you are actually running. |
| Q10 | A | 1.2 | authored | The REPL echoes the value of any expression you type; a script does not, so a script that computes without printing appears to do nothing. That surprise is the single most common first-week confusion. |
| Q11 | A | 1.2 | docs | `python hello.py` runs the file. If `python` is not found, the launcher `py hello.py` on Windows or `python3 hello.py` on macOS and Linux usually is. |
| Q12 | A | 1.3 | mined | `input()` always returns a string, even when the user types digits, so `"25" + 1` raises `TypeError: can only concatenate str`. Wrap it: `age = int(input("Age? "))`. Python never converts types silently for `+` between `str` and `int`. |
| Q13 | A | 1.3 | authored | `//` floors toward negative infinity, so `-7 // 2` is `-4`, not `-3`. Python's `%` then returns a result with the sign of the divisor, so `-7 % 2` is `1`. This differs from C and Java and is a reliable trap. |
| Q14 | A | 1.3 | authored | `**` is right-associative, so this is `2 ** (3 ** 2)` = `2 ** 9` = `512`. Left-associative evaluation would give `8 ** 2` = `64`, which is option B and the answer most people pick. |
| Q15 | A | 1.3 | authored | Step by step: 5, then `+= 3` gives 8, `*= 2` gives 16, `-= 1` gives 15, `//= 3` gives 5. Augmented assignment applies the operator and rebinds the name. |
| Q16 | A | 1.3 | authored | The right-hand side `y, x` is built into a tuple first, then unpacked into the left, so the swap needs no temporary variable. This is idiomatic Python and worth recognising on sight. |
| Q17 | A | 1.3 | authored | `int("12")` converts the string to a number, then `+ 3` is arithmetic. `"12" + 3` raises `TypeError`; `"12" + str(3)` gives the string `"123"`, which is concatenation, not addition. |
| Q18 | A | 1.3 | docs | An f-string substitutes the expression inside `{}`. Without the `f` prefix the braces are literal characters, which is why option C prints `Total: n`. Option D fails because you cannot concatenate `str` and `int`. |
| Q19 | A | 1.3 | authored | Python allows chained comparison: `1 < x < 10` means `1 < x and x < 10`, evaluating `x` once. Most languages parse this as `(1 < x) < 10` and get a nonsense result. |
| Q20 | A | 1.4 | mined | `while ... else` runs the `else` block when the loop finishes without `break`. Here the condition is false immediately, so the body never runs, the loop ends normally, and `else` executes `i = i + 1`, giving 1. Practice sites key this question three different ways and one popular copy renders `!=` with a space as `! =`, which would be a `SyntaxError` and is a typesetting artifact, not the question. |
| Q21 | A | 1.4 | authored | `for ... else` runs the `else` only if the loop was never broken out of. The `break` at `n == 3` fires, so `finished` never prints. Read `else` here as "no break". |
| Q22 | A | 1.4 | docs | `range(start, stop, step)` excludes the stop value. From 2 in steps of 3: 2, 5, 8 — the next would be 11, which is past 10. The exclusive endpoint is the standard off-by-one source. |
| Q23 | A | 1.4 | authored | `continue` skips even numbers, so only 1, 3, 5 reach the second test. `break` fires at 5 before it is added. Total is 1 + 3 = 4. |
| Q24 | A | 1.4 | docs | `pass` is the null statement — it does nothing, and exists because Python's block syntax requires at least one statement. Use it for a stub class or an empty `except`. `continue` and `break` are the loop controls. |
| Q25 | A | 1.4 | authored | `break` exits only the innermost loop, so each outer iteration prints once at `j == 0` then breaks. To leave both loops you need a flag, a `return`, or an `else` clause on the outer loop. |
| Q26 | A | 1.4 | authored | An `if/elif` chain stops at the first true test. `95 >= 50` is true, so `grade` becomes `Pass` and the Distinction branch is unreachable for every score. Order the tests from most specific to least, or test `score >= 90` first. |
| Q27 | A | 2.1 | authored | Assignment binds another name to the same object; it does not copy. Mutating through either name is visible through both. This aliasing is the most common beginner data-structure bug. |
| Q28 | A & C | 2.1 | authored | Both `nums[:]` and `list(nums)` build a new list. `copy = nums` aliases. `nums.append` without parentheses binds the method object itself, which is legal but does nothing useful. Both copies here are shallow — nested objects are still shared. |
| Q29 | A | 2.1 | docs | Slicing includes the start index and excludes the stop, so `[1:4]` gives indices 1, 2 and 3. |
| Q30 | A | 2.1 | authored | `list.sort()` mutates in place and returns `None`, so assigning its result throws away the list and keeps `None`. The pattern `nums = nums.sort()` silently destroys data and is worth recognising. |
| Q31 | A | 2.1 | docs | `sorted()` is the built-in that returns a new sorted list and leaves the original alone. There is no `nums.sorted()` method, and `reverse()` is a list method that reverses in place. |
| Q32 | A | 2.1 | authored | The comprehension filters first with the `if`, then applies the expression, so only 2 and 4 survive and become 4 and 8. |
| Q33 | A & B | 2.2 | authored | Tuples are immutable, which is exactly what makes them hashable and therefore usable as dictionary keys when their contents are hashable too. They have no `append()`, and they can hold mixed types freely. |
| Q34 | A | 2.2 | authored | The comma makes a tuple, not the parentheses. `(5)` is just `5` in brackets; `(5,)` is a one-element tuple. This bites when returning a single value you meant to be a tuple. |
| Q35 | A | 2.2 | authored | Item assignment on a tuple raises `TypeError: 'tuple' object does not support item assignment`, which the handler catches. Note it is `TypeError`, not `AttributeError`. |
| Q36 | A | 2.3 | docs | `get(key, default)` returns the default when the key is missing instead of raising. With no default it returns `None`. |
| Q37 | A | 2.3 | docs | Subscripting a missing key raises `KeyError`; `get()` returns `None`. Choose the subscript when a missing key is a bug you want to hear about, and `get()` when absence is normal. |
| Q38 | A | 2.3 | authored | Assigning a new key adds it; assigning an existing key replaces the value. So the dict has three keys and `"a"` is 9. |
| Q39 | A | 2.3 | docs | `.items()` yields `(key, value)` pairs, which unpack into `k, v`. Iterating the dict directly yields keys only, so B fails to unpack, and `.values()` yields values, so C indexes with the wrong thing. |
| Q40 | A | 2.4 | authored | A set discards duplicates, leaving `{1, 2, 3}` — length 3. `len(set(x))` is the idiomatic way to count distinct values. |
| Q41 | A | 2.4 | docs | `&` is intersection (members of both) and `|` is union (members of either). `-` gives difference and `^` symmetric difference. |
| Q42 | A & B | 2.4 | authored | Sets hold no duplicates and are unordered, so there is no indexing and no reliable insertion order. Elements must be hashable, which is why a list cannot go in a set but a tuple can. |
| Q43 | A | 2.4 | authored | `{}` is an empty dictionary — dictionaries got the braces first. An empty set has to be `set()`. Non-empty `{1, 2}` is a set, which makes the empty case inconsistent-looking and easy to get wrong. |
| Q44 | A | 2.1 | authored | Ordered, duplicates allowed and mutable is the definition of a list. A set loses order and duplicates, a tuple cannot be edited, and a frozenset is an immutable set. |
| Q45 | A | 3.1 | docs | A class describes structure and behaviour; an object is one concrete thing built from it. `Dog` is the class, `Rex` is the object. |
| Q46 | A | 3.1 | authored | Compilation is a build step, not an OOP principle. The pillars usually listed are encapsulation, inheritance, polymorphism and abstraction. |
| Q47 | A | 3.2 | authored | `species` is defined in the class body, so it is a class attribute shared by every instance. `name` is assigned on `self` in `__init__`, so each instance has its own. |
| Q48 | A | 3.2 | authored | `Counter.total` names the class attribute, so both calls increment the same counter and both instances read the same value. Had `bump` used `self.total += 1` it would have created a separate instance attribute on first assignment and printed `1 1`. |
| Q49 | A | 3.3 | authored | The list is created fresh inside `__init__` on each instantiation, so it belongs to the instance. Had `items = []` been written in the class body instead, every instance would share one list - the classic mutable-class-attribute bug. |
| Q50 | A | 3.3 | authored | Each call to `Point()` builds a distinct object, so `a is b` is false. `c = a` binds another name to the same object, so `a is c` is true. `is` compares identity, `==` compares value. |
| Q51 | A & C | 3.4 | docs | `__init__` initialises an already-created instance and receives it as `self`. Allocation is `__new__`'s job. A class with no `__init__` inherits `object.__init__` and works fine. |
| Q52 | A | 3.4 | authored | `__init__` must return `None`; returning anything else raises `TypeError: __init__() should return None`. Set attributes on `self` instead of returning a value. |
| Q53 | A | 3.4 | authored | A default value makes the parameter optional, so `User("Ada")` uses `member`. This is the Python answer to "constructors with different signatures" - one constructor with defaults, not several. |
| Q54 | A | 3.5 | docs | `hasattr` reports whether the attribute exists. `getattr(obj, name, default)` returns the default rather than raising when it does not. Without the default it would raise `AttributeError`. |
| Q55 | A | 3.5 | authored | Attribute lookup checks the instance first, then the class. Assigning `b.tag` creates an instance attribute that shadows the class attribute for that object only - `Base.tag` is untouched, and other instances still see `class`. |
| Q56 | A | 3.5 | authored | An instance's `__dict__` holds only what was set on the instance. Class attributes live in `P.__dict__`, which is why lookup has to check both. |
| Q57 | A | 3.6 | docs | Calling a class instantiates it and returns an instance. The vocabulary matters on this exam: class, instance, attribute, method, instantiation. |
| Q58 | A | 3.6 | docs | `obj.method()` is shorthand for `Class.method(obj)`, so the instance arrives as the first positional argument. `self` is a naming convention, not a keyword - but breaking it will confuse every reader. |
| Q59 | A | 3.7 | docs | Encapsulation bundles state with the behaviour that acts on it and keeps the internals out of the public surface. Option B describes multiple inheritance and C describes polymorphism. |
| Q60 | A | 3.7 | docs | One underscore is a documented convention meaning "not part of the public API". Nothing enforces it - the attribute is fully readable. PEP 8 describes it as a weak internal-use indicator. |
| Q61 | A | 3.8 | authored | `Dog` defines nothing, so lookup walks up to `Animal` and finds `speak`. Inheritance means the subclass gets the parent's methods without repeating them. |
| Q62 | A | 3.8 | docs | The subclass's `__init__` overrides the parent's, so the parent's must be called explicitly. `super().__init__(2)` does that, setting `wheels` before the subclass adds `pedals`. Forgetting the `super()` call is how half-initialised objects happen. |
| Q63 | A | 3.8 | docs | `isinstance(b, A)` is true because `B` derives from `A`, and `issubclass(B, A)` is true for the same reason. An `A` is not a `B`, so the third is false - inheritance runs one way only. |
| Q64 | A | 3.8 | authored | Python resolves multiple inheritance by the method resolution order, which for `D(B, C)` is D, B, C, A. `B.who` is found first. Python does not raise on the diamond; it linearises it. |
| Q65 | A | 3.9 | authored | `Square.area` overrides `Shape.area` because the subclass is searched first. This is the mechanism behind polymorphism: same call, different behaviour by type. |
| Q66 | A | 3.9 | docs | `print()` converts its argument with `str()`, which calls `__str__`. Without it you get the default `<Coin object at 0x...>`. `__repr__` is the developer-facing sibling and is what the REPL shows. |
| Q67 | A | 3.10 | authored | An attribute starting with two underscores is name-mangled to `_ClassName__attr`, so `v.__code` fails from outside while `v._Vault__code` works. The purpose is avoiding accidental clashes in subclasses, not security. |
| Q68 | A | 3.10 | docs | Python has no access modifiers. Double underscore mangles the name, single underscore signals intent, and neither blocks access. The documented model is that everything is reachable and conventions carry the meaning. |
| Q69 | A | 3.11 | authored | Defining a method twice simply rebinds the name - the second definition wins and the first is gone, so a two-argument call would now fail. This is why the blueprint's phrase "function overloading" does not describe real Python behaviour. See the objectives note on 3.11. |
| Q70 | A | 3.11 | authored | Both objects answer `speak()`, so the loop works without a common base class. Python cares that the method exists, not what the type is - duck typing, and the usual meaning of polymorphism here. |
| Q71 | A & B | 3.11 | docs | Defaults and `*args` are how one Python function accepts varying calls. Defining it twice replaces the first definition. `typing.overload` exists but is a type-checker hint with no runtime effect. |
| Q72 | A | 4.1 | docs | `import math` binds the module object to the name `math`; its contents are reached through the dot. A bare `sqrt(9)` fails with `NameError` unless it was imported directly. |
| Q73 | A | 4.1 | docs | Both load the module. The difference is what lands in your namespace: the module object, or the individual name. `from ... import` is not faster - the whole module still executes; only the binding differs. |
| Q74 | A | 4.1 | docs | `as` renames the binding in your file only. Nothing on disk changes. `np` is a universal convention for NumPy and worth using. |
| Q75 | A | 4.1 | docs | A star import binds every public name at once, so an unnoticed collision can silently replace one of your own functions - and a reader cannot tell where a name came from. Explicit imports are the documented preference. |
| Q76 | A | 4.2 | authored | `ceil` rounds up toward positive infinity, so `-2.5` becomes `-2`. `floor` rounds down toward negative infinity, giving `-3`. For negative numbers "up" and "down" are the opposite of "bigger" and "smaller" in magnitude, which is the trap. |
| Q77 | A | 4.2 | docs | `\d+` matches one or more consecutive digits, and `findall` returns every non-overlapping match as a list of strings - note strings, not integers. Without the `+` it would match single digits. |
| Q78 | A | 4.2 | docs | `%Y` is the four-digit year, `%m` the zero-padded month and `%d` the zero-padded day. The `date` object also exposes `.year`, `.month` and `.day` directly. |
| Q79 | A & B | 4.2 | docs | Seeding fixes the generator's starting state, so the same sequence follows - essential for reproducible tests. `randint(a, b)` is inclusive at *both* ends, so 6 is possible, and `random()` returns a float in [0.0, 1.0). |
| Q80 | A | 4.2 | docs | `sys.path` is the list of directories searched on import, starting with the script's own directory. Appending to it is how a script reaches modules outside its folder. |
| Q81 | A | 4.3 | docs | The module name is the filename without `.py`, so `import helpers`. Writing `import helpers.py` makes Python look for a module `py` inside a package `helpers` and fails. |
| Q82 | A | 4.3 | docs | The documentation defines a module as a file containing Python definitions and statements, with the file name being the module name plus the `.py` suffix. |
| Q83 | A | 4.4 | docs | Python sets `__name__` to `"__main__"` in the file being run directly, and to the module's own name when it is imported. The guard therefore separates "run me" behaviour from "import me" behaviour, so importing the file does not execute the script. |
| Q84 | A | 4.4 | docs | On import, `__name__` is the module's name - here `"helpers"`. Only the file the interpreter was pointed at gets `"__main__"`. |
| Q85 | A | 4.5 | docs | `__init__.py` marks the directory as a package and runs on import. It may be empty. Namespace packages can omit it, but the exam-level answer is the `__init__.py` layout. |
| Q86 | A & B | 4.5 | docs | Both reach the function: `from tools.text.strip import clean` binds it directly, and importing the full dotted path lets you call it through the chain. Option C reverses the syntax, and `from tools import clean` fails because `clean` is not defined in the top package. |
| Q87 | A | 4.6 | authored | NumPy's array display separates elements with spaces, not commas - so `[1 2 3]`. Seeing commas means it is a list. The `array([1, 2, 3])` form is the `repr`, which is what the REPL echoes. |
| Q88 | A | 4.6 | docs | `shape` is (rows, columns), `ndim` is the number of dimensions and `size` is the total element count. Two rows of three gives `(2, 3)`, 2 and 6. |
| Q89 | A | 4.6 | docs | `arange(start, stop, step)` excludes the stop value, exactly like `range` - 0, 3, 6, 9, and 12 would be past 10. |
| Q90 | A | 4.6 | docs | `zeros` defaults to float, which is why they print as `0.` with a trailing dot. `dtype=int` forces the integer type, so the ones print without dots. |
| Q91 | A | 4.7 | authored | An array has one dtype for every element. This array is integer, so assigning 9.7 truncates toward zero to 9 - no error, no warning, silent data loss. It is the sharpest practical difference from a list. |
| Q92 | A & B | 4.7 | docs | An array is homogeneous and typed, and arithmetic is element-wise (vectorised) rather than list concatenation. It has no `append` method - `np.append` exists but returns a new array. |
| Q93 | A | 4.8 | authored | Both `+` and `*` work element by element on arrays. On lists `+` concatenates and `*` repeats, which is the exact confusion the next question tests. |
| Q94 | A | 4.8 | authored | Same operator, two meanings: `list * 2` repeats the sequence, `array * 2` multiplies every element. Anyone moving from lists to NumPy hits this in the first hour. |
| Q95 | A | 4.8 | authored | Basic slicing of a NumPy array returns a *view* that shares memory with the original, so writing through the slice changes the parent. Slicing a list returns a copy. Use `a[1:3].copy()` when you want independence. |
| Q96 | A | 4.8 | docs | `a > 2` produces a boolean array, and indexing with it selects the elements where it is True. This is boolean masking, the standard NumPy way to filter. |
| Q97 | A | 4.9 | authored | `mean()` returns a float even for integer input, so `5.0`. `sum()` and `max()` keep the integer type. |
| Q98 | A | 4.9 | docs | `axis=0` collapses down the rows, giving one total per column: 1+3 and 2+4. `axis=1` collapses across the columns, giving one total per row: 1+2 and 3+4. Reading the axis as "the axis that disappears" is the reliable way to remember it. |
| Q99 | A | 4.9 | authored | With an even number of values the median is the mean of the two middle ones, so (2+3)/2 = 2.5, and the result is a float. |
| Q100 | A | 4.9 | docs | `np.std` is the standard deviation and `np.var` the variance. `np.deviation` and `np.sd` do not exist - plausible-looking names that were never real, which is the single most common wrong answer pattern in Python question banks. |
| Q101 | A | 5.1 | docs | A syntax error is found while the source is being parsed, so nothing runs at all and it cannot be caught by a `try` in the same file. An exception is raised by code that parsed fine but hit a problem at run time, and that is what `try`/`except` is for. |
| Q102 | A | 5.1 | docs | `BaseException` is the root. `Exception` sits below it and deliberately excludes `SystemExit`, `KeyboardInterrupt` and `GeneratorExit`, which is exactly why catching `Exception` is the safe default - it leaves the ways of stopping a program alone. |
| Q103 | A | 5.1 | authored | A name that was never bound gives `NameError`; `'a' + 1` mixes incompatible types so `TypeError`; `int('abc')` gets the right type with an unusable value so `ValueError`; an index past the end gives `IndexError`. Learning to predict the class is most of debugging. |
| Q104 | A | 5.1 | docs | `TypeError` means the *type* was inappropriate, `ValueError` means the type was fine but the *value* was not. `int()` accepts strings, so `"abc"` is a value problem. `int([])` is a type problem and does raise `TypeError`. |
| Q105 | A | 5.2 | authored | Handlers are checked in order and the first matching one runs. `ZeroDivisionError` matches first, so the broader handler never fires. |
| Q106 | A | 5.2 | docs | `as e` binds the exception instance. `e.args` is the tuple of arguments it was raised with - here one string - and `str(e)` gives the message. |
| Q107 | A | 5.2 | authored | `finally` runs on the way out no matter how the block is left, including a `return`. The return value is computed first, then `finally` runs, then the function actually returns - which is why `finally` prints first. |
| Q108 | A | 5.2 | docs | A bare `except:` catches `BaseException`, so it swallows Ctrl-C and `SystemExit` along with real errors, and makes a program hard to stop or debug. Catch `Exception` if you must be broad, and prefer naming the class. |
| Q109 | A | 5.2 | docs | Multiple types go in a parenthesised tuple. The comma form without parentheses was Python 2 syntax for `as` and is a syntax error now, and `or` evaluates to a single class rather than combining them. |
| Q110 | A | 5.2 | authored | Handlers are tried top to bottom and `Exception` matches everything, so listing it first makes every narrower clause below it dead code. Order handlers most specific first - the same rule as `if`/`elif`. |
| Q111 | A | 5.3 | docs | No exception was raised, so `except` is skipped and `else` runs. `finally` runs last, always. |
| Q112 | A | 5.3 | docs | `else` holds the code that should run only on success. Keeping it out of the `try` matters: if it lived inside, an exception raised by *it* would be caught by the same handler, which usually hides a bug. |
| Q113 | A | 5.3 | authored | The exception fires, so `except` runs and `else` is skipped entirely. `finally` still runs. `else` means "the try block succeeded", not "otherwise". |
| Q114 | A | 5.4 | docs | Subclass `Exception` - the documentation's own recommendation. `pass` is enough for a body; the inherited `__init__` already accepts a message. There is no built-in class called `Error`. |
| Q115 | A | 5.4 | authored | The inherited `Exception.__init__` stores the message, and `str(e)` returns it, so printing the instance shows the text. No custom `__init__` is required. |
| Q116 | A | 5.4 | docs | `except` matches the named class and anything derived from it, so a base exception per application lets one handler cover a whole family. This is why exception hierarchies are worth designing. |
| Q117 | A | 5.5 | docs | Division by zero raises `ZeroDivisionError`. It is a subclass of `ArithmeticError`, so `except ArithmeticError` would also catch it - but the exception actually raised is `ZeroDivisionError`. |
| Q118 | A & B | 5.5 | authored | Floor division and modulo by zero both raise. `0 / 7` is a normal division giving `0.0`, and `0 ** 0` is defined as `1` in Python. |
| Q119 | A | 5.5 | authored | Unlike C or JavaScript, Python raises rather than returning infinity. `float('inf')` exists, but you will not get it from dividing by zero. |
| Q120 | A | 5.5 | authored | Catching the specific exception keeps the happy path clean and handles the one real failure. Option B tests after the division has already raised, and `//` raises just the same. |
| Q121 | A | 5.6 | docs | `FileNotFoundError` is the specific subclass raised when the path does not exist. Catching it by name is better than catching `OSError`, which would also swallow permission problems. |
| Q122 | A & B | 5.6 | docs | `FileNotFoundError` derives from `OSError`, and since Python 3.3 `IOError` is an alias of `OSError` rather than a separate class. An empty file opens fine and raises nothing. |
| Q123 | A | 5.6 | authored | The handler runs, `data` is set to the fallback, and the program continues - the standard shape for an optional config file. |
| Q124 | A | 5.6 | authored | Catching `FileNotFoundError` alone handles the case you planned for while letting a permission error or a bad disk surface as a crash you can see. Options B and C hide the second case, and D still leaves a race between the check and the open. |
| Q125 | A | 6.1 | docs | `with` is a context manager: it closes the file on the way out, including when an exception is raised inside the block. Without it a raised exception can leave the handle open and the write unflushed. |
| Q126 | A | 6.1 | docs | The default is `"r"` - read, text mode. Text mode decodes bytes to `str` and translates newlines. `"w"` would destroy the file's contents, which is why the default is read. |
| Q127 | A | 6.1 | docs | `open()` returns a file object. The contents only arrive when you call `read()`, `readline()` or `readlines()`, or iterate it. |
| Q128 | A | 6.2 | docs | A relative path resolves against the current working directory, which is wherever the process was started - not the script's folder. This is why a script works when run from its own directory and fails from anywhere else. |
| Q129 | A & B | 6.2 | authored | An absolute path is complete from the root: a drive letter and backslash on Windows, a leading slash on Linux and macOS. Bare and dotted names are relative. |
| Q130 | A | 6.2 | docs | `os.path.abspath()` normalises a path against the current working directory. `os.path.realname` does not exist; the real neighbour is `os.path.realpath`, which also resolves symlinks. |
| Q131 | A | 6.3 | authored | `read()` returns the entire file as a single string with newlines intact. `repr()` is used here so the newline characters are visible instead of being printed. |
| Q132 | A | 6.3 | docs | `readlines()` returns a list of lines and keeps the trailing newline on each. Forgetting that is why comparisons against `"a"` fail - the value is `"a\n"`. `strip()` or `splitlines()` removes it. |
| Q133 | A | 6.3 | docs | A file object is its own iterator and yields one line per step, which is the memory-efficient way to read a large file. `strip()` removes the trailing newline before printing. |
| Q134 | A | 6.3 | authored | The file keeps a read position. After the first `read()` it sits at the end, so the second returns an empty string. Call `f.seek(0)` to go back, or store the contents in a variable. |
| Q135 | A | 6.4 | docs | Mode `"w"` truncates the file to zero length the moment it is opened, so opening for write and doing nothing still empties it. This is the most destructive default in file handling. |
| Q136 | A | 6.4 | docs | `"a"` positions at the end and preserves what is there. `"w"` truncates, and `"x"` creates but fails if the file already exists. |
| Q137 | A | 6.4 | authored | `write()` returns the number of characters written and adds no newline of its own, so two writes run together. Add `"\n"` yourself, or use `print(..., file=f)`. |
| Q138 | A | 6.5 | docs | `mkdir` creates a single directory and raises `FileNotFoundError` if the parent chain is missing; `makedirs` builds the whole chain. Add `exist_ok=True` to `makedirs` when the directory may already be there. |
| Q139 | A | 6.5 | docs | `os.listdir(path)` returns the entry names - names only, not full paths, which is why joining with `os.path.join` is nearly always the next line. `os.scandir` is the richer modern alternative. |
| Q140 | A | 6.6 | docs | `os.path.join` uses the platform's separator, so the same source runs on Windows and on Linux. It does not touch the filesystem and does not check existence. |
| Q141 | A | 6.6 | docs | `exists` is true for anything at that path, `isfile` narrows it to a regular file and `isdir` to a directory. For an existing file that gives True, True, False. |
| Q142 | A | 6.6 | docs | `basename` returns the last component, `dirname` everything before it, and `splitext` splits into stem and extension with the dot kept on the extension. |
| Q143 | A | 7.1 | docs | Tkinter is part of the standard library on a normal CPython install, so no `pip install` is needed - and `pip install tkinter` fails, which confuses beginners. Some Linux distributions package it separately as `python3-tk`. |
| Q144 | A | 7.1 | authored | A GUI presents widgets and reacts to events in whatever order the user produces them. A command-line program follows its own fixed sequence. That inversion of control is the core idea of the domain. |
| Q145 | A | 7.1 | docs | `mainloop()` starts the event loop: it waits for events and dispatches them to the bound handlers, and it does not return until the window is closed. Nothing appears without it. |
| Q146 | A & B | 7.2 | docs | `Label` shows non-editable text or an image, `Entry` takes one line of typed input. `Button` triggers a command, and `Frame` is an invisible container used to group widgets. Multi-line text is the `Text` widget. |
| Q147 | A | 7.2 | docs | `Entry.get()` returns the current contents as a string. There is no `.text` attribute holding the value; `insert()` and `delete()` are the write side. |
| Q148 | A | 7.2 | docs | `Text` is the multi-line editable widget. `Label` and `Message` display text without editing, and `Entry` is single-line. |
| Q149 | A | 7.3 | authored | `command=say_hi()` runs the function right there and hands the button its return value, so the message prints once at startup and the button then does nothing. Pass the function object itself: `command=say_hi`. Use `lambda: say_hi(arg)` when you need arguments. |
| Q150 | A | 7.3 | docs | `bind(sequence, handler)` connects an event to a callback, with sequences such as `<Button-1>` for a left click and `<Return>` for the Enter key. The handler receives an event object. |
| Q151 | A | 7.3 | authored | In an event-driven program you register handlers and hand control to the event loop; the user decides what runs and when. That is why a GUI has no single top-to-bottom path through the code. |
| Q152 | A | 7.4 | docs | Tkinter has exactly three geometry managers: `pack` stacks against a side, `grid` uses rows and columns, and `place` uses explicit coordinates. |
| Q153 | A | 7.4 | authored | A container may be managed by one geometry manager only; mixing `pack` and `grid` in the same parent raises `TclError`. You can still use different managers in different frames, which is the normal way to build a mixed layout. |
| Q154 | A | 7.4 | docs | `row` and `column` are the grid cell coordinates within the parent, numbered from zero. `sticky`, `rowspan` and `columnspan` refine the placement. |
| Q155 | A & B | 7.4 | docs | `pack` places each widget against a side of the remaining space, controlled by `side` with `top`, `left`, `right` or `bottom`. Exact coordinates are `place`, and `row`/`column` belong to `grid`. |
| Q156 | A | 7.5 | docs | `Tk()` creates the main window. Every other widget takes it - or a frame inside it - as its parent, and `mainloop()` is called on it. Extra windows use `Toplevel()`. |
| Q157 | A | 7.5 | authored | Creating a widget does not display it. Until a geometry manager is called it has no place in the layout and nothing is drawn, so the window opens empty with no error. This is the most common first Tkinter bug. |
| Q158 | A | 1.4 | authored+scenario | A default argument is evaluated **once**, when the `def` runs — not on each call. So every call that omits `bucket` appends to the same list, and it grows for the life of the program. The fix is `def collect(item, bucket=None):` then `if bucket is None: bucket = []`. This is the single most-cited Python gotcha and it is worth recognising instantly. |
| Q159 | A | 1.3 | authored+scenario | `==` asks "same value", `is` asks "same object in memory". Two separately built lists are equal but not identical. Use `is` only for `None`, `True` and `False`; everywhere else you almost always mean `==`. |
| Q160 | A | 1.3 | authored+scenario | Binary floating point cannot represent 0.1 or 0.2 exactly, so the sum is 0.30000000000000004. Never compare floats with `==`; round, or test that the difference is below a small tolerance. Money is better handled with `decimal.Decimal` or whole pence as integers. |
| Q161 | A | 1.4 | authored+scenario | `break` ends the whole loop on the first iteration. `continue` is the one that skips the rest of the current pass and moves to the next item. Mixing them up is a very common first-week error. |
| Q162 | A | 2.1 | authored+scenario | The loop walks by position while `remove()` shifts everything left, so after removing index 1 the loop moves to index 2 and steps straight over the second `2`. Iterate over a copy (`for n in nums[:]`) or build a new list with a comprehension. |
| Q163 | A | 2.3 | authored+scenario | Adding or deleting keys during iteration raises `RuntimeError: dictionary changed size during iteration`. Iterate over a snapshot — `for k in list(scores)` — or collect the keys to delete and remove them afterwards. |
| Q164 | A | 2.2 | authored+scenario | A tuple fixes *which objects* it holds, not whether those objects can change. The inner list is still mutable. And because that list is unhashable, the whole tuple becomes unhashable too, so it cannot go in a set or be a dictionary key. |
| Q165 | A | 2.4 | authored+scenario | Set members must be hashable, and lists are not because they can change. Convert to tuples. The same rule governs dictionary keys — note `("c",)` needs the trailing comma to be a tuple. |
| Q166 | A | 3.2 | authored+scenario | `items = []` in the class body creates **one** list shared by every instance, so both carts see the apple. Assign it in `__init__` with `self.items = []` and each instance gets its own. A mutable class attribute is the OOP twin of the mutable default argument in Q158. |
| Q167 | A | 3.1 | authored+scenario | Classes earn their place when data and the behaviour that acts on it belong together. Values with no behaviour are usually better as a dictionary or a small data class. "Use a class for everything" produces classes that are dictionaries with extra typing. |
| Q168 | A | 3.3 | authored+scenario | Reading falls back to the class, but *writing* always creates an instance attribute. So `a.debug = True` shadows the class attribute for `a` alone, and `b` and `Config` are untouched. Set it on the class (`Config.debug = True`) if you meant it globally. |
| Q169 | A | 3.6 | docs+scenario | `report` is an instance, `export` is a method on its class, and `"csv"` is the argument passed to that method. The parameter is the name inside the method definition that receives it; the argument is the value at the call site. |
| Q170 | A | 3.7 | authored+scenario | Encapsulation is about controlling access, not hiding names. Keep the value internal and put the rule in a `property` setter or a method, so an invalid assignment raises rather than silently succeeding. Renaming to `__balance` only mangles the name — `acc._Account__balance = -50` still works. |
| Q171 | A | 3.9 | authored+scenario | Defining `__init__` in the subclass **replaces** the parent's; it is not added to it. Without `super().__init__(name)` the parent's setup never runs and `name` is never assigned, so the attribute lookup fails at use, far from the real cause. |
| Q172 | A | 3.10 | authored+scenario | Name mangling is per class: `Base.__value` becomes `_Base__value` and `Child.__value` becomes `_Child__value`. They are two different attributes, so `Base.get()` still reads its own. That isolation is exactly what mangling is for — it prevents a subclass clobbering a parent's internals by accident. |
| Q173 | A | 3.9 | authored+scenario | `super().write(...)` calls the parent implementation from inside the override, so the subclass can extend rather than replace. Calling `self.write(...)` instead would recurse forever. |
| Q174 | A | 4.3 | authored+scenario | The script's own directory is first on `sys.path`, so a local `random.py` is found before the standard library's. Every `import random` in that folder then gets the wrong module. Avoid naming files after standard modules — `random.py`, `string.py`, `math.py`, `email.py` are all common casualties. |
| Q175 | A | 4.4 | authored+scenario | Every top-level statement runs on import. The `if __name__ == "__main__":` guard confines self-tests and demo output to direct execution. Without it, importing the module for one function drags along all of its side effects. |
| Q176 | A | 4.5 | docs+scenario | In the traditional layout `utils/` needs an `__init__.py`, and the directory that *contains* `utils/` has to be on the import path — usually because it is the script's own folder. Namespace packages can go without `__init__.py`, but at this level the missing file is the likelier cause. |
| Q177 | A | 4.7 | authored+scenario | An array occupies a fixed block of memory with a fixed size, so there is nothing to append to in place. `np.append` allocates a new array and copies — fine occasionally, expensive in a loop. Collect into a Python list and convert once. |
| Q178 | A | 4.8 | authored+scenario | Element-wise operations require the shapes to be compatible; broadcasting can stretch a dimension of size 1, but 3 against 2 has no valid alignment, so it raises. This is not concatenation — `np.concatenate` is what joins arrays. |
| Q179 | A | 4.9 | authored+scenario | With no axis the mean is taken over every element: (60+70+80+90)/4 = 75.0. `axis=1` collapses across the columns, giving a mean per row: 65 and 85. Read the axis as "the one that disappears". |
| Q180 | A | 4.2 | docs+scenario | `%Y` four-digit year, `%m` zero-padded month, `%d` zero-padded day. `%y` is the two-digit year and `%M` is minutes, so option B silently produces something plausible and wrong — the worst kind of mistake in a timestamp. |
| Q181 | A | 5.2 | authored+scenario | `valeus` is a typo, which raises `NameError` — and the bare `except` catches it along with everything else, converting a crash that would have named the line into a silent `None`. Catch the specific exception you expect, and let the ones you did not expect surface. |
| Q182 | A | 5.2 | authored+scenario | `finally` always runs, and a `return` inside it overrides the value the `try` was about to return. The real result vanishes with no error. Never `return` from `finally` — use it for cleanup only. |
| Q183 | A | 5.1 | authored+scenario | `int("twelve")` gets an acceptable *type* with an unusable *value*, so it raises `ValueError`. The `TypeError` clause is simply never reached. Predicting the exception class is most of writing a handler that works. |
| Q184 | A | 5.4 | authored+scenario | Subclassing `Exception` with an empty body still inherits an `__init__` that stores its arguments in `args`, and `str(e)` returns the single argument. You only need a custom `__init__` when you want extra structured fields. |
| Q185 | A | 6.4 | authored+scenario | Writes are buffered and are not guaranteed to reach disk until the file is closed or flushed, so the first read sees an empty file. `with open(...) as f:` closes on the way out including on exception, which is why it is the default advice. |
| Q186 | A | 6.2 | authored+scenario | A relative path resolves against the current working directory, which is wherever the process was launched — not the script's folder. `__file__` gives the script's own location, and building the path from it makes the script runnable from anywhere. `./data.txt` is still relative to the working directory, so option C changes nothing. |
| Q187 | A | 6.5 | docs+scenario | `os.listdir()` returns bare entry names. Opening one only works while the working directory happens to be that folder. Rejoin with `os.path.join(directory, name)` — or use `os.scandir()`, whose entries carry a usable `.path`. |
| Q188 | A | 7.5 | authored+scenario | Widget code runs to completion *before* `mainloop()` starts accepting input, so a read at build time happens before the user has typed. Read the value inside the callback, which runs in response to the click. This is the practical consequence of event-driven control flow. |
| Q189 | A | 7.4 | authored+scenario | `grid` is built for rows and columns, and `columnspan=2` is exactly how one widget stretches across both. `pack` with `side="left"` would put the status bar beside them, not under. Option D is the error from Q153 — one container, one geometry manager. |
| Q190 | A | 7.3 | authored+scenario | `command=handler()` runs the function immediately and hands the button its return value, usually `None` — so the button is wired to nothing and clicking is silent. Pass the function object: `command=handler`, or `command=lambda: handler(arg)` when arguments are needed. Silent failure is what makes it hard to spot. |
