import subprocess

def RunConan(buildType):
	subprocess.run((
		'conan', 'install', '.', '--build', 'missing', 
		'--output-folder=./dependencies', f'--settings=build_type={buildType}'
	))

def RunPremake(action):
	subprocess.run((
		f'./Vendor/Binaries/Premake/Windows/premake5', action
	))

if __name__ == "__main__":
	RunConan("Debug")
	RunConan("Release")
	RunPremake("vs2022")