#!/usr/bin/python

from pwdgen.password import Password
from pwdgen import PasswordGenerator as PGen
from parser import parser


if __name__ == "__main__":
    args = parser.parse_args()

    if not args.create_new:
        try:
            pwd = Password.load()
            pwd.learn()
        except IOError:
            pass

    gen = PGen(args.length, allowed_chars=args.allowed_chars,
               exclude_ambigous_chars=args.exclude_ambigous_chars)
    pwd = gen.generate()

    pwd.learn()
