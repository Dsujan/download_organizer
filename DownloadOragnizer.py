
import os
import logging

logging.basicConfig(filename='app.log', filemode='a+',format='%(name)s - %(levelname)s - %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',level=logging.DEBUG)



class DownloadOrganizer():
    def __init__(self):


        logging.debug('Initializing constant variables')
        
        self.DOWNLOAD_FOLDER = os.path.expanduser('~/Downloads')  
        self.IMAGE_EXT = ['jpg','tiff','tif','gif','png','jepg']
        self.EBOOK_EXT = ['epub','mobi','awz','awz3','iba','pdf','rft']
        self.VIDEO_EXT = ['mp4', 'm4v', 'f4v', 'm4b', 'm4r', 'f4b','ipynb', 'mov','3gp', '3gp2', '3g2', '3gpp', '3gpp2','avi','flv','webm','wmv', 'wma']
        self.AUDIO_EXT  = ['aac','mp3','m4a','m3u','oga','mid','wav','aa3','ogg']
        self.APP_EXT  = ['exe','msi']
        self.DOCS_EXT = ['txt','md','docx','csv','doc','xlsx','xls','pptx']
        self.COMPRESSED_EXT = ['zip','tar','rar','gzip','7z','zz','bzip','gz','tar.gz','tar.bz2','tar.gz2']        
        self.ALL_EXT = {'Images':self.IMAGE_EXT,'Pdfs':self.EBOOK_EXT,'Videos':self.VIDEO_EXT,'Audios':self.AUDIO_EXT,'Apps':self.APP_EXT,'Documents':self.DOCS_EXT,'Compressed':self.COMPRESSED_EXT}
        
        logging.debug('Constant variables initialization finished!')


    def organize_files(self):

        for root, dirs, files in os.walk(self.DOWNLOAD_FOLDER, topdown=True):
            if root == self.DOWNLOAD_FOLDER:
                for name in files:

                    file_path = os.path.join(root,name)

                    logging.debug(f'{file_path} found in {self.DOWNLOAD_FOLDER}')

                    extension = os.path.splitext(file_path)[1].replace('.','')
                    print('the founnd extension is',extension)

                    for key,value in self.ALL_EXT.items():
                        if extension in value:
                            logging.debug(f'{file_path} contains predefined extension')
                            new_path = os.path.join(self.DOWNLOAD_FOLDER,key,name)
                            try:
                                os.replace(file_path,new_path)
                                logging.debug(f'{file_path} moved to {new_path}')
                                break
                            except:
                                print(new_path,'Folder should exist! No such folder found')
                                logging.debug(f'{new_path} doesn\'t exist!') 



                        else:
                            if key == 'Compressed':
                                logging.debug(f'{file_path} doesn\'t contains predefined extension')
                                new_path = os.path.join(self.DOWNLOAD_FOLDER,'Others',name)
                                os.replace(file_path,new_path)
                                logging.debug(f'{file_path} moved to {new_path}')
                                break
        else:
            logging.debug("No any files found to organize!")

        logging.debug('File organization finished!')

                            



if __name__ == "__main__":

    print('Started!')

    organizer  = DownloadOrganizer()
    organizer.organize_files()

    print('Fin!')



            
