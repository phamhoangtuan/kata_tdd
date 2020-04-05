class PrimeFactors():
    def __init__(self, number: int):
        self.number = number

    @property
    def result(self):
        result = []
        current_number = self.number
        division = 2
        while current_number > 1:
            while current_number % division == 0:
                result.append(division)
                current_number = current_number / division
            division += 1
        return result
