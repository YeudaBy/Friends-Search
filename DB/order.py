import os
import re

# rename files name by template
p = "Files/s10/"
for f in os.listdir(p):
    print(f)
    name = r".*s(?P<s>\d{2})e(?P<e>\d{2}).*"
    data = re.match(name, f, re.IGNORECASE).groupdict()
    new_name = f"{p}{data['s']}-{data['e']}"
    os.rename(p + f, new_name)
    print(f"rename from -{f}- to -{new_name}-")

