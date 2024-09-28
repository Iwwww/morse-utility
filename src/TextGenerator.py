#!/bin/env python3

from random import randint
from typing import List

GROUP_DELIMITER: str = " "
GROUP_LENGTH: int = 5


class GroupGenerator:
    def __init__(
        self, group_length: int = GROUP_LENGTH, group_delimiter: str = GROUP_DELIMITER
    ):
        self.group_length = group_length
        self.group_delimiter = group_delimiter

    def generate(self, list: List[str], groups: int) -> List[str]:
        """
        Generate list of groups with random text
        """
        data: List = []
        for _ in range(groups):
            group: str = ""
            for _ in range(self.group_length):
                index: int = randint(0, len(list) - 1)
                group += list[index]
            data.append(group)

        return data

    def add_repeat(self, data: List[str], repeat_times: int) -> List[str]:
        """
        Repeat each group `repeat_times` times
        """
        result: List[str] = []
        for group in data:
            for _ in range(repeat_times):
                result.append(group)

        return result

    def to_text(self, data: List[str]) -> str:
        """
        Convert list of groups to string and add `GROUP_DELIMITER`
        """
        text: str = ""
        for i in range(len(data)):
            text += data[i]
            if i != len(data) - 1:
                text += self.group_delimiter

        return text


if __name__ == "__main__":
    generator = GroupGenerator()
    char_list = [i for i in "адужилорст"]
    data = generator.generate(char_list, 25)
    data = generator.add_repeat(data, 2)
    result_text = generator.to_text(data)
    print("result text:", result_text)
