import pickle, os, sys
from schedule import Schedule

class Reddit_grabber():

    def __init__(self, filename, sub, image_type = ('.gif', '.jpg', '.png'),
                 image_num=50, schedule=Schedule([])):
        self.filename = filename
        self.sub = sub
        self.image_type = image_type
        self.image_num = image_num
        self.schedule = schedule

    def save(self):
        try:
            if not os.path.join(os.getcwd(), 'grabber'):
                os.makedirs(os.path.join(os.getcwd(), 'grabber'))
        except:
            print('Could not create storage folder.')
            sys.exit(1)
        with open(os.path.join('grabber', self.filename + '.p'), 'wb') as outfile:
            pickle.dump(self.__dict__, outfile)

    @staticmethod
    def load(filename):
        try:
            with open(os.path.join('grabber', filename + '.p'), 'rb') as infile:
                store = pickle.load(infile)
            to_ret = Reddit_grabber(store['filename'], store['sub'],
                                    store['image_type'], store['image_num'],
                                    store['schedule'])
            print('Loaded {}'.format(filename))
            print(to_ret)
            return to_ret
        except:
            print('Could not find file')

    def __str__(self):
        to_ret = 'Sub: ' + self.sub
        to_ret += ' Type: ' + str(self.image_type)
        to_ret += ' Num: ' + str(self.image_num)
        to_ret += '\n' + str(self.schedule)
        return to_ret
