# Import packages
from math import degrees, hypot, acos


def compute_angle(ab, bc):
	# Compute larger triangle hypotenuse
	hypotenuse = hypot(ab, bc)

	# Compute angle using arc cosine (base / hypotenuse)
	return int(round(degrees(acos(bc/hypotenuse))))


if __name__ == "__main__":
	# Read triangle side input from stdin
	ab = int(input().strip())
	bc = int(input().strip())

	# Compute angle at mbc
	angle = compute_angle(ab, bc)
	print(f"Computed Angle: {angle}{chr(176)}") # Show degree symbol
