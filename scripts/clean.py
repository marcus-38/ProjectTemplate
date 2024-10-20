import os
import sys
import shutil

def RecursiveRemove(root_dir, extensions_to_remove = (), exclude_subdirs = ()):
	for content in os.listdir(root_dir):
		path = f'{root_dir}{content}'
	
		if os.path.isfile(path):
			for ext in extensions_to_remove:
				if str(path).endswith(ext):
					print(f'Removing {path}')
					os.remove(path)

		if os.path.isdir(path):
			if path not in exclude_subdirs:
				RecursiveRemove(f'{path}/', extensions_to_remove)

if __name__ == '__main__':
	# clear output
	print("Removing ./build")
	shutil.rmtree('./build', ignore_errors=True)
	print("Removing ./temp")
	shutil.rmtree('./temp', ignore_errors=True)
	
	# clear dependencies
	print("Removing ./dependencies")
	shutil.rmtree('./dependencies', ignore_errors=True)

	# clear project
	print("Removing ./vs")
	shutil.rmtree('./vs', ignore_errors=True)

	RecursiveRemove(
		'./',
		('.sln', '.vcxproj', '.vcxproj.user', 'vcxproj.filters', 'Makefile'),
		('.git')
	)
