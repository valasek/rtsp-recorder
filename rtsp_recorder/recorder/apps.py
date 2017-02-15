from django.apps import AppConfig


class RecorderConfig(AppConfig):
    name = 'rtsp_recorder.recorder'
    verbose_name = "RTPS recorder"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
