# Continuous loop until CctrI]Cc]
while True:

	# Read the first byte, if no byte, loop
	bytel = Serial_Portl.read(l)

	if len(byte1) < 1:
	break
	# Check for IJSX header - XB5 and X62, Unicode = ub
	if bytel == b"\xb5": 
       byte2 = Serial_portl.read(l)
	   if len(byte2) < 1:
		break
		
	if byte2 == b"\X62": 
		# Get the UBX class
		byte3 = Serial_Portl.read(1)
		# Get the UBX message
		byte4 = Serial_Portl.read(1)
		# Get the UBX payload length
		byte5byte6 = Serial_Portl.read(2)
		
		# Calculate the length of the payload
		length_of_payload = int.from_bytes (byte5and6,"little",signed=False)
		# Read the buffer for the payload length
		ubx_payload = Serial_Portl.read(length_of_payload)
		# Last two bytes are 2*CRC, save them for later use
		ubx_crc_a = serial_port1.read(1)
		ubx_crc_b = serial_port1.read(1)
		# Calculate CRC using CLASS + MESSAGE LENGTH + PAYLOAD
		payload_for_crc = byte3 + byte4 + byte5and6+ubx_payload