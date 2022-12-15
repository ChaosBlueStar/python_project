a = "Life is too short, you need python"
if "wife" in a: print("wife")
#변수 a안에 'wife'가 있으면 'wife'를 출력하라
elif "python" in a and "you" not in a: print("python")
#변수 a안에 "python'이있고, 'you'가 없으면 'python'을 출력하라
elif "shirt" not in a: print("shirt")
#변수 a안에 "shirt"가 없으면 "shirt"를 출력하라
elif "need" in a: print("need")
#변수 a안에 "need"가 있으면 need를 출력하라"need"
else: print("none")