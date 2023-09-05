clean:
	rm -rf ./__pycache__ ./build ./dist ./server.spec

build_elf:
	pyinstaller --onefile ./server.py 