from password import generate_password

def run():
  user_input = int(input("Insert how long you want your password: "))
  print(generate_password(user_input))


if __name__ == "__main__":
  run()