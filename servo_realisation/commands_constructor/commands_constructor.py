import canalystii
import servo_realisation.servo_object.servo_interface


def get_bytes_code(
    num_of_bytes: int = None, is_read: bool = False, is_write: bool = False
):
    if is_read and not is_write:
        return "0x40"

    elif not is_read and is_write:
        if num_of_bytes == 1:

            return "0x2F"

        elif num_of_bytes == 2:
            return "0x2B"

        elif num_of_bytes == 4:
            return "0x23"


class CommandConstructor:
    def __init__(self, servo_object: servo_realisation.servo_object.servo_interface.ServoInterface):
        self.device_id = servo_object.device_id
        self.servo_id = 

    def create_command(
        self,
        command_from_documentation: str,
        is_read: bool = False,
        is_write: bool = False,
        address: int = None,
        write_value: int = None,
    ) -> canalystii.Message:

        result = []



        if not is_write and not is_read:
            
            
            
            final_command = canalystii.Message(
                remote=False,
                extended=False,
                data_len=1,
                data=int("0x"+str(write_value), 0),
            )



            return final_command

        else:


            num_of_bytes_for_command = int(int(command_from_documentation[-2:], 16) / 8)

            # "0x" + command_byte_first

            result.append(
                get_bytes_code(
                    num_of_bytes=num_of_bytes_for_command,
                    is_read=is_read,
                    is_write=is_write,
                )
            )

            command_byte_first = command_from_documentation[:2]
            command_byte_second = command_from_documentation[2:4]

            if is_write:
                result.append("0x" + command_byte_second)
                result.append("0x" + command_byte_first)
                result.append("0x00")

                write_value = hex(write_value)[2:]

                num_of_iterations = 0
                while write_value:
                    result.append("0x" + write_value[-2:])
                    write_value = write_value[:-2]
                    num_of_iterations += 1

                while num_of_bytes_for_command != num_of_iterations:
                    result.append("0x00")
                    num_of_iterations += 1

                convert_to_hex = ()
                for element in result:
                    convert_to_hex += (int(element, 0),)

                final_command = canalystii.Message(
                    can_id=address,
                    remote=False,
                    extended=False,
                    data_len=len(convert_to_hex),
                    data=convert_to_hex,
                )

                # print(convert_to_hex, final_command)
                # final_command = result
                return final_command

            elif is_read:
                result.append("0x" + command_byte_second)
                result.append("0x" + command_byte_first)
                result.append("0x00")

                convert_to_hex = ()
                for element in result:
                    convert_to_hex += (int(element, 0),)

                # final_command = result

                # print(convert_to_hex)

                final_command = canalystii.Message(
                    can_id=address,
                    remote=False,
                    extended=False,
                    data_len=len(convert_to_hex),
                    data=convert_to_hex,
                )

                return final_command
    