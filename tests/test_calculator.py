from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

class TestCalculator:
    def test_subtract(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 3087
        assert result == expected

class TestCalculator:
    def test_multiply(self):
        # arrange
        a = 10
        b = 100
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 1000
        assert result == expected

class TestCalculator:
    def test_divide(self):
        # arrange
        a = 1000
        b = 100
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 100000
        assert result == expected
