import os
from functools import reduce
from pathlib import Path

script_dir = os.path.dirname(os.path.realpath(__file__))
addons_dir = Path(script_dir) / "addons"

addon_names = [filename.stem for filename in addons_dir.glob("*.py")]
addons = sorted(
    [__import__(f"addons.{name}", fromlist=name) for name in addon_names],
    key=lambda mod: getattr(mod, 'weight', 0))

text = input()
print(reduce(lambda acc, val: val.process(acc), addons, text))
