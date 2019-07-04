# devnet3624

# Setup Instructions

Hostname#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Hostname(config)#iox
Hostname(config)#end
Hostname#

Verify IOX-service is running:

Hostname#sh iox-service
Virtual Service Global State and Virtualization Limits:

Infrastructure version : 1.7
Total virtual services installed : 0
Total virtual services activated : 0

Machine types supported   : KVM, LXC
Machine types disabled    : none

Maximum VCPUs per virtual service : 4
Resource virtualization limits:
Name                         Quota     Committed     Available
--------------------------------------------------------------
system CPU (%)                  75             0            75
memory (MB)                   4096             0          4096
bootflash (MB)                1000             0          1000
harddisk (MB)                20000             0         19090
volume-group (MB)           190768             0        170288


IOx Infrastructure Summary:
---------------------------
IOx service (CAF)    : Running
IOx service (HA)     : Not Running
IOx service (IOxman) : Running
Libvirtd             : Running

Hostname#
