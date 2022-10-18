import servo_realisation.control_objects.servo_interface


class ServoAbstraction(
    servo_realisation.control_objects.servo_interface.ServoInterface
):
    def __init__(
        self,
        interface: servo_realisation.control_objects.servo_interface.ServoInterface,
    ) -> None:
        self.interface = interface
        self.servo_id = interface.servo_id
        self.device = interface.device

    def receive(self, channel: int):
        return self.interface.receive(channel=channel)

    def send(self, channel: int, messages):
        return self.interface.send(channel=channel, messages=messages)