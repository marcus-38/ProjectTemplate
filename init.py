import subprocess
import argparse

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
	parser = argparse.ArgumentParser()
	group = parser.add_mutually_exclusive_group()
	group.add_argument("--windows", help="Create Visual Studio solution files", action="store_true")
	group.add_argument("--mac", help="Create Xcode project files", action="store_true")
	group.add_argument("--linux", help="Create Makefiles", action="store_true")
	
	args = parser.parse_args()

	RunConan("Debug")
	RunConan("Release")

	if args.windows:
		print("Creating Visual Studio solution files")
		RunPremake("vs2022", "Windows")
	elif args.mac:
		print("Creating Xcode project files")
		RunPremake("xcode4", "macOS")
	elif args.linux:
		print("Creating Makefile files")
		RunPremake("gmake2", "Linux")
	

	