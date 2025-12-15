def deco_result(result_function):
	def distnction(marks):
		for m in marks:
			if m>=75:
				print("distnction")
	return distnction	
@deco_result

def result(marks):
	for m in marks:
		if m>=33:
			pass
		else:
			print("FAIL")
			break
	else:
		print("PASS")
result([80,60,66,99,45])