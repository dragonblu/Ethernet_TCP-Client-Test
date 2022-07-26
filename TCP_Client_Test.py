import socket
import struct

import GlobalConst
import CRC16

#client_socket = socket.socket()
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((GlobalConst.Server_Address, GlobalConst.Server_Port))

    data_header = struct.pack('BBH', 0x02, 0x00, 50)
    data = struct.pack('<H12f', 1, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 0.0, 1.0, 2.0, 3.0, 5.0, 6.0)
    data_tail = struct.pack('HB', CRC16.crc16(data), 0x03)

    client_socket.send(data_header)
    client_socket.send(data)
    client_socket.send(data_tail)

    client_socket.settimeout(5)
    recv_data = client_socket.recv(512)

    print(recv_data)

except Exception as e:
    print(str(e))

client_socket.close()