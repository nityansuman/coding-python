# https://leetcode.com/problems/design-parking-system/

class ParkingSystem:

	def __init__(self, big: int, medium: int, small: int):
		self.parking = {
			1: big,
			2: medium,
			3: small
		}

	def addCar(self, carType: int) -> bool:
		self.parking[carType] -= 1
		return self.parking[carType] >= 0
