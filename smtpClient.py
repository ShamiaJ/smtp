from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    # print(recv) #You can use these print statement to validate return codes from the server.
    # if recv[:3] != '220':
    #     print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    # if recv1[:3] != '250':
    #     print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFrom = "MAIL FROM: <test@gmail.com>\r\n"
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    # print(recv2)
    # if recv2[:3] != '250':
    #     print('250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    mailTo = "RCPT TO: <shamiaajonson@gmail.com>\r\n"
    clientSocket.send(mailTo.encode())
    recv3 = clientSocket.recv(1024).decode()
    # print(recv3)
    # if recv3[:3] != '250':
    #     print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    Data = b'DATA\r\n'
    clientSocket.send(Data)
    recv4 = clientSocket.recv(1024).decode()
    # print(recv4)
    # if recv4[:3] != '354':
    #     print('354 reply not received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    message = msg
    clientSocket.send(message.encode())
    # Fill in end

    # Fill in start
    end = endmsg
    clientSocket.send(end.encode())
    recv5 = clientSocket.recv(1024).decode()
    # print(recv5)
    # if recv5[:3] != '250':
    #     print('250 reply not received from server.')
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quitCom = 'QUIT\r\n'
    clientSocket.send(quitCom.encode())
    recv6 = clientSocket.recv(1024).decode()
   #print(recv6)
    #if recv6[:3] != '221':
     #   print('221 reply not received from server.')
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')

