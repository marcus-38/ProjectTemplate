import subprocess
from sys import platform

def RunConan(buildType):
	subprocess.run((
		'conan', 'install', '.', '--build', 'missing', 
		'--output-folder=./dependencies', f'--settings=build_type={buildType}'
	))

def RunPremake(action, osType):
	subprocess.run((
		f'./Vendor/Binaries/Premake/{osType}/premake5', action
	))

if __name__ == "__main__":
	RunConan("Debug")
	RunConan("Release")

	if platform == "win32":
		print("Creating Visual Studio solution files")
		RunPremake("vs2022", "Windows")
	elif platform == "darwin":
		print("Creating Xcode project files")
		RunPremake("xcode4", "macOS")
	elif platform == "linux" or platform == "linux2":
		print("Creating Makefile files")
		RunPremake("gmake2", "Linux")
	

	