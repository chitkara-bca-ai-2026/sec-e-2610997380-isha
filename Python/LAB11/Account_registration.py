username=input("Enter a Username: ")
password=input("Enter a Password: ")
length=len(password)
digit=False
upper=False
for ch in password:
  if ch.isdigit():
    digit=True
  if ch.isupper():
    upper=True
if len(password)>=8 and digit and upper:
  password1="valid"
else:
  password1="invalid"

print("="*40)
print("\n PASSWORD VALIDATION REPORT")
print("="*40)
print("Username : ",username)
print("Password : ",password)
print("\n ------Validation Rules -----")
print(f"[PASS] Minimum 8 charaters ({length} characters)")
print(f"[PASS] Atleast one digit")
print(f"[PASS] Atleast one uppercase letter")

print("\n-----Result-----")
print(f"Password is {password1}!")
if password1=="valid":
  print(f"Account created successfully for {username}")
else:
  print(f"Account not created successfully for {username}TRY AGAIN!!")

print("="*40,end="")






