# libspec-conventional-commits

Executable [libspec](https://github.com/libspec/libspec) specification for the [Conventional Commits v1.0.0](https://www.conventionalcommits.org/) specification.

Inherit `Commit` (or `ConvCommit`) into any `libspec.Feature` subclass to endow your features with Conventional Commits specifications, schemas, definitions, and rules.

---

## Installation

```bash
uv add libspec-conventional-commits
```

or

```bash
pip install libspec-conventional-commits
```

---

## Usage

```python
from libspec import Feature
from libspec.conventional_commits import Commit

class MyBaseFeature(Feature, Commit):
    pass

class MyAwesomeFeature(MyBaseFeature):
    pass
```

You can also combine it with other generic specs like `libspec-diataxis`:

```python
from libspec import Feature
from libspec.diataxis import Diataxis
from libspec.conventional_commits import Commit

class MyBaseFeature(Feature, Diataxis, Commit):
    pass

class MyAwesomeFeature(MyBaseFeature):
    def tutorial(self):    return "..."
    def how_to(self):      return "..."
    def reference(self):   return "..."
    def explanation(self): return "..."
```

---

## License

GPL-3.0-or-later
