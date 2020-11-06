import os
__all__ = ['Config']
class Config:
GOOGLE_CHROME_DRIVER = os.environ.get("GOOGLE_CHROME_DRIVER", None)
GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)
