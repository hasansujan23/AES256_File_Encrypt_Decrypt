import codecs, time, os, sys, getpass
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
#Coded by Th3Tr1ckst3r.
#########################################################################
#Internal Settings#######################################################
#########################################################################
#Warning: This IV was randomly generated as it should be. If you want to
#change it, go ahead, but be aware that it must be at least 16 bytes.
IV = b",c@jF&VVS(dC'5Va"
#########################################################################

def Main():
	try:
		if sys.platform == "win32":
			os.system("cls")
			os.system("color 0a")
		else:
			os.system("clear")
		os.chdir("C:/Users/{}/Desktop".format(os.environ['username']))
		print("Welcome to AES256_Encrypt, by @Th3Tr1ckst3r on Twitter!")
		print("\n")
		print("First, please place the file you want encrypted on your desktop. Then,")
		print("\n")
		Password = input("please enter the password you want for your file: ")
		print("\n")
		convert_2_bytes = Password.encode()
		pad_password = convert_2_bytes.ljust(32, b" ")
		slice_password = pad_password[0:32]
		print("Warning: This program encrypts the original file. Your in charge of backing up the original file if needed.")
		print("\n")
		local_file_name = input("Enter a local filename: ")
		file_data = open("{}".format(local_file_name), "rb").read()
		backend = default_backend()
		cipher = Cipher(algorithms.AES(slice_password), modes.CBC(IV), backend=backend)
		encryptor = cipher.encryptor()
		padder = padding.PKCS7(256).padder()
		pad = padder.update(file_data) + padder.finalize()
		enc = encryptor.update(pad) + encryptor.finalize()
		file_data2 = open("{}".format(local_file_name), "wb")
		file_data2.write(enc)
		file_data2.close()
		print("\n")
		print("Finished encrypting {}!".format(local_file_name))
		print("\n")
		print("Warning: It is your responsibility to remember your password.")
		print("\n")
		time.sleep(60)
	except FileNotFoundError:
		print("Error: File not found...")
		time.sleep(10)
		return Main()
	except ValueError as errormsg1: 
		print("{}".format(errormsg1))
		time.sleep(10)
		return Main()
	except KeyboardInterrupt:
		exit()
	
if __name__ == "__main__":
	Main()