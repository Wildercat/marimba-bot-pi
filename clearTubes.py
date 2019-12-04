import servoActions

try:
	while True:
		servoActions.main()
except KeyboardInterrupt:
	print('stop\n')
