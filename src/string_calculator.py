import re


class StringCalculator:
    def add(self, numbers: str) -> int:
        """Adds numbers in a string.

        An empty string will return 0.
        """
        if not numbers:
            return 0
        return sum(int(num) for num in re.split(r"[,\n]", numbers))
