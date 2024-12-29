import socket
import random

sv_port = 1783
sv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sv_socket.bind(("", sv_port))
print("Se asteapta conectarea clientului...")
rules = {"P":"F", "F":"H", "H":"P"}

while 1:

    txt, cl_addr = sv_socket.recvfrom(1024)
    txt = txt.decode()

    if txt == "START":
        sv_socket.sendto("\n======JOCUL A INCEPUT!====== \n  =========SUCCES=========\n".encode(), cl_addr)
        print("Clientul a pornit jocul")

        cl_win = 0
        sv_win = 0
        runda = 1

        while True:
            if sv_win == 2:
                sv_socket.sendto("\nServer-ul a castigat meciul\n \nTastati 'START' pentru a incepe un nou joc!\n".encode(), cl_addr)
                break
            elif cl_win == 2:
                sv_socket.sendto("\nAi castigat meciul\n \nTastati 'START' pentru a incepe un nou joc!\n".encode(), cl_addr)
                break

            sv_choice = random.choice(list(rules.keys()))

            cl_choice, _ = sv_socket.recvfrom(1024)
            cl_choice = cl_choice.decode()

            if cl_choice in ["P", "F", "H"]:
                if sv_choice == cl_choice:
                    sv_txt = f"Server-ul a ales {sv_choice}. Suntem egali"
                    sv_socket.sendto(sv_txt.encode(), cl_addr)
                elif rules[sv_choice] == cl_choice:
                    sv_txt = f"Server-ul a ales {sv_choice}. Serverul a castigat runda {runda}"
                    sv_socket.sendto(sv_txt.encode(), cl_addr)
                    sv_win += 1
                    runda += 1
                    print(f"{sv_win}:{cl_win}")
                else:
                    sv_txt = f"Server-ul a ales {sv_choice}. Ai castigat runda {runda}"
                    sv_socket.sendto(sv_txt.encode(), cl_addr)
                    cl_win += 1
                    runda += 1
                    print(f"{sv_win}:{cl_win}")
            else:
                sv_socket.sendto("Input invalid!".encode(), cl_addr)
    else:
        print("Clientul s-a conectat.")