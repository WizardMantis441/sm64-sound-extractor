import os
import subprocess

VERSION = "all" # TODO make this an argument
POSSIBLE_VERSIONS = ["eu", "jp", "sh", "us"]

def convert(ver):
	if ver not in POSSIBLE_VERSIONS or ver != "all":
		print('thats not a version. how dare you.')
		return

	IMPORT_DIR = f"sm64/sound/sequences/{ver}"
	EXPORT_DIR = f"export/generate-midis/{ver}"
	os.makedirs(EXPORT_DIR, exist_ok=True)

	for filename in os.listdir(IMPORT_DIR):
		if filename.endswith(".m64"):
			input_path = os.path.join(IMPORT_DIR, filename)
			output_path = os.path.join(EXPORT_DIR, filename.replace(".m64", ".mid"))

			with open(output_path, "w") as f:
				f.write("")

			subprocess.run(f"seq64_console in={input_path} out={output_path} game=sm64", shell=True)

def main():
	if VERSION == "all":
		for version_type in POSSIBLE_VERSIONS:
			convert(version_type)
	else:
		convert(VERSION)

if __name__ == "__main__":
	main()