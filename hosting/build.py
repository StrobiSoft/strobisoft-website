"""Build the public company site from an explicit inventory; refuse overwrites."""
import argparse
import hashlib
import json
import shutil
import tempfile
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[1]
PUBLIC = ("index.html", "node-ijet/index.html", "use-cases/index.html", "site.css",
          "robots.txt", "sitemap.xml", "google99a08fb987dd6c86.html")


def build(target):
    if target.exists() or target.is_symlink():
        raise FileExistsError(target)
    with tempfile.TemporaryDirectory(dir=target.parent) as tmp:
        tree = Path(tmp) / "release"
        web = tree / "public"
        hashes = {}
        for name in PUBLIC:
            src = SOURCE / name
            path = web / name
            path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src, path)
            hashes[name] = hashlib.sha256(path.read_bytes()).hexdigest()
        (tree / "manifest.json").write_text(json.dumps(hashes, indent=2, sort_keys=True) + "\n")
        tree.rename(target)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("target", type=Path)
    build(parser.parse_args().target)
