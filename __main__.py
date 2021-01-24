from pwdgen import PasswordGenerator as PGen

if __name__ == "__main__":
    gen = PGen(16)
    pwd = gen.generate()

    print(pwd.contents)
