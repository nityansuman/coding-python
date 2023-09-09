# import functools

def eggs(func):

	def _eggs(*args, **kwargs):
		# new_args = list()
		# for arg in args:
		# 	print("arg:", arg)
		# 	new_args.append(arg)

		# for kw in kwargs:
		# 	print("kw:", kw)

		# new_args[0] *= 2

		if kwargs["str_flag"]:
			out = func(*args, **kwargs)
			out = str(out)
		else:
			out = func(*args, **kwargs)
		return out

	return _eggs

@eggs
def spam(a:int, b:int, c:int, **kwargs) -> int:
	return a+b+c

# res = main_method()
# decorator_method() -> main_method -> res
if __name__ == "__main__":
	res = spam(10, 20, 30, str_flag=True)
	print(res, type(res))
