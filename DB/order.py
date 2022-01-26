from os import listdir, rename
from re import IGNORECASE, match

# rename files name by template
p = "Files/s10/"
for f in listdir(p):
    print(f)
    name = r".*s(?P<s>\d{2})e(?P<e>\d{2}).*"
    data = match(name, f, IGNORECASE).groupdict()
    new_name = f"{p}{data['s']}-{data['e']}"
    rename(p + f, new_name)
    print(f"rename from -{f}- to -{new_name}-")

