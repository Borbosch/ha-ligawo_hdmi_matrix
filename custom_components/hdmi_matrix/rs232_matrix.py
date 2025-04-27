import serial

class HdmiMatrix:
    def __init__(self, port='/dev/ttyUSB0', baudrate=19200):
        self.port = port
        self.baudrate = baudrate

    def _checksum(self, data):
        val_a = data[0] + data[1]
        val_b = sum(data[2:])
        return (val_a - val_b) % 256

    def _send_command(self, cmd):
        with serial.Serial(self.port, self.baudrate, timeout=1) as ser:
            ser.write(cmd)
            return ser.read(13)

    def get_status(self, output: int) -> int:
        cmd = [0xA5, 0x5B, 0x02, 0x01, output, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        cmd.append(self._checksum(cmd))
        response = self._send_command(bytes(cmd))
        if len(response) == 13:
            return response[6]
        return None

    def switch(self, output: int, input_: int):
        cmd = [
            0xA5, 0x5B, 0x02, 0x03,
            input_, 0x00, output, 0x00, 0x00, 0x00, 0x00, 0x00
        ]
        cmd.append(self._checksum(cmd))
        self._send_command(bytes(cmd))
