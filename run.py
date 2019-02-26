import cv2
import os
import pprint
class VideoWriter:
	"""docstring for VideoWriter"""
	def __init__(self, arg):
		super(VideoWriter, self).__init__()
		self.arg = arg
	def __init__(self, video_path, output_dir, clip_duration):
		self.video_path = video_path
		self.output_dir = output_dir
		self.clip_duration = clip_duration 

	def GenerateClips(self):
		cap = cv2.VideoCapture(self.video_path)

		nframe = cap.get(cv2.CAP_PROP_FRAME_COUNT)
		width  = int(cap.get(3))   # float
		height = int(cap.get(4)) # float
		fps = cap.get(cv2.CAP_PROP_FPS)
		frames_per_clip = fps * self.clip_duration
		number_of_clips = int(nframe / frames_per_clip)

		print("[INFO]...Frames:" + str(nframe))
		print("[INFO]...Width: " + str(width) + ", height: " + str(height))
		print("[INFO]...FPS: " + str(fps))
		print("[INFO]...Clip Duration: " + str(self.clip_duration) + " seconds")
		print("[INFO]...Frames Per Clip: " + str(frames_per_clip))
		print("[INFO]...Number of Clips for Video " 
			+ self.video_path + " : " + str(number_of_clips))
		# Reading the frames and writing as video
		filename = self.GetFileNameFromPath()
		output_file = self.output_dir + filename
		print("[INFO]... Output Path " + output_file)
		self.CheckDirectory()
		clip_no = 1
		writer = cv2.VideoWriter(output_file + "_" + str(clip_no) + ".avi",
			cv2.VideoWriter_fourcc('X','V','I','D'),
			fps, (width,height))
		print("[INFO]... Writing Clip:  " + str(clip_no) + " of " + str(number_of_clips))
		fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
		for x in range(1,int(nframe)):
			flag, frame = cap.read()
			if flag:
				writer.write(frame)
				# cv2.imshow('frame',frame)
				# if cv2.waitKey(1) & 0xFF == ord('q'):
				# 	break
			if(x%int(frames_per_clip) == 0):
				writer.release()
				clip_no = clip_no + 1
				if(clip_no == number_of_clips + 1):
					break;
				print("[INFO]... Writing Clip:  " + str(clip_no) + " of " + str(number_of_clips))
				writer = cv2.VideoWriter(output_file + "_" + str(clip_no) + ".avi", fourcc, fps, (width,height))
		cap.release()
	def CheckDirectory(self):
		if not os.path.exists(self.output_dir):
			os.makedirs(self.output_dir)
	def GetFileNameFromPath(self):
		## File Name without extension
		file = os.path.basename(self.video_path)
		return os.path.splitext(file)[0]
		## Complete File name
		#return os.path.basename(self.video_path)

class VideoCaption:
	"""docstring for VideoCaption"""
	def __init__(self, arg):
		super(VideoCaption, self).__init__()
		self.arg = arg

	def __init__(self, data_dir):
		self.videos_path = data_dir
		self.videos_list = os.listdir(data_dir)
		self.unique_videos = []
		videos_dict = {}
		for x in range(len(self.videos_list)):
			file_name = os.path.splitext(self.videos_list[x])[0].split('_')[0]
			if not file_name in self.unique_videos:
				self.unique_videos.append(file_name)
				videos_dict[file_name] = []
			
			sub_clips = {}
			sub_clips['name'] = os.path.splitext(self.videos_list[x])[0]
			sub_clips['captions'] = []
			sub_clips['captions'].append("Caption 1")
			sub_clips['captions'].append("Caption 2")
			sub_clips['captions'].append("Caption 3")
			sub_clips['captions'].append("Caption 4")
			sub_clips['captions'].append("Caption 5")
			videos_dict[file_name].append(sub_clips)

		# print(self.unique_videos)
		# videos_dict = {}
		# sub_clips = {}
		# sub_clips['name'] = "19_1"
		# sub_clips['captions'] = []
		# sub_clips['captions'].append("Caption 1")
		# sub_clips['captions'].append("Caption 2")
		# sub_clips['captions'].append("Caption 3")
		# sub_clips['captions'].append("Caption 4")
		# sub_clips['captions'].append("Caption 5")
		# sub_clips1 = {}
		# sub_clips1['name'] = "19_2"
		# sub_clips1['captions'] = []
		# sub_clips1['captions'].append("Caption 1")
		# sub_clips1['captions'].append("Caption 2")
		# sub_clips1['captions'].append("Caption 3")
		# sub_clips1['captions'].append("Caption 4")
		# sub_clips1['captions'].append("Caption 5")

		# for i in range(len(self.unique_videos)):
		# 	videos_dict[self.unique_videos[i]] = []
		# 	videos_dict[self.unique_videos[i]].append(sub_clips)
		# 	videos_dict[self.unique_videos[i]].append(sub_clips1)
		pprint.pprint(videos_dict, width=10)


class VideoClip:
	"""docstring for VideoClip"""
	def __init__(self, arg):
		super(VideoClip, self).__init__()
		self.arg = arg
	def __init__(self):
		#self.clip_file = 
		self.sub_clips = []
def BatchProcessor(videos_directory):
	OUTPUT_DIR = videos_directory + "/data/"
	if not os.path.exists(OUTPUT_DIR):
			os.makedirs(OUTPUT_DIR)
	CLIP_DURATION = 2 # in seconds
	videos = os.listdir(videos_directory)
	for i in range(len(videos)):
		vw = VideoWriter(videos_directory + "\\" + videos[i], OUTPUT_DIR, CLIP_DURATION)
		vw.GenerateClips()
		#print(vw.GetFileNameFromPath())
def OneVideo(video_path):
	#video_path = "58.mp4"
	output_dir = "data/"
	clip_duration = 2 # in seconds
	vw = VideoWriter(video_path, output_dir, clip_duration)
	vw.GenerateClips()
def main():
	videos_directory = "Videos"
	#data_dir = videos_directory + "\\data\\"
	data_dir = "Videos\\data\\"
	v_caption = VideoCaption(data_dir)
	# BatchProcessor(videos_directory)
	#OneVideo("58.mp4")
	
	#print(vw.GetFileNameFromPath())
if __name__ == '__main__':
	main()

		