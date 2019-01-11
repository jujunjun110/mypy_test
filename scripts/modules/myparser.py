from typing import Union


class MyParser:
    def extract_number(self, text: str) -> Union[float, None]:
        res = "".join([char for char in text if char in "0123456789.-"])

        if len(res) == 0:
            return None

        return float(res)
