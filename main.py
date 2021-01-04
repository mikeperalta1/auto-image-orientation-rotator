#!/usr/bin/env python3


from ApplyImageOrientation import ApplyImageOrientation

import argparse


def main():
	
	parser = argparse.ArgumentParser(
		prog="Mike's Auto Image Orientation Applier"
	)
	
	parser.add_argument(
		"--input", "--dir", "--folder",
		dest="input_folder",
		required=True,
		type=str,
		help="Specify an input folder of images"
	)
	
	parser.add_argument(
		"--output", "--output-dir", "--output-folder",
		dest="output_folder",
		required=True,
		type=str,
		help="Specify an output folder for the images"
	)
	
	parser.add_argument(
		"--jpg", "--jpeg",
		dest="output_jpeg",
		default=False,
		action="store_true",
		help="Output to jpeg files, not png. Should be faster but sacrifices the quality of png."
	)
	
	parser.add_argument(
		"--threads",
		dest="threads_count",
		default=None,
		type=int,
		help="Specify the number of threads to use. Default: Same as the number of detected CPU cores."
	)
	parser.add_argument(
		"--single-thread",
		dest="threads_count",
		default=None,
		action="store_const", const=1,
		help="Use only one thread."
	)
	
	args = parser.parse_args()
	
	assert args.input_folder != args.output_folder, "Input and Output folders must be different"
	
	app = ApplyImageOrientation(
		input_folder=args.input_folder,
		output_folder=args.output_folder
	)
	app.run(
		threads_count=args.threads_count,
		jpeg=args.output_jpeg
	)


if __name__ == "__main__":
	main()
