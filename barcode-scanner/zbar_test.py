from sys import argv
import zbar

def video_opened(zbar, param):
    """callback invoked when the zbar widget opens or closes a video
    device.  also called when a device is closed due to error.
    updates the status button state to reflect the current video state
    """
    opened = zbar.get_video_opened()
    print opened

# create a Processor
proc = zbar.Processor()

# configure the Processor
proc.parse_config('enable')

# initialize the Processor
device = '/dev/video0'
if len(argv) > 1:
    device = argv[1]
proc.init(device)

# setup a callback
def my_handler(proc, image, closure):
    # extract results
    for symbol in image.symbols:
        # do something useful with results
        print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data

proc.set_data_handler(my_handler)

# enable the preview window
proc.visible = True

# initiate scanning
proc.active = True
try:
    # keep scanning until user provides key/mouse input
    proc.user_wait()
except zbar.WindowClosed, e:
    pass

