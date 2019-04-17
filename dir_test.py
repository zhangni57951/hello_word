import os
print(os.path.abspath('.'))
print(os.path.abspath(".."))
print(os.path.exists("/python_work"))
print(os.path.exists("\python_work\test"))
print(os.path.isdir('\python_work'))

from pathlib import Path
p = Path('.')
print(p.resolve("."))
p.is_dir()
q = Path("/tmp/a/b/c")
Path.mkdir(q,parents=True)