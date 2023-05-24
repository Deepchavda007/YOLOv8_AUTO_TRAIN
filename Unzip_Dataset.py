from zipfile import ZipFile


class Unzipper:
    def __init__(self, zip_path):
        self.zip_path = zip_path
    
    def unzip(self, path):
        with ZipFile(self.zip_path, 'r') as zObject:
            zObject.extractall(path=path)

            

if __name__== "__main__":

    unzip_1 = Unzipper('dataset.zip')
    path = unzip_1.unzip("")
    print(path)            