import hashlib
import argparse
import os
import json


def file_checksum(filename):
	print(calculate_file_checksum(filename))


def directory_checksum(directory, output_file_name):
	checksums, files_count, errors = calculate_directory_checksum(directory)
	checksums['files_count'] = files_count

	save_result_to_file(checksums, output_file_name)


def calculate_directory_checksum(directory, compare_data=None):
	files_checksums = {}
	errors = {}
	files_count = 0

	for root, dirs, files in os.walk(directory):
		for file in files:
			root = root[:-1] if root.endswith('/') else root
			file_path = root + '/' + file
			checksum = calculate_file_checksum(file_path)

			if compare_data and compare_data[file_path]:
				if checksum != compare_data[file_path]:
					print('ERROR: File: ' + file_path + ' checksum not match.')
					print('Old checksum: ' + compare_data[file_path])
					print('Current checksum: ' + checksum)
					errors[file_path] = 'Old checksum: ' + compare_data[file_path] + ' Current checksum: ' + checksum

			files_checksums[file_path] = checksum
			files_count += 1

	return files_checksums, files_count, errors


def calculate_file_checksum(filename):
	"""
	Method taken from stackoverflow with small modifications. Original Author: Piotr Czapla.
	https://stackoverflow.com/questions/1131220/get-md5-hash-of-big-files-in-python
	"""
	md5 = hashlib.md5()
	with open(filename,'rb') as f: 
		for chunk in iter(lambda: f.read(8192), b''): 
			md5.update(chunk)
	return md5.hexdigest()


def save_result_to_file(data, output_file_name):
	with open(output_file_name, 'w') as file:
		file.write(json.dumps(data))


def read_data_from_file(compare_file):
	with open(compare_file) as file:
		content = file.read()

	return json.loads(content)


def check_and_compare(directory, compare_file):
	compare_data = read_data_from_file(compare_file)
	checksums, files_count, errors = calculate_directory_checksum(directory, compare_data)

	if files_count != compare_data['files_count']:
		print('ERROR: Files count do not match')
		print('Old directory: ' + compare_data['files_count'])
		print('New directory: ' + files_count)
		errors['file_count'] = 'ERROR: Files count do not match'

	if errors:
		save_result_to_file(errors, 'errors.txt')
		print('Completed. Status: FAILED')

	if not errors:
		print('Completed. Status: OK')


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('filename')
	parser.add_argument('-o', '--output')
	parser.add_argument('-c', '--compare')

	args = parser.parse_args()

	if args.compare:
		check_and_compare(args.filename, args.compare)
	else:
		if os.path.isfile(args.filename):
			file_checksum(args.filename)

		if os.path.isdir(args.filename):
			output_file_name = args.output if args.output else 'checksums.txt'
			directory_checksum(args.filename, output_file_name)
