System Time Management and Synchronization in Linux! 🚀

🔍 Mastering Accurate Timekeeping for Reliable System Operations!
This project focused on configuring and managing system time settings in Linux, ensuring precise time synchronization essential for logging, cron jobs, and consistent network operations. Key skills and accomplishments include:

⏰ System Time and Date Configuration:
Set System Time: Used sudo date +%T -s "hh:mm:ss" to manually set the system time, ensuring accurate logging and scheduling.
Set System Date: Configured system date with sudo date +%F -s "YYYY-MM-DD" to maintain correct timestamps.
Set Timezone: Managed timezones using sudo timedatectl set-timezone timezone, allowing systems in different geographical locations to sync correctly.

🔄 Time Synchronization Using NTP and Chrony:
NTP Installation and Management: Installed NTP (sudo apt-get install ntp), started the service (sudo systemctl start ntp), and enabled autostart (sudo systemctl enable ntp) to synchronize time with reliable NTP servers.
Chrony as an Alternative: Explored Chrony (sudo apt-get install chrony) for faster synchronization, ensuring accurate timekeeping in virtualized and unstable network environments.

🛠 Troubleshooting Time Synchronization Issues:
Service Status Check: Used sudo systemctl status ntp and sudo systemctl status chrony to verify active synchronization.
Configuration Management: Edited configuration files (/etc/ntp.conf and /etc/chrony/chrony.conf) to add reliable time servers.
Unmasking NTP: Resolved issues of NTP being masked using sudo systemctl unmask ntp, enabling proper startup.
