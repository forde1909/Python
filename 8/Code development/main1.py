"""
Joseph Forde
Exercise_8
Student number: L00169708
"""
from NTWK_Devices import Firewall, Switches, Loadbal     

# Create a firewall instance 
firewall1 = Firewall("firewall1") 
# Configure it 
firewall1.configure_firewall() 

# Create a firewall instance 
firewall2 = Firewall("firewall2") 
# Verify a CRC 
firewall2.calculate_crc("dummy data")

# Create a Switches intance 
switches1 = Switches("switches1") 
# Configure it 
switches1.configure_switches() 

# Create a Switches instance 
switches2 = Switches("switches2") 
# Verify a CRC 
switches2.calculate_crc("dummy data")

# Create a Load Balancers intance 
loadbalancer1 = Loadbal("Loadbalancers1") 
# Configure it 
loadbalancer1.configure_loadbal() 

# Create a Load Balnacers instance 
loadbalancers2 = Loadbal("Loadcalancers2") 
# Verify a CRC 
loadbalancers2.calculate_crc("dummy data")

"""
# Create a Load Balancer intance 
load_balancer1 = Loadbalancers("Load_balancer1") 
# Configure it 
loadbalancer1.configure_load_balancer1() 

# Create a Load Balancer instance 
loadbalancer2 = Loadbalancers("Loan_balancer2") 
# Verify a CRC 
loadbalances2.calculate_crc("dummy data")
"""
