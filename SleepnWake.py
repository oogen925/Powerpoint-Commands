from talon import Module, speech_system

mod = Module()


@mod.action_class
class Actions:
    def dragon_engine_sleep():
        """Sleep the dragon engine"""
        speech_system.engine_mimic("go to sleep"),

    def dragon_engine_wake():
        """Wake the dragon engine"""
        speech_system.engine_mimic("wake up")