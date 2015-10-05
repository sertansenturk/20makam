__author__ = 'hsercanatli'

import compmusic.file
import codecs
from metadata import MetadataExtractorRecording, MetadataExtractorWork

def getFileNamesInDir(dir_name, ext=".mp3", skipFoldername=''):
    import os
    """
    :param dir_name:
    :param ext:
    :param skipFoldername:
    :return: returnpath = dir
             fileNames = release/songnames
    """
    names = []
    folders = []

    for (path, dirs, files) in os.walk(dir_name):
        for f in files:
            if ext in f.lower():
                if skipFoldername not in path.split(os.sep)[1:]:
                    names.append(f)
                    folders.append(path)

    returnpath = [folders[i] + '/' + names[i] for i in range(len(folders))]
    lastFolders = [folders[i].replace(dir_name, '') for i in range(len(folders))]
    fileNames = [lastFolders[i][1:] + '/' + names[i][:-len(ext)] for i in range(len(names))]

    return returnpath, fileNames

returnpath, fileNames = getFileNamesInDir("/media/hsercanatli/ORTAK/CompMusic/Audio")

recording_text = codecs.open("recording_meta.txt", 'w')
work_text = codecs.open("work.txt", 'w')
errors = codecs.open("errors.txt", 'w')

for i in range(0, len(returnpath)):
    print "\n", i, "/", len(returnpath), returnpath[i], fileNames[i]
    try:
        # mbid
        mbid = compmusic.file.file_metadata(returnpath[i])['meta']['recordingid']
        meta_recording = MetadataExtractorRecording(mbid)

        # recording meta
        recording_out = meta_recording.run()
        recording_text.write(fileNames[i] + "\t" + recording_out + "\n")

        # work meta
        if recording_out.split("\t")[-1] is not "":
            meta_work = MetadataExtractorWork(recording_out.split("\t")[-1])
            work_out = meta_work.run()
            work_text.write(work_out + "\n")

    except:
        errors.write(returnpath[i])
        errors.write("\n")

recording_text.close()
work_text.close()
errors.close()
