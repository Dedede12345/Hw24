
class Device:

    def __init__(self):
        self.type_of_fork = "belarusian"
        self.electrified = False

    def plug_in(self, socket):
        if self.type_of_fork == socket.type_of_socket and socket.electrified:
            self.electrified = True
            # print(f"Runs successfully, powered by {socket.electrify()}")

    def runs(self):
        if self.electrified:
            print(f"Runs successfully")
        else:
            print("Nothing happens")


class SocketBY:

    def __init__(self):
        self.type_of_socket = "belarusian"  # type of holes
        self.electrified = True

    def electrify(self, device):
        if device.type_of_fork == self.type_of_socket:
            return "electricity"


class SocketMX:

    def __init__(self):
        self.type_of_socket = "mexican" # type of holes
        self.electrified = True

    def electrify(self, device):
        if device.type_of_fork == self.type_of_socket:
            return "electricity"


class Adapter:

    def __init__(self):
        self.type_of_fork = "mexican"
        self.type_of_socket = "belarusian"
        self.electrified = False

    def plug_in(self, socket):
        if self.type_of_fork == socket.type_of_socket:
            self.electrified = True
            # print(f"Runs successfully, powered by {socket}")

    def runs(self):
        if self.electrified:
            print(f"Runs successfully")
        else:
            print("Nothing happens")

    def electrify(self, device):
        if device.type_of_fork == self.type_of_socket:
            return "electricity"

# Values
BEL = SocketBY()
MEX = SocketMX()
ADA = Adapter()
device = Device()

# via Adapter
ADA.plug_in(MEX)
device.plug_in(ADA)
device.runs()

# via SocketBY
device.plug_in(BEL)
device.runs()



