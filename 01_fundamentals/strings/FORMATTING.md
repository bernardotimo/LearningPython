# String Formatting in Python

Python has three ways to build strings from values. This folder has a demo
for each of the modern styles plus the classic `%` operator.

| Style | Example | Demo file |
|-------|---------|-----------|
| `%` operator (old) | `"Hi %s" % name` | [formatOperatorDemo.py](formatOperatorDemo.py) |
| `.format()` method | `"Hi {}".format(name)` | [formattingDemo.py](formattingDemo.py) |
| f-strings (modern) | `f"Hi {name}"` | [formattingDemo.py](formattingDemo.py) |

For new code, prefer **f-strings** — they are the most readable and fastest.
Learn `%` because you will still meet it in old code and log messages.

---

## 1. The `%` operator

Syntax: `"template" % (values)`

```python
"My name is %s and I am %d years old" % (name, age)
```

### Conversion codes

| Code | Meaning | Example input | Output |
|------|---------|---------------|--------|
| `%s` | string  | `"Ana"`       | `Ana`  |
| `%d` | integer | `22`          | `22`   |
| `%f` | float   | `3.14159`     | `3.141590` |
| `%x` | hexadecimal | `255`     | `ff`   |
| `%o` | octal   | `8`           | `10`   |
| `%e` | scientific | `1000000`  | `1.000000e+06` |
| `%%` | literal percent sign | — | `%` |

### Precision and width

```python
"%.2f"   % 3.14159   # "3.14"   -> 2 decimal places
"%5d"    % 42        # "   42"  -> width 5, right aligned
"%-5d"   % 42        # "42   "  -> width 5, left aligned
"%8.2f"  % 3.5       # "    3.50" -> width 8, 2 decimals
```

- **Width** = minimum number of characters (pads with spaces).
- A minus sign (`%-5d`) makes it **left aligned**.
- **Precision** (`.2`) controls decimal places for floats.

### Named placeholders

Pass a dictionary and reference keys by name:

```python
person = {"name": "Ana", "age": 30}
"%(name)s is %(age)d years old" % person
```

---

## 2. The `.format()` method

Placeholders are `{}`; values go inside `format()`.

```python
"My name is {} and I am {} years old".format(name, age)  # by position
"{0} {1} {0}".format("a", "b")                            # by index -> "a b a"
"{n} is {a}".format(n="Ana", a=30)                        # by name
```

Format spec after a colon, same idea as `%`:

```python
"{:.2f}".format(3.14159)   # "3.14"
"{:>10}".format("hi")      # right aligned in 10 spaces
"{:,}".format(1000000)     # "1,000,000" -> thousands separator
```

---

## 3. f-strings (recommended)

Put an `f` before the quotes and write expressions directly inside `{}`.

```python
f"My name is {name} and I am {age} years old"
f"The sum is {a + b}"          # expressions allowed
f"Uppercase: {name.upper()}"   # method calls allowed
```

Same format spec after a colon:

```python
f"{pi:.2f}"      # 2 decimals
f"{number:,}"    # thousands separator
f"{score:.2%}"   # percentage
f"{name:<10}"    # left aligned in 10 spaces
f"{price:>5.2f}" # right aligned, 2 decimals
```

### Alignment quick reference (works in `.format()` and f-strings)

| Symbol | Meaning |
|--------|---------|
| `<` | left align |
| `>` | right align |
| `^` | center |
| `,` | thousands separator |
| `.Nf` | N decimal places |
| `.N%` | percentage with N decimals |

---

## Running the demos

These files just print — run them from the terminal:

```bash
python formatOperatorDemo.py
python formattingDemo.py
```
