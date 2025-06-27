from string_calculator import StringCalculator


class TestStringCalculator:
    def test_returns_zero_for_empty_string(self):
        # Arrange
        calculator = StringCalculator()

        # Act
        result = calculator.add("")

        # Assert
        assert result == 0

    def test_returns_number_for_single_number_string(self):
        # Arrange
        calculator = StringCalculator()

        # Act
        result = calculator.add("1")

        # Assert
        assert result == 1

    def test_returns_sum_for_two_comma_separated_numbers(self):
        # Arrange
        calculator = StringCalculator()

        # Act
        result = calculator.add("1,2")

        # Assert
        assert result == 3

    def test_returns_sum_for_three_comma_separated_numbers(self):
        # Arrange
        calculator = StringCalculator()

        # Act
        result = calculator.add("1,2,3")

        # Assert
        assert result == 6

    def test_returns_sum_for_numbers_with_newline_delimiter(self):
        # Arrange
        calculator = StringCalculator()

        # Act
        result = calculator.add("1\n2,3")

        # Assert
        assert result == 6
