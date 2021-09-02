import traceback

try:
    raise ValueError
except ValueError:
    tb = traceback.format_exc()
else:
    tb = "No error"
finally:
    print(tb)