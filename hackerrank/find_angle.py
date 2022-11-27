# Import packages
from math import degrees, hypot, acos

def compute_angle(ab, bc):
	return int(round(degrees(acos(bc/hypot(ab, bc)))))


if __name__ == "__main__":
	ab = int(input().strip())
	bc = int(input().strip())

	angle = compute_angle(ab, bc)
	print(f"Computed Angle: {angle}{chr(176)}")
