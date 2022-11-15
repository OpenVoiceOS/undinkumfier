# Copyright 2016 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ovos_workshop.skills.dinkum import GuiClear, UnDinkumSkill, SkillControl, MessageSend
from adapt.intent import IntentBuilder
from mycroft.messagebus.message import Message
from mycroft.skills import intent_handler


class StopSkill(UnDinkumSkill):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @intent_handler(IntentBuilder("").require("Stop"))
    def handle_stop(self, event):
        self.bus.emit(Message("mycroft.stop"))
        return self.end_session()

    @intent_handler(IntentBuilder("").require("Nevermind"))
    def handle_nevermind(self, event):
        return self.end_session()


def create_skill():
    return StopSkill()
