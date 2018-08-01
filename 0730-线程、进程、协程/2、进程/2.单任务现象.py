from time import sleep

def run():
	while True:
		print("aspiring perseverance")
		sleep(1.2)

if __name__ == "__main__":
	while True:
		print("aspiring does not admit defeat")
		sleep(1)

	#不会执行到run方法，只有上面的while循环结束才可以执行
	run()