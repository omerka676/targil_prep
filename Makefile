clean:
	rm -rf ./__pycache__ ./build ./dist ./server.spec

build_elf:
	pyinstaller --onefile ./server.py 
upload_red:
	sshpass -p "DP6LWE8c1nKaNiT2a0au" scp ./dist/server PurpleEncrypt2@98.71.140.24:~/
connect_red:
	sshpass -p "DP6LWE8c1nKaNiT2a0au" ssh -i ~/.ssh/id_rsa.pem PurpleEncrypt2@98.71.140.24
