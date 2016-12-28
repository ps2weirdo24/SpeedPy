# Taken from https://blogs.oracle.com/ksplice/entry/learning_by_doing_writing_your

import socket

def main(dest):
	dest_address = socket.gethostbyname(dest)
	icmp = socket.getprotobyname("icmp")
	udp = socket.getprotobyname("udp")
	ttl = 1
	port = 33434
	max_hops = 30

	while True:
		recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
		send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)
		send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
		recv_socket.bind(("", port))
		send_socket.sendto("", (dest, port))
		curr_addr = None
		curr_name = None
		try:
			_, curr_addr = recv_socket.recvfrom(512)
			curr_addr = curr_addr[0]
			try:
				curr_name = socket.gethostbyaddr(curr_addr)[0]
			except socket.error:
				curr_name = curr_addr
		except socket.error:
			pass
		finally:
			send_socket.close()
			recv_socket.close()

		if curr_addr is not None:
			curr_host = "%s (%s)" % (curr_name, curr_addr)
		else:
			curr_host = "*"
		print("%d\t%s" % (ttl, curr_host))

		ttl += 1
		if (curr_addr == dest_address) or (ttl > max_hops):
			break

if __name__ == "__main__":
	main("google.com")