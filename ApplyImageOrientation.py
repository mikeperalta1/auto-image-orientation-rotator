

import exif
from exif import Image as ExifImage


from PIL import Image as PilImage


import os


class ApplyImageOrientation:
	
	def __init__(self, input_folder, output_folder):
		
		self.ensure_folder(output_folder)
		
		assert os.path.isdir(input_folder), "Invalid input folder: %s" % input_folder
		assert os.path.isdir(output_folder), "Invalid output folder: %s" % output_folder
		
		self.__input_folder = os.path.abspath(input_folder)
		self.__output_folder = os.path.abspath(output_folder)
		
		self.__valid_image_extensions = [
			"jpeg", "jpg",
			"png",
			"tiff"
		]
	
	def run(self, jpeg=False):
		
		images_paths = self.get_input_images()
		
		for image_path in images_paths:
			self.apply_orientation(
				image_path=image_path,
				jpeg=jpeg
			)
	
	@staticmethod
	def ensure_folder(folder_path):
	
		os.makedirs(folder_path, exist_ok=True)
	
	def get_input_images(self):
		
		return self.get_directory_images(self.__input_folder)
	
	def get_directory_images(self, path):
		
		images_files_paths = []
		
		for current_dir, subdirs, files in os.walk(path):
			
			for file_name in files:
				
				file_path = os.path.join(current_dir, file_name)
				file_basename, file_extension = os.path.splitext(file_path)
				if file_extension:
					file_extension = file_extension[1:]
					file_extension = file_extension.lower()
					if file_extension in self.__valid_image_extensions:
						images_files_paths.append(file_path)
		
		return images_files_paths
	
	def apply_orientation(self, image_path, jpeg=False):
		
		image_basename = os.path.basename(image_path)
		
		with open(image_path, "rb") as f:
			
			exif_image = ExifImage(f)
			orientation = exif_image.orientation
		
		pil_image = PilImage.open(image_path)
		
		rotation_degrees = 0
		if orientation == exif.Orientation.LEFT_BOTTOM:
			rotation_degrees = 90
		
		if rotation_degrees != 0:
			pil_image_rotated = pil_image.rotate(rotation_degrees, expand=True)
		else:
			pil_image_rotated = pil_image
		
		print(image_basename, pil_image.size, "==>", orientation, "==>", rotation_degrees)
		
		image_rotated_file_path = self.make_image_output_path(image_path=image_path, jpeg=jpeg)
		self.ensure_folder(os.path.dirname(image_rotated_file_path))
		pil_image_rotated.save(image_rotated_file_path, None if jpeg else "png")
	
	def get_image_relative_path(self, image_path):
		
		image_path_relative = image_path[len(self.__input_folder):]
		
		return image_path_relative
	
	def make_image_output_path(self, image_path, jpeg=False):
		
		image_path_relative = self.get_image_relative_path(image_path=image_path)
		
		image_output_path = self.__output_folder + image_path_relative
		
		if not jpeg:
			path_name, extension = os.path.splitext(image_output_path)
			image_output_path = path_name + ".png"
		
		return image_output_path
