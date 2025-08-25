import pydoc
from itertools import batched

obj = "example_str"

methods = []
for item in dir(obj):
    # Get the actual attribute object
    attribute = getattr(obj, item)
    # Check if it's callable (a method) and not a dunder method
    if callable(attribute) and not item.startswith('__'):
        methods.append(item)

print("====="*10)
print(f"===== There are {len(methods)} methods in the 'str' class ====")
n = 5
print("===== here they are, split in batches of {n} =====")
print("====="*10)
for batch in batched(methods, n):
    print(batch)
print("====="*10)



print(pydoc.render_doc(str.ljust))
