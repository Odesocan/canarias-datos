"""Entry point: `python3 -m ccaa --ccaa <id3> ...`."""
from ._common.dispatcher import main
import sys

if __name__ == "__main__":
    sys.exit(main())
