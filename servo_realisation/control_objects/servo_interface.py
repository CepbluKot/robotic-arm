import abc
import canalystii


class ServoInterface(abc.ABC):
    servo_id = int()
    device = canalystii.CanalystDevice

    @abc.abstractmethod
    def receive(self, channel: int):
        raise NotImplemented

    @abc.abstractmethod
    def send(self, channel: int, messages):
        raise NotImplemented