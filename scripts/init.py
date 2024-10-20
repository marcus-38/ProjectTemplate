import os
import sys
import tarfile
import zipfile
import subprocess
import importlib.util
import urllib.request

def ConanBuild(conf):
	return (
		'conan', 'install', '.',
		'--build', 'missing',
		'--output-folder=./dependencies',
		'--deployer=full_deploy',
		f'--settings=build_type={conf}',
		'--settings=compiler.cppstd=20',
	)

def RunConan(buildType):
	subprocess.run((
		'conan', 'install', '.', '--build', 'missing', 
		'--output-folder=./dependencies', f'--settings=build_type={buildType}'
	))

def GetPremakeGenerator():
	if sys.platform.startswith('linux'):
		return 'gmake2'
	else:
		return 'vs2022'

def GetPremakeDownloadUrl(version):
	baseUrl = f'https://github.com/premake/premake-core/releases/download/v{version}/premake-{version}'
	if sys.platform.startswith('linux'):
		return baseUrl + '-linux.tar.gz'
	elif sys.platform == 'win32':
		return baseUrl + '-windows.zip'

def GetExecutable(exe):
	if sys.platform.startswith('linux'):
		return exe
	else:
		return f'{exe}.exe'


def DownloadPremake(version = '5.0.0-beta2'):
	url = GetPremakeDownloadUrl(version)
	targetFolder = './dependencies/premake5'
	premakeTargetZip = f'{targetFolder}/premake5.tmp'
	premakeTargetExe = f'{targetFolder}/{GetExecutable("premake5")}'

	if not os.path.exists(premakeTargetExe):
		print('Downloading premake5...')
		os.makedirs(targetFolder, exist_ok=True)
		urllib.request.urlretrieve(url, premakeTargetZip)

		if url.endswith('zip'):
			with zipfile.ZipFile(premakeTargetZip, 'r') as zipFile:
				zipFile.extract('premake5.exe', targetFolder)
		else:
			with tarfile.open(premakeTargetZip, 'r') as tarFile:
				tarFile.extract('./premake5', targetFolder)

def InstallPythonPackage(package_name):
	spec = importlib.util.find_spec(package_name)
	if spec is None:
		print(f'Package {package_name} will be installed')
		proc = subprocess.Popen([sys.executable, '-m', 'pip', 'install', package_name])
		proc.wait()
		subprocess.run(['conan', 'profile', 'detect', '--force'])
	else:
		print(f'Package {package_name} is already installed')


if __name__ == "__main__":

	DownloadPremake()

	InstallPythonPackage("conan")
	subprocess.run(ConanBuild('Debug'))
	subprocess.run(ConanBuild('Release'))

	premakeGenerator = GetPremakeGenerator()
	subprocess.run((
		f'./dependencies/premake5/premake5', '--file=./scripts/premake5.lua', premakeGenerator
	))

