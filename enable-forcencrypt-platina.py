import re

userStr = "abcd abc efgh"
math = re.search(r'\w{4}', userStr)
print(match.group())
print(match.span()

import re

userStr = "2021 - 2022 competetion calendar:30.11.2021 -\
 2021 Grand Prix series 99.99.9999 14.01.2022 -\
 Grand Pemio D'Italia"
match2 = re.findall(r'\d{2}')
