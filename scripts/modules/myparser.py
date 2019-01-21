import re
from typing import Union


class MyParser:
    def extract_number(self, text: str) -> Union[float, None]:
        res = re.findall("[-.\d]{1}", text)

        if len(res) == 0:
            return None

        return float("".join(res))
