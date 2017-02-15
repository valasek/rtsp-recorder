from __future__ import absolute_import
from celery import shared_task
import sys
from subprocess import Popen
import shlex
import os
import signal
from rtsp_recorder.recorder.models import Task
from datetime import datetime


@shared_task
def start_ffmpeg():
    filename = 'recording ' + str(datetime.now()) + '.mp4'
    filename = filename.replace(' ', '_')
    print('Task start_ffmpeg called, filename: "%s" ' % filename)
    command = """ffmpeg -i rtsp://mpv.cdn3.bigCDN.com:554/bigCDN/mp4:bigbuckbunnyiphone_400.mp4 -acodec copy
    -vcodec copy {0}""".format(filename)
    process = ""
    try:
        process = Popen(shlex.split(command))
        print("*** Started recording with PID {0} saved to {1}".format(process.pid, filename))
        # Save PID into DB
        process_id = Task(pid=process.pid)
        process_id.save()
    except KeyboardInterrupt:
        process.kill()
        print("Goodbye!")
        sys.exit(0)
    except Exception as e:
        print("Something went wrong when we tried to start the recording!")
        print("The error is {0}".format(str(e)))
        sys.exit(2)


@shared_task
def stop_ffmpeg():
    print('Task stop_ffmpeg called')
    try:
        # Send CTRL+C
        process_pid = Task.objects.first()
        os.kill(process_pid.pid, signal.SIGINT)
        Task.objects.all().delete()
        print("******************Recording stopped************************")
    except Exception as e:
        print("Something went wrong when we tried to stop the recording!")
        print("The error is {0}".format(str(e)))
        sys.exit(2)
