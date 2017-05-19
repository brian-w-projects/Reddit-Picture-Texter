import praw, sys, os, time, argparse
from twilio.rest import TwilioRestClient
from reddit_grabber import Reddit_grabber
from schedule import Schedule

# SEE README FILE FOR INFORMATION ON SETTING THESE VARIABLES
ACCOUNT_SID = ''
AUTH_TOKEN = ''
TWILIO_NUMBER = ''
MY_NUMBER = ''

MY_CLIENT_ID = ''
MY_CLIENT_SECRET = ''
USER_AGENT = ''

def text_myself(media):
    '''Uses Twilio to send picture message'''
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(to = MY_NUMBER, from_ = TWILIO_NUMBER,
                           media_url = media)

def get_image(grabber):
    '''Uses Praw to grab top pictures from indicated sub'''
    try:
        reddit = praw.Reddit(user_agent=USER_AGENT, client_id=MY_CLIENT_ID,
                             client_secret=MY_CLIENT_SECRET) 
        submissions = reddit.subreddit(grabber.sub).hot(limit=grabber.image_num)
        for submission in submissions:
            if 'imgur.com/' not in submission.url:
                continue
            if 'http://i.imgur.com/' in submission.url and submission.url.endswith(
                    grabber.image_type):
                yield submission.url
        yield None
    except Exception as e:
        print('Praw experienced a problem. Please check file inputs.')

def get_started(filename, schedules):
    '''loads or creates grabber object'''
    if filename:
        grabber = Reddit_grabber.load(filename)
        if not grabber:
            print('Could not find file.')
            sys.exit(1)
        else:
            return grabber
    else:
        while True:
            name = input('What would you like to name this Reddit grabber?: ')
            if os.path.exists(os.path.join('redditPictureSender', name + '.p')):
                print('File by that name already exists.')
            else:
                break

        sub = input('Which sub would you like to grab from?: ')

        grabber = Reddit_grabber(name, sub, schedule=Schedule(schedules))
        grabber.schedule.create_time()
        grabber.save()
    return(grabber)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Automatically text the top images from your favor subreddits on custom schedule\n'
                    'Provide either "grabber" to load or "schedules" to base new grabber on.')
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('-s', nargs='*', dest='schedules', action='store',
        help='Set schedules to initalize grabber with')
    group.add_argument('grabber', nargs='?', default=None, help='Select grabber to load')
    parser.add_argument('-m', dest='modify', action='store_true', default=None,
        help='Further modify grabber schedule.')

    results = parser.parse_args()
    grabber = get_started(results.grabber, results.schedules)

    if results.modify:
        grabber.schedule.create_time()
        grabber.save()

    try:
        while True:
            for to_send in get_image(grabber):
                if to_send == None:
                    continue
                for i in range(grabber.schedule.next_action(display=True)):
                    time.sleep(1)
                text_myself(to_send)
                time.sleep(1)
    except KeyboardInterrupt:
        print('Program Exited on Keyboard Interrupt')
