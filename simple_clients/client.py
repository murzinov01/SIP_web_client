import sys
from pycall import CallFile, Call, Application


def call(number):
    c = Call('SIP/%s' % number, wait_time=10, retry_time=60, max_retries=2)
    a = Application('Playback', 'please-try-call-later')
    cf = CallFile(c, a)
    cf.spool()


if __name__ == '__main__':
    call(sys.argv[1])
