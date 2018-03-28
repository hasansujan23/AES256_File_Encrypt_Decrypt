import codecs, time, sys, os, getpass
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
		print("Welcome to AES256_Decrypt, by @Th3Tr1ckst3r on Twitter!")
		print("\n")
		print("First, please place the file you want decrypted on your desktop. Then,")
		print("\n")
		Password = input("please enter the password to the file you encrypted: ")
		print("\n")
		convert_2_bytes = Password.encode()
		pad_password = convert_2_bytes.ljust(32, b" ")
		slice_password = pad_password[0:32]
		backend = default_backend()
		cipher = Cipher(algorithms.AES(slice_password), modes.CBC(IV), backend=backend)
		decryptor = cipher.decryptor()
		unpadder = padding.PKCS7(256).unpadder()
		local_file_name = input("Enter a local filename: ")
		file_data = open("{}".format(local_file_name), "rb").read()
		dec = decryptor.update(file_data) + decryptor.finalize()
		unpad = unpadder.update(dec) + unpadder.finalize()
		file_data2 = open("{}".format(local_file_name), "wb")
		file_data2.write(unpad)
		file_data2.close()
		print("\n")
		print("Finished decrypting {}!".format(local_file_name))
		print("\n")
		time.sleep(5)
	except FileNotFoundError:
		print("File not found...")
		time.sleep(5)
		return Main()
	except ValueError:
		print("Invalid password...")
		time.sleep(5)
		return Main()
	except KeyboardInterrupt:
		exit()
	
if __name__ == "__main__":
	Main()