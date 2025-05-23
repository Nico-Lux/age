driving = input('你有開過車嗎？')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
	raise SystemExit	
age = input('你幾歲？')
age = int(age)
if driving == '有':
	if age >= 18:
		print('通過測驗')
	else:
		print('無照bad')
elif driving == '沒有':
	if age >= 18:
		print('該考駕照了')
	else:
		print('再等個年吧')
