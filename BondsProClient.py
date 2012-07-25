import sys
import os
import time
import thread
import quickfix as fix
import quickfix44 as fix44
from datetime import datetime
import Application

print sys.path
if (len(sys.argv)<2):
    print "usage: ", sys.argv[0] + " FILE."
    
file = sys.argv[1]
settings = fix.SessionSettings (file)
application = Application.Application ()
storeFactory = fix.FileStoreFactory (settings)
logFactory = fix.FileLogFactory (settings)
initiator = fix.SocketInitiator (application, storeFactory, settings, logFactory)

initiator.start ()
application.run ()
initiator.stop ()


