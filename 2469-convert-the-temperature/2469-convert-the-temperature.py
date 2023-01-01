class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius+273.15 , round(celsius*1.80 + 32, 5)]
        